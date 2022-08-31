# Python Assignment (Tenant Management System)
# Chiu Wai Kin TP065600 & Damon Ng Khai Weng TP064820
def register(listCode,code):
   username = input("Create your account's username\n")
   password = input("Next, create your account's password: ")
   userType = "new"
   UID = None
   UserID = gettenantID(UID,userType)
   print("UserID is"+UserID,type(UserID))
   with open (listIdentifier(listCode),"a") as useradd:
      useradd.write(username+","+password+","+UserID+",\n")
   listCode = "t"
   tenantOrTransactionEntryForm(UserID,listCode,code)

def login():                                                   # Define the login function
   print("\nWelcome to Tenant Management System Login page.\nPlease enter username and password to proceed.\n") 
   listCode = "u"
   code = None
   while True:
      new = input("[Y]-Yes I am.\n[Any Other Key]-No,I have an existing account\nAre you a new user: ")
      if new in ["Y","y"]:
         register(listCode,code)
      else:
         chance = 3                                                  # Specify login chances
         while chance > 0:                                           # Iterate when there are more than 0 chances remaining
            username = input("Username: ")                           # Input login credentials
            password = input("Password: ")                           # Input login credentials
            with open(listIdentifier(listCode),"r") as userInfo:                   # Open user.txt file in read mode as userInfo and match for correct login credentials
               userCheck = userInfo.readlines()                      # Read each lines in userInfo  
               for record in userCheck:
                  listRecord = record.split(",")                     # Split the record using comma as a separator
                  if username == listRecord[0]:
                     if password == listRecord[1]:
                        print("\n- Login successful -\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        if (username == "john" and password == "1234u-78") or (username == "david" and password == "55467913"):     # Check for admin credentials
                           UID = None                                # Activate admin access
                        else:
                           with open("currentUser.txt","w") as current:
                              current.write(record)                  # Write record into current
                           UID = listRecord[2]                       # Deactivate admin access
                        menu(UID,code)                                    # Redirect to menu
                        chance = 0                                   # Empty login chances
                        break                                        # Break loop to avoid running error message
               else:
                  chance -= 1                                        # Decrease chances by 1
                  print("\nError, incorrect username or password.\n",chance,"chances remaining.\n")

def message(code):                                             # Define message function
   x,y,z="Error, ","Incorrect "," Please try again."           # Declare x as 'Error', y as 'Incorrect' and z is 'Please try again'
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

def specialCharacterList(SCL):                                       # Define specialCharacterList function
    if SCL == None:
        return ["~","`","!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]","|",",","\'",".","/","<",">","?",";",":","'",'"'] 
    elif SCL == "SCL1":
        return ['~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|',',','\\','\'','\"','.','/','<','>','?',';',':']
    elif SCL == "SCL2":
        return ['~','`','!','@','#','$','%','^','&','*','_','=','+','{','}','[',']','|','\\','\'','\"',',','.','/','<','>','?',':',';']

def listIdentifier(listCode):                                        # Define listIdentifier function
   if listCode == "t":                                               # If listCode is equal to 't' Then:
      l = "tenant.txt"                                               # l is "tenant.txt"
   elif listCode == "a":                                             # If listCode is equal to 'a' Then:
      l = "Apartment.txt"                                            # l is "Apartment.txt"
   elif listCode == "p":                                             # If listCode is equal to 'p' Then:
      l = "transaction.txt"                                          # l is "transaction.txt"
   elif listCode == "u":                                             # If listCode is equal to 'u' Then:
      l = "user.txt"                                                 # l is "user.txt"
   return l                                                          # return value is l

def appendFile(list,listCode):                                       # Define appendFile function
   with open (listIdentifier(listCode), "a") as fAppend:             # Open selected text file in Append Mode as fAppend
      for item in list:                                              # For each item in a list: 
         fAppend.write(item)                                         # Write item into fAppend
         fAppend.write(",")                                          # Write a comma (,) into fAppend
      fAppend.write("\n")                                            # Write a newline ("\n") into fAppend

def readFile(listCode):                                              # Define readFile function
   returnList = []                                                   # Declare returnlist as array
   with open (listIdentifier(listCode),"r") as fRead:                # Open selected text file in Read Mode as fRead
      line = fRead.readlines()                                       # line = read each line in fRead
      for record in line:                                            # For each records in a line:
         stripped = record.rstrip("\n").rstrip(",")                  # stripped = Right stripped from the end of string (record) with the separators (all commas and newlines)
         splitRecord = stripped.split(",")                           # splitRecord = Use comma as the separator to split from a string into a list
         returnList.append(str(splitRecord))                         # Append returnlist to splitRecord in string type
         print(int(line.index(record))+1,splitRecord)                # Print 
   return returnList                                                 # Return value is returnlist

def chooseItem(UID,listCode,displayColumn,currentColumn):            # Define chooseItem function
   displayRecord = searchColumn(listCode,displayColumn,UID)          # displayRecord = call function searchColumn(listCode,displayColumn,UID)
   currentRecord = searchColumn(listCode,currentColumn,UID)          # currentRecord = call function searchColumn(listCode,currentColumn,UID)
   listLength = len(displayRecord)                                   # listlength = return the number of items in displayRecord
   if listCode == "u":                                               # If listCode is equal to 'u' Then:
      startPoint = 2                                                 # Set startPoint equals to '2'
      changeIndex = +1                                               # ChangeIndex add 1 (+1)
   else:
      startPoint = 0
      changeIndex = -1
   for item in range(startPoint,listLength,2):
      try:
         print(displayRecord[item],"   ",displayRecord[item+1])
      except IndexError:
         print(displayRecord[item])
   
   index = input("IDs are indexed from upper-left to lower-right starting from 1.\nChoose a user ID:")
   if index.isdecimal():
      return currentRecord[int(index)+changeIndex]
   else:
      code = 0
      message(code)

def gettenantID(UID,userType):                                                #define gettenantID function
   if UID:
      with open("currentUser.txt","r") as uRead:                     #fetch existing UID
         userRecord = uRead.read().split(",")
         return userRecord[2]
   else:
      while True:
         if userType == "new":
            number = 1
         else:
            path = input("[1]-Generate new ID or [2]-Choose existing ID:\n")
            if path.isdecimal():
               number = int(path)
            else:
               code = 1
               message(code)
         if number == 1:
            return dt.datetime.now().strftime("%d%m%Y%H%M%S%f")
         elif number == 2:
            listCode = "u"
            displayColumn = 0
            currentColumn = 2
            return chooseItem(UID,listCode,displayColumn,currentColumn)
         else:
            code = 0 
            message(code)

def getname(code,nameType):                                           #define getname function
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
   specials = specialCharacterList(None)
   while True:
      referenceNumber = input("Reference number comes from their relevant bank transaction. They cannot repeat.\nEnter the reference number :\n")
      if len(referenceNumber) > 5:
         for location in referenceNumber:
            if location not in specials:
               if (location.isnumeric() or (location.isnumeric() and location.isupper())for location in referenceNumber):
                  code = None
                  continue
               else:
                  code = 1
                  break
            else:
               code = 2
               break
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
            UserID  = gettenantID(UID,"existing")                         #Get input for tenant data
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
            list = [UserID,name,gender,pNum,nationality,startDate,workHistory,employer,income,rental,birthDate,birthCity]   #Declare list containing relevant input data
         else:
            referenceNumber = getreferenceNumber(code)
            transactionDate = getDate(code,"transaction")
            UserID  = gettenantID(UID,"existing")
            #Declare arguments for choosing apartment code
            chooseList = "a"
            displayColumn = 0
            currentColumn = 1
            apartmendCode = chooseItem(UID,chooseList,displayColumn,currentColumn)
            amount = getdecimal(code)
            list = [referenceNumber,transactionDate,UserID,apartmendCode,amount]
         appendFile(list,listCode)
      break

def tenantAndApartment():                                   #define tennantAndApartment function
   listCode = "p"
   reference1 = "t"
   reference2 = "a"
   primaryKeys = [] #[[]]
   TAList = []
   with open(listIdentifier(listCode),"r") as pRead:
      file = pRead.readlines()
      for record in file:
         list = record.split(",")
         if str(list[2]+","+list[3]) not in primaryKeys:
            primaryKeys.append(list[2]+","+list[3])
         else:
            continue
   for item in primaryKeys:
      TARecord = []
      tenantID,ApartmentCode = item.split(",")
      with open(listIdentifier(reference1),"r") as tRead:
         file = tRead.readlines()
         for record in file:
            list = record.split(",")
            if tenantID in list[0]:
               TARecord.append(list[0]+","+list[1])
               break
            else:
               continue
      with open(listIdentifier(reference2),"r") as aRead:
         file = aRead.readlines()
         for record in file:
            list = record.split(",")
            if ApartmentCode in list[1]:
               TARecord.append(list[1]+","+list[0]+","+list[3])
               break
            else:
               continue
      TAList.append(str(TARecord).lstrip("[").rstrip("]")) 
   for item in TAList:
      print(item)
      
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

# - Apartment - Chiu Wai Kin TP065600 (Need to delete)

def apartment(UID,listCode,code):                              # Define apartment function
   
   listCode = "a"
   print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n- Apartment info: -")
   
   # Put sample data
   list1 = ["Room Info: Standard Room (Triple)","Code: SR1","Dimensions: 140+ sqft","Pricing: RM350","Apartment ID: A01-L01-R01 to A01-L01-R21","Date of Acquisition: 03/01/2015","Rental History: 27/02/2015 rent","Status: Available"]        # Put sample data
   list2 = ["Room Info: Standard Room (Twin)","Code: SR2","Dimensions: 120+ sqft","Pricing: RM450","Apartment ID: A01-L01-R22 to A01-L01-R41","Date of Acquisition: 10/02/2015","Rental History: 28/03/2015 rent","Status: Available"]          # Put sample data
   list3 = ["Room Info: Standard Room A/C (Triple)","Code: SR3","Dimensions: 150+ sqft","Pricing: RM550","Apartment ID: A01-L02-R01 to A01-L02-R21","Date of Acquisition: 21/03/2016","Rental History: 24/04/2016 rent","Status: Available"]    # Put sample data
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
   ApartmentList = [list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12,list13,list14,list15,list16]      # Apply data at the list
   with open(listIdentifier(listCode),"w") as apartmentHandler:                              # Open text file and named as apartmentHandler 
      for record in ApartmentList:
         for data in record:
            apartmentHandler.write(data)                                                     # Write data into the text file
            apartmentHandler.write(",")                                                      # Write a comma (,) into the text file
         apartmentHandler.write("\n")                                                        # Write a newline ("\n") into the text file 
   
   for item in ApartmentList:
      print(item,"\n")                                                                       # Print each item that inside the ApartmentList  
   print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
   if UID == None:
      modifyData(UID,listCode,code,None)                                                     # Call function modifyData(UID,listCode,code,None)
   else:
      return False

def modifyData(UID,listCode,code,modifyType):                                                # Define modifyData function
   modify = True
   while True:                                                                               # Run loop with the condition is 'True'
      if modifyType:
         dataInput = modifyType
      else:
         dataInput = input('\n- Modification of records: -\n\n1. Add data\n2. Edit Data\n3. Delete Data\n4. Exit\n\nPlease select which operation to perform task (1-4): ')
      print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
      if dataInput == "1":
         if listCode == "a":
            apartmentAddData(modify,listCode)                                                # Call apartmentAddData(modify,listcode) functiom
         else:
            tenantOrTransactionEntryForm(UID,listCode,code)                                  # Call tenantOrTransactionEntryForm(UID,listCode,code) function
      elif dataInput == "2":
         editData(UID,listCode,code)                                                         # Call editData(UID,listCode,code) function
      elif dataInput == "3":
         deleteRecord(listCode,code)                                                         # Call deleteRecord(listCode,code) function
      elif dataInput == "4":
         break                                                                               # Break and end the loop
      else:
         code = 1                                                                            # Error detected
         message(code)                                                                       # Error message
         continue                                                                            # Jump back to the top of loop, Rerun again 
      if UID == None:
         continue                                                                            # Jump back to the top of loop, Rerun again
      else:
         break                                                                               # Break and end the loop
   
def apartmentAddData(modify,listCode):                                                       # Define apartmentAddData function
   adddatalist = []
   print("\nDear admin, we need your ATTENTION !\n\nFor your information, all the new data will only be stored if you insert each information with the correct format provided.\n\nOnce you finish each entry,a confirmation message will appear. Please ensure that the data is typed correctly before saving.\n- Now, you are required to enter new data. -\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
   newroom = newRoom()
   newroomcode = newRoomCode()
   newroomdimension = newRoomDimension()
   newroompricing = newRoompricing()
   newroomID = newRoomID()
   newroomdateofacquisition = newRoomDate("Acquisition")     
   newroomrentalhistory = newRoomDate("History")
   newroomstatus = newRoomStatus()
   adddatalist = [str(newroom),str(newroomcode),str(newroomdimension),str(newroompricing),str(newroomID),str(newroomdateofacquisition),str(newroomrentalhistory),str(newroomstatus)]   # Apply data to the list
   print("\nNew Data:",adddatalist)                                                          # Print all the add data details to display and easier to make admin do their checking 
   addDataconfirmation = input("\nAre you sure with the records you inserted just now? Enter to continue, 'N' to unsave: ")
   if addDataconfirmation in ["N","n"]:
      adddatalist.clear()                                                                    # Clear all the data that inserted previously
   else:
      appendFile(adddatalist,listCode)                                                       # Append each record into the selected text file 
      print("\n- Data Saved -\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
   return modify                                                                             # Return modify function

def newRoom():                                                                               # Define newRoom function
   while True:                                                                               # Run loop with the condition is 'True'
      code = None                                                                            # Code set as 'None' 
      SCL = 'SCL2'                                                                           # Set specials as 'SCL2'
      specials = specialCharacterList(SCL)
      newRoom = input("\nRoom info only contains alphabets, no numbers and special characters [Except these special characters: '(' ')' '/' '-' ]\nExample: Dual Key Premium Rooms - Single Room\n\nRoom Info: ")    # Get input from admin

      if [character for character in newRoom if (character in specials)]:                    # 1st Data Validation - Check special characters 
         code = 2                                                                            # Error detected, code change from 'None' to '2'
         message(code)                                                                       # Print error message
         print("- Room info does not contain special character(s) -")                        # Error message explanation
         continue                                                                            # Jump back to the top of loop, rerun again 
      else:
         code = None                                                                         # Error not detected, remain the same value 'None'
      if 0 <= len(newRoom) < 6:                                                              # 2nd Data Validation - Input length check
         code = 2                                                                            # Error detected, code change from 'None' to '2'
         message(code)                                                                       # Print error message
         print("-  Refer to the Room Info to look for its details and format -")             # Error message explanation
         continue                                                                            # Jump back to the top of loop, rerun again 
      else:
         code = None                                                                         # Error not detected, remain the same value 'None'
      if newRoom.isdigit() and any(location.isdigit() for location in newRoom):              # 3rd Data Validation - Check numbers 
         code = 1                                                                            # Error detected, code change from 'None' to '1'
         message(code)                                                                       # Print error message
         print("- Room info does not contain number(s) -")                                   # Error message explanation
         continue                                                                            # Jump back to the top of loop, rerun again
      else:
         code = None                                                                         # Error not detected, remain the same value 'None'
      if code == None:                                                                       # No error detected, correct input                                                                       # No error detected, correct input                                                                 
         newRoom.title()                                                                     # Return where the first character in each word is uppercase
         decisionkey = input("Save data? (Enter to continue, 'N' to return back):")          # Confirmation message and get input from admin whether to save the record or not
         if decisionkey in ['N','n']:
            continue                                                                         # Jump back to the top of loop. rerun again
         else:
            return "New Room Info: " + newRoom                                               # End the loop and return newRoom
      else:
         code = 2                                                                            # Error detected, code change from 'None' to '2'
         message(code)                                                                       # Print error messsage
         print("- Please fill in the correct format for room info. Refer to the description above for its details and format -")  # Error message explanation
         continue                                                                            # Jump back to the top of loop, rerun again 

def newRoomCode():                                                                           # Define newRoomCode function
   while True:                                                                               # Run loop with the condition is 'True'
      code = None                                                                            # Code set as 'None' 
      newRoomCode = input("\nRoom code only contains alphanumeric (A combination of uppercased alphabet and number), and no special characters\nExample: DKPRS1\n\nRoom Code: ")    # Get input from admin
      if len(newRoomCode) <= 1 :                                                             # 1st Data Validation - Check empty input and length input
         code = 2                                                                            # Error detected, code change from 'None' to '2'
         message(code)                                                                       # Print error message
         print("- Room Code must contain at least 2 or more alphanumeric long -\n")          # Error message explanation
         continue                                                                            # Jump back to the top of loop, rerun again
      else:
         code = None                                                                         # Error not detected, remain the same value 'None'
      if newRoomCode.isalnum():                                                              # 2nd Data Validation - Check input contains alphanumeric or not
         code = None                                                                         # Error not detected, remain the same value 'None'
      else:
         code = 2                                                                            # Error detected, code change from 'None' to '2'
         message(code)                                                                       # Print error message
         print("- Please note that room code is only acceptable when it contains alphanumeric only-\n")  # Error message explanation
         continue                                                                            # Jump back to the top of loop, rerun again
      if code == None:                                                                       # No error detected, correct input                                                                   
         decisionkey = input("Save data? (Enter to continue, 'N' to return back): ")         # Save Data Confirmation Message
         if decisionkey in ['N','n']:                                                        # Get confirmation
            continue                                                                         # Jump back to the top of loop, rerun again
         else:
            return "New Room Code: " + newRoomCode                                           # End of loop and return newRoomCode
      else:
         code = 2                                                                            # Error detected, code change from 'None' to '2'
         message(code)                                                                       # Error message
         print("- Please fill in the correct format for room code. Refer to the description above for its details and format -")  # Error message explanation
         continue                                                                            # Jump back to the top of loop, rerun again

def newRoomDimension():                                                                      # Define newRoomDimension function
   while True:                                                                               # Run loop with the condition is 'True'
      code = None                                                                            # Code set as 'None' 
      newRoomDimension=input("\nRoom Dimension only contains numbers, no alphabets and special characters (The unit (in sqft) will be provided at the back)\nExample: 300(+sqft)\n\nRoom Dimension: ")   # Get input from admin 
      if len(newRoomDimension) == 0:                                                         # 1st Data Validation - Check empty input exist or not
         code = 5                                                                            # Error detected, incorrect input
         message(code)                                                                       # Error message
         print("- Please fill in the room dimension, and room dimension must have at least 100 or more sqft -\n")  # Error message explanation
         continue                                                                            # Jump back to the top of loop, rerun again
      else:
         code = None                                                                         # Error not detected, remain the same value 'None'
      if newRoomDimension.isdigit():                                                         # 2nd data Validation - Input check that only contain numbers  
         code = None                                                                         # Error not detected, remain the same value 'None'
      else:
         code = 2                                                                            # Error detected, incorrect input
         message(code)                                                                       # Error message
         print("- Room dimension must consist of number(s) -")                               # Error message explanation
         continue                                                                            # Jump back to the top of loop, rerun again
      if code == None:                                                                       # No error detected, correct input
         decisionkey = input("Save data? (Enter to continue, 'N' to return back):")          # Save Data Confirmation Message
         if decisionkey in ["N","n"]:                                                        # Get confirmation
            continue                                                                         # Jump back to the top of loop, rerun again
         else:
            return "Dimensions: " + newRoomDimension + "+ sqft"                              # End of loop and return newRoomDimension
      else:
         code = 2                                                                            # Error detected, code change from 'None' to '2'
         message(code)                                                                       # Print error message
         print("- Please fill in the correct format for room dimension. Refer to the description above for its details and format -\n")   # Error message explanation
         continue                                                                            # Jump back to the top of loop, rerun again

def newRoompricing():                                                                        # Define newRoompricing function
   while True:                                                                               # Run loop with the condition is 'True'
      code = None                                                                            # Code set as 'None' 
      newRoompricing=input("\nRoom Pricing only contain numbers, no special characters (The unit (in RM) will be provided at the front)\nExample: (RM)500\n\nRoom Pricing: ")    # Get input from admin
      if newRoompricing.isdigit():                                                           # Validation - Input check that only contain numbers 
         nRp=int(newRoompricing)                                                             # Convert to integer 
         if nRp >= 350:
            code = None                                                                      # No error detected, correct input
         else:
            code = 1                                                                         # Error detected, code change from 'None' to '1' 
            message(code)                                                                    # Print error messaage
            print("- Minimum starting price starts from RM350 and above -\n")                # Error message confirmation
            continue                                                                         # Jump back to the top of loop, rerun again
      else:
         code = 2                                                                            # Error detected, code change from 'None' to '2'
         message(code)                                                                       # Print error message
         print("- Please fill in the room pricing, it must be in numeric and the minimum starting price starts from RM350 and above -\n")  # Error message explanation
         continue                                                                            # Jump back to the top of loop, rerun again
      if code == None:                                                                       # No error detected, correct input                                                                       # No error detected, correct input
         decisionkey = input("Save data? (Enter to continue, 'N' to return back):")          # Confirmation message
         if decisionkey in ["N","n"]:                                                        # Get confirmation 
            continue
         else:
            return "Pricing: RM" + newRoompricing
      else:
         code = 2
         message(code)
         print("- Please follow the correct format for new room pricing. Refer to the description above to know its details and format -\n")
         continue

def newRoomID():
   while True:
      code = None
      newRoomID = input('\nThis is the correct format for RoomID: A(01)-L(01)-R(01)x(to)xA(99)-L(99)-R(99), x means space\nPlease enter the new Room ID: ')
      if 0 <= len(newRoomID) <= 25:
         print("\n- Please fill in the new room ID with the correct format -")
         continue
      else:
         if (newRoomID[0] == 'A' and newRoomID[3] == '-' and newRoomID[4] == 'L' and newRoomID[7] == '-' and newRoomID[8] == 'R' and newRoomID[11] == ' ' and newRoomID[12] == 't' and newRoomID[13] == 'o' and newRoomID[14] == ' ' and newRoomID[15] == 'A' and newRoomID[18] == '-' and newRoomID[19] == 'L' and newRoomID[22] == '-' and newRoomID[23] == 'R'):
            if ((newRoomID[1] and newRoomID[2] and newRoomID[5] and newRoomID[6] and newRoomID[9] and newRoomID[10] and newRoomID[16] and newRoomID[17] and newRoomID[20] and newRoomID[21] and newRoomID[24] and newRoomID[25]).isdigit):
               decisionkey = input("Save data? (Enter to continue, 'N' to return back):")
               if decisionkey in ["N","n"]:
                  continue
               else:
                  return "Apartment ID: " + newRoomID
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
      if dateType == "Acquisition":
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
      if code == None:                                                                       # No error detected, correct input
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
         return gettenantID(UID,"existing")
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
         return gettenantID(UID,"existing")
      elif editDataType == 3:
         chooseList = "a"
         displayColumn = 0
         currentColumn = 1
         return chooseItem(UID,chooseList,displayColumn,currentColumn)
      else:
         return getdecimal(code)

def ApartmentDataInfo():
   data = True
   while data == True:
      opt = input("\n[R] - Room Info [C] - Room code, [D] - Dimensions, [P] - Pricing, [A] - Apartment ID, [D] - Date of Acquisition, [H] - Rental History, [S] - Status \nAnswer: ")
      if opt in ["R","r"]:
         return 0
      elif opt in ["C","c"]:
         return 1
      elif opt in ["D","d"]:
         return 2
      elif opt in ["P","p"]:
         return 3
      elif opt in ["A","a"]:
         return 4
      elif opt in ["D","d"]:
         return 5
      elif opt in ["H","h"]:
         return 6
      elif opt in ["S","s"]:
         return 7
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
            message(code)
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
            message(code)
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

def replaceOldData(listCode,recordindex,editDataType,newData):
   with open(listIdentifier(listCode),"r") as Xhandler:
      updatedData = []
      newRecord = []
      dataRead = Xhandler.readlines()
      for record in dataRead:
         strippedRecord = record.rstrip(",\n").split(",")
         if dataRead.index(record) == int(recordindex):
            if newData:
               strippedRecord[int(editDataType)] = newData               #modify the record with new data
               newRecord = ",".join(strippedRecord)                         #capture the new record
               updatedData.append(newRecord+",\n")
            else:
               continue
         else:
            updatedData.append(record)
   with open(listIdentifier(listCode),"w") as fUpdate:
      for record in updatedData:
         fUpdate.write(record)
   return False

def editData(UID,listCode,code):
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
            selectedData = input("Placement of items displayed above are labeled from left to right starting from 1\nPlease enter the number of the item to edit:")
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
      newData = inputidentifier(UID,listCode,editDataType,code)
      editdataconfirmation = input("\nAre you sure with your records just now? ([Y]-Yes/[N]-No): ")
      if editdataconfirmation in ["Y","y"]:
         replaceOldData(listCode,recordindex,editDataType,newData)
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
               if listCode == "u":
                  if int(num) == 0:
                     displayList.append("ID: "+str(individualList[int(num)])+";relevant data: "+str(individualList[2]))
                  else:
                     displayList.append(individualList[int(num)])
               else:
                  if int(num) == 0:
                     displayList.append(individualList[int(num)])
                  else:
                     displayList.append("ID: "+str(individualList[0])+";relevant data: "+str(individualList[int(num)]))
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
      
def deleteRecord(listCode,code):
   while True:
      print("\n- Delete Data -")
      deletedata = input("\n1. Delete specified records\n2. Delete all records\n\n[E] - Exit\n\nPlease select and enter which operator that you want to proceed: ")
      if deletedata == '1':
         print("\n- 1. Delete specified records -")
         deleteSpecRecord(listCode,code)
      elif deletedata == '2':
         print("\n- 2. Delete all records -")
         deleteAllrecords(listCode,code)
      elif deletedata in ["E","e"]:
         break
      else:
         code = 0
         message(code)
         continue

def deleteSpecRecord(listCode,code):
   modify = True
   while True:
      readFile(listCode)
      selecteddatarow = input("\nWhich data row that you want to delete? ")
      if selecteddatarow.isdigit():
         number = int(selecteddatarow)-1
         editDataType = None
         newData = None
         replaceOldData(listCode,number,editDataType,newData)
      else:
         code = 0
         message(code)
         continue
      return modify

def deleteAllrecords():
   modify = None
   while modify == True:
      listCode = 'a'
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
         break
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
      print(searchColumn(listCode,num,UID))
      searchInformation(listCode,num,details)

def menu(UID,code):                                                # Define menu function
   mainMenu = True
   while mainMenu == True:
      if UID:
         print("\nMain menu:\n\n[S] - Search box\n\nReview information about:\n[A] - Available Apartments\n[T] - My Tenant details\n[P] - My Transactions\n\nQuick functions:\n[D] - Print my House & Tenant Details\n[E] - Exit")
      else:
         print("\nMain menu:\n\n[S] - Search box\n\nReview information about:\n[A] - Apartment\n[T] - Tenant\n[P] - Transaction\n\nQuick functions:\n[D] - Print Specific House & Tenant Details\n[I] - Inquiry of Past Tenant Details\n[E] - Exit")
      opt=input("\nPlease enter which operation that you want to do: ")
      if opt in ["S","s"]:
         searchBox(UID)                                        # Redirect to searchbox function
      elif opt in ["A","a"]:                                   # Check for basic Functions
         listCode = "a"
         apartment(UID,listCode,code)
      elif opt in ["P","p"]:
         listCode = "p"
         tenantOrTransaction(UID,listCode,code)
      elif opt in ["T","t"]:
         listCode = "t"
         tenantOrTransaction(UID,listCode,code)
      elif opt in ["D","d"]:                                   # Check for quick functions
         tenantAndApartment()
      elif opt in ["I","i"] and UID == None:
         listCode = "t"
         searchInformation(listCode,9,"Past")
      elif opt in ["L","l"] and UID == None:
         print("loginHistory()")
      elif opt in ["E","e"]:                                   # Get confirmation to exit
         exitconfirmationkey = input("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nYou're about to leave Tenant Management System. Are you sure? [Enter]-Continue, [x]-Return to main menu): ")
         if exitconfirmationkey in ["X","x"]:
            continue
         else:
            print("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nExit successful, have a nice day~\n")
            return False
      else:
         code = 0
         message(code)

import datetime as dt
login()