# Python Assignment (Tenant Management System)
# Chiu Wai Kin TP065600 & Damon Ng Khai Weng TP064820

def register(listCode,code):                                               # Define register function
   userType = "new"                                                        # Set userType to 'new'
   UID = None                                                              # Set UID to 'None'
   username = input("\nCreate your account's username: ")                  # Input login credentials
   password = input("Next, create your account's password: ")              # Input login credentials
   UserID = gettenantID(UID,userType)                                      # UserID = call function gettenantID(UID,userType)
   print("UserID is"+UserID)                                               # Print userID
   with open (listIdentifier(listCode),"a") as userAdd:                    # Open selected text file in append mode as userAdd and match for correct login credentials
      userAdd.write(username+","+password+","+UserID+",\n")                # Write username, password, userID into userAdd
   listCode = "t"                                                          # Set listCode as 't'
   tenantOrTransactionEntryForm(UserID,listCode,code)                      # Call function tenantOrTransactionEntryForm(UserID,listCode,code)
   return username,password                                                # Exit function and send the value back to the program

def login(listCode,code,nameInput,passInput):                                                               # Define login function
   chance = 3
   while chance > 0:
      if nameInput and passInput:
         username = nameInput
         password = passInput
      else:                                                                # Other than that:
         print("Please enter username and password to proceed.\n")
         username = input("Username: ")                                    # Input login credentials
         password = input("Password: ")                                    # Input login credentials
      with open(listIdentifier(listCode),"r") as userInfo:              # Open selected text file in read mode as userInfo and match for correct login credentials
         userCheck = userInfo.readlines()                               # Read each lines in userInfo  
         for record in userCheck:                                       # For each record in usercheck:
            listRecord = record.split(",")                              # Split the record with comma as a separator
            if username == listRecord[0]:                               # If username equals to listRecord that is in index 0:
               if password == listRecord[1]:                            # If password equals to listRecord that is in index 1:
                  print("\n- Login successful -\n\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                  if (username == "john" and password == "1234u-78") or (username == "david" and password == "55467913"):     # Check for admin credentials
                     UID = None                                         # UID set to 'None', activate admin access
                  else:                                                 # Other than that:
                     with open("currentUser.txt","w") as current:       # Open currentUser text file in Write Mode as current
                        current.write(record)                           # Write record into current
                     UID = listRecord[2]                                # UID = listrecord index 2, deactivate admin access
                  menu(UID,code)                                        # Call function menu(UID,code), redirect to menu
                  chance = 0                                            # reassign login chances to 0
                  break
               else:
                  continue
            else:
               continue
         else:                                                          # Other than that:
            chance -= 1                                                 # Decrease chances by 1
            print("\nError, incorrect username or password.\n",chance,"chances remaining.") # Print message

def menu(UID,code):                                                           # Define menu function
   while True:                                                                # when mainMenu is equal to True Then:
      if UID:                                                                 # If UID exists:
         print("\nMain menu:\n\n[S] - Search box\n\nReview information about:\n[A] - Available Apartments\n[T] - My Tenant details\n[P] - My Transactions\n\nQuick functions:\n[D] - Print my House & Tenant Details\n[E] - Exit")  # Print message
      else:                                                                   # Other than that:
         print("\nMain menu:\n\n[S] - Search box\n\nReview information about:\n[A] - Apartment\n[T] - Tenant\n[P] - Transaction\n\nQuick functions:\n[D] - Print Specific House & Tenant Details\n[I] - Inquiry of Past Tenant Details\n[E] - Exit")  # Print message 
      opt=input("\nPlease enter which operation that you want to do: ")       # Print message and get opt
      if opt in ["S","s"]:                                                    # Check for basic Functions, If opt is equal to ["I","i"] Then:
         searchBox(UID,code)                                                  # Redirect to searchbox function, call function searchBox(UID,code)
      elif opt in ["A","a"]:                                                  # Check for basic Functions, If opt is equal to ["A","i\a"] Then:
         listCode = "a"                                                       # listCode is equal to "a"
         apartment(UID,listCode,code)                                         # Redirect to searchbox function, call function apartment(UID,listCode,code)
      elif opt in ["P","p"]:                                                  # Check for basic Functions, If opt is equal to ["P","p"] Then:
         listCode = "p"                                                       # listCode is equal to "p"
         tenantOrTransaction(UID,listCode,code)                               # Redirect to searchbox function, call function tenantOrTransaction(UID,listCode,code)
      elif opt in ["T","t"]:                                                  # Check for basic Functions, If opt is equal to ["I","i"] Then:
         listCode = "t"                                                       # listCode is equal to "t"
         tenantOrTransaction(UID,listCode,code)                               # Redirect to searchbox function, call function tenantOrTransaction(UID,listCode,code)
      elif opt in ["D","d"]:                                                  # Check for quick functions, If opt is equal to ["D","d"] Then:
         tenantAndApartment(UID)                                              # Redirect to searchbox function, call function tenantAndApartment(UID) 
      elif opt in ["I","i"] and UID == None:                                  # Check for quick functions, If opt is equal to ["I","i"] and UID equals to None Then:
         listCode = "t"                                                       # listCode equals to "t"
         searchInformation(listCode,9,"Past")                                 # Redirect to searchbox function, call function searchInformation(listCode,9,"Past")
      elif opt in ["L","l"] and UID == None:                                  # Check for quick functions, If opt is equal to ["L","l"] and UID equals to None Then:
         print("loginHistory()")                                              # Print function ("loginHistory()") 
      elif opt in ["E","e"]:                                                  # Get confirmation to exit
         exitconfirmationkey = input("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nYou're about to leave Tenant Management System. Are you sure? [Enter]-Continue, [x]-Return to main menu): ") # Print message and get exitconfirmationkey
         if exitconfirmationkey in ["X","x"]:                                 # If exitconfirmationkey is equal to ["X","x"] Then:
            continue                                                          # Continue the loop
         else:                                                                # Other than that:
            print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nExit successful, have a nice day~\n") # Print message
            return False                                                      # Exit function and send the value back to the program
      else:                                                                   # Other than that:
         code = 0                                                             # Code equals to 0
         message(code)                                                        # Print error message, call function message(code)

def message(code):                                                            # Define message function
   x,y,z="Error, ","Incorrect "," Please try again."                          # Declare x as 'Error', y as 'Incorrect' and z as 'Please try again'
   if code == 0:                                                              # If code equals 0 Then:
      print("\n"+x+y+"input."+z)                                              # Print message
   elif code == 1:                                                            # If code equals 1 Then:
      print("\n"+x+y+"data type present."+z)                                  # Print message
   elif code == 2:                                                            # If code equals 2 Then:
      print("\n"+x+y+"format."+z)                                             # Print message
   elif code == 3:                                                            # If code equals 3 Then:
      print("\n"+x+y+"length."+z)                                             # Print message
   elif code == 4:                                                            # If code equals 4 Then:
      print("\n"+x+"data not found.")                                         # Print message
   elif code == 5:                                                            # If code equals 5 Then:
      print("\n"+x+"zero input."+z)                                           # Print message

def specialCharacterList(SCL):                                                # Define specialCharacterList function
    if SCL == None:                                                           # If SCL equals to 'None' Then:
        return ["~","`","!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]","|",",","\'",".","/","<",">","?",";",":","'",'"'] # Exit function and send the value back to the program
    elif SCL == "SCL1":                                                       # If SCL equals to "SCL1" Then:
        return ['~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|',',','\\','\'','\"','.','/','<','>','?',';',':']  # Exit function and send the value back to the program
    elif SCL == "SCL2":                                                       # If SCL equals to "SCL2" Then:
        return ['~','`','!','@','#','$','%','^','&','*','_','=','+','{','}','[',']','|','\\','\'','\"',',','.','/','<','>','?',':',';']  # Exit function and send the value back to the program

def listIdentifier(listCode):                                                 # Define listIdentifier function
   if listCode == "t":                                                        # If listCode equals to "t" Then:
      l = "tenant.txt"                                                        # l is "tenant.txt"
   elif listCode == "a":                                                      # If listCode equals to "a" Then:
      l = "Apartment.txt"                                                     # l is "Apartment.txt"
   elif listCode == "p":                                                      # If listCode equals to "p" Then:
      l = "transaction.txt"                                                   # l is "transaction.txt"
   elif listCode == "u":                                                      # If listCode equals to "u" Then:
      l = "user.txt"                                                          # l is "user.txt"
   return l                                                                   # Exit function and send the value back to the program

def appendFile(list,listCode):                                                # Define appendFile function
   with open (listIdentifier(listCode), "a") as fAppend:                      # Open selected text file in Append Mode as fAppend
      for item in list:
         fAppend.write(item)                                                  # Write item into fAppend
         fAppend.write(", ")                                                  # Write a comma and space (", ") into fAppend
      fAppend.write("\n")                                                     # Write a newline ("\n") into fAppend

def readFile(listCode):                                                       # Define readFile function
   returnList = []                                                            # Declare returnlist as array
   with open (listIdentifier(listCode),"r") as fRead:                         # Open selected text file in Read Mode as fRead
      line = fRead.readlines()                                                # line = read each line in fRead
      for record in line:                                                  
         stripped = record.rstrip("\n").rstrip(",")                           # stripped = Right stripped from the end of string (record) with the separators (all commas and newlines)
         splitRecord = stripped.split(",")                                    # splitRecord = Use comma as the separator to split from a string into a list
         returnList.append(str(splitRecord))                                  # Append returnlist to splitRecord in string type
         print(int(line.index(record))+1,splitRecord)
   return returnList                                                          # Exit function and send the value back to the program

def chooseItem(UID,listCode,displayColumn,currentColumn):                     # Define chooseItem function
   displayRecord = searchColumn(listCode,displayColumn,UID)                   # displayRecord = call function searchColumn(listCode,displayColumn,UID)
   currentRecord = searchColumn(listCode,currentColumn,UID)                   # currentRecord = call function searchColumn(listCode,currentColumn,UID)
   listLength = len(displayRecord)                                            # Return the number of items in displayRecord
   if listCode == "u":                                                        # If listCode is equal to 'u' Then:
      startPoint = 2                                                          # startPoint equals to '2'
      changeIndex = +1                                                        # changeIndex add 1 (+1)
   else:                                                                      # Other than that:
      startPoint = 0                                                          # startPoint set as 0
      changeIndex = -1                                                        # changeIndex subtract 1 (-1)
   for item in range(startPoint,listLength,2):                                # For item from startPoint to listLength, but incremented by 2
      try:
         print(displayRecord[item],"   ",displayRecord[item+1])
      except IndexError:
         print(displayRecord[item])
   while True:
      print("\n\nOptions are indexed from upper-left to lower-right starting from 1 to",len(displayRecord)) # Print message
      index = input("Choose one of the options: ")                            # Print message and get index
      if index.isdecimal() and  0 < int(index) < len(displayRecord)+1:        # Number check, if index is decimal then:
         return currentRecord[int(index)+changeIndex]                         # Exit a function and send the value back to the main program
      else:                                                                   # Other than that:
         code = 0                                                             # Error detected, code equals to '0'
         message(code)                                                        # Print error message, call function message(code)
         continue                                                             # Continue the loop

def gettenantID(UID,userType):                                                # Define gettenantID function
   if UID:                                                                    # Fetch existing UID
      with open("currentUser.txt","r") as uRead:                              # Open currentUser.txt file in Read Mode as uRead
         userRecord = uRead.read().split(",")                                 # Read and split the record with comma as a separator
         return userRecord[2]                                                 # Exit function and send the value back to the program
   else:                                                                      # Other than that:
      while True:
         number = None
         if userType == "new":                                                # If userType equals to "new" Then:
            number = 1                                                        # Number equals to 1
         else:                                                                # Other than that:
            path = input("[1]-Generate new ID or [2]-Choose existing ID:\n")
            if path.isdecimal():                                              # Check path contain numbers or not
               number = int(path)                                             # Convert to integer
            else:                                                             # Other than that:
               code = 1                                                       # Code equals to 1
               message(code)                                                  # Print error message, call function message(code)
         if number == 1:
            return dt.datetime.now().strftime("%d%m%Y%H%M%S%f")               # Exit function and send the value back to the program
         elif number == 2:
            listCode = "t"                                                    # listCode equals to 'u'
            displayColumn = 1                                                 # displayColumn equals to '0'
            currentColumn = 0                                                 # currentColumn equals to '2'
            return chooseItem(UID,listCode,displayColumn,currentColumn)       # Exit function and send the value back to the program
         else:                                                                # Other than that:
            code = 0                                                          # code equals to '0'
            message(code)                                                     # Print error message, call function message(code)

def getname(code,nameType):                                                   # Define getname function
   specials = specialCharacterList(None)                                      # specials = call function specialCharacterList(None)
   while True:
      print("Format: Name Name or Name-Name Name or Na'me Name")
      if nameType == "tenant":                                                # If nameType equals to "tenant" Then:
         name = input("\nEnter tenant's fullname:")                           # Print message and get name
      elif nameType == "employer":                                            # If nameType equals to "employer" Then:
         name = input("\nEnter tenant's current employer:")                   # Print message and get name
      else:                                                                   # Other than that:
         name = input("\nEnter tenant's place-city-country of birth")         # Print message and get name
      nameList = name.split(" ")                                              # Right stripped from the end of string (record) with the separators (all commas and newlines)
      if len(nameList) >= 2:                                                  # if the length of namelist is greater than or equal to 2 Then:
         for words in nameList:
            if words.isalpha() or [character for character in words if(character in specials[12]) or (character in specials[22])]:
               if words[0].isupper():                                         # Checking words in index 0 is uppercased or not
                  code = None                                                 # Set code as 'None'
                  continue                                                    # End loop and cntinue with the next iteration
               else:                                                          # Other than that:
                  code = 2                                                    # Set code as '2'
                  break                                                       # Break out of the function
            else:                                                             # Other than that:
               code = 1                                                       # Set code as '1'
               break                                                          # Break out of the function
      else:                                                                   # Other than that:
         code = 3                                                             # Set code as '3'
      if code:                                                                # If code exists:
         message(code)                                                        # Print error message, call function message(code)                            
         print("ATTENTION||Error detected.||ATTENTION")                       # Print message
      else:                                                                   # Other than that:
         print("No errors detected.")                                         # Print message
      retry = input("\n[R]-Retry,[Any other key]-Exit using "+name+"")        # Print message and get retry
      if retry in ["R","r"]:                                                  # If retry equal to ["R","r"] Then:
         continue                                                             # End loop and cntinue with the next iteration
      else:                                                                   # Other than that:
         return name                                                          # Exit function and send the value back to the program

def getabbreviation(code,abbreviationType):                                   # Define getabbreviation function
   while True:
      if abbreviationType == "gender":                                        # If abbreviation equals to "gender" Then:
         abbreviation = input("[M]-Male\n[F]-Female\nEnter tenant gender:\n") # Print messsage and get abbreviation
      else:                                                                   # Other than that:
         abbreviation = input("[M]-Malaysian\n[N]-non-Malaysian\nEnter tenant nationality: \n") # Print messsage and get abbreviation
      if len(abbreviation)== 1:                                               # If the length of abbreviation is equal to 1 Then:
         if abbreviation.isalpha():                                           # Alphahabet checking
            if abbreviationType == "gender":                                  # If abbreviation equals to "gender" Then:
               if abbreviation in ["M","m"]:                                  # If abbreviation equals to ["M","m"] Then:
                  code = None                                                 # code equals to None
                  abbreviation = "Male"                                       # abbreviation equals to "Male"
               elif abbreviation in ["F","f"]:                                # If abbreviation equals to ["F","f"] Then:
                  code = None                                                 # code equals to None
                  abbreviation = "Female"                                     # abbreviation equals to "Female"
               else:                                                          # Other than that:
                  code = 0                                                    # Set code to 0
            else:                                                             # Other than that:
               if abbreviation in ["M","m"]:                                  # If abbreviation equals to ["M","m"] Then:
                  code = None                                                 # code equals to None
                  abbreviation = "Malaysian"                                  # abbreviation equals to "Malaysian"
               elif abbreviation in ["N","n"]:                                # If abbreviation equals to ["N","n"] Then:
                  code = None                                                 # code equals to None
                  abbreviation = "non-Malaysian"                              # abbreviation equals to "non-Malaysian"
               else:                                                          # Other than that:
                  code = 0                                                    # code equals to 0
         else:                                                                # Other than that:
            code = 1                                                          # code equals to 1
      else:                                                                   # Other than that:
         code = 3                                                             # code equals to 3
      if code or code == 0:                                                   # If code exists or code equals to 0:
         message(code)                                                        # Print error message, call function message(code)
         print("ATTENTION||Error detected.||ATTENTION")                       # Print message
      else:                                                                   # Other than that:
         print("No errors detected.")                                         # Print message
      retry = input("[R]-Retry,[Any other key]-Exit using "+abbreviation+"\n") # Print message and get retry
      if retry in ["R","r"]:                                                  # If abbreviation equals to ["M","m"] Then:
         continue                                                             # End loop and cntinue with the next iteration
      else:                                                                   # Other than that:
         return abbreviation                                                  # Exit function and send the value back to the program

def getpNum(code):                                                            # Define getpNum function
   while True:
      pNum = input("Format: ############\nEnter tenant phone number:\n")      # Print message and get pNum
      if 6 < len(pNum) < 16:                                                  # if the length of pNum is lesser than 6 and 16: 
         for digit in pNum:
            if digit.isdigit():                                               # Number check
               code = None                                                    # Set code as None
               continue                                                       # End loop and cntinue with the next iteration
            else:                                                             # Other than that:
               code = 1                                                       # Code equals to 1
               break                                                          # Break out of the function
      else:                                                                   # Other than that:
         code = 3                                                             # Code equals to 3
      if code:                                                                # If code exists:
         message(code)                                                        # Print error message, call function message(code)
         print("ATTENTION||Error detected.||ATTENTION")                       # Print message
      else:                                                                   # Other than that:
         print("No errors detected.")                                         # Print message
      retry = input("[R]-Retry,[Any other key]-Exit using "+pNum+"\n")        # Print message and get retry
      if retry in ["R","r"]:                                                  # If retry is equal to ["R","r"] Then:
         continue                                                             # End loop and continue with the next iteration
      else:                                                                   # Other than that:
         return pNum                                                          # Exit function and send the value back to the program

def getDate(code,dateType):                                                   # Define getDate function
   specials = specialCharacterList(None)                                      # specials = call function specialCharacterList(None)
   while True:
      if dateType == "start":                                                 # If dateType equals to "start" Then:
         path = input("Use current date as rental start date?\n[Y]-Yes\n[Any Other Key]-No\n")
         if path in ["Y","y"]:                                                # If path is equal to ["Y","y"] Then:
            date = dt.date.today().strftime("%Y/%m/%d")                       # Return a numpy array of datetime.date objects
            print("Current date:",date)                                       # Print message
         else:                                                                # Other than that:
            date = input("Format: YYYY/MM/DD\nEnter Rental start date:\n")    # Print message and get date
      elif dateType == "birth":                                               # If dateType is equal to "birth" Then: 
         date = input("Format: YYYY/MM/DD\nEnter tenant birth date:\n")       # Print message and get date
      else:                                                                   # Other than that:
         date = input("Format: YYYY/MM/DD\nEnter transaction date:\n")        # Print message and get date
      if len(date) == 10:                                                     # If the date length is equal to 10:
         if date[4] == date[7] == specials[24]:                               # If the date in location 7 and 14 is equal to specials in location 24 Then:
            year,month,day = date.split("/")                                  # Split the date to year, month, day using the separator ("/") 
            try:
               dt.datetime(int(year),int(month),int(day))                     # Insert the year, month, day in integer
               code = None                                                    # code equals to None
            except ValueError:
               code = 1                                                       # code equals to 1
         else:                                                                # Other than that:
            code = 2                                                          # code equals to 2
      else:                                                                   # Other than that:
         code = 3                                                             # code equals to 3
      if code:                                                                # If code exists:
         message(code)                                                        # Print error message, call function message(code)
         print("ATTENTION||Error detected.||ATTENTION\n")                     # Print message
      else:                                                                   # Other than that:
         print("No errors detected.\n")                                       # Print message
      retry = input("[R]-Retry,[Any other key]-Exit using "+date+"\n")        # Print message and get retry
      if retry in ["R","r"]:                                                  # If retry is equal to ["R","r"] Then:
         continue                                                             # End loop and continue with the next iteration
      else:                                                                   # Other than that:
         return date                                                          # Exit function and send the value back to the program

def getnumber(code,numberType):                                               # Define getincome function
    while True:                                                                               
      if numberType == "workHistory":                                         # If numberType is equal to "workHistory" Then:
         t = "Total work history is around "                                  # t is "Total work history is around"
         number = input(t+"\n[1]-1 to 2 month\n[2]-2 to 3 months\n[3]-3 to 6 months\n[4]-6 to 9 months\n[5]-9 months to 1 year\n[6]-1 to 2 years\n[7]-2 to 3 years\n[8]-3 to 4 years\n[9]-4 to 5 years\n[0]-5 years or more\nChoose how long you have been working: ")
      else:                                                                   # Other than that:
         number = input("[1]-RM 1500~1599\n[2]-RM 1600~1699\n[3]-RM 1700~1799\n[4]-RM 1800~1899\n[5]-RM 1900~1999\n[6]-RM 2000~2099\n[7]-RM 2100~2199\n[8]-RM 2200~2499\n[9]-RM 2500~3000\n[0]-RM > 3000\nChoose tenant income range in Ringgit Malaysia: ")
      if number.isdigit():                                                    # If number is digit Then:
         num = int(number)                                                    # Convert into integer
         if numberType == "workHistory":                                      # If numberType is equal to "workHistory" Then: 
            if num == 1:                                                      # If num is equal to 1 Then:
               number = t + "1 to 2 months"                                   # number is t + "1 to 2 month"
            elif num == 2:                                                    # If num is equal to 2 Then:
               number = t + "2 to 3 months"                                   # number is t + "2 to 3 months"
            elif num == 3:                                                    # If num is equal to 3 Then:
               number = t + "3 to 6 months"                                   # number is t + "3 to 6 months"
            elif num == 4:                                                    # If num is equal to 4 Then:
               number = t + "6 to 9 months"                                   # number is t + "6 to 9 months"
            elif num == 5:                                                    # If num is equal to 5 Then:
               number = t + "9 months to 1 year"                              # number is t + "9 months to 1 year"
            elif num == 6:                                                    # If num is equal to 6 Then:
               number = t + "1 to 2 years"                                    # number is t + "1 to 2 years"
            elif num == 7:                                                    # If num is equal to 7 Then:
               number = t + "2 to 3 years"                                    # number is t + "2 to 3 years"
            elif num == 8:                                                    # If num is equal to 8 Then:
               number = t + "3 to 4 years"                                    # number is t + "3 to 4 years"
            elif num == 9:                                                    # If num is equal to 9 Then:
               number = t + "4 to 5 years"                                    # number is t + "4 to 5 years"
            elif num == 0:                                                    # If num is equal to 0 Then:
               number = t + "5 years or more"                                 # number is t + "5 years or more"
            else:                                                             # Other than that:
               code = 0                                                       # code equals to 0
               message(code)                                                  # Print error message, call function message(code)
               continue                                                       # End loop and cntinue with the next iteration
         else:                                                                # Other than that:
            if num == 1:                                                      # If num is equal to 1 Then:
               number = "RM 1500~1599"                                        # number is "RM 1500~1599"
            elif num == 2:                                                    # If num is equal to 2 Then:
               number = "RM 1600~1699"                                        # number is "RM 1600~1699"
            elif num == 3:                                                    # If num is equal to 3 Then:
               number = "RM 1700~1799"                                        # number is "RM 1700~1799"
            elif num == 4:                                                    # If num is equal to 4 Then:
               number = "RM 1800~1899"                                        # number is "RM 1800~1899"
            elif num == 5:                                                    # If num is equal to 5 Then:
               number = "RM 1900~1999"                                        # number is "RM 1900~1999"
            elif num == 6:                                                    # If num is equal to 6 Then:
               number = "RM 2000~2099"                                        # number is "RM 2000~2099"
            elif num == 7:                                                    # If num is equal to 7 Then:
               number = "RM 2100~2199"                                        # number is "RM 2100~2199"
            elif num == 8:                                                    # If num is equal to 8 Then:
               number = "RM 2200~2499"                                        # number is "RM 2200~2499"
            elif num == 9:                                                    # If num is equal to 9 Then:
               number = "RM 2500~3000"                                        # number is "RM 2500~3000"
            elif num == 0:                                                    # If num is equal to 0 Then:
               number = "RM > 3000"                                           # number is "RM > 3000"
            else:                                                             # Other than that:
               code = 0                                                       # code equals to 0
               message(code)                                                  # Print error message, call function message(code)
               continue                                                       # End loop and cntinue with the next iteration
      else:                                                                   # Other than that:
         code = 0                                                             # code equals to 0
         message(code)                                                        # Print error message, call function message(code)
         continue                                                             # End loop and cntinue with the next iteration
      retry = input("[R]-Retry,[Any other key]-Exit using "+number+"\n")      # Print message and get retry
      if retry in ["R","r"]:                                                  # If retry is equal to ["R","r"] Then:
         continue                                                             # End loop and cntinue with the next iteration
      else:                                                                   # Other than that:
         return number                                                        # Exit function and send the value back to the program

def getrental(UID):                                                           # Define getrental function
   if UID:                                                                    # If UID exists:
      return "Current"                                                        # Exit function and send the value back to the program
   else:                                                                      # Other than that:
      while True:                                                                               
         rental = input("[P]-Past\n[Any other key]-Current\nChoose tenant rental status(current/past)\n")   # Print message and give rental
         if rental in ["P","p"]:                                              # If rental is equal to ["P","p"] Then:
            rental = "Past"                                                   # rental is equal to "Past"
         else:                                                                # Other than that:
            rental = "Current"                                                # rental is equal to "Current"
         retry = input("[R]-Retry,[Any other key]-Exit using "+rental+"\n")   # Print message and get retry
         if retry in ["R","r"]:                                               # If retry is equal to ["R","r"] Then:
            continue                                                          # End loop and continue with the next iteration
         else:                                                                # Other than that:
            return rental                                                     # Exit function and send the value back to the program

def getreferenceNumber(code):                                                 # Define getreferenceNumber function
   specials = specialCharacterList(None)                                      # specials = call function specialCharacterList(None)
   while True:                                                                               
      referenceNumber = input("Reference number comes from its relevant bank transaction. They cannot repeat.\nIf transaction is payed physically, please enter according to the format:   Tenantname year Month ; no special characters\nEnter the reference number :\n")
      if len(referenceNumber) > 5:                                            # If the length for referenceNumber is greater than 5 Then:
         for character in referenceNumber:                                     # Iterate through every character in the reference to check for special characters
            if character not in specials:                                      # If special character is not detected:
               code = None                                                    # code equals to None 
               continue                                                       # End loop and continue with the next iteration
            else:                                                             # Other than that:
               code = 2                                                       # code equals to 2
               break                                                          # Break out of the function 
      else:                                                                   # Other than that:
         code = 3                                                             # code equals to 3
      if code:                                                                # If code exists:
         message(code)                                                        # Print error message, call function message(code)
         print("ATTENTION||Error detected.||ATTENTION\n")                     # Print message
      else:                                                                   # Other than that:
         print("No errors detected.\n")                                       # Print message
      retry = input("[R]-Retry,[Any other key]-Exit using "+referenceNumber+"\n")  # Print message and get retry
      if retry in ["R","r"]:                                                  # If retry is equal to ["R","r"] Then:
         continue                                                             # End loop and continue with the next iteration
      else:                                                                   # Other than that:
         return referenceNumber                                               # Exit function and send the value back to the program

def getdecimal(code):                                                         # Define getdecimal function
   specials = specialCharacterList(None)                                      # specials = call function specialCharacterList(None)
   while True:                                                                               
      decimal = input("Format: ########.##\nEnter the transaction amount in Ringgit Malaysia:\n")  # Print message and get decimal
      if specials[23] in decimal:                                             # If the length in specials (location 23) is decimal Then:
         money = decimal.split(".")                                           # Split the decimal using the separator (".") 
         for numbers in money:
            try:
               numbers[1] in money[1]                                         # location 1 in numbers 
               if (digits.isnumeric() for digits in numbers):                 # Data validation - number check
                  code = None                                                 # code equals to None                                                
                  continue                                                    # End loop and continue with the next iteration
               else:                                                          # Other than that:
                  code = 1                                                    # code equals to 1
                  break                                                       # Break out of the function
            except IndexError:
               code = 2                                                       # code equals to 2
               break                                                          # Break out of the function
      else:                                                                   # Other than that:
         code = 2                                                             # code equals to 2
         print(specials[23])                                                  # Print specials 23rd location
      if code:                                                                # If code exists:
         message(code)                                                        # Print error message, call function message(code)
         print("ATTENTION||Error detected.||ATTENTION\n")                     # Print message
      else:                                                                   # Other than that:
         print("No errors detected.\n")                                       # Print message
      retry = input("[R]-Retry,[Any other key]-Exit using "+decimal+"\n")     # Print message and get retry
      if retry in ["R","r"]:                                                  # If retry is equals to ["R","r"] Then:
         continue                                                             # End loop and continue with the next iteration
      else:                                                                   # Other than that:
         return "RM" + decimal                                                # Exit function and send the value back to the program

def tenantOrTransactionEntryForm(UID,listCode,code):                          # Define tenantOrTransactionEntryForm function
   while True:                                                                               
      if UID == None:                                                         # If UID equals to None Then:
         n = input("Number of new Records: ")                                 # Print message and get n
         if n.isdecimal():                                                    # Data validation - number check
            code = None                                                       # code equals to None
         else:                                                                # Other than that:
            code = 0                                                          # code equals to 0
            message(code)                                                     # Print error message, call function message(code)
            continue                                                          # End loop and continue with the next iteration
      else:                                                                   # Other than that:
         n = 1                                                                # n equals to 1
      for list in range(0,int(n)):                                            # Definite loops iterate through the members of a set from 0 to n in integer type
         if listCode == "t":                                                  # If listCode is equals to "t" Then:
            UserID  = gettenantID(UID,"existing")                             # Get input for tenant data, userID = call function gettenantID(UID,"existing")
            name = getname(code,"tenant")                                     # Get input for tenant data, name = call function getname(code,"tenant")
            gender = getabbreviation(code,"gender")                           # Get input for tenant data, gender = call function getabbreviation(code,"gender") 
            pNum = getpNum(code)                                              # Get input for tenant data, pNum = call function getpNum(code)
            nationality = getabbreviation(code,"nationality")                 # Get input for tenant data, nationality = call function getabbreviation(code,"nationality")
            startDate = getDate(code,"start")                                 # Get input for tenant data, startDate = call function getDate(code,"start") 
            workHistory = getnumber(code,"workHistory")                       # Get input for tenant data, workHistory = call function getnumber(code,"workHistory") 
            employer = getname(code,"employer")                               # Get input for tenant data, employer = call function getname(code,"employer")
            income = getnumber(code,"income")                                 # Get input for tenant data, income = call function getnumber(code,"income") 
            rental = getrental(UID)                                           # Get input for tenant data, rental = call function getrental(UID)
            birthDate = getDate(code,"birth")                                 # Get input for tenant data, birthDate = call function getDate(code,"birth")
            birthCity = getname(code,"city")                                  # Get input for tenant data, birthCity = call function getname(code,"city") 
            list = [UserID,name,gender,pNum,nationality,startDate,workHistory,employer,income,rental,birthDate,birthCity]   # Declare list containing relevant input data
         else:                                                                # Other than that:
            referenceNumber = getreferenceNumber(code)                        # Get input for transaction data, referenceNumber = call function getreferenceNumber(code)
            transactionDate = getDate(code,"transaction")                     # Get input for transaction data, transactionDate = call function getDate(code,"transaction")
            UserID  = gettenantID(UID,"existing")                             # Get input for transaction data, userID = call function gettenantID(UID,"existing")
            chooseList = "a"                                                  # chooseList equals to "a"
            displayColumn = 0                                                 # displayColoum equals to 0
            currentColumn = 1                                                 # currentColumn equals to 1
            tenantAndApartment(UserID)                                        # Redirect to tenantAndApartment function
            apartmendCode = chooseItem(UID,chooseList,displayColumn,currentColumn) # Get input for transaction data, apartmendCode = call function chooseItem(UID,chooseList,displayColumn,currentColumn)
            amount = getdecimal(code)                                         # Get input for transaction data, amount = call function getdecimal(code)
            list = [referenceNumber,transactionDate,UserID,apartmendCode,amount]  # Declare list containing relevant input data
         appendFile(list,listCode)                                            # Call function appendFile(list,listCode)
      break                                                                   # Break out of the fumction

def tenantAndApartment(UID):                                                  # Define tennantAndApartment function
   listCode = "p"                                                             # listCode equals to "p"
   reference1 = "t"                                                           # reference1 equals to "t"
   reference2 = "a"                                                           # reference2 equals to "a"
   primaryKeys = []                                                           # Define primaryKeys as array
   TAList = []                                                                # Declare TAList as array
   with open(listIdentifier(listCode),"r") as pRead:                          # Open selected text file in read mode as pRead 
      file = pRead.readlines()                                                # Read each lines in pRead
      for record in file:
         list = record.split(",")                                             # Split record by using comma (",") as a separator
         if UID:                                                              # If UID exists:
            if UID in list[2]:                                                # If UID exists in the second location from list:
               primaryKeys.append(list[2]+","+list[3])                        # Append second and third location from list into primaryKeys
               break                                                          # Break out of the function
            else:                                                             # Other than that:
               continue                                                       # End loop and continue with the next iteration
         else:                                                                # Other than that:
            if str(list[2]+","+list[3]) not in primaryKeys:                   # If second and third location from list (in string) not in primaryKeys:
               primaryKeys.append(list[2]+","+list[3])                        # Append the item in second and third location from list into primaryKeys
            else:                                                             # Other than that:
               continue                                                       # End loop and continue with the next iteration
   for item in primaryKeys:
      TARecord = []                                                           # Define TARecord as array
      tenantID,ApartmentCode = item.split(",")                                # Split item using comma (",") as a separator
      with open(listIdentifier(reference1),"r") as tRead:                     # Open selected text file in read mode as tRead 
         file = tRead.readlines()                                             # Read each lines in tRead
         for record in file:
            list = record.split(",")                                          # Split record using comma (",") as a separator
            if tenantID in list[0]:                                           # If tenantID is in the zero location from list:
               TARecord.append(list[0]+","+list[1])                           # Append the item in zero and first location from list into TARecord
               break                                                          # Break out of the function
            else:                                                             # Other than that:
               continue                                                       # End loop and continue with the next iteration
      with open(listIdentifier(reference2),"r") as aRead:                     # Open selected text file in read mode as aRead:
         file = aRead.readlines()                                             # Read each lines in aRead
         for record in file:
            list = record.split(",")                                          # Split record using comma (",") as a separator 
            if ApartmentCode in list[1]:                                      # If ApartmentCode is in the first location from list:
               TARecord.append(list[1]+","+list[0]+","+list[3])               # Append the item in first, zero and third location from list into TARecord
               break                                                          # Break out of the function
            else:                                                             # Other than that:
               continue                                                       # End loop and continue with the next iteration
      TAList.append(str(TARecord).lstrip("[").rstrip("]"))                    # Append TARecord in string, leftstrip("["), and rightstrip("]") into TAList 
   for item in TAList:
      print(item)
      
def tenantOrTransaction(UID,listCode,code):                                   # Define tenantOrTransaction function
   while True:                                                                               
      if UID:                                                                 # If UID exists:
         if listCode == "t":                                                  # If listCode equals to "t" Then:
            num = 0                                                           # num equals t0 0
         else:                                                                # Other than that:
            num = 2                                                           # num equals to 2
         searchInformation(listCode,num,UID)                                  # Call function searchInformation(listCode,num,UID)
         if listCode == "t":                                                  # If listCode equals to "t" Then:
            print("\n[C]-Change my tenant details")                           # Print message
         else:                                                                # Other than that:
            print("[A]-Add new transaction")                                  # Print message
         opt = input("[E]-Exit\nWhat would you like to do: ")                 # Print message and get opt 
         if opt in ["C","c"] and listCode == "t":                             # If opt equals to ["C","c"] and listCode equals to "t" Then:
            modifyData(UID,listCode,code,"2")                                 # Call function modifyData(UID,listCode,code,"2") 
         elif opt in ["A","a"] and listCode == "p":                           # If opt equals to ["A","a"] and listCode equals to "p" Then:
            modifyData(UID,listCode,code,"1")                                 # Call function modifyData(UID,listCode,code,"1")
         elif opt in ["E","e"]:                                               # If opt equals to ["E","e"] Then:
            break                                                             # Break out of the function
         else:                                                                # Other than that:
            message(0)                                                        # Print error message
            continue                                                          # End loop and continue with the next iteration
         break                                                                # Break out of the function
      else:                                                                   # Other than that:
         opt = input("[D]-Display existing Data, [M]-Modify Data\n[E]-Exit\nWhat would you like to do:")  # Print message and get opt
         if opt in ["D","d"]:                                                 # If opt equals to ["D","d"] Then:
            print("Current Data:")                                            # Print message 
            readFile(listCode)                                                # Call function readFile(listCode)
         elif opt in ["M","m"]:                                               # If opt equals to ["M","m"] Then:
            modifyData(UID,listCode,code,None)                                # Call function modifyData(UID,listCode,code,None)
         elif opt in ["E","e"]:                                               # If opt equals to ["E","e"] Then:
            break                                                             # Break out of the function
         else:                                                                # Other than that:
            message(0)                                                        # Print error message
            continue                                                          # End loop and continue with the next iteration
         break                                                                # Break out of the function

# - Apartment - #

def apartment(UID,listCode,code):                                             # Define apartment function
   
   listCode = "a"
   print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n- Apartment Info: -\n")
   
   list1 = ["Room Info: Standard Room (Triple)","Code: SR1","Dimensions: 140+ sqft","Pricing: RM350","Apartment ID: A01-L01-R01 to A01-L01-R21","Date of Acquisition: 03/01/2015","Rental History: 27/02/2015 rent","Status: Available"]        # Put sample data
   list2 = ["Room Info: Standard Room (Twin)","Code: SR2","Dimensions: 120+ sqft","Pricing: RM450","Apartment ID: A01-L01-R22 to A01-L01-R41","Date of Acquisition: 10/02/2015","Rental History: 28/03/2015 rent","Status: Available"]          # Put sample data
   list3 = ["Room Info: Standard Room A/C (Triple)","Code: SR3","Dimensions: 150+ sqft","Pricing: RM550","Apartment ID: A01-L02-R01 to A01-L02-R21","Date of Acquisition: 21/03/2016","Rental History: 24/04/2016 rent","Status: Available"]    # Put sample data
   list4 = ["Room Info: Standard Room A/C (Twin)","Code: SR4","Dimensions: 130+ sqft","Pricing: RM650","Apartment ID: A01-L02-R22 to A01-L02-R41","Date of Acquisition: 02/04/2016","Rental History: 20/05/2016 rent","Status: Available"]      # Put sample data
   list5 = ["Room Info: Deluxe Room (Triple)","Code: DR1","Dimensions: 170+ sqft","Pricing: RM750","Apartment ID: A01-L04-R01 to A01-L04-R21","Date of Acquisition: 11/05/2017","Rental History: 21/06/2017 rent","Status: Available"]          # Put sample data
   list6 = ["Room Info: Deluxe Room (Twin)","Code: DR2","Dimensions: 160+ sqft","Pricing: RM840","Apartment ID: A01-L04-R22 to A01-L04-R41","Date of Acquisition: 22/06/2017","Rental History: 22/07/2017 rent","Status: Available"]            # Put sample data
   list7 = ["Room Info: Deluxe Room A/C with shared attached bath / toilet (Triple)","Code: DR3","Dimensions: 180+ sqft","Pricing: RM950","Apartment ID: A01-L03-R1 to A01-L03-R21","Date of Acquisition: 30/07/2018","Rental History: 25/08/2018 rent","Status: Available"]  # Put sample data
   list8 = ["Room Info: Deluxe Room A/C with shared attached bath / toilet","Code: DR4","Dimensions: 170+ sqft","Pricing: RM1040","Apartment ID: A01-L03-R22 to A01-L03-R41","Date of Acquisition: 16/08/2018","Rental History: 18/09/2018 rent","Status: Available"]         # Put sample data
   list9 = ["Room Info: Compact Premium Single","Code: CPS1","Dimensions: 130+ sqft","Pricing: RM690","Apartment ID: A01-L05-R01 to A01-L05-R41","Date of Acquisition: 02/09/2019","Rental History: 29/10/2019 rent","Status: Available"]          # Put sample data
   list10 = ["Room Info: Medium Premium Single","Code: MPS1","Dimensions: 150+ sqft","Pricing: RM750","Apartment ID: A02-L01-R01 to A02-L01-R21","Date of Acquisition: 15/10/2019","Rental History: 31/11/2019 rent","Status: Available"]       # Put sample data
   list11 = ["Room Info: Medium Premium Twin","Code: MPT1","Dimensions: 180+ sqft","Pricing: RM890","Apartment ID: A02-L02-R01 to A02-L02-R21","Date of Acquisition: 25/11/2020","Rental History: 31/12/2020 rent","Status: Available"]         # Put sample data
   list12 = ["Room Info: Medium Premium with attached bath / toilet (Twin)","Code: MP1","Dimensions: 180+ sqft","Pricing: RM940","Apartment ID: A02-L03-R01 to A02-L03-R21","Date of Acquisition: 30/12/2020","Rental History: 31/01/2020 rent","Status: Available"]    # Put sample data
   list13 = ["Room Info: Medium Premium with attached bath / toilet (Single)","Code: MP2","Dimensions: 160+ sqft","Pricing: RM1050","Apartment ID: A02-L03-R22 to A02-L03-R41","Date of Acquisition: 16/01/2021","Rental History: 28/02/2021 rent","Status: Available"] # Put sample data
   list14 = ["Room Info: En-Suite Single (Super Premium - Triple)","Code: ESS3","Dimensions: 160+ sqft","Pricing: RM700","Apartment ID: A02-L04-R01 to A02-L04-R41","Date of Acquisition: 25/02/2021","Rental History: 31/03/2021 rent","Status: Available"]            # Put sample data
   list15 = ["Room Info: En-Suite Single (Super Premium - Twin)","Code: ESS2","Dimensions: 140+ sqft","Pricing: RM800","Apartment ID: A02-L04-R01 to A02-L04-R41","Date of Acquisition: 31/05/2022","Rental History: Empty","Status: Not Available"]                    # Put sample data
   list16 = ["Room Info: En-Suite Twin (Super Premium)","Code: EST2","Dimensions: 200+ sqft","Pricing: RM900","Apartment ID: A02-L05-R01 to A02-L05-R41","Date of Acquisition: 26/06/2022","Rental History: Empty","Status: Not Available"]                             # Put sample data
   ApartmentList = [list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12,list13,list14,list15,list16]    # Declare list containing relevant input data
   with open(listIdentifier(listCode),"w") as apartmentHandler:                               # Open selected text file and named as apartmentHandler 
      for record in ApartmentList:
         for data in record:
            apartmentHandler.write(data)                                                      # Write data into the text file
            apartmentHandler.write(",")                                                       # Write a comma (,) into the text file
         apartmentHandler.write("\n")                                                         # Write a newline ("\n") into the text file 
   
   for item in ApartmentList:
      print(item,"\n")                                                                   # Print each item that inside the ApartmentList  
   print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
   if UID == None:                                                                            # If UID equals to None Then:
      modifyData(UID,listCode,code,None)                                                      # Call function modifyData(UID,listCode,code,None)
   else:                                                                                      # Other than that:
      return False                                                                            # Exit function and send the value back to the program

def modifyData(UID,listCode,code,modifyType):                                                 # Define modifyData function
   modify = True                                                                              # modify equals to True
   while True:                                                                                                                                                              
      if modifyType:                                                                          # If modifyType exists:
         dataInput = modifyType                                                               # dataInput is modifyTYpe
      else:                                                                                   # Other than that:
         dataInput = input('\n- Modification of records: -\n\n1. Add data\n2. Edit Data\n3. Delete Data\n4. Exit\n\nPlease select which operation to perform task (1-4): ') # Print message and get dataInput
      print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
      if dataInput == "1":                                                                    # If dataInput equals to "1" Then:
         if listCode == "a":                                                                  # If listCode equals to "a" Then:
            apartmentAddData(modify,listCode)                                                 # Call apartmentAddData(modify,listcode) functiom
         else:                                                                                # Other than that:
            tenantOrTransactionEntryForm(UID,listCode,code)                                   # Call tenantOrTransactionEntryForm(UID,listCode,code) function
      elif dataInput == "2":                                                                  # If dataInput equals to "2" Then:
         editData(UID,listCode,code)                                                          # Call editData(UID,listCode,code) function
      elif dataInput == "3":                                                                  # If dataInput equals to "3" Then:
         deleteRecord(listCode,code)                                                          # Call deleteRecord(listCode,code) function
      elif dataInput == "4":                                                                  # If dataInput equals to "4" Then:
         break                                                                                # Break and end the loop
      else:                                                                                   # Other than that:
         code = 1                                                                             # Error detected
         message(code)                                                                        # Call function message(code) to print error message
         continue                                                                             # Jump back to the top of loop, Rerun again 
      if UID == None:                                                                         # If UID equals to None:
         continue                                                                             # Jump back to the top of loop, Rerun again
      else:                                                                                   # Other than that:
         break                                                                                # Break and end the loop
   
def apartmentAddData(modify,listCode):                                                        # Define apartmentAddData function
   adddatalist = []                                                                           # Declare adddatalist as array
   print("\nDear admin, we need your ATTENTION !\n\nFor your information, all the new data will only be stored if you insert each information with the correct format provided.\n\nOnce you finish each entry,a confirmation message will appear. Please ensure that the data is typed correctly before saving.\n- Now, you are required to enter new data. -\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------") # Print message
   newroom = newRoom()                                                                        # newroom = call function newRoom()
   newroomcode = newRoomCode()                                                                # newroomcode = call function newRoomCode()
   newroomdimension = newRoomDimension()                                                      # newroomdimension = call function newRoomDimension()
   newroompricing = newRoompricing()                                                          # newroompricing = call function newRoompricing()
   newroomID = newRoomID()                                                                    # newroomID = call function newRoomID()
   newroomdateofacquisition = newRoomDate("Acquisition")                                      # newroomdateofacquisition = call function newRoomDate("Acquisition") 
   newroomrentalhistory = newRoomDate("History")                                              # newroomrentalhistory = call function newRoomDate("History")
   newroomstatus = newRoomStatus()                                                            # newroomstatus = call function newRoomStatus()
   adddatalist = [str(newroom),str(newroomcode),str(newroomdimension),str(newroompricing),str(newroomID),str(newroomdateofacquisition),str(newroomrentalhistory),str(newroomstatus)]   # Apply data to the list
   print("\nNew Data:",adddatalist)                                                           # Print all the add data details to display and easier to make admin do their checking 
   addDataconfirmation = input("\nAre you sure with the records you inserted just now? Enter to continue, 'N' to unsave: ") # Print message and get addDataconfirmation
   if addDataconfirmation in ["N","n"]:                                                       # If addDataconfirmation is equal to ["N","n"] Then:
      adddatalist.clear()                                                                     # Clear all the data that inserted previously
   else:                                                                                      # Other than that:
      appendFile(adddatalist,listCode)                                                        # Append each record into the selected text file 
      print("\n- Data Saved -\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
   return modify                                                                              # Exit function and send the value back to the program

def newRoom():                                                                                # Define newRoom function
   while True:
      code = None                                                                             # Code set as 'None' 
      SCL = 'SCL2'                                                                            # Set specials as 'SCL2'
      specials = specialCharacterList(SCL)                                                    # specials = call function specialCharacterList(SCL)
      newRoom = input("\nRoom info only contains alphabets, no numbers and special characters [Except these special characters: '(' ')' '/' '-' ]\nExample: Dual Key Premium Rooms - Single Room\n\nRoom Info: ") # Print message and get newroom

      if [character for character in newRoom if (character in specials)]:                     # 1st Data Validation - Check special characters 
         code = 2                                                                             # Error detected, code change from 'None' to '2'
         message(code)                                                                        # Print error message, call function message(code)
         print("- Room info does not contain special character(s) -")                         # Error message explanation
         continue                                                                             # Jump back to the top of loop, rerun again 
      else:                                                                                   # Other than that:
         code = None                                                                          # Error not detected, remain the same value 'None'
      if 0 <= len(newRoom) < 6:                                                               # 2nd Data Validation - Input length check
         code = 2                                                                             # Error detected, code change from 'None' to '2'
         message(code)                                                                        # Print error message, call function message(code)
         print("-  Refer to the Room Info to look for its details and format -")              # Error message explanation
         continue                                                                             # Jump back to the top of loop, rerun again 
      else:                                                                                   # Other than that:
         code = None                                                                          # Error not detected, remain the same value 'None'
      if newRoom.isdigit() and any(location.isdigit() for location in newRoom):               # 3rd Data Validation - Check numbers 
         code = 1                                                                             # Error detected, code change from 'None' to '1'
         message(code)                                                                        # Print error message, call function message(code)
         print("- Room info does not contain number(s) -")                                    # Error message explanation
         continue                                                                             # Jump back to the top of loop, rerun again
      else:                                                                                   # Other than that:
         code = None                                                                          # Error not detected, remain the same value 'None'
      if code == None:                                                                        # No error detected, correct input                                                                       # No error detected, correct input                                                                 
         newRoom.title()                                                                      # Return where the first character in each word is uppercase
         decisionkey = input("Save data? (Enter to continue, 'N' to return back):")           # Print message and get decisionkey
         if decisionkey in ['N','n']:                                                         # If decisionkey is equal to ["N","n"] Then:
            continue                                                                          # Jump back to the top of loop. rerun again
         else:                                                                                # Other than that:
            return "New Room Info: " + newRoom                                                # Exit function and send the value back to the program
      else:                                                                                   # Other than that:
         code = 2                                                                             # Error detected, code change from 'None' to '2'
         message(code)                                                                        # Print error message, call function message(code)
         print("- Please fill in the correct format for room info. Refer to the description above for its details and format -")  # Error message explanation
         continue                                                                             # Jump back to the top of loop, rerun again 

def newRoomCode():                                                                            # Define newRoomCode function
   while True:                                                                               
      code = None                                                                             # Code set as 'None' 
      newRoomCode = input("\nRoom code only contains alphanumeric (A combination of uppercased alphabet and number), and no special characters\nExample: DKPRS1\n\nRoom Code: ")    # Get input from admin
      if len(newRoomCode) <= 1 :                                                              # 1st Data Validation - Check empty input and length input
         code = 2                                                                             # Error detected, code change from 'None' to '2'
         message(code)                                                                        # Print error message, call function message(code)
         print("- Room Code must contain at least 2 or more alphanumeric long -\n")           # Error message explanation
         continue                                                                             # Jump back to the top of loop, rerun again
      else:                                                                                   # Other than that:
         code = None                                                                          # Error not detected, remain the same value 'None'
      if newRoomCode.isalnum():                                                               # 2nd Data Validation - Check input contains alphanumeric or not
         code = None                                                                          # Error not detected, remain the same value 'None'
      else:                                                                                   # Other than that:
         code = 2                                                                             # Error detected, code change from 'None' to '2'
         message(code)                                                                        # Print error message, call function message(code)
         print("- Please note that room code is only acceptable when it contains alphanumeric only-\n")  # Error message explanation
         continue                                                                             # Jump back to the top of loop, rerun again
      if code == None:                                                                        # No error detected, correct input                                                                   
         decisionkey = input("Save data? (Enter to continue, 'N' to return back): ")          # Save Data Confirmation Message
         if decisionkey in ['N','n']:                                                         # If decisionkey equals to ["N","n"] Then:
            continue                                                                          # Jump back to the top of loop, rerun again
         else:                                                                                # Other than that:
            return "New Room Code: " + newRoomCode                                            # Exit function and send the value back to the program
      else:                                                                                   # Other than that:
         code = 2                                                                             # Error detected, code change from 'None' to '2'
         message(code)                                                                        # Print error message, call function message(code)
         print("- Please fill in the correct format for room code. Refer to the description above for its details and format -")  # Error message explanation
         continue                                                                             # Jump back to the top of loop, rerun again

def newRoomDimension():                                                                       # Define newRoomDimension function
   while True:                                                                               
      code = None                                                                             # Code set as 'None' 
      newRoomDimension=input("\nRoom Dimension only contains numbers, no alphabets and special characters (The unit (in sqft) will be provided at the back)\nExample: 300(+sqft)\n\nRoom Dimension: ")   # Get input from admin 
      if len(newRoomDimension) == 0:                                                          # 1st Data Validation - Check empty input exist or not
         code = 5                                                                             # Error detected, incorrect input
         message(code)                                                                        # Print error message, call function message(code)
         print("- Please fill in the room dimension, and room dimension must have at least 100 or more sqft -\n")  # Error message explanation
         continue                                                                             # Jump back to the top of loop, rerun again
      else:                                                                                   # Other than that:
         code = None                                                                          # Error not detected, remain the same value 'None'
      if newRoomDimension.isdigit():                                                          # 2nd data Validation - Input check that only contain numbers  
         code = None                                                                          # Error not detected, remain the same value 'None'
      else:                                                                                   # Other than that:
         code = 2                                                                             # Error detected, incorrect input
         message(code)                                                                        # Print error message, call function message(code)
         print("- Room dimension must consist of number(s) -")                                # Error message explanation
         continue                                                                             # Jump back to the top of loop, rerun again
      if code == None:                                                                        # No error detected, correct input
         decisionkey = input("Save data? (Enter to continue, 'N' to return back):")           # Print message and get decisionkey
         if decisionkey in ["N","n"]:                                                         # If decisionkey is equal to ["N","n"] Then:
            continue                                                                          # Jump back to the top of loop, rerun again
         else:                                                                                # Other than that:
            return "Dimensions: " + newRoomDimension + "+ sqft"                               # Exit function and send the value back to the program
      else:                                                                                   # Other than that:
         code = 2                                                                             # Error detected, code change from 'None' to '2'
         message(code)                                                                        # Print error message, call function message(code)
         print("- Please fill in the correct format for room dimension. Refer to the description above for its details and format -\n")   # Error message explanation
         continue                                                                             # Jump back to the top of loop, rerun again

def newRoompricing():                                                                         # Define newRoompricing function
   while True:                                                                               
      code = None                                                                             # Code set as 'None' 
      newRoompricing=input("\nRoom Pricing only contain numbers, no special characters (The unit (in RM) will be provided at the front)\nExample: (RM)500\n\nRoom Pricing: ")    # Get input from admin
      if newRoompricing.isdigit():                                                            # Validation - Input check that only contain numbers 
         nRp=int(newRoompricing)                                                              # Convert to integer 
         if nRp >= 350:                                                                       # If nRp equals or greater than 350 Then:
            code = None                                                                       # No error detected, correct input, code equals to None
         else:                                                                                # Other than that:
            code = 1                                                                          # Error detected, code change from 'None' to '1' 
            message(code)                                                                     # Print error message, call function message(code)
            print("- Minimum starting price starts from RM350 and above -\n")                 # Error message confirmation
            continue                                                                          # Jump back to the top of loop, rerun again
      else:                                                                                   # Other than that:
         code = 2                                                                             # Error detected, code change from 'None' to '2'
         message(code)                                                                        # Print error message, call function message(code)
         print("- Please fill in the room pricing, it must be in numeric and the minimum starting price starts from RM350 and above -\n")  # Error message explanation
         continue                                                                             # Jump back to the top of loop, rerun again
      if code == None:                                                                        # No error detected, correct input                                                                       # No error detected, correct input
         decisionkey = input("Save data? (Enter to continue, 'N' to return back):")           # Print message and get decisionkey
         if decisionkey in ["N","n"]:                                                         # If decisionkey is equal to ["N","n"] Then:
            continue                                                                          # Jump back to the top of loop, rerun again
         else:                                                                                # Other than that:
            return "Pricing: RM" + newRoompricing                                             # Exit function and send the value back to the program
      else:                                                                                   # Other than that:
         code = 2                                                                             # code equals to 2
         message(code)                                                                        # Print error message, call function message(code)
         print("- Please follow the correct format for new room pricing. Refer to the description above to know its details and format -\n") # Print error message explanation
         continue                                                                             # Jump back to the top of loop, rerun again

def newRoomID():                                                                              # Define newRoomID function
   while True:                                                                               
      code = None                                                                             # code equals to None 
      newRoomID = input('\nThis is the correct format for RoomID: A(01)-L(01)-R(01)x(to)xA(99)-L(99)-R(99), x means space\nPlease enter the new Room ID: ') # Print message and get newRoomID
      if 0 <= len(newRoomID) <= 25:                                                           # If len(newRoomID) is between range 0 to 25 Then:
         print("\n- Please fill in the new room ID with the correct format -")                # Print message
         continue                                                                             # Jump back to the top of loop, rerun again
      else:                                                                                   # Other than that:
         if (newRoomID[0] == 'A' and newRoomID[3] == '-' and newRoomID[4] == 'L' and newRoomID[7] == '-' and newRoomID[8] == 'R' and newRoomID[11] == ' ' and newRoomID[12] == 't' and newRoomID[13] == 'o' and newRoomID[14] == ' ' and newRoomID[15] == 'A' and newRoomID[18] == '-' and newRoomID[19] == 'L' and newRoomID[22] == '-' and newRoomID[23] == 'R'):
            if ((newRoomID[1] and newRoomID[2] and newRoomID[5] and newRoomID[6] and newRoomID[9] and newRoomID[10] and newRoomID[16] and newRoomID[17] and newRoomID[20] and newRoomID[21] and newRoomID[24] and newRoomID[25]).isdigit): # Data validation - 
               decisionkey = input("Save data? (Enter to continue, 'N' to return back):")     # Print message and get decisionkey
               if decisionkey in ["N","n"]:                                                   # If decisionkey is equal to ["N","n"] Then:
                  continue                                                                    # Jump back to the top of loop, rerun again
               else:                                                                          # Other than that:
                  return "Apartment ID: " + newRoomID                                         # Exit function and send the value back to the program
            else:                                                                             # Other than that:
               code = 1                                                                       # code equals to 1
               message(code)                                                                  # Print error message, call function message(code)
               continue                                                                       # Jump back to the top of loop, rerun again
         else:                                                                                # Other than that:
            code = 2                                                                          # Code equals to 2
            message(code)                                                                     # Print error message, call function message(code)
            print("- Incorrect Room ID -")                                                    # Error message explanation
            continue                                                                          # Jump back to the top of loop, rerun again

def newRoomDate(dateType):                                                                    # Define newRoomDate function
   while True:                                                                               
      code = None                                                                             # code equals to None
      if dateType == "Acquisition":                                                           # if dataType equals to "Acquisition" Then:
         roomDate = input("\nRoom Date of Acquisition: dd/mm/yyyy\nNo special characters included, except '/'\n\nRoom Acquisition Date: ")  # Print message and getroomDate
      else:                                                                                   # Other than that:
         roomDate = input("\nRoom Rental History: (Accepted input: 'dd/mm/yyyy' or 'Empty')\nNo special characters included, except '/'\n\nRoom Rental History: ")  # Print message and getroomDate
      if any(location.isdigit() for location in roomDate) and len(roomDate) == 10:            # Data validation: Date check, check roomDate only consists numbers and length must have 10 characters long
         day,month,year = roomDate.split('/')                                                 # Split roomDate to day, month, and year using ("/") as a separator 
         ValidDate = True                                                                     # ValidDate equals to True
         try:
            dt.datetime(int(year),int(month),int(day))                                        # Insert the year, month, day in integer
            ValidDate = True                                                                  # ValidDate equals to True
         except ValueError:
            ValidDate = False                                                                 # ValidDate equals to False
         if ValidDate == True :                                                               # If ValidDate equals to True:
            code = None                                                                       # code equals to None
            decisionkey = input("Save data? (Enter to continue, 'N' to return back):")        # Print message and get decisionkey
            if decisionkey in ["N","n"]:                                                      # If decisionkey is equal to ["N","n"] Then:
               continue                                                                       # Jump back to the top of loop, rerun again
            else:                                                                             # Other than that:
               return "Acquisition Date: " + roomDate                                         # Exit function and send the value back to the program
         else:                                                                                # Other than that:
            code = 2                                                                          # Code equals to 2
            message(code)                                                                     # Print error message, call function message(code)
            print("- The given date is not valid -\n")                                        # Error message explanation
            continue                                                                          # Jump back to the top of loop, rerun again
      else:                                                                                   # Other than that:
         code = 2                                                                             # Code equals to 2
         message(code)                                                                        # Print error message, call function message(code)
         print("- Wrong Date Format (dd/mm/yyyy) -\n")                                        # Error message explanation
         continue                                                                             # Jump back to the top of loop, rerun again

def newRoomStatus():                                                                          # Define newRoomStatus
   while True:                                                                               
      code = None                                                                             # code equals to None
      newRoomStatus = input("\nRoom Status: [A]-Available; [Any other key]-Not Available')\n\nRoom Status ( Available / Not Available ): ")  # Print message and get nreRoomStatus
      if newRoomStatus in ["A","a"]:                                                          # If decisionkey is equal to ["N","n"] Then:
         newRoomStatus = "Available"                                                          # newRoomStatus equals to "Available"
      else:                                                                                   # Other than that:
         newRoomStatus = "Not Available"                                                      # newRoomStatus equals to "Not Available"
      if code == None:                                                                        # No error detected, correct input
         decisionkey = input("Save data? (Enter to continue, 'N' to return back):")           # Print message and get decisionkey
         if decisionkey in ["N","n"]:                                                         # If decisionkey is equal to ["N","n"] Then:
            continue                                                                          # Jump back to the top of loop, rerun again
         else:                                                                                # Other than that:
            return "Status: "+newRoomStatus                                                   # Exit function and send the value back to the program
      else:                                                                                   # Other than that:
         code = 3                                                                             # code equals to 3
         message(code)                                                                        # Print error message, call function message(code)
         print("Please insert the correct format for room status. Refer to the description above for its details and format -\n")  # Print error message explanation
         continue                                                                             # Jump back to the top of loop, rerun again

def inputidentifier(UID,listCode,editDataType,code):                                          # Define inputidentifier function
   if listCode == "a":                                                                        # If listCode equals to "a" Then:
      if editDataType == 0:                                                                   # If editDataType equals to 0 Then:
         return newRoom()                                                                     # Exit function and send the value back to the program
      elif editDataType == 1:                                                                 # If editDataType equals to 0 Then:
         return newRoomCode()                                                                 # Exit function and send the value back to the program
      elif editDataType == 2:                                                                 # If editDataType equals to 0 Then:
         return newRoomDimension()                                                            # Exit function and send the value back to the program
      elif editDataType == 3:                                                                 # If editDataType equals to 0 Then:
         return newRoompricing()                                                              # Exit function and send the value back to the program
      elif editDataType == 4:                                                                 # If editDataType equals to 0 Then:
         return newRoomID()                                                                   # Exit function and send the value back to the program
      elif editDataType == 5:                                                                 # If editDataType equals to 0 Then:
         return newRoomDate("acquisition")                                                    # Exit function and send the value back to the program
      elif editDataType == 6:                                                                 # If editDataType equals to 0 Then:
         return newRoomDate("history")                                                        # Exit function and send the value back to the program
      else:                                                                                   # Other than that:
         return newRoomStatus()                                                               # Exit function and send the value back to the program
   elif listCode == "t":
      if editDataType == 0:                                                                   # If editDataType equals to 0 Then:
         return gettenantID(UID,"existing")                                                   # Exit function and send the value back to the program
      elif editDataType == 1:                                                                 # If editDataType equals to 0 Then:
         return getname(code,"tenant")                                                        # Exit function and send the value back to the program
      elif editDataType == 2:                                                                 # If editDataType equals to 0 Then:
         return getabbreviation(code,"gender")                                                # Exit function and send the value back to the program
      elif editDataType == 3:                                                                 # If editDataType equals to 0 Then:
         return getpNum(code)                                                                 # Exit function and send the value back to the program
      elif editDataType == 4:                                                                 # If editDataType equals to 0 Then:
         return getabbreviation(code,"nationality")                                           # Exit function and send the value back to the program
      elif editDataType == 5:                                                                 # If editDataType equals to 0 Then:
         return getDate(code,"start")                                                         # Exit function and send the value back to the program
      elif editDataType == 6:                                                                 # If editDataType equals to 0 Then:
         return getnumber(code,"workHistory")                                                 # Exit function and send the value back to the program
      elif editDataType == 7:                                                                 # If editDataType equals to 0 Then:
         return getname(code,"employer")                                                      # Exit function and send the value back to the program
      elif editDataType == 8:                                                                 # If editDataType equals to 0 Then:
         return getnumber(code,"income")                                                      # Exit function and send the value back to the program
      elif editDataType == 9:                                                                 # If editDataType equals to 0 Then:
         return getrental(UID)                                                                # Exit function and send the value back to the program
      elif editDataType == 10:                                                                # If editDataType equals to 0 Then:
         return getDate(code,"birth")                                                         # Exit function and send the value back to the program
      else:                                                                                   # Other than that:
         return getname(code,"city")                                                          # Exit function and send the value back to the program
   else:                                                                                      # Other than that:
      if editDataType == 0:                                                                   # If editDataType equals to 0 Then:
         return getreferenceNumber(code)                                                      # Exit function and send the value back to the program
      elif editDataType == 1:                                                                 # If editDataType equals to 0 Then:
         return getDate(code,"transaction")                                                   # Exit function and send the value back to the program
      elif editDataType == 2:                                                                 # If editDataType equals to 0 Then:
         return gettenantID(UID,"existing")                                                   # Exit function and send the value back to the program
      elif editDataType == 3:                                                                 # If editDataType equals to 0 Then:
         chooseList = "a"                                                                     # chooseList equals to "a"
         displayColumn = 0                                                                    # displayColoumn equals to 0
         currentColumn = 1                                                                    # currentColoumn equals to 1
         return chooseItem(UID,chooseList,displayColumn,currentColumn)                        # Exit function and send the value back to the program
      else:                                                                                   # Other than that:
         return getdecimal(code)                                                              # Exit function and send the value back to the program

def ApartmentDataInfo():                                                                      # Define ApartmentDataInfo function:
   data = True                                                                                # Data equals to True
   while data == True:                                                                        # When Data equals to True Then:
      opt = input("\n[R] - Room Info [C] - Room code, [D] - Dimensions, [P] - Pricing, [A] - Apartment ID, [E] - Date of Acquisition, [H] - Rental History, [S] - Status \nAnswer: ")  # Print message and get opt
      if opt in ["R","r"]:                                                                    # If opt equals to ["R","r"] Then:
         num = 0                                                                              # num equals to 0
      elif opt in ["C","c"]:                                                                  # If opt equals to ["C","c"] Then:
         num = 1                                                                              # num equals to 1
      elif opt in ["D","d"]:                                                                  # If opt equals to ["D","d"] Then:
         num = 2                                                                              # num equals to 2
      elif opt in ["P","p"]:                                                                  # If opt equals to ["P","p"] Then:
         num = 3                                                                              # num equals to 3
      elif opt in ["A","a"]:                                                                  # If opt equals to ["A","a"] Then:
         num = 4                                                                              # num equals to 4
      elif opt in ["E","e"]:                                                                  # If opt equals to ["E","e"] Then:
         num = 5                                                                              # num equals to 5
      elif opt in ["H","h"]:                                                                  # If opt equals to ["H","h"] Then:
         num = 6                                                                              # num equals to 6
      elif opt in ["S","s"]:                                                                  # If opt equals to ["S","s"] Then:
         num = 7                                                                              # num equals to 7
      else:                                                                                   # Other than that:
         code = 0                                                                             # code equals to 0
         message(code)                                                                        # Print error message, call function message(code)
         continue                                                                             # End loop and continue with the next iteration                                                                         # Jump back to the top of loop, rerun again
      return num                                                                              # Exit function and send the value back to the program

def category(listCode,code,sourceFunction):                                                   # Define category function
   while True:                                                                               
      if listCode == "p":                                                                     # If listCode equals to "p" Then:
         opt = input("\n[R]-Reference number,[D]-Transaction date,[T]-TenantID,[A]-Apartment code,[S]-Amount\n Choose a category: ")  # Print message and get opt
         if opt in ["R","r"]:                                                                 # If opt is equal to ["R","r"] Then:
            num = 0                                                                           # num equals to 0
         elif opt in ["D","d"]:                                                               # If opt is equal to ["D","d"] Then:
            num = 1                                                                           # num equals to 1
         elif opt in ["T","t"]:                                                               # If opt is equal to ["T","t"] Then:
            num = 2                                                                           # num equals to 2
         elif opt in ["A","a"]:                                                               # If opt is equal to ["A","a"] Then:
            num = 3                                                                           # num equals to 3
         elif opt in ["S","s"]:                                                               # If opt is equal to ["S","s"] Then:
            num = 4                                                                           # num equals to 4
         else:                                                                                # Other than that:
            code = 0                                                                          # code equals to 0
            message(code)                                                                     # Print error message, call function message(code)
            continue                                                                          # End loop and continue with the next iteration
      else:                                                                                   # Other than that:
         if sourceFunction == "edit":                                                         # If sourceFunction equals to "edit" Then:
            print("\n[N]-Name,[G]-Gender,[P]-Phone number,[R]-Nationality,[D]-Rental start date,[W]-Work history,[E]-Employer,[I]-Income,[S]-Tenant status,[B]-Birthdate,[C]-Birth City")  # Print message
         else:                                                                                # Other than that:
            print("\n[U]-User ID,[N]-Name,[G]-Gender,[P]-Phone number,[R]-Nationality,[D]-Rental start date,[W]-Work history,[E]-Employer,[I]-Income,[S]-Tenant status,[B]-Birthdate,[C]-Birth City")  # Print message
         opt = input("Choose a category: ")                                                   # Print message and get opt
         if opt in ["U","u"] and sourceFunction == "search":                                  # If opt is equal to ["U","u"] and sourceFunction equals to "search" Then:
            num = 0                                                                           # num equals to 0
         elif opt in ["N","n"]:                                                               # If opt is equal to ["N","n"] Then:
            num = 1                                                                           # num equals to 0
         elif opt in ["G","g"]:                                                               # If opt is equal to ["G","g"] Then:
            num = 2                                                                           # num equals to 0
         elif opt in ["P","p"]:                                                               # If opt is equal to ["P","p"] Then:
            num = 3                                                                           # num equals to 0
         elif opt in ["R","r"]:                                                               # If opt is equal to ["R","r"] Then:
            num = 4                                                                           # num equals to 0
         elif opt in ["D","d"]:                                                               # If opt is equal to ["D","d"] Then:
            num = 5                                                                           # num equals to 0
         elif opt in ["W","w"]:                                                               # If opt is equal to ["W","w"] Then:
            num = 6                                                                           # num equals to 0
         elif opt in ["E","e"]:                                                               # If opt is equal to ["E","e"] Then:
            num = 7                                                                           # num equals to 0
         elif opt in ["I","i"]:                                                               # If opt is equal to ["I","i"] Then:
            num = 8                                                                           # num equals to 0
         elif opt in ["S","s"]:                                                               # If opt is equal to ["S","s"] Then:
            num = 9                                                                           # num equals to 0
         elif opt in ["B","b"]:                                                               # If opt is equal to ["B","b"] Then:
            num = 10                                                                          # num equals to 0
         elif opt in ["C","c"]:                                                               # If opt is equal to ["C","c"] Then:
            num = 11                                                                          # num equals to 0
         else:                                                                                # Other than that:
            code = 0                                                                          # code equals to 0
            message(code)                                                                     # Print error message, call function message(code)
            continue                                                                          # End loop and continue with the next iteration 
      return num                                                                              # Exit function and send the value back to the program

def replaceOldData(listCode,recordindex,editDataType,newData):                                # Define replaceOldData function
   with open(listIdentifier(listCode),"r") as Xhandler:                                       # Open selected text file in read mode as Xhandler
      updatedData = []                                                                        # Declare adddatalist as array
      newRecord = []                                                                          # Declare adddatalist as array
      dataRead = Xhandler.readlines()                                                         # Read each lines in Xhandler
      for record in dataRead:
         strippedRecord = record.rstrip(",\n").split(",")                                     # Rightstrip comma and newline (",\n"), and split record by using comma {","} as a separator
         if dataRead.index(record) == int(recordindex):
            if newData:                                                                       # If newData exists:
               strippedRecord[int(editDataType)] = newData                                    # Modify the record with new data
               newRecord = ",".join(strippedRecord)                                           # Capture the new record, join each strippedrecord with a comma at the end
               updatedData.append(newRecord+",\n")                                            # Append record, comma and newline into updatedData
            else:                                                                             # Other than that:
               continue                                                                       # Jump back to the top of loop, rerun again
         else:                                                                                # Other than that:
            updatedData.append(record)                                                        # Append record into updatedData
   with open(listIdentifier(listCode),"w") as fUpdate:                                        # Open selected text file in Write Mode asfUpdate
      for record in updatedData:
         fUpdate.write(record)                                                                # Write record into fUpdate
   return False                                                                               # Exit function and send the value back to the program

def editData(UID,listCode,code):                                                              # Define editData function
   sourceFunction = "edit"                                                                    # sourceFunction equals to "edit"
   while True:                                                                               
      if listCode == "a":                                                                     # If listCode equals to "a" Then:
         editDataType = ApartmentDataInfo()                                                   # editDataType = call function ApartmentDataInfo()
      else:                                                                                   # Other than that:
         editDataType = category(listCode,code,sourceFunction)                                # editDataType = call function category(listCode,code,sourceFunction)
      display = searchColumn(listCode,editDataType,UID)                                       # display = call function searchColumn(listCode,editDataType,UID) 
      oldDataFormat = False                                                                   # oldDataFormat equals to False
      while oldDataFormat == False:                                                           # When oldDataFormat equals to False Then:
         if UID == None:                                                                      # If UID equals to None
            listLength = len(display)                                                         # listlength = the length of display
            for item in range(0,listLength,2):                                                # For item from 0 to listLength, but incremented by 2
               try:
                  print(display[item],"   ",display[item+1])
               except IndexError:
                  print(display[item])
            print("\nPlacement of items displayed above are labeled from upper-left to lower-right starting from 1 to",len(display))  # Print message
            selectedData = input("\nPlease enter the number of the item to edit:")            # Print message and get selectedData
            if selectedData.isdecimal():                                                      # Data validation, Number check - If selectedData only consists of numbers Then:
               recordindex = int(selectedData)-1                                              # recordindex = selectedData (in integer) subtract by 1 to search specific data location
               oldDataFormat = True                                                           # oldDataFormat equal to True
            else:                                                                             # Other than that:
               code = 1                                                                       # code equals to 1
               message(code)                                                                  # Print error message, call function message(code)
               continue                                                                       # Jump back to the top of loop, rerun again
         else:                                                                                # Other than that, tenants edit their own infromation:
            for item in range(0,len(display)):                                                # For item from 0 to listLength, but incremented by 2
               if item == len(display)-1:                                                     # If the current iteration is the last item
                  recordindex = item                                                          # recordindex is item
                  oldDataFormat = True                                                        # oldDataFormaat equal to True
               else:                                                                          # Other than that:
                  continue                                                                    # Jump back to the top of loop, rerun again
      print("\nPlease insert the new data with the correct format as below: ")                # Print message
      newData = inputidentifier(UID,listCode,editDataType,code)                               # newData = call function inputidentifier(UID,listCode,editDataType,code)
      editdataconfirmation = input("\nAre you sure with your records just now? ([Y]-Yes/[N]-No): ")  # Print message and get editdataconfirmation
      if editdataconfirmation in ["Y","y"]:                                                   # If editdataconfirmation is equal to ["Y","y"] Then:
         replaceOldData(listCode,recordindex,editDataType,newData)                            # Call function replaceOldData(listCode,recordindex,editDataType,newData) 
         break                                                                                # Break and end the loop
      elif editdataconfirmation in ["N","n"]:                                                 # If editdataconfirmation is equal to ["N","n"] Then:         
         break                                                                                # Break and end the loop
      else:                                                                                   # Other than that:
         code = 0                                                                             # code equals to 0
         message(code)                                                                        # Print error message, call function message(code)
         continue                                                                             # End loop and continue with the next iteration                                                                                      # Jump back to the top of loop, rerun again
      
def deleteRecord(listCode,code):                                                              # Define deleteRecord function
   while True:                                                                               
      print("\n- Delete Data -")                                                              # Print message 
      deletedata = input("\n1. Delete specified records\n2. Delete all records\n\n[E] - Exit\n\nPlease select and enter which operator that you want to proceed: ")  # Print message and get deletedata
      if deletedata == '1':                                                                   # If deletedata is equal to 1 Then:
         print("\n- 1. Delete specified records -")                                           # Print message
         deleteSpecRecord(listCode,code)                                                      # Call function deleteSpecRecord(listCode,code)
      elif deletedata == '2':                                                                 # If deletedata is equal to 2 Then:
         print("\n- 2. Delete all records -")                                                 # Print message
         deleteAllrecords(listCode)                                                           # Call function deleteAllrecords(listCode)
      elif deletedata in ["E","e"]:                                                           # If deletedata is equal to ["E","e"] Then:
         break                                                                                # Break out of the function
      else:                                                                                   # Other than that:
         code = 0                                                                             # code equals to 0
         message(code)                                                                        # Print error message, call function message(code)
         continue                                                                             # End loop and continue with the next iteration 

def deleteSpecRecord(listCode,code):                                                          # Define deleteSpecRecord 
   modify = True                                                                              # Modify equals to True
   while True:
      readFile(listCode)                                                                      # Call function readFile(listCode)
      selecteddatarow = input("\nWhich data row that you want to delete? ")                   # Print message and get selecteddatarow 
      if selecteddatarow.isdigit():                                                           # Data validation - Number check, if selecteddatarow only consists of numbers:
         number = int(selecteddatarow)-1                                                      # number = selecteddatarow (in integer) subtract by 1 to search specific data location
         editDataType = None                                                                  # editDataType equals to None
         newData = None                                                                       # newData equals to None
         confirmation = input("\nAre you sure that you want to delete all the record(s)?\nIt will be not recovered once you hit [X]. However, you still can discard this changes by hitting any other keys if you change your mind: ")  # Print message and get confirmation
         if confirmation in ["X","x"]:                                                        # If confirmation equals to ["X","x"] Then:
            replaceOldData(listCode,number,editDataType,newData)                              # call function replaceOldData(listCode,number,editDataType,newData)
            print("\n- Delete successful -")                                                  # Print message
         else:                                                                                # Other than that:
            print("\n- Delete unsuccessful -")                                                # Print message
      else:                                                                                   # Other than that:
         code = 0                                                                             # code equals to 0
         message(code)                                                                        # Print error message, call function message(code)
         continue                                                                             # End loop and continue with the next iteration
      return modify                                                                           # Exit function and send the value back to the program

def deleteAllrecords(listCode):                                                               # Define deleteAllrecords function
   modify = True                                                                              # modify equals to True
   while modify == True:                                                                      # When modify equals to True Then:
      confirmation = input("\nAre you sure that you want to delete all the record(s)?\nIt will be not recovered once you hit [X]. However, you still can discard this changes by hitting any other keys if you change your mind: ")  # Print message and get confirmation
      if confirmation in ["X","x"]:                                                           # If confirmation equals to ["X","x"] Then:
         with open (listIdentifier(listCode),"r+") as ADeletedhandler:                        # Open selected text file in read and write mode as Adeletehandler
            ADeletedhandler.seek(0)                                                           # Absolute file positioning
            ADeletedhandler.truncate()                                                        # Erase all data
            print("\n- Delete successful -")                                                  # Print message
      else:                                                                                   # Other than that:
         print("\n- Delete unsuccessful -")                                                   # Print message
      return modify                                                                           # Exit function and send the value back to the program

def searchColumn(listCode,num,UID):                                                           # Define searchColumn function
   displayList=[]                                                                             # Declare displayList as array
   with open (listIdentifier(listCode), "r") as Tread:                                        # Open selected text file in read mode as Tread
      bulkData = Tread.readlines()                                                            # Read each line in Tread
      for line in bulkData:
         individualList = line.strip(",\n").split(",")                                        # Strip with comma and newline (",\n"), and split with comma (",")
         if listCode == "a":                                                                  # If listCode equals to "a" Then:
            if int(num) < 7:                                                                  # If num in integer less than 7 Then:
               displayList.append(individualList[num])                                        # Append individualList (num location) into displayList
            else:                                                                             # Other than that:
               displayList.append(str(individualList[1])+" ;"+str(individualList[num]))       # Append individualist (first location in string), semicolon and individualList (num in string) into displayList
         else:                                                                                # Other than that:
            if UID == None:                                                                   # If UID equals to None Then:
               if listCode == "u":                                                            # If listCode equals to "u" Then:
                  if num == 0:                                                                # If num equals to 0 Then:
                     displayList.append("ID: "+str(individualList[num])+" ;relevant data: "+str(individualList[2]))  # Append into displayList
                  else:                                                                       # Other than that:
                     displayList.append(individualList[num])                                  # Append individualList (num location) into displayList
               else:                                                                          # Other than that:
                  if num == 0:                                                                # If num is equal to 0 Then:
                     displayList.append(individualList[num])                                  # Append individualList (num location) into displayList
                  else:                                                                       # Other than that:
                     displayList.append("ID: "+str(individualList[0])+" ;relevant data: "+str(individualList[num]))   # Append into displayList
            else:                                                                             # Other than that:
               if listCode == "t":                                                            # If listCode is equal to "t" Then:
                  if individualList[0] == UID:                                                # If individualList (in zero location) is equals to UID Then:
                     if num == 0:                                                             # If num equals to 0 Then:
                        displayList.append(individualList[num])                               # Append individualList (num location) into displayList
                        break                                                                 # Break out of the function
                     else:                                                                    # Other than that:
                        displayList.append("ID: "+str(individualList[0])+" ;relevant data: "+str(individualList[num]))  # Append into displayList
                        break                                                                 # Break out of the function
                  else:                                                                       # Other than that:
                     displayList.append("")                                                   # Append ("") into displayList
   if displayList == []:                                                                      # if display is equal to empty array [] Then:
      code = 5                                                                                # code equals to 5
      message(code)                                                                           # Print error message, call function message(code)
   else:                                                                                      # Other than that:
      return displayList                                                                      # Exit function and send the value back to the program

def searchBox(UID,code):                                                                      # Define search function
   while True:                                                                               
      print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nWelcome to search box!")   # Print message
      sourceFunction = "search"                                                               # sourceFunction equals to "search"
      num = None                                                                              # num equals to None
      print("\n1. Search room specific details.\n2. Search transaction details.\n3. Search specific tenant details.\n4. Exit search box.\n")
      option=input("Please type the search criteria based on the listing above: ")            # Print message and get option
      if option.isdigit and option == "1":                                                    # If option is digit and option equals to '1' Then:
         listCode= "a"                                                                        # listCode is "a"
         opt = input("\n[C]-Room code, [D]- Dimension, [P]-Pricing, [A]- Apartment ID, [E]-Date of Acquisition, [R]-Rental History\nSearch?  ")   # Print message and get opt  
         if opt in ["C","c"]:                                                                 # If opt is equal to ["C","c"] Then:
            num = 1                                                                           # num equals to 0
         elif opt in ["D","d"]:                                                               # If opt is equal to ["D","d"] Then:
            num = 2                                                                           # num equals to 0
         elif opt in ["P","p"]:                                                               # If opt is equal to ["P","p"] Then:
            num = 3                                                                           # num equals to 0
         elif opt in ["A","a"]:                                                               # If opt is equal to ["A","a"] Then:
            num = 4                                                                           # num equals to 0
         elif opt in ["E","e"]:                                                               # If opt is equal to ["E","e"] Then:
            num = 5                                                                           # num equals to 0
         elif opt in ["R","r"]:                                                               # If opt is equal to ["R","r"] Then:
            num = 6                                                                           # num equals to 0
         else:                                                                                # Other than that:
            code = 0                                                                          # code equals to 0
            message(code)                                                                     # Print error message, call function message(code)
            continue                                                                          # End loop and continue with the next iteration
         print(searchColumn(listCode,num,UID))                                                # Print function (searchColumn(listCode,num,UID)) 
      elif option.isdigit() and option == "2":                                                # If option only consists of number and option is equal to "2":
         listCode = "p"                                                                       # listCode equals to "p"
         if UID:                                                                              # If UID exists:
            num = 2                                                                           # num equals to 2
         else:                                                                                # Other than that:
            num = category(listCode,code,sourceFunction)                                      # num = call function category(listCode,code,sourceFunction)
            print(searchColumn(listCode,num,UID))                                             # Print function (searchColumn(listCode,num,UID))                              
      elif option.isdigit() and option == "3" :                                               # If option only consists of number and option is equal to "3":
         listCode = "t"                                                                       # listCode equals to "t"
         if UID:                                                                              # If UID exists:
            num = 0                                                                           # num equals to 0
         else:                                                                                # Other than that:
            num = category(listCode,code,sourceFunction)                                      # num = call function category(listCode,code,sourceFunction)
            print(searchColumn(listCode,num,UID))                                             # Print function (searchColumn(listCode,num,UID)) 
      elif option.isdigit() and option == "4":                                                # If option only consists of number and option is equal to "3":
         print("\n- Return to main menu -\n\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n- Welcome back ! -") # Print message
         break                                                                                # Break out of the function
      else:                                                                                   # Other than that:
         code = 0                                                                             # code equals to 0
         message(code)                                                                        # Print error message, call function message(code)
         continue                                                                             # End loop and continue with the next iteration 
      if UID:                                                                                 # If UID exists:
         if listCode == "a":                                                                  # If listCode equals to "a" Then:
            details = None                                                                    # details set to None
         else:                                                                                # Other than that:
            details = UID                                                                     # details set to UID
      else:                                                                                   # Other than that:
         details = None                                                                       # details set to None 
      searchInformation(listCode,num,details)                                                 # call function searchInformation(listCode,num,details)

def searchInformation(listCode,num,details):                                                  # Define searchinformation function
   while True:                                                                               
      if details:                                                                             # If details exists:
         searchInformation = details                                                          # searchinformation is details 
      else:                                                                                   # Other than that:
         searchInformation = input("\nPlease enter text to begin the search: ")               # Print message and get searchinformation
      recordExist = False                                                                     # recordExist set as False
      with open(listIdentifier(listCode),"r") as Xhandler:                                    # Open selected text file in read mode as Xhandler:
         print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nResults:\n")   # Print message 
         for record in Xhandler:
            data=record.split(",")                                                            # Split record with comma (",")
            if searchInformation in data[num]:                                                # If searchinformation is in the data (in num) Then:
               print(record.rstrip(", ").rstrip("\n"))                                        # Print record, rightstrip comma and space, rightstrip newline
               print()                                                                        # Print a newline
               recordExist = True                                                             # recordExist equals to True
            else:                                                                             # Other than that:
               continue                                                                       # Jump back to the top of loop, rerun again
         if recordExist == True:                                                              # If recordExist equals to True Then:
            code = 0                                                                          # code equals to 0
            print("- Matching records ends here -")                                           # Print message
         else:                                                                                # Other than that:
            code = 4                                                                          # code equals to 4
            message(code)                                                                     # Print error message, call function message(code)
         break

import datetime as dt
listCode = "u"                                                          # Set listCOde to 'u'
code = None                                                             # Set code to 'None'
username = None
password = None
print("\nWelcome to Tenant Management System.")
new = input("[Y]-Yes I am.\n[Any Other Key]-No,I have an existing account\nAre you a new user: ")
if new in ["Y","y"]:                                                 # If new in ["Y","y"] Then:
   username,password = register(listCode,code)                       # call function register(listCode,code)
   login(listCode,code,username,password)
else:
   login(listCode,code,username,password)
