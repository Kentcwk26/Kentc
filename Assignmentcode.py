def login():                                   #define the login function
   print("\nWelcome to Tenant Management System Login page.\nPlease enter username and password to proceed.\n") 
   chance = 3                                  #Specify login chances
   while chance > 0:                           #iterate when there are more than 0 chances remaining
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
                  print("\n- Login successful -")
                  #check for admin credentials
                  if (username == "john" and password == "1234u-78") or (username == "david" and password == "55467913"):
                     masterKey = True        #activate masterKey
                     UID = None
                  else:
                     with open("currentUser.txt","w") as current:
                        current.write(record)
                     masterKey = False       #deactivate masterKey
                     UID = listRecord[2]
                  menu(masterKey,UID)        #redirect to menu
                  chance=0                   #empty login chances
                  break                      #break loop to avoid running error message
         else:
            chance-=1                        #decrease chances by 1
            print("\nError, incorrect username or password.\n"+chance+"chances remaining.\n")

def listIdentifier(listCode):
   if listCode == "t":
      l = "tenant.txt"
   elif listCode == "a":
      l = "Apartment.txt"
   else:
      l = "transaction.txt"
   return l

def appendFile(list,listCode):
   with open (listIdentifier(listCode), "a") as fAppend:
      for item in list:
         fAppend.write(item)
         fAppend.write(", ")
      fAppend.write("\n")

def readFile(listCode):
   with open (listIdentifier(listCode),"r") as fRead:
      string = fRead.readlines()
      for record in string:
            stripped = record.rstrip("\n").rstrip(",")
            splitRecord = stripped.split(",")
            print(splitRecord)

def tenant(masterKey,UID,listCode,code):
   if masterKey == False:
      num = 0
      searchInformation(listCode,num,UID)
   else:
      while True:
         opt = input("[D]-Display tenant Data, [M]-Modify Tenant Data")
         if opt in ["D","d"]:      
            print("Current Tenant Data:")
            readFile(listCode)
         elif opt in ["M","m"]:
            modifyData(masterKey,listCode,code)
         return False

def tenantEntryForm(masterKey,listCode):          #Define tenantEntryForm function
   if masterKey == True:
      n = input("Number of new tenants: ")
   else:
      n = 1
   for tenantList in range(n):
      #Get input for tenant data
      tenantID = gettenantID(masterKey)
      name = getname()
      gender = getgender()
      pNum = getpNum()
      nationality = getnationality()
      startDate = getstartDate()
      income = getincome()
      rental = getrental()
      #Apply data to end of list 
      tenantList = [tenantID,name,gender,pNum,nationality,startDate,income,rental]
      #Return the list
      appendFile(tenantList,listCode)

def gettenantID(masterKey):
   if masterKey == False:
      #fetch existing UID
      with open("user.txt","r") as uRead:
         userRecord = uRead.read().split(",")
         return userRecord[2]
   else:
      # generate new UID
      UID = dt.datetime.now().strftime("%Y%m%d%H%M%S%f")
      return UID

def getname():
   while True:
      code = None
      name = input("Format: Name Name.....\nEnter tenant fullname:\n")
      if type(name) != int:
         nameList = name.split(" ")
         if len(nameList) >= 2:
               for words in nameList:
                  print("Checking",words)
                  if words[0].islower():
                     code = 2
                     message(code)
                     break
                  else:
                     continue
         else:
            code = 3
            message(code)
      else:
         code = 1
         message(code)
      if code:
         print("Error was detected.\n")
      else:
         print("No errors detected.\n")
      retry = input("[R]-Retry,[Any other key]-Exit using "+name+"\n")
      if retry in ["R","r"]:
         continue
      else:
         return name

def getgender():
   gender = input("Enter tenant gender: (m/f):\n")
   genderCheck = gender
   if genderCheck.len == 1:
      if type(genderCheck) != str:
         code = 1
         message(code)
   else: 
      code = 3
      message(code)
   return gender

def getpNum():
   pNum = input("Enter tenant phone number: (############):\n")
   pNumCheck = pNum
   for digit in pNumCheck:
      if type(digit) != int():
         continue
      else:
         code = 1
         message(code)
   return pNum

def getnationality():
  while True:
      nationality = input("Enter tenant nationality: (M: Malaysian/N: non-Malaysian):\n")
      nationalityCheck = nationality
      if len(nationalityCheck) == 1:
         if type(nationalityCheck) == str:
            continue
         else:
            code = 1
            message(code)
      else: 
         code = 3
         message(code)
      return nationality

def getstartDate():
   startDate = input("Enter Rental start date: (YYYY,MM,DD):\n")

   return startDate

def getincome():
   income = input("Enter tenant income range(RM):\n")

   return income

def getrental():
   rental = input("Enter tenant rental status(current/past)\n")
   return rental

def message(code):
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
      print("\n"+x+"zero input"+z)

def specialCharacterList():
   return['"',"{","}","<",">","!","@","#","$","%","^","&","*","?",":",";","'","+","=","-","_","]","[","/"]

def apartment(masterKey,listCode,code):                        #Define apartment function
   
   print("\nApartment info:\n")
   record=[]
   
   #Put sample data
   list1=["Tyoe: Standard Room (Triple)","Code: SR1","Dimensions: 140+ sqft","Pricing: RM350","Number of Rooms: 20","Apartment ID: A01-L01-R01 to A01-L01-R21, Date of Acquisition: 03/01/2015, Rental History: 27/02/2015 rent, Status: Available"]
   list2=["Tyoe: Standard Room (Twin)","Code: SR2","Dimensions: 120+ sqft","Pricing: RM450","Number of Rooms: 20","Apartment ID: A01-L01-R22 to A01-L01-R41, Date of Acquisition: 10/02/2015, Rental History: 28/03/2015 rent, Status: Available"]
   list3=["Tyoe: Standard Room A/C (Triple)","Code: SR3","Dimensions: 150+ sqft","Pricing: RM550","Number of Rooms: 20","Apartment ID: A01-L02-R01 to A01-L02-R21, Date of Acquisition: 21/03/2016, Rental History: 24/04/2016 rent, Status: Available"]
   list4=["Tyoe: Standard Room A/C (Twin)","Code: SR4","Dimensions: 130+ sqft","Pricing: RM650","Number of Rooms: 20","Apartment ID: A01-L02-R22 to A01-L02-R41, Date of Acquisition: 02/04/2016, Rental History: 20/05/2016 rent, Status: Available"]
   list5=["Type: Deluxe Room (Triple)","Code: DR1","Dimensions: 170+ sqft","Pricing: RM750","Number of Rooms: 20","Apartment ID: A01-L04-R01 to A01-L04-R21, Date of Acquisition: 11/05/2017, Rental History: 21/06/2017 rent, Status: Available"]
   list6=["Type: Deluxe Room (Twin)","Code: DR2","Dimensions: 160+ sqft","Pricing: RM840","Number of Rooms: 20","Apartment ID: A01-L04-R22 to A01-L04-R41, Date of Acquisition: 22/06/2017, Rental History: 22/07/2017 rent, Status: Available"]
   list7=["Type: Deluxe Room A/C with shared attached bath / toilet (Triple)","Code: DR3","Dimensions: 180+ sqft","Pricing: RM950","Number of Rooms: 20","Apartment ID: A01-L03-R1 to A01-L03-R21, Date of Acquisition: 30/07/2018, Rental History: 25/08/2018 rent, Status: Available"]
   list8=["Type: Deluxe Room A/C with shared attached bath / toilet","Code: DR4","Dimensions: 170+ sqft","Pricing: RM1040","Number of Rooms: 20","Apartment ID: A01-L03-R22 to A01-L03-R41, Date of Acquisition: 16/08/2018,, Rental History: 18/09/2018 rent, Status: Available"]
   list9=["Type: Compact Premium Single","Code: CPS","Dimensions: 130+ sqft","Pricing: RM690","Number of Rooms: 20","Apartment ID: A01-L05-R01 to A01-L05-R41, Date of Acquisition: 02/09/2019, Rental History: 29/10/2019 rent, Status: Available"]
   list10=["Type: Medium Premium Single","Code: MPS","Dimensions: 150+ sqft","Pricing: RM750","Number of Rooms: 20","Apartment ID: A02-L01-R01 to A02-L01-R21, Date of Acquisition: 15/10/2019, Rental History: 31/11/2019 rent, Status: Available"]
   list11=["Type: Medium Premium Twin","Code: MPT","Dimensions: 180+ sqft","Pricing: RM890","Number of Rooms: 20","Apartment ID: A02-L02-R01 to A02-L02-R21, Date of Acquisition: 25/11/2020, Rental History: 31/12/2020 rent, Status: Available"]
   list12=["Type: Medium Premium with attached bath / toilet (Twin)","Code: MP1","Dimensions: 180+ sqft","Pricing: RM940","Number of Rooms: 20","Apartment ID: A02-L03-R01 to A02-L03-R21, Date of Acquisition: 30/12/2020, Rental History: 31/01/2020 rent, Status: Available"]
   list13=["Type: Medium Premium with attached bath / toilet (Single)","Code: MP2","Dimensions: 160+ sqft","Pricing: RM1050","Number of Rooms: 20","Apartment ID: A02-L03-R22 to A02-L03-R41, Date of Acquisition: 16/01/2021, Rental History: 28/02/2021 rent, Status: Available"]
   list14=["Type: En-Suite Single (Super Premium - Triple)","Code: ESS3","Dimensions: 160+ sqft","Pricing: RM700","Number of Rooms: 20","Apartment ID: A02-L04-R01 to A02-L04-R41, Date of Acquisition: 25/02/2021, Rental History: 31/03/2021 rent, Status: Available"]
   list15=["Type: En-Suite Single (Super Premium - Twin)","Code: ESS2","Dimensions: 140+ sqft","Pricing: RM800","Number of Rooms: 20","Apartment ID: A02-L04-R01 to A02-L04-R41, Date of Acquisition: 31/05/2022, Rental History: Empty, Status: Not Available"]
   list16=["Type: En-Suite Twin (Super Premium)","Code: EST2","Dimensions: 200+ sqft","Pricing: RM900","Number of Rooms: 20","Apartment ID: A02-L05-R01 to A02-L05-R41, Date of Acquisition: 26/06/2022, Rental History: Empty, Status: Not Available"]

   #Apply data at the list
   record.append(list1)
   record.append(list2)
   record.append(list3)
   record.append(list4)
   record.append(list5)
   record.append(list6)
   record.append(list7)
   record.append(list8)
   record.append(list9)
   record.append(list10)
   record.append(list11)
   record.append(list12)
   record.append(list13)
   record.append(list14)
   record.append(list15)
   record.append(list16)

   for item in record:
      print(item)

   with open("Apartment.txt","w") as Ahandler:
      for item in record:
         for data in item:
               Ahandler.write(data)
               Ahandler.write(",")
         Ahandler.write("\n")

   if masterKey == True:
      modifyData(masterKey,listCode,code)

   else:
      return False

def modifyData(masterKey,listCode,code):
  while True:
      print("\n1. Add data\n2. Edit Data\n3. Delete Data\n4. Exit\n")
      dataInput=int(input('Please select which operation to perform task (1-4): '))

      if dataInput==1:
         print("\n- Add Data -")
         if listCode == "a":
            apartmentAddData(listCode,code)
         elif listCode == "t":
            tenantEntryForm(masterKey,code)
         else:
            print("transactionEntryForm()")

      elif dataInput==2:
         print("\n- Edit Data -")
         apartmentEditData()

      elif dataInput==3:
         print("\n- Delete Data -")
         apartmentDeleteData()

      elif dataInput==4:
         print("\n- Exit -")
         return False

      else:
         code=2
         message(code)
         print("\n---------------------------------------------------------------------------------------------------\n\n- Tenant Management System -")
         return True

def apartmentAddDataNum(code,specials):
   while True:
      nospecialcharacter=0
      adddata = input('\nDear admin, how many records that you decide to add? ')
      if len(adddata) == 1:
         for location in adddata:
            for character in specials:
               if location == character:
                  nospecialcharacter = 1
                  code = 0
                  message(code)
                  print("- Special character(s) exist -\n")
                  return True
               else:
                  nospecialcharacter = 0
         if adddata.isdigit() and nospecialcharacter == 0:
            return adddata
         else:
            code=1
            message(code)
            print("- Please enter a number -\n")
            return True
      else:
         code=0
         message(code)

def apartmentAddData(listCode,code):
   specials = specialCharacterList()
   adddatanum = apartmentAddDataNum(code,specials)
   if adddatanum == 0:
      code=0
      message(code)
      print("- Error, cannot insert zero records -")
      return True
   else:
      adddatalist=[]
      print("\n- Dear admin, we need your Attention! -\n\nFor your information, all the new data will be only stored if Admin insert the information with the correct format for each new data entry provided.\n\nNew room info: only contains alphabets, no numbers and special characters [Except these: ( ) / - ]\nExample: Dual Key Premium Rooms - Single Room\n\nNew room code: only contains alphanumeric (A combination of Uppercased alphabet and number), and no special characters\nExample: DKPRS1\n\nNew Room Dimension (in range sqft): only contains numbers, no special characters (The unit will be provided at the back)\nExample: 300(+sqft)\n\nNew Room Pricing (in RM): only contain numbers, no special characters (The unit will be provided at the front)\nExample: (RM)500\n\nNumber of new rooms: only contains numbers and no special characters\nExample: 10 (Accepted range: 1-99)\n\nNew Apartment ID: A(01)-L(01)-R(01)x(to)xA(99)-L(99)-R(99)\nPlease follow this format as written above (A stands for Apartment Block, L stands for Room Level, R stands for Room Number, x means space)")
      print("\nNow, you are required to enter new data after reading the message.\n")
      for adddatanum in [0,adddatanum]:
         newroom=newRoom(code,specials)
         newroomcode=newRoomCode(code,specials)
         newroomdimension=newRoomDimension(code,specials)
         newroompricing=newRoompricing(code,specials)
         newnumberofRooms=newNumberofRooms(code)
         newroomID=newRoomID(code,specials)
         newroomdateofacquisition=newRoomDateofAcquisition(code,specials)
         newroomrentalhistory=newRoomRentalHistory(code,specials)
         newroomstatus=newRoomStatus(code,specials)
         adddatalist.append("New Room Info: "+str(newroom))
         adddatalist.append("New Room Code: "+str(newroomcode))
         adddatalist.append("New Room Dimension in range (sqft): "+str(newroomdimension)+'+ sqft')
         adddatalist.append("New Room Pricing: RM"+str(newroompricing))
         adddatalist.append("Number for the new room: "+str(newnumberofRooms))
         adddatalist.append("New room Apartment ID: "+str(newroomID))
         adddatalist.append("New room Acquisition Date: "+str(newroomdateofacquisition))
         adddatalist.append("New room Rental History: "+str(newroomrentalhistory)+" rent")
         adddatalist.append("New room Status: "+str(newroomstatus))
         print("\nNew Data:",adddatalist)
         apartmentadddataconfirmation(adddatalist,listCode)
      return False

def newRoom(code,specials):
   while True:
      nonumber=0 ; nospecialcharacter=0 ; emptymessage = 0 ; acceptableinput = 0
      newRoom=input("New room Info: ")
      if len(newRoom) == 0:
         code=5
         message(code)
         print("- Please fill in the new room info -\n")
         continue
      else:
         emptymessage = 0
             
      if len(newRoom) <= 5:
         code=3
         message(code)
         print("- New room info does not have a short information name -\n")
         continue
      else:
         acceptableinput=1

      if any(location.isdigit() for location in newRoom):
         code=0
         message(code)
         print("- New room info does not contain number(s) -\n")
         continue
      else:
         nonumber = 1

      for location in newRoom:
         for character in specials:
            if location == character:
               nospecialcharacter = 0
               code = 0
               message(code)
               print("- New room info does not have special character(s) -\n")
               return True
            else:
               nospecialcharacter = 1

      if nonumber == 1 and nospecialcharacter == 1 and emptymessage == 0 and acceptableinput == 1:
         return newRoom
      else:
         code=2
         message(code)
         print("- Please insert the correct format for the new room information. Refer to the description above to know its format and details. -\n")
         continue

def newRoomCode(code,specials):
   while True:
      uppercased = 0 ; alnum = 0 ; nospecialcharacter = 0 ; nospecialcharacter = 0 ; emptymessage = 1
      newRoomCode = input("New Room Code: ")

      if len(newRoomCode) <= 1 :
         code=2
         message(code)
         print("- New Room Code must contain at least 2 or more alphanumeric long -\n")
         continue
      else:
         emptymessage=0

      if newRoomCode[0:1].isupper() and newRoomCode.isalnum():
         uppercased = 1
         alnum = 1
      else:
         code=2
         message(code)
         print("- Please noted that new room code is only acceptable when it contains alphanumeric with uppercased alphabet(s) and number(s) -\n")
         continue

      for location in newRoomCode:
         for character in specials:
            if location == character:
               nospecialcharacter = 0
               code = 0
               message(code)
               print("- New apartment code only contains alphanumeric and does not have special character(s) -\n")
               continue
            else:
               nospecialcharacter = 1

      if uppercased == 1 and alnum == 1 and nospecialcharacter == 1  and emptymessage == 0:
         return newRoomCode
      else:
         code = 2
         message(code)
         print("- Please fill in the correct format for new Apartment code. Refer to the New Room Pricing to look for its details and format --")
         continue

def newRoomDimension(code,specials):
   while True:
      emptymessage=1 ; nospecialcharacter=0 ; correctmessage=0
      newRoomDimension=input("New Room Dimension in range (sqft): ")
      if len(newRoomDimension) == 0:
         code=5
         message(code)
         print("- Please fill in the new room dimension -\n")
         continue
      else:
         emptymessage=0

      if len(newRoomDimension) <= 2:
         code=3
         message(code)
         print("- Room dimension must have at least 100 or more sqft -\n")
         continue
      else:
         correctmessage=1

      for location in newRoomDimension:
         for character in specials:
            if location == character:
               nospecialcharacter = 1
               code = 0
               message(code)
               print("- New apartment info does not have special character(s) -\n")
               continue
            else:
               nospecialcharacter = 0

      if newRoomDimension.isdigit() and emptymessage == 0 and nospecialcharacter == 0 and correctmessage == 1:
         return newRoomDimension
      else:
         code=2
         message(code)
         print("- Please fill in the correct format for new room dimension. Refer to the top description for its details and format -\n")
         continue

def newRoompricing(code,specials):
   while True:
      emptymessage = 1 ; nospecialcharacter = 0 ; correctmessage = 0
      newRoompricing=input("New Room Pricing (in RM): ")
      if len(newRoompricing) == 0:
         code = 5
         message(code)
         print("- Please fill in the new room pricing -\n")
         continue
      else:
         emptymessage = 0

      if len(newRoompricing) <= 2 and newRoompricing.isdigit():
         code = 3
         message(code)
         print("- Room pricing must be in numeric and the starting price starts from RM100 -\n")
         continue
      else:
         correctmessage = 1

      for location in newRoompricing:
         for character in specials:
            if location == character:
               nospecialcharacter = 1
               code = 0
               message(code)
               print("- New apartment info does not have special character(s) -\n")
               continue
            else:
               nospecialcharacter = 0

      if newRoompricing.isdigit() and emptymessage == 0 and nospecialcharacter == 0 and correctmessage == 1:
         return newRoompricing
      else:
         code=2
         message(code)
         print("- Please fill in the correct format for new room pricing. Refer to the description above to look for its details and format -\n")
         continue

def newNumberofRooms(code):
   while True:
      emptymessage = 1 ; correctmessage = 0 ; number = 0
      newNumberofRooms=input("Number of new rooms: ")
      if len(newNumberofRooms) == 0:
         code = 5
         message(code)
         print("- Please fill in the number of new rooms -\n")
         continue
      else:
         emptymessage = 0

      if len(newNumberofRooms) >= 3 and newNumberofRooms.isdigit():
         code = 3
         message(code)
         print("- Number of new rooms must be in numeric -\n")
         continue
      else:
         correctmessage = 1

      if newNumberofRooms.isdigit():
         number = 1
      else:
         code=0
         message(code)
         print("- Number of new rooms contain number(s) -\n")
         continue

      if emptymessage == 0 and correctmessage == 1 and number == 1:
         return newNumberofRooms
      else:
         code=2
         message(code)
         print("- Please fill in the correct format for the number of new rooms. Refer to the description above to look for its details and format -\n")
         continue

def newRoomID(code,specials):
   while True:
      lennewAparID = 0 ; notlowercase = 0 ; newAparIDdash = 0 ; emptymessage = 1
      newRoomID = input("New Room Apartment ID: ")

      if len(newRoomID) == 0:
         code = 5
         message(code)
         print("- Please fill in the new Apartment ID -\n")
         continue
      else:
         emptymessage = 0

      if len(newRoomID)>26 or len(newRoomID)<1:
         code = 2
         message(code)
         print("- Please follow the format as: A01-L10-R40 to A02-L01-R09 -\n - A stands for Apartment Block, L stands for Level, and R stands for Room (The length must have 11 characters long, including the dash -) -\n")
         continue
      else:
         lennewAparID = 1

      if newRoomID[0:4:8].islower():
         code=2
         message(code)
         print("- Must contain uppercase, not lower case -\n")
         continue
      else:
         notlowercase = 3

      if (newRoomID[3] and newRoomID[7] and newRoomID[18] and newRoomID[22]) == specials[19]:
         newAparIDdash = 4 
      else:
         code=2
         message(code)
         print("- Please include the dash inside the apartment ID -\n")
         continue
         
      if lennewAparID == 1 and notlowercase == 3 and newAparIDdash == 4 and emptymessage == 0 :
         return newRoomID
      else:
         code=3
         message(code)
         print("- Please fill in the correct format for new room Apartment ID. Refer to the description above to look for its details and format -")
         continue         

def newRoomDateofAcquisition(code,specials):
   while True:
      nospecialcharacter = 1 ; correctmessage = 0 ; number = 1 ; symbol = 0
      newRoomDateOfAcquisition = input("New Room Date of Acquisition: ")
      if 0 < len(newRoomDateOfAcquisition) < 9 or len(newRoomDateOfAcquisition) >=11:
         code = 3
         message(code)
         print("- Please reenter the acquisiition date for the new room and follow the correct format (29/12/9999), consists 10 characters long -\n")
         continue
      else:
         correctmessage = 1
      for location in newRoomDateOfAcquisition:
         for character in specials:
            if location == character:
               nospecialcharacter = 0
               code = 0
               message(code)
               print("- New room acquisiition date does not contain special character(s) except this symbol: / -\n")
               continue
            else:
               nospecialcharacter = 1
      if ((newRoomDateOfAcquisition[2] and newRoomDateOfAcquisition[5]) == specials[23]) and any(location.isdigit() for location in newRoomDateOfAcquisition):
         number = 1 ; symbol = 1
      else:
         code=0
         message(code)
         print("- New room acquisiition date does not contain number(s) -\n")
         continue
      if nospecialcharacter == 1  and correctmessage == 1 and number == 1 and symbol == 1:
         return newRoomDateOfAcquisition
      else:
         code = 2
         message(code)
         print("Please insert the correct format for new room acquisition date. Refer to the top description to let its details and format -\n")
         continue

