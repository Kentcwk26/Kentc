# Python Assignment (Tenant Management System)
# Chiu Wai Kin TP065600 & Damon Ng Khai Weng TP064820
def login():                                                         #define the login function
   print("\nWelcome to Tenant Management System Login page.\nPlease enter username and password to proceed.\n") 
   chance = 3                                                        #Specify login chances
   while chance > 0:                                                 #iterate when there are more than 0 chances remaining
      #input login credentials
      username = input("Username: ")
      password = input("Password: ")
      #open file and match for correct login credentials
      with open("user.txt",'r') as userInfo:
         userCheck = userInfo.readlines()
         for record in userCheck:
            listRecord = record.split(",")
            if username == listRecord[0]:
               if password == listRecord[1]:
                  print("\n- Login successful -\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                  #check for admin credentials
                  if (username == "john" and password == "1234u-78") or (username == "david" and password == "55467913"):
                     UID = None                                      #activate admin access
                  else:
                     with open("currentUser.txt","w") as current:
                        current.write(record)
                     UID = listRecord[2]                             #deactivate admin access
                  menu(UID)                                          #redirect to menu
                  chance = 0                                         #empty login chances
                  break                                              #break loop to avoid running error message
         else:
            chance -= 1                                              #decrease chances by 1
            print("\nError, incorrect username or password.\n",chance,"chances remaining.\n")

def message(code):                                                   #define message function
   x,y,z="Error, ","Incorrect "," Please try again."
   if code == 0:
      print("\n"+x+y+"input."+z)
   elif code == 1:
      print("\n"+x+y+"data type present."+z)
   elif code == 2:
      print("\n"+x+y+"format."+z)
   elif code == 3:
      print("\n"+x+y+"length."+z)
   elif code == 4:
      print("\n"+x+"data not found."+z)
   elif code == 5:
      print("\n"+x+"zero input."+z)

def specialCharacterList(SCL):                                       #define specialCharacterList function
    if SCL == None:
        return ["~","`","!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]","|",",","\'",".","/","<",">","?",";",":","'",'"'] #0-31
    elif SCL == "SCL1":
        return ['~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|',',','\\','\'','\"','.','/','<','>','?',';',':'] #0-31
    elif SCL == "SCL2":
        return ['~','`','!','@','#','$','%','^','&','*','_','=','+','{','}','[',']','|','\\','\'','\"',',','.','/','<','>','?',':',';'] #0-28

def listIdentifier(listCode):                                        #define listIdentifier function
   if listCode == "t":
      l = "tenant.txt"
   elif listCode == "a":
      l = "Apartment.txt"
   else:
      l = "transaction.txt"
   return l

def appendFile(list,listCode):                                       #define appendFile function
   with open (listIdentifier(listCode), "a") as fAppend:
      for item in list:
         fAppend.write(item)
         fAppend.write(",")
      fAppend.write("\n")

def readFile(listCode):                                              #define readFile function
   with open (listIdentifier(listCode),"r") as fRead:
      string = fRead.readlines()
      for record in string:
         stripped = record.rstrip("\n").rstrip(",")
         splitRecord = stripped.split(",")
         print(splitRecord)

def gettenantID(UID):                                          #define gettenantID function
   if UID:
      #fetch existing UID
      with open("currentUser.txt","r") as uRead:
         userRecord = uRead.read().split(",")
         return userRecord[2]
   else:
      # generate new UID
      UID = dt.datetime.now().strftime("%d%m%Y%H%M%S%f")
      return UID

def getname(code,nameType):                                          #define getname function
   specials = specialCharacterList(None)
   while True:
      print("Format: Name Name or Name-Name Name or Na'me Name")
      if nameType == "tenant":
         name = input("Enter tenant's fullname:\n")
      elif nameType == "employer":
         name = input("Enter tenant's current employer:\n")
      else:
         name = input("Enter tenant's place-city-country of birth\n")
      nameList = name.split(" ")
      if len(nameList) >= 2:
         for words in nameList:
            print("Checking",words)
            if words.isalpha() or [character for character in words if(character in specials[12]) or (character in specials[22])]:
               if words[0].isupper():
                  code = None
                  continue
               else:
                  code = 2
                  break
            else:
               code = 1
               break
      else:
         code = 3
      if code:
         message(code)
         print("ATTENTION||Error detected.||ATTENTION")
      else:
         print("No errors detected.")
      retry = input("[R]-Retry,[Any other key]-Exit using "+name+"\n")
      if retry in ["R","r"]:
         continue
      else:
         return name

def getabbreviation(code,abbreviationType):                          #define getnabbreviation function
   while True:
      if abbreviationType == "gender":
         abbreviation = input("[M]-Male\n[F]-Female\nEnter tenant gender:\n")
      else:
         abbreviation = input("[M]-Malaysian\n[N]-non-Malaysian\nEnter tenant nationality: \n")
      if len(abbreviation)== 1:
         if abbreviation.isalpha():
            if abbreviationType == "gender":
               if abbreviation in ["M","m"]:
                  code = None
                  abbreviation = "Male"
               elif abbreviation in ["F","f"]:
                  code = None
                  abbreviation = "Female"
               else: 
                  code = 0
            else:
               if abbreviation in ["M","m"]:
                  code = None
                  abbreviation = "Malaysian"
               elif abbreviation in ["N","n"]:
                  code = None
                  abbreviation = "non-Malaysian"
               else: 
                  code = 0
         else:
            code = 1
      else: 
         code = 3
      if code or code == 0:
         message(code)
         print("ATTENTION||Error detected.||ATTENTION")
      else:
         print("No errors detected.")
      retry = input("[R]-Retry,[Any other key]-Exit using "+abbreviation+"\n")
      if retry in ["R","r"]:
         continue
      else:
         return abbreviation

def getpNum(code):                                                   #define getpNum function
   while True:
      pNum = input("Format: ############\nEnter tenant phone number:\n")
      if 6 < len(pNum) < 16:
         for digit in pNum:
            if digit.isdigit():
               code = None
               continue
            else:
               code = 1
               break
      else:
         code = 3
      if code:
         message(code)
         print("ATTENTION||Error detected.||ATTENTION")
      else:
         print("No errors detected.")
      retry = input("[R]-Retry,[Any other key]-Exit using "+pNum+"\n")
      if retry in ["R","r"]:
         continue
      else:
         return pNum

def getDate(code,dateType):                                          #define getDate function
   specials = specialCharacterList(None)
   while True:
      if dateType == "start":
         path = input("Use current date as rental start date?\n[Y]-Yes\n[Any Other Key]-No\n")
         if path in ["Y","y"]:
            date = dt.date.today().strftime("%Y/%m/%d")
            print("Current date:",date)
         else:
            date = input("Format: YYYY/MM/DD\nEnter Rental start date:\n")
      elif dateType == "birth":
         date = input("Format: YYYY/MM/DD\nEnter tenant birth date:\n")
      else:
         date = input("Format: YYYY/MM/DD\nEnter transaction date:\n")
      if len(date) == 10:
         if date[4] == date[7] == specials[24]:
            year,month,day = date.split("/")
            try:
               dt.datetime(int(year),int(month),int(day))
               code = None
            except ValueError:
               code = 1
         else:
            code = 2
      else:
         code = 3 
      if code:
         message(code)
         print("ATTENTION||Error detected.||ATTENTION\n")
      else:
         print("No errors detected.\n")
      retry = input("[R]-Retry,[Any other key]-Exit using "+date+"\n")
      if retry in ["R","r"]:
         continue
      else:    
         return date

def getnumber(code,numberType):                                                 #define getincome function
    while True:
      if numberType == "workHistory":
         t = "Total work history is around "
         number = input(t+"\n[1]-1 to 2 month\n[2]-2 to 3 months\n[3]-3 to 6 months\n[4]-6 to 9 months\n[5]-9 months to 1 year\n[6]-1 to 2 years\n[7]-2 to 3 years\n[8]-3 to 4 years\n[9]-4 to 5 years\n[0]-5 years or more\nChoose how long you have been working: ")
      else:
         number = input("[1]-RM 1500~1599\n[2]-RM 1600~1699\n[3]-RM 1700~1799\n[4]-RM 1800~1899\n[5]-RM 1900~1999\n[6]-RM 2000~2099\n[7]-RM 2100~2199\n[8]-RM 2200~2499\n[9]-RM 2500~3000\n[0]-RM > 3000\nChoose tenant income range in Ringgit Malaysia: ")
      if number.isdigit():
         num = int(number)
         if numberType == "workHistory":
            if num == 1:
               number = t+"1 to 2 month"
            elif num == 2:
               number = t+"2 to 3 months"
            elif num == 3:
               number = t+"3 to 6 months"
            elif num == 4:
               number = t+"6 to 9 months"
            elif num == 5:
               number = t+"9 months to 1 year"
            elif num == 6:
               number = t+"1 to 2 years"
            elif num == 7:
               number = t+"2 to 3 years"
            elif num == 8:
               number = t+"3 to 4 years"
            elif num == 9:
               number = t+"4 to 5 years"
            elif num == 0:
               number = t+"5 years or more"
            else:
               code = 0
               message(code)
               continue
         else:
            if num == 1:
               number = "RM 1500~1599"
            elif num == 2:
               number = "RM 1600~1699"
            elif num == 3:
               number = "RM 1700~1799"
            elif num == 4:
               number = "RM 1800~1899"
            elif num == 5:
               number = "RM 1900~1999"
            elif num == 6:
               number = "RM 2000~2099"
            elif num == 7:
               number = "RM 2100~2199"
            elif num == 8:
               number = "RM 2200~2499"
            elif num == 9:
               number = "RM 2500~3000"
            elif num == 0:
               number = "RM > 3000"
            else:
               code = 0
               message(code)
               continue
      else:
         code = 0
         message(code)
         continue
      retry = input("[R]-Retry,[Any other key]-Exit using "+number+"\n")
      if retry in ["R","r"]:
         continue
      else:    
         return number

def getrental(UID):                                            #define getrental function
   if UID:
      return "Current"
   else:
      while True:
         rental = input("[P]-Past\n[Any other key]-Current\nChoose tenant rental status(current/past)\n")
         if rental in ["P","p"]:
               rental = "Past"
         else:
               rental = "Current"
         retry = input("[R]-Retry,[Any other key]-Exit using "+rental+"\n")
         if retry in ["R","r"]:
               continue
         else:    
               return rental

def getreferenceNumber(code):                                        #define getreferenceNumber function
   while True:
      referenceNumber = input("Reference number comes from their relevant bank transaction. They cannot repeat.\nEnter the reference number :\n")
      if len(referenceNumber) > 5:
         if (location.isalnum() for location in referenceNumber):
            code = None
         else:
            code = 1
      else:
         code = 3
      if code:
         message(code)
         print("ATTENTION||Error detected.||ATTENTION\n")
      else:
         print("No errors detected.\n")
      retry = input("[R]-Retry,[Any other key]-Exit using "+referenceNumber+"\n")
      if retry in ["R","r"]:
         continue
      else:    
         return referenceNumber

def getdecimal(code):                                                #define getdecimal function
   specials = specialCharacterList(None)
   while True:
      decimal = input("Format: ########.##\nEnter the transaction amount in Ringgit Malaysia:\n")
      if specials[23] in decimal:
         money = decimal.split(".")
         for numbers in money:
            try:
               numbers[1] in money[1]
               if (digits.isnumeric() for digits in numbers):
                  code = None
                  continue
               else:
                  code = 1
                  break
            except IndexError:
               code = 2
               break
      else:
         code = 2
         print(specials[23])
      if code:
         message(code)
         print("ATTENTION||Error detected.||ATTENTION\n")
      else:
         print("No errors detected.\n")
      retry = input("[R]-Retry,[Any other key]-Exit using "+decimal+"\n")
      if retry in ["R","r"]:
         continue
      else:    
         return decimal

def tenantOrTransactionEntryForm(UID,listCode,code):           #Define tenantOrTransactionEntryForm function
   while True:
      if UID == None:
         n = input("Number of new Records: ")
         if n.isdecimal():
            code = None
         else:
            code = 0
            message(code)
            continue
      else:
         n = 1
      for list in range(0,int(n)):
         if listCode == "t":
            #Get input for tenant data
            UserID  = gettenantID(UID)
            name = getname(code,"tenant")
            gender = getabbreviation(code,"gender")
            pNum = getpNum(code)
            nationality = getabbreviation(code,"nationality")
            startDate = getDate(code,"start")
            workHistory = getnumber(code,"workHistory")
            employer = getname(code,"employer")
            income = getnumber(code,"income")
            rental = getrental(UID)
            birthDate = getDate(code,"birth")
            birthCity = getname(code,"city")
            #Declare list containing relevant input data
            list = [UserID,name,gender,pNum,nationality,startDate,workHistory,employer,income,rental,birthDate,birthCity]
         else:
            referenceNumber = getreferenceNumber(code)
            transactionDate = getDate(code,"transaction")
            UserID  = gettenantID(UID,listCode)
            apartmendCode = newRoomCode()
            amount = getdecimal(code)
            list = [referenceNumber,transactionDate,UserID,apartmendCode,amount]
         appendFile(list,listCode)
      break

def tenantOrTransaction(UID,listCode,code):                #Define tenantOrTransaction function
   while True:
      if UID:
         searchInformation(listCode,0,UID)
         if listCode == "t": 
            print("[C]-Change my tenant details")
         else:
            print("[A]-Add new transaction")
         opt = input("\n[E]-Exit\nWhat would you like to do:")
         if opt in ["C","c"]:
            modifyData(UID,listCode,code,"2")
         elif opt in ["A","a"]:
            modifyData(UID,listCode,code,"1")
         elif opt in ["E","e"]:
            break
         else:
            message(0)
            continue
         break
      else:
         opt = input("[D]-Display existing Data, [M]-Modify Data\n[E]-Exit\nWhat would you like to do:")
         if opt in ["D","d"]:      
            print("Current Data:")
            readFile(listCode)
         elif opt in ["M","m"]:
            modifyData(UID,listCode,code,None)
         elif opt in ["E","e"]:
            break
         else:
            message(0)
            continue
         break

# - Apartment - Chiu Wai Kin TP065600
def apartment(UID,listCode,code):                              #Define apartment function
   
   listCode = "a"
   print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
   print("\n- Apartment info: -")
   
   #Put sample data
   list1 = ["Room Info: Standard Room (Triple)","Code: SR1","Dimensions: 140+ sqft","Pricing: RM350","Apartment ID: A01-L01-R01 to A01-L01-R21","Date of Acquisition: 03/01/2015","Rental History: 27/02/2015 rent","Status: Available"]
   list2 = ["Room Info: Standard Room (Twin)","Code: SR2","Dimensions: 120+ sqft","Pricing: RM450","Apartment ID: A01-L01-R22 to A01-L01-R41","Date of Acquisition: 10/02/2015","Rental History: 28/03/2015 rent","Status: Available"]
   list3 = ["Room Info: Standard Room A/C (Triple)","Code: SR3","Dimensions: 150+ sqft","Pricing: RM550","Apartment ID: A01-L02-R01 to A01-L02-R21","Date of Acquisition: 21/03/2016","Rental History: 24/04/2016 rent","Status: Available"]
   list4 = ["Room Info: Standard Room A/C (Twin)","Code: SR4","Dimensions: 130+ sqft","Pricing: RM650","Apartment ID: A01-L02-R22 to A01-L02-R41","Date of Acquisition: 02/04/2016","Rental History: 20/05/2016 rent","Status: Available"]
   list5 = ["Room Info: Deluxe Room (Triple)","Code: DR1","Dimensions: 170+ sqft","Pricing: RM750","Apartment ID: A01-L04-R01 to A01-L04-R21","Date of Acquisition: 11/05/2017","Rental History: 21/06/2017 rent","Status: Available"]
   list6 = ["Room Info: Deluxe Room (Twin)","Code: DR2","Dimensions: 160+ sqft","Pricing: RM840","Apartment ID: A01-L04-R22 to A01-L04-R41","Date of Acquisition: 22/06/2017","Rental History: 22/07/2017 rent","Status: Available"]
   list7 = ["Room Info: Deluxe Room A/C with shared attached bath / toilet (Triple)","Code: DR3","Dimensions: 180+ sqft","Pricing: RM950","Apartment ID: A01-L03-R1 to A01-L03-R21","Date of Acquisition: 30/07/2018","Rental History: 25/08/2018 rent","Status: Available"]
   list8 = ["Room Info: Deluxe Room A/C with shared attached bath / toilet","Code: DR4","Dimensions: 170+ sqft","Pricing: RM1040","Apartment ID: A01-L03-R22 to A01-L03-R41","Date of Acquisition: 16/08/2018","Rental History: 18/09/2018 rent","Status: Available"]
   list9 = ["Room Info: Compact Premium Single","Code: CPS1","Dimensions: 130+ sqft","Pricing: RM690","Apartment ID: A01-L05-R01 to A01-L05-R41, Date of Acquisition: 02/09/2019, Rental History: 29/10/2019 rent, Status: Available"]
   list10 = ["Room Info: Medium Premium Single","Code: MPS1","Dimensions: 150+ sqft","Pricing: RM750","Apartment ID: A02-L01-R01 to A02-L01-R21","Date of Acquisition: 15/10/2019","Rental History: 31/11/2019 rent","Status: Available"]
   list11 = ["Room Info: Medium Premium Twin","Code: MPT1","Dimensions: 180+ sqft","Pricing: RM890","Apartment ID: A02-L02-R01 to A02-L02-R21","Date of Acquisition: 25/11/2020","Rental History: 31/12/2020 rent","Status: Available"]
   list12 = ["Room Info: Medium Premium with attached bath / toilet (Twin)","Code: MP1","Dimensions: 180+ sqft","Pricing: RM940","Apartment ID: A02-L03-R01 to A02-L03-R21","Date of Acquisition: 30/12/2020","Rental History: 31/01/2020 rent","Status: Available"]
   list13 = ["Room Info: Medium Premium with attached bath / toilet (Single)","Code: MP2","Dimensions: 160+ sqft","Pricing: RM1050","Apartment ID: A02-L03-R22 to A02-L03-R41","Date of Acquisition: 16/01/2021","Rental History: 28/02/2021 rent","Status: Available"]
   list14 = ["Room Info: En-Suite Single (Super Premium - Triple)","Code: ESS3","Dimensions: 160+ sqft","Pricing: RM700","Apartment ID: A02-L04-R01 to A02-L04-R41","Date of Acquisition: 25/02/2021","Rental History: 31/03/2021 rent","Status: Available"]
   list15 = ["Room Info: En-Suite Single (Super Premium - Twin)","Code: ESS2","Dimensions: 140+ sqft","Pricing: RM800","Apartment ID: A02-L04-R01 to A02-L04-R41","Date of Acquisition: 31/05/2022","Rental History: Empty","Status: Not Available"]
   list16 = ["Room Info: En-Suite Twin (Super Premium)","Code: EST2","Dimensions: 200+ sqft","Pricing: RM900","Apartment ID: A02-L05-R01 to A02-L05-R41","Date of Acquisition: 26/06/2022","Rental History: Empty","Status: Not Available"]
   #Apply data at the list
   ApartmentList = [list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12,list13,list14,list15,list16]
   with open(listIdentifier(listCode),"w") as apartmentHandler:
      for record in ApartmentList:
         for data in record:
            apartmentHandler.write(data)
            apartmentHandler.write(",")
         apartmentHandler.write("\n")
   
   for item in ApartmentList:
      print(item,"\n")
   print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
   if UID == None:
      modifyData(UID,listCode,code,None)
   else:
      return False

def modifyData(UID,listCode,code,modifyType):
   modify = True
   while modify == True:
      if modifyType:
         dataInput = modifyType
      else:
         dataInput = input('\n- Modification of records: -\n\n1. Add data\n2. Edit Data\n3. Delete Data\n4. Exit\n\nPlease select which operation to perform task (1-4): ')
      print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
      if dataInput == "1":
         if listCode == "a":
            apartmentAddData(modify,listCode)
         else:
            tenantOrTransactionEntryForm(UID,listCode,code)
      elif dataInput == "2":
         replaceOldData(UID,listCode,code)
         modify = False
      elif dataInput == "3":
         apartmentDeleteData()
         modify = False
      elif dataInput == "4":
         modify = False
      else:
         code = 1
         message(code)
         continue
      break

def apartmentAddData(modify,listCode):
   adddatalist = []
   print("\nDear admin, we need your ATTENTION !\n\nFor your information, all the new data will only be stored if you insert each information with the correct format provided.\n\nOnce you finish each entry,a confirmation message will appear. Please ensure that the data is typed correctly before saving.\n- Now, you are required to enter new data. -\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
   newroom = newRoom()
   newroomcode = newRoomCode()
   newroomdimension = newRoomDimension()
   newroompricing = newRoompricing()
   newroomID = newRoomID()
   newroomdateofacquisition = newRoomDate("acquisition")     
   newroomrentalhistory = newRoomDate("history")
   newroomstatus = newRoomStatus()
   adddatalist = [str(newroom),str(newroomcode),str(newroomdimension),str(newroompricing),str(newroomID),str(newroomdateofacquisition),str(newroomrentalhistory),str(newroomstatus)]
   print("\nNew Data:",adddatalist)
   addDataconfirmation = input("\nAre you sure with the records you inserted just now? Enter to continue, 'N' to unsave: ")
   if addDataconfirmation in ["N","n"]:
      return modify
   else:
      appendFile(adddatalist,listCode)
      print("\n- Data Saved -\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
      return modify
def newRoom():
   while True:
      code = None
      SCL = 'SCL2'
      specials = specialCharacterList(SCL)
      newRoom = input("\nRoom info only contains alphabets, no numbers and special characters [Except these special characters: '(' ')' '/' '-' ]\nExample: Dual Key Premium Rooms - Single Room\n\nRoom Info: ")
      if [character for character in newRoom if (character in specials)]:
         code = 2
         message(code)
         print("- Room info does not contain special character(s) -")
         continue
      else:
         code = None
      if 0 <= len(newRoom) < 6:
         code = 2
         message(code)
         print("-  Refer to the Room Info to look for its details and format -")
         continue
      else:
         code = None
      if newRoom.isdigit() and any(location.isdigit() for location in newRoom):
         code = 1
         message(code)
         print("- Room info does not contain number(s) -")
         continue
      else:
         code = None
      if code == None:
         newRoom.title()
         decisionkey = input("Save data? (Enter to continue, 'N' to return back):")
         if decisionkey in ['N','n']:
            continue
         else:
            return "New Room Info: "+newRoom
      else:
         code = 2
         message(code)
         print("- Please fill in the correct format for room info. Refer to the description above for its details and format -")
         continue

def newRoomCode():
   while True:
      code = None
      newRoomCode = input("\nRoom code only contains alphanumeric (A combination of uppercased alphabet and number), and no special characters\nExample: DKPRS1\n\nRoom Code: ")
      if len(newRoomCode) <= 1 :
         code=2
         message(code)
         print("- Room Code must contain at least 2 or more alphanumeric long -\n")
         continue
      else:
         code = None 
      if newRoomCode.isalnum():
         code = None
      else:
         code=2
         message(code)
         print("- Please note that room code is only acceptable when it contains alphanumeric only-\n")
         continue
      if code == None:
         decisionkey = input("Save data? (Enter to continue, 'N' to return back): ")
         if decisionkey in ['N','n']:
            continue
         else:
            return "New Room Code: "+newRoomCode
      else:
         code = 2
         message(code)
         print("- Please fill in the correct format for room code. Refer to the description above for its details and format -")
         continue

def newRoomDimension():
   while True:
      code = None
      newRoomDimension=input("\nRoom Dimension only contains numbers, no alphabets and special characters (The unit (in sqft) will be provided at the back)\nExample: 300(+sqft)\n\nRoom Dimension: ")
      if len(newRoomDimension) == 0:
         code = 5
         message(code)
         print("- Please fill in the room dimension, and room dimension must have at least 100 or more sqft -\n")
         continue
      else:
         code = None
      if newRoomDimension.isdigit():
         code = None
      else:
         code = 2 
         message(code)
         print("- Room dimension must consist of number(s) -")
         continue
      if code == None:
         decisionkey = input("Save data? (Enter to continue, 'N' to return back):")
         if decisionkey in ["N","n"]:
            continue
         else:
            return "Dimensions: "+newRoomDimension
      else:
         code=2
         message(code)
         print("- Please fill in the correct format for room dimension. Refer to the description above for its details and format -\n")
         continue

def newRoompricing():
   while True:
      code = None
      newRoompricing=input("\nRoom Pricing only contain numbers, no special characters (The unit (in RM) will be provided at the front)\nExample: (RM)500\n\nRoom Pricing: ")
      if newRoompricing.isdigit():
         nRp=int(newRoompricing)
         if nRp >= 350:
            code = None
      else:
         code = 2
         message(code)
         print("- Please fill in the room pricing, it must be in numeric and the minimum starting price starts from RM350 and above -\n")
         continue
      if code == None:
         decisionkey = input("Save data? (Enter to continue, 'N' to return back):")
         if decisionkey in ["N","n"]:
            continue
         else:
            return "Pricing: RM"+newRoompricing
      else:
         code = 2
         message(code)
         print("- Please follow the correct format for new room pricing. Refer to the description above to know its details and format -\n")
         continue

def newRoomID():
   while True:
      code = None
      validnewRoomID = input('\nThis is the correct format for RoomID: A(01)-L(01)-R(01)x(to)xA(99)-L(99)-R(99), x means space\nPlease enter the new Room ID: ')
      if 0 <= len(validnewRoomID) <= 25:
         print("\n- Please fill in the new room ID with the correct format -")
         continue
      else:
         if (validnewRoomID[0] == 'A' and validnewRoomID[3] == '-' and validnewRoomID[4] == 'L' and validnewRoomID[7] == '-' and validnewRoomID[8] == 'R' and validnewRoomID[11] == ' ' and validnewRoomID[12] == 't' and validnewRoomID[13] == 'o' and validnewRoomID[14] == ' ' and validnewRoomID[15] == 'A' and validnewRoomID[18] == '-' and validnewRoomID[19] == 'L' and validnewRoomID[22] == '-' and validnewRoomID[23] == 'R'):
            if ((validnewRoomID[1] and validnewRoomID[2] and validnewRoomID[5] and validnewRoomID[6] and validnewRoomID[9] and validnewRoomID[10] and validnewRoomID[16] and validnewRoomID[17] and validnewRoomID[20] and validnewRoomID[21] and validnewRoomID[24] and validnewRoomID[25]).isdigit):
               decisionkey = input("Save data? (Enter to continue, 'N' to return back):")
               if decisionkey in ["N","n"]:
                  continue
               else:
                  return "Apartment ID: "+validnewRoomID
            else:
               code = 1
               message(code)
               continue
         else:
            code = 2
            message(code)
            continue

def newRoomDate(dateType):
   while True:
      code = None
      if dateType == "acquisition":
         roomDate = input("\nRoom Date of Acquisition: dd/mm/yyyy\nNo special characters included, except '/'\n\nRoom Acquisition Date: ")
      else:
         roomDate = input("\nRoom Rental History: (Accepted input: 'dd/mm/yyyy' or 'Empty')\nNo special characters included, except '/'\n\nRoom Rental History: ")
      if any(location.isdigit() for location in roomDate) and len(roomDate) == 10:
         day,month,year = roomDate.split('/')
         ValidDate = True
         try:
            dt.datetime(int(year),int(month),int(day))
            ValidDate = True
         except ValueError:
            ValidDate = False
         if ValidDate == True :
            code = None
            decisionkey = input("Save data? (Enter to continue, 'N' to return back):")
            if decisionkey in ["N","n"]:
               return True
            else:
               return "Acquisition Date: " + roomDate
         else:
            code = 2
            message(code)
            print("- The given date is not valid -\n")
            continue
      else:
         code = 2
         message(code)
         print("- Wrong Date Format (dd/mm/yyyy) -\n")
         continue

def newRoomStatus():
   while True:
      code = None
      SCL = None
      specials = specialCharacterList(SCL)
      newRoomStatus = input("\nRoom Status: (Accepted Input: 'Available' or 'Not Available')\nNo numbers and special characters included\n\nRoom Status ( Available / Not Available ): ")
      if (0 <= len(newRoomStatus) <= 7) or (len(newRoomStatus) >= 14) :
         code = 5
         message(code)
         print("- Please fill the room status again with the correct format ( Accepted input: Available / Not Available ) -")
         continue
      else:
         code = None
      if any(location.isdigit() for location in newRoomStatus) and newRoomStatus.isdigit(): 
         code = 2
         message(code)
         print("- Room status must not contain number(s) -")
         continue
      else:
         code = None
      if [character for character in newRoomStatus if (character in specials)]:
         code = 2
         message(code)
         print("- Room status must not have special character(s) -")
         continue
      else:
         code = None
      if (0 <= len(newRoomStatus) <= 7 or len(newRoomStatus) >= 14) and (any(location.isdigit() for location in newRoomStatus)):
         code = 2
         message(code)
         print("- Room status must not consists of number(s) -")
         continue
      else:
         code = None
      if ([character for character in newRoomStatus if (character in specials)] and any(location.isdigit() for location in newRoomStatus) and [character for character in newRoomStatus if (character in specials)]):
         code = 3
         message(code)
         print("- Room rental history must not contain number(s) and special character(s) -\n")
         continue
      else:
         code = None
      if (0 < len(newRoomStatus) <= 7 or len(newRoomStatus) >= 14) and (any(location.isdigit() for location in newRoomStatus)) and ([character for character in newRoomStatus if (character in specials)]):
         code=3
         message(code)
         print("- Input too short or long, and also number(s) and special character(s) exist, please follow the correct format ( Accepted input: Available / Not Available ) -\n")
         continue
      else:
         code = None
      if newRoomStatus in ["Available","Not Available"] and (len(newRoomStatus) == 9 or len(newRoomStatus) == 13):
         code = None
      else:
         code = 2
         message(code)
         print("- Room Status can only be accepted either the input is 'Available' or 'Not Available'. -\n")
         continue
      if code == None:
         decisionkey = input("Save data? (Enter to continue, 'N' to return back):")
         if decisionkey in ["N","n"]:
            continue
         else:
            return "Status: "+newRoomStatus
      else:
         code = 3
         message(code)
         print("Please insert the correct format for room status. Refer to the description above for its details and format -\n")
         continue

def inputidentifier(UID,listCode,editDataType,code):
      if listCode == "a":
         if editDataType == 0:
            return newRoom()
         elif editDataType == 1:
            return newRoomCode()
         elif editDataType == 2:
            return newRoomDimension()
         elif editDataType == 3:
            return newRoompricing()
         elif editDataType == 4:
            return newRoomID()
         elif editDataType == 5:
            return newRoomDate("acquisition")
         elif editDataType == 6:
            return newRoomDate("history")
         else:
            return newRoomStatus()
      elif listCode == "t":
         if editDataType == 0:
            return gettenantID(UID)
         elif editDataType == 1:
            return getname(code,"tenant")
         elif editDataType == 2:
            return getabbreviation(code,"gender")
         elif editDataType == 3:
            return getpNum(code)
         elif editDataType == 4:
            return getabbreviation(code,"nationality")
         elif editDataType == 5:
            return getDate(code,"start")
         elif editDataType == 6:
            return getnumber(code,"workHistory")
         elif editDataType == 7:
            return getname(code,"employer")
         elif editDataType == 8:
            return getnumber(code,"income")
         elif editDataType == 9:
            return getrental(UID)
         elif editDataType == 10:
            return getDate(code,"birth")
         else:
            return getname(code,"city")
      else:
         if editDataType == 0:
            return getreferenceNumber(code)
         elif editDataType == 1:
            return getDate(code,"transaction")
         elif editDataType == 2:
            return gettenantID(UID,listCode)
         elif editDataType == 3:
            return newRoomCode()
         else:
            return getdecimal(code)

def ApartmentDataInfo():
   data = True
   while data == True:
      opt = input("\n[R] - Room Info [C] - Room code, [D] - Dimensions, [P] - Pricing, [N] - Number of Rooms, [A] - Apartment ID, [D] - Date of Acquisition, [H] - Rental History, [S] - Status \nAnswer: ")
      if opt in ["R","r"]:
         return 0
      elif opt in ["C","c"]:
         return 1
      elif opt in ["D","d"]:
         return 2
      elif opt in ["P","p"]:
         return 3
      elif opt in ["N","n"]:
         return 4
      elif opt in ["A","a"]:
         return 5
      elif opt in ["D","d"]:
         return 6
      elif opt in ["H","h"]:
         return 7
      elif opt in ["S","s"]:
         return 8
      else:
         code = 0
         message(code)
         continue

def category(listCode,code):
   while True:
      if listCode == "p":
         opt = input("\n[R]-Reference number,[D]-Transaction date,[T]-TenantID,[A]-Apartment code,[S]-Amount\n Choose a category: ")
         if opt in ["R","r"]:
            return 0
         elif opt in ["D","d"]:
            return 1
         elif opt in ["T","t"]:
            return 2
         elif opt in ["A","a"]:
            return 3
         elif opt in ["S","s"]:
            return 4
         else:
            code = 0
            message(0)
            continue
      else:
         opt = input("\n[U]-User ID,[N]-Name,[G]-Gender,[P]-Phone number,[R]-Nationality,[D]-Rental start date,[W]-Work history,[E]-Employer,[I]-Income,[S]-Tenant status,[B]-Birthdate,[C]-Birth City\nChoose a category: ")
         if opt in ["U","u"]:
            return 0
         elif opt in ["N","n"]:
            return 1
         elif opt in ["G","g"]:
            return 2
         elif opt in ["P","p"]:
            return 3
         elif opt in ["R","r"]:
            return 4
         elif opt in ["D","d"]:
            return 5
         elif opt in ["W","w"]:
            return 6
         elif opt in ["E","e"]:
            return 7
         elif opt in ["I","i"]:
            return 8
         elif opt in ["S","s"]:
            return 9
         elif opt in ["B","b"]:
            return 10
         elif opt in ["C","c"]:
            return 11
         else:
            code = 0
            message(0)
            continue

def searchInformation(listCode,num,details):                   #Define searchinformation function
   while True:
      if details:
         searchInformation = details
      else:
         searchInformation = input("\nPlease enter text to begin the search: ")
      recordExist = False
      with open(listIdentifier(listCode),"r") as Xhandler:
         print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nResults:\n")
         for record in Xhandler:
            strippedItem = record.rstrip()
            data=strippedItem.split(",")
            if searchInformation in data[num]:
               print(record.rstrip(",").rstrip("\n"))
               recordExist = True
            else:
               continue
         if recordExist == True:
            code = 0
            print("\n- Matching records ends here -")
         else:
            code = 4
            message(code)
         break
def replaceOldData(UID,listCode,code):
   while True:
      if listCode == "a":
         editDataType = ApartmentDataInfo()
      else:
         editDataType = category(listCode,code)
      display = searchColumn(listCode,editDataType,UID)
      oldDataFormat = False
      while oldDataFormat == False:
         print(display)
         if UID == None:
            selectedData = input("Placement of items displayed above are labeled from left-to-right starting from 1\nPlease enter the number of the item to edit:")
            if selectedData.isdecimal():
               recordindex = int(selectedData)-1
               oldDataFormat = True
            else:
               code = 1
               message(code)
               continue
         else:
            for item in display:
               if item != "":
                  recordindex = display.index(item)
                  oldDataFormat = True
               else:
                  continue

      print("Last step, please insert the new data with the correct format: ")
      newdata = inputidentifier(UID,listCode,editDataType,code)
      editdataconfirmation = input("\nAre you sure with your records just now? ([Y]-Yes/[N]-No): ")
      if editdataconfirmation in ["Y","y"]:
         with open(listIdentifier(listCode),"r") as Xhandler:
            updatedData = []
            newRecord = []
            dataRead = Xhandler.readlines()
            for record in dataRead:
               strippedRecord = record.rstrip(",\n").split(",")
               if dataRead.index(record) == int(recordindex):
                  strippedRecord[int(editDataType)] = newdata               #modify the record with new data
                  newRecord = ",".join(strippedRecord)                         #capture the new record
                  updatedData.append(newRecord+",\n")
               else:
                  updatedData.append(record)
         with open(listIdentifier(listCode),"w") as fUpdate:
            for record in updatedData:
               fUpdate.write(record)
         return False
      elif editdataconfirmation in ["N","n"]:
         return False
      else:
         code = 0
         message(code)
         continue

def searchColumn(listCode,num,UID):
   displayList=[]
   with open (listIdentifier(listCode), "r") as Tread:
      bulkData = Tread.readlines()
      for line in bulkData:
         individualList = line.strip(",\n").split(",")
         if listCode == "a":
            if int(num) == 1:
               displayList.append(individualList[int(num)])
            else:
               displayList.append(str(individualList[int(1)])+";"+str(individualList[int(num)]))
         else:
            if UID == None:
               if int(num) == 0:
                  displayList.append(individualList[int(num)])
               else:
                  displayList.append("ID: "+str(individualList[int(0)])+";relevant data: "+str(individualList[int(num)]))
            else:
               if listCode == "t":
                  if int(num) == 0:
                     displayList.append(individualList(UID))
                  else:
                     if individualList[0] == UID:
                        displayList.append("ID: "+str(individualList[int(0)])+";relevant data: "+str(individualList[int(num)]))
                        break
                     else:
                        displayList.append("")
                        continue
   if displayList == []:
      code = 5
      message(code)
   else:
      return displayList
      
def apartmentDeleteData():
   modify = True
   while True:
      print("\n- Delete Data -")
      deletedata = input("\n1. Delete specified records\n2. Delete all records\n\n[E] - Exit\n\nPlease select and enter which operator that you want to proceed: ")
      if deletedata == '1':
         print("\n- 1. Delete specified records -")
         deleteSpecRecord()
      elif deletedata == '2':
         print("\n- 2. Delete all records -")
         deleteAllrecords()
      elif deletedata in ["E","e"]:
         return modify
      else:
         code = 0
         message(code)
         continue

def deleteSpecRecord():
   code = None
   modify = True
   while True:
      listCode = 'a'
      print("\n- 2. Delete specified row  -\n")
      selecteddatarow = input("\nWhich data row that you want to delete? ")
      if selecteddatarow.isdigit():
         with open (listIdentifier(listCode),"r") as readfile:
            record = readfile.readlines()[selecteddatarow-"1"]
         with open (listIdentifier(listCode),"w") as writefile:
            removeddata = record.replace(selecteddatarow," ")
            writefile.write(removeddata)
      else:
         code = 0
         message(code)
         continue
      return modify

def deleteAllrecords():
   modify = None
   while modify == True:
      listCode = 'a'
      print("\n- 3. Delete all records -")
      confirmation = input("\nAre you sure that you want to delete all the record(s)?\nIt will be not recovered once you hit the enter button. However, you still can discard this changes by hitting a 'X' if you change your mind: ")
      if confirmation in ["X","x"]:
         print("\n- Delete unsuccessful -")
      else:
         with open (listIdentifier(listCode),"r+") as ADeletedhandler:
            ADeletedhandler.seek(0)
            ADeletedhandler.truncate()
            print("\n- Delete successful -")
      return modify

def searchBox(UID):                                                     #Define search function
   while True:
      print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nWelcome to search box!")
      num = None
      print("\n1. Search room specific details.\n2. Search transaction details.\n3. Search specific tenant details.\n4. Exit search box.\n")
      option=input("Please type the search criteria based on the listing above: ")
      if option.isdigit and option == "1":
         listCode= "a"
         opt = input("\n[C]-Room code, [P]-Pricing, [N]-Number of Rooms, [A]- Apartment ID, [D]-Date of Acquisition, [R]-Rental \nSearch?  ")     
         if opt in ["C","c"]:
            num = 1
         elif opt in ["X","x"]:
            num = 2
         elif opt in ["P","p"]:
            num = 3
         elif opt in ["N","n"]:
            num = 4
         elif opt in ["A","a"]:
            num = 5
         elif opt in ["D","d"]:
            num = 6
         elif opt in ["R","r"]:
            num = 7
         else:
            code = 0
            message(code)
            continue
      elif option.isdigit() and option == "2":
         listCode = "p"
         num = category(listCode,code)
      elif option.isdigit() and option == "3" :
         listCode = "t"
         num = category(listCode,code)
      elif option.isdigit() and option == "4":
         print("\n- Return to main menu -\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n- Welcome back ! -")
         break                                          #return to menu function
      else:
         code = 0
         message(code)
         continue
      if UID:
         if listCode == "a":
            details = None
         else:
            details = UID
      else:
         details = None
      print(searchColumn(listCode,num))
      searchInformation(listCode,num,details)

def menu(UID):                                       #Define menu function
   mainMenu = True
   while mainMenu == True:
      code = None
      if UID:
         print("\nMain menu:\n\n[S] - Search box\n\nReview information about:\n[A] - Available Apartments\n[T] - My Tenant details\n[P] - My Transactions\n\nQuick functions:\n[D] - Print my House & Tenant Details\n\n[E] - Exit")
      else:
         print("\nMain menu\n\n[S] - Search box\n\nReview information about:\n[A] - Apartment\n[T] - Tenant\n[P] - Transaction\n\nQuick functions:\n[D] - Print Specific House & Tenant Details\n[I] - Inquiry of Past Tenant Details\n\n[E] - Exit")
      opt=input("\nPlease enter which operation that you want to do: ")
      if opt in ["S","s"]:
         searchBox(UID)                                        #redirect to searchbox function
#Check for basic Functions
      elif opt in ["A","a"]:
         listCode = "a"
         apartment(UID,listCode,code)
      elif opt in ["P","p"]:
         listCode = "p"
         tenantOrTransaction(UID,listCode,code)
      elif opt in ["T","t"]:
         listCode = "t"
         tenantOrTransaction(UID,listCode,code)
#Check for quick functions
      elif opt in ["D","d"]:
         print("tenantAndApartment()")
      elif opt in ["I","i"] and UID == None:
         searchInformation(listCode,9,"past")
      elif opt in ["L","l"] and UID == None:
         print("loginHistory()")
      elif opt in ["E","e"]:                                #get confirmation to exit
         exitconfirmationkey=input("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nYou're about to leave Tenant Management System. Are you sure? [Enter]-Continue, [x]-Return to main menu): ")
         if exitconfirmationkey in ["X","x"]:
            continue
         else:
            print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nExit successful, have a nice day~\n")
            return False
      else:
         code = 0
         message(code)

import datetime as dt
login()