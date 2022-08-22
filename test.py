def login():                                   #define the login function
   print("\nWelcome to Tenant Management System Login page.\nPlease enter username and password to proceed.\n") 
   chance = 3                                  #Specify login chances
   while chance > 0:                           #iterate when there are more than 0 chances remaining
      #input login credentials
      username = input("Username:")
      password = input("Password:")
      #open file and match for correct login
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
                     masterKey = False       #deactivate masterKey
                     UID = listRecord[2]
                  menu(masterKey,UID)        #redirect to menu
                  chance=0                   #empty login chances
                  break                      #break loop to avoid running error message
         else:
            chance-=1                        #decrease chances by 1
            print("\nError, incorrect username or password.\n",chance,"chances remaining.\n")

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
         fAppend.write(",")
      fAppend.write("\n")

def readFile(listCode):
   with open (listIdentifier(listCode),"r") as fRead:
      string = fRead.readlines()
      for record in string:
            stripped = record.rstrip("\n").rstrip(",")
            splitRecord = stripped.split(",")
            print(splitRecord)

def tenant(masterKey,UID):
   listCode = "t"
   if masterKey == False:
      num = 0
      searchInformation(listCode,num,UID)
   else:
      opt = input("[R]-Register new tenant, [M]-Modify Tenant Data")
      print("Current Tenant Data:")
      readFile(listCode)
      if opt in ["R","r"]:
         tenantEntryForm(listCode)

def tenantEntryForm(listCode):          #Define tenantEntryForm function
   n = input("Number of new tenants: ")
   tenantList = []
   for i in range(n):
      #Get input for tenant data
      name = getname()
      gender = getgender()
      pNum = getpNum()
      nationality = getnationality()
      startDate = getstartDate()
      income = getincome()
      rental = getrental()
      #Apply data to end of list 
      tenantList.append(name,gender,pNum,nationality,startDate,income,rental)
      #Return the list
      appendFile(tenantList,listCode)

def getname():
   validity = True
   code = None
   while validity == True:
      name = input("Enter tenant name: Firstname Familyname Lastname \n")
      nameList = name.split(" ")
      print("Splitted into",nameList)
      for words in nameList:
         print("Checking",words)
         if words[0].isupper():
            code = None
            continue
         else:
            code = 2
            message(code)
      if code:
         print("code has been assigned")
         continue
      else:
         retry = input("\n[R]-Retry,[E]-Exit:\n")
         if retry in ["R","r"]:
            continue
         else:
            validity = False
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
   if code == 0:
      print("\nIncorrect input.")
   elif code == 1:
      print("\nIncorrect data type present.")
   elif code == 2:
      print("\nFormat error.")
   elif code == 3:
      print("\nLength error.")
   elif code == 4:
      print("\nData not found.")
   print("Please try again.")

def checkSpecialCharacter():
    specials= ["{","}","<",">","!","@","#","$","%","^","&","*","(",")","?",":",";","'","+","=","-","_","]","["]
    specials.append('"')
    return specials

def apartment(masterKey,code):                        #Define apartment function
   
   print("\nApartment info:\n")
   record=[]
   
   #Put sample data
   list1=["Standard Room (Triple)","Code: SR1","Dimensions: 140+ sqft","Pricing: RM350","Number of Rooms: 20","Apartment ID: A01-L01-R01 to A01-L01-R21"]
   list2=["Standard Room (Twin)","Code: SR2","Dimensions: 120+ sqft","Pricing: RM450","Number of Rooms: 20","Apartment ID: A01-L01-R22 to A01-L01-R41"]
   list3=["Standard Room A/C (Triple)","Code: SR3","Dimensions: 150+ sqft","Pricing: RM550","Number of Rooms: 20","Apartment ID: A01-L02-R01 to A01-L02-R21"]
   list4=["Standard Room A/C (Twin)","Code: SR4","Dimensions: 130+ sqft","Pricing: RM650","Number of Rooms: 20","Apartment ID: A01-L02-R22 to A01-L02-R41"]
   list5=["Deluxe Room (Triple)","Code: DR1","Dimensions: 170+ sqft","Pricing: RM750","Number of Rooms: 20","Apartment ID: A01-L04-R01 to A01-L04-R21"]
   list6=["Deluxe Room (Twin)","Code: DR2","Dimensions: 160+ sqft","Pricing: RM840","Number of Rooms: 20","Apartment ID: A01-L04-R22 to A01-L04-R41"]
   list7=["Deluxe Room A/C with shared attached bath / toilet (Triple)","Code: DR3","Dimensions: 180+ sqft","Pricing: RM950","Number of Rooms: 20","Apartment ID: A01-L03-R1 to A01-L03-R21"]
   list8=["Deluxe Room A/C with shared attached bath / toilet","Code: DR4","Dimensions: 170+ sqft","Pricing: RM1040","Number of Rooms: 20","Apartment ID: A01-L03-R22 to A01-L03-R41"]
   list9=["Compact Premium Single","Code: CPS","Dimensions: 130+ sqft","Pricing: RM690","Number of Rooms: 20","Apartment ID: A01-L05-R01 to A01-L05-R41"]
   list10=["Medium Premium Single","Code: MPS","Dimensions: 150+ sqft","Pricing: RM750","Number of Rooms: 20","Apartment ID: A02-L01-R01 to A02-L01-R21"]
   list11=["Medium Premium Twin","Code: MPT","Dimensions: 180+ sqft","Pricing: RM890","Number of Rooms: 20","Apartment ID: A02-L02-R01 to A02-L02-R21"]
   list12=["Medium Premium with attached bath / toilet (Twin)","Code: MP1","Dimensions: 180+ sqft","Pricing: RM940","Number of Rooms: 20","Apartment ID: A02-L03-R01 to A02-L03-R21"]
   list13=["Medium Premium with attached bath / toilet (Single)","Code: MP2","Dimensions: 160+ sqft","Pricing: RM1050","Number of Rooms: 20","Apartment ID: A02-L03-R22 to A02-L03-R41"]
   list14=["En-Suite Single (Super Premium - Triple)","Code: ESS3","Dimensions: 160+ sqft","Pricing: RM700","Number of Rooms: 20","Apartment ID: A02-L04-R01 to A02-L04-R41"]
   list15=["En-Suite Single (Super Premium - Twin)","Code: ESS2","Dimensions: 140+ sqft","Pricing: RM800","Number of Rooms: 20","Apartment ID: A02-L04-R01 to A02-L04-R41"]
   list16=["En-Suite Twin (Super Premium)","Code: EST2","Dimensions: 200+ sqft","Pricing: RM900","Number of Rooms: 20","Apartment ID: A02-L05-R01 to A02-L05-R41"]

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

   if masterKey==True:
      modifyData(code)

   elif masterKey==False:
      menu()

def modifyData(code):
  while True:
      print("\n1. Add data\n2. Edit Data\n3. Delete Data\n4. Exit\n")
      dataInput=int(input('Please select which operation: '))

      if dataInput==1:
         print("\nAdd Data")
         apartmentAddData(code)

      elif dataInput==2:
         print("\nEdit Data")
         apartmentEditData()

      elif dataInput==3:
         print("\nDelete Data")
         apartmentDeleteData()

      elif dataInput==4:
         print("\nExit")
         return False

      else:
         code=2
         message(code)
         return True

def newApartmenttype(code,specials):
   nonumeric=0 ; nospecialcharacter=0 ; apartmentinfoemptymessage = 0
   while True:
      Newapartmentinfo=input("New apartment Info: ")
      for a in range(0,len(Newapartmentinfo)):
         if len(Newapartmentinfo) <= 0:
            apartmentinfoemptymessage = 1
         if Newapartmentinfo.isalpha():
            nonumeric = 1
         if Newapartmentinfo != specials:
            nospecialcharacter = 1
         if nonumeric != 1 and nospecialcharacter != 1 and apartmentinfoemptymessage != 1:
            code=1
            message(code)
            print("- Apartment info does not contain numbers and special characters. -")
            return True
         else:
            continue
      return False

def newApartmentCode(code):
   uppercase = 0 ; number = 0
   while True:
      newApartmentcode = input("New Room Code: ")
      for x in range(0,len(newApartmentcode)):
         if newApartmentcode[0].isupper() and newApartmentcode.isalnum() and len(newApartmentcode)!=0:
            uppercase = 1
            number = 1
         if uppercase != 1 and number != 1 and len(newApartmentcode)==0:
            code = 2
            message(code)
            print("- Please fill in the new Apartment Code. Apartment Code must contain uppercase and number only in order to differentiate -")
            return True
         else:
            continue
      return False

def newApartmentDimension(code):
   validApartmentDimension = 0
   while True:
      newapartmentDimension=input("New Room Dimension (Range): ")
      if len(newapartmentDimension) >= 3 and newapartmentDimension.isdigit():
         validApartmentDimension = 1
      if validApartmentDimension != 1:
         code=0
         message(code)
         print("- Room dimension must consist number and must have at least 100 or more sqft -\n")
         return True
      else:
         return False

def newApartmentID(code,specials):
   while True:
      lennewAparID = 0 ; notlowercase = 0 ; newAparIDdash = 0
      newApartmentID = input("New Room Apartment ID: ")
      if len(newApartmentID)>26 or len(newApartmentID)<1:
         code = 2
         message(code)
         print("- Please follow the format as: A01-L10-R40 to A02-L01-R09 -\n - A stands for Apartment Block, L stands for Level, and R stands for Room (The length must have 11 characters long, including the dash -) -")
         return True
      else:
         lennewAparID = 1
      if newApartmentID[0:4:8].islower():
         code=2
         message(code)
         print("- Must contain uppercase, not lower case -")
         return True
      else:
         notlowercase = 3
      if (newApartmentID[3] and newApartmentID[7] and newApartmentID[18] and newApartmentID[22]) == specials[20]:
         newAparIDdash = 4 
      else:
         code=2
         message(code)
         print("\nPlease include the dash inside the apartment ID")
         return True
      if lennewAparID == 1 and notlowercase == 3 and newAparIDdash == 4:
         return False
      else:
         return True

def apartmentAddData(code):
   specials = checkSpecialCharacter()
   while True:
      adddatanum = int(input('\nDear admin, how many records that you decide to add? '))
      if adddatanum < 1:
         code=0
         message(code)
         print("Error, cannot insert zero records")
         return True
      else:
         adddata=[]
         print("\nNow, you are required to enter new data\n")
         for adddatanum in range(0,adddatanum):
            newapartment=str(newApartmenttype(code,specials))
            newapartmentcode=newApartmentCode(code)
            newapartmentdimension=newApartmentDimension(code)
            newapartmentpricing=int(input("New Room Pricing in RM: "))
            newapartmentnumberofrooms=int(input("Number of new rooms: "))
            newapartmentID=newApartmentID(code,specials)
            adddata.append("New Room Info: " + str(newapartment))
            adddata.append("New Room Code: " + str(newapartmentcode))
            adddata.append("New Room Dimension in range (sqft): " + str(newapartmentdimension) + '+ sqft')
            adddata.append("New Room Pricing: RM" + str(newapartmentpricing))
            adddata.append("Number for the new room: " + str(newapartmentnumberofrooms))
            adddata.append("New room Apartment ID: " + str(newapartmentID))
            print("\nNew Data:",adddata)
            apartmentadddataconfirmation(adddata)
         return False

def apartmentadddataconfirmation(adddata):
   listCode = "a"
   while True:
      addDataconfirmation=int(input("\nAre you sure with the records you inserted just now? Enter '1' to save record, Enter '0' to unsave record: "))
      if addDataconfirmation == 1:
         appendFile(adddata,listCode)
         print("\nData Saved")

      addDataconfirmation2=input("\nAre you going to add more data? Yes/No: ")
      if addDataconfirmation2 in ['Yes','yes']:
         return True
      elif addDataconfirmation2 in ['No','no']:
         print("\n-Apartment-")
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
      print("\n- Return to main menu - ")
      return False

def apartmentEditData():
   editdatanum=int(input('How many records that you decide to edit? '))

def apartmentDeleteData():
   deletedatanum=int(input('How many records that you decide to add? '))

def searchBox():                             #Define search function
   print("\nWelcome to search box!")
   while True:
      print("\n1. Search room specific details.\n2. Search transaction details.\n3. Search specific tenant details.\n4. Exit search box.\n")
      option=int(input("Please type the search criteria based on the listing above: "))
      if option == 1:
         listCode= "a"
         opt = input("\n[A]-Apartment code, [P]-Pricing\n")     
         if opt in ["A","a"]:
            num = 1
         elif opt in ["P","p"]:
            num = 3
         else:
            code = 0
            message(code)

      elif option == 2:
         listCode = "p"
         opt = input("\n[R]-Reference number,[D]-Transaction date,[T]-TenantID,[A]-Apartment code,[S]-Amount:\n ")
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
         opt = input("\n[N]-Name,[G]-Gender,[P]-Phone number,[R]-Nationality,[D]-Rental start date,[I]-Income,[S]-Tenant status")
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
   print("\nWelcome, you are now entering Tenant Management System")
   while True:
      print("\n[S] - Search box\n\nReview information about:\n")

      if masterKey == False:
         print("[A] - Apartment\n[P] - Transaction\n[T] - My Tenant details\n\n[D] - Print my House and Tenant Details\n[E] - Exit\n")
      else:
         print("[A] - Apartment\n[P] - Transaction\n[T] - Tenant\n[D] - Print Specific House & Tenant Details\n[I] - Inquiry of Past Tenant Details\n[L] - Login History\n[E] - Exit\n")

      opt=input("Please select which operation that you want to do: ")

      if opt in ["S","s"]:
         searchBox()
      #Check for basic Functions
      elif opt in ["A","a"]:
         listCode = "a"
         apartment(masterKey,listCode)
      
      elif opt in ["P","p"]:
         listCode = "p"
         print("transaction(masterKey,listCode)")
      
      elif opt in ["T","t"]:
         listCode = "t"
         tenant(masterKey,UID,listCode)
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
         print("\n--------------------------------------------------\n\nWelcome back to Tenant Management System")


login()