def newRoomRentalHistory(code,specials):
   while True:
      nospecialcharacter = 1 ; correctmessage = 0 ; number = 1 ; symbol = 0
      newRoomRentalHistory = input("New Room Rental History: ")
      if 0 < len(newRoomRentalHistory) < 9 or len(newRoomRentalHistory) >=11:
         code = 3
         message(code)
         print("- Please reenter the new room rental history and follow the correct format (29/12/9999), consists 10 characters long -\n")
         continue
      else:
         correctmessage = 1
      for location in newRoomRentalHistory:
         for character in specials:
            if location == character:
               nospecialcharacter = 0
               code = 0
               message(code)
               print("- New room rental history does not contain special character(s) except this symbol: / -\n")
               continue
            else:
               nospecialcharacter = 1
      if ((newRoomRentalHistory[2] and newRoomRentalHistory[5]) == specials[23]) and any(location.isdigit() for location in newRoomRentalHistory):
         number = 1 ; symbol = 1
      else:
         code=0
         message(code)
         print("- New room rental history must contain number(s) -\n")
         continue
      if nospecialcharacter == 1  and correctmessage == 1 and number == 1 and symbol == 1:
         return newRoomRentalHistory
      else:
         code = 2
         message(code)
         print("Please insert the correct format for new room rental history. Refer to the top description to let its details and format -\n")
         continue

def newRoomStatus(code,specials):
   while True:
      message = 0 ; nospecialcharacter = 0 ; number = 1 ; phrase = 0
      newRoomStatus = input("New Room Status: ")
      if len(newRoomStatus) == 0 or len(newRoomStatus) >= 3:
         code = 3
         message(code)
         print("- Please reenter the new room rental history and follow the correct format (29/12/9999), consists 10 characters long -\n")
         continue
      else:
         message = 1
      if any(location.isdigit() for location in newRoomStatus):
         code=3
         message(code)
         print("- New Room Status does not contain number -\n")
         continue
      else:
         number = 0
      for location in newRoomStatus:
         for character in specials:
            if location == character:
               nospecialcharacter = 0
               code = 0
               message(code)
               print("- New room rental history does not contain special character(s) except this symbol: / -\n")
               continue
            else:
               nospecialcharacter = 1
      if newRoomStatus in ["Available","Not Available"]:
         phrase=1
      else:
         code=0
         message(code)
         print("- Room Status can only b eaccepted either the input is 'Available' or 'Not Available'. -\n")
         continue
      if message == 1 and number == 0 and nospecialcharacter == 1 and phrase == 1:
         return newRoomStatus
      else:
         code = 3
         message(code)
         print("Please insert the correct format for new room status. Refer to the top description to let its details and format -\n")
         continue

def apartmentadddataconfirmation(adddata,listCode):
   listCode = "a"
   while True:
      addDataconfirmation=int(input("\nAre you sure with the records you inserted just now? Enter '1' to save record, Enter '0' to unsave record: "))
      if addDataconfirmation == 1:
         appendFile(adddata,listCode)
         print("\n- Data Saved -")

      addDataconfirmation2=input("\nAre you going to add more data? Yes/No: ")
      if addDataconfirmation2 == 'Yes':
         print("\n- Continue to add more data -\n")
         return True
      elif addDataconfirmation2 == 'No':
         print("\n- Modification of Records (Apartment) -")
         return False
      else:
         code=0
         message(code)
         return True

def Apartmentadddatarewrite():
   rewriteDataConfirmation=input("\nEnter 'W' to rewrite the data again, Enter any key to exit: ")
   if rewriteDataConfirmation == 'W':
      return True
   else:
      print("Return to main menu")
      return False

def apartmentEditData():
   editdatanum=int(input('How many records that you decide to edit? '))

def apartmentDeleteData():
   deletedatanum=int(input('How many records that you decide to delete? '))

def searchBox():                             #Define search function
   print("\nWelcome to search box!")
   while True:
      print("\n1. Search room specific details.\n2. Search transaction details.\n3. Search specific tenant details.\n4. Exit search box.\n")
      option=int(input("Please type the search criteria based on the listing above: "))
      if option == 1:
         listCode= "a"
         opt = input("\n[C]-Room code, [P]-Pricing, [N]-Number of Rooms, [A]- Apartment ID, [D]-Date of Acquisition, [R]-Rental \n")     
         if opt in ["A","a"]:
            num = 1
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
            num = 8
         else:
            code = 0
            message(code)

      elif option == 2:
         listCode = "p"
         opt = input("\n[R]-Reference number,[D]-Transaction date,[T]-TenantID,[A]-Apartment code,[S]-Amount: ")
         if opt in ["R","r"]:
            num = 0
         elif opt in ["D","d"]:
            num = 1
         elif opt in ["T","t"]:
            num = 2
         elif opt in ["A","a"]:
            num = 3
         elif opt in ["S","s"]:
            num = 4
         else:
            code = 0
            message(code)     
      
      elif option == 3 :
         listCode = "t"
         opt = input("\n[N]-Name,[G]-Gender,[P]-Phone number,[R]-Nationality,[D]-Rental start date,[I]-Income,[S]-Tenant status: ")
         if opt in ["N","n"]:
            num = 0
         elif opt in ["G","g"]:
            num = 1
         elif opt in ["P","p"]:
            num = 2
         elif opt in ["R","r"]:
            num = 3
         elif opt in ["D","d"]:
            num = 4
         elif opt in ["I","i"]:
            num = 5
         elif opt in ["S","s"]:
            num = 6
         else:
            code = 0
            message(code)

      elif option == 4:
         print("\nReturn to main menu\n\n--------------------------------")
         return False                                 #return to menu function
      
      else:
         code = 0
         message(code)
      details = None
      searchInformation(listCode,num,details)

def searchInformation(listCode,num,details):                  #Define searchinformation function
   while True:
      if details:
         searchInformation == details
      else:
         searchInformation=input("\nPlease enter text to begin the search: ")
      recordExist = False
      with open(listIdentifier(listCode),"r") as Xhandler:
         print("\nResults:\n")
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

      exitSearch=input("\nExit program?\n[C]-Continue Program.\n[Any other key]-Exit: ")
      if exitSearch in ["C","c"]:
         continue
      else:
         return False

def menu(masterKey,UID):                                  #Define menu function
   while True:
      code = None

      if masterKey == False:
         print("\nWelcome Tenant, you are now entering Tenant Management System (Tenant Page)\n\n[S] - Search box\n\nReview information about:\n\n[A] - Apartment\n[P] - Transaction\n[T] - My Tenant details\n\n[D] - Print my House and Tenant Details\n[E] - Exit\n")
      else:
         print("\nWelcome Admin, you are now entering Tenant Management System (Admin Page)\n\n[S] - Search box\n\nReview information about:\n\n[A] - Apartment\n[P] - Transaction\n[T] - Tenant\n[D] - Print Specific House & Tenant Details\n[I] - Inquiry of Past Tenant Details\n[L] - Login History\n[E] - Exit\n")

      opt=input("Please select which operation that you want to do: ")

      if opt in ["S","s"]:
         searchBox()
      #Check for basic Functions
      elif opt in ["A","a"]:
         listCode = "a"
         apartment(masterKey,listCode,code)
      
      elif opt in ["P","p"]:
         listCode = "p"
         print("transaction(masterKey,listCode,code)")
      
      elif opt in ["T","t"]:
         listCode = "t"
         tenant(masterKey,UID,listCode,code)
      #Check for quick functions
      elif opt in ["D","d"]:
         print("tenantAndApartment()")
      
      elif opt in ["I","i"] and masterKey == True:
         details = "past"
         print("searchTenant(details)")

      elif opt in ["L","l"] and masterKey == True:
         print("loginHistory()")

      elif opt in ["E","e"]:
         print("\nThank you for using us, have a nice day~\n")
         return False

      else:
         code = 0
         message(code)
         print("\n--------------------------------------------------\n\nWelcome back")

import datetime as dt
login()
