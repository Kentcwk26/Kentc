#with open("user.txt","r") as user:
#    rd = user.readlines()
#    for columns in rd:
#        print(columns.rstrip(",").rstrip("\n"))

#Adminkey=False

#def search():
#   while True:
#      category = input("[T-Tenant\n[A-Apartment\n[P-Transaction\n[L-Leave\nChoose a category:")
#      if category in ["T","t":
#         tenantsearch()
#      elif category in  ["A","a":
#         searchbox()
#      elif category in  ["P","p":
#         transactionsearch()
#      elif category in  ["L","l":
#         return False
#      else:
#         code = 0
#         message(code)

#t= "transaction.txt"
#with open(t,"r") as thandler:
#    tread = thandler.readline()
#if tread:
#    print(tread.rstrip(","))
#else:
#    print("record doesnt exist")

#FUNCTION tenantSearch(details):  REPLACED BY UPDATED searchInformation FUNCTION
#    OPEN "tenant.txt" IN READ AS TSearch
#        READ TSearch
#        TSearch STRIP (",")
#        list = JOIN TSearch INTO string(",")
#        FOR record IN list
#            IF record STARTS WITH details THEN
#                PRINT("Found record", record RIGHTSTRIP(",") RIGHTSTRIP(""))
#            ENDIF
#        ENDFOR
#    CLOSEFILE
#ENDFUNCTION
#FUNCTION tenantRead()  REPLACED BY UPDATED readFile FUNCTION
#    OPEN (tenant.txt) IN READ AS fTenant
#        tenantList = READ fTenant LINE-BY-LINE
#        FOR record IN tenantList
#            PRINT(record RIGHTSTRIP(",") RIGHTSTRIP("NEWLINE"))
#        ENDFOR
#    CLOSEFILE
#ENDFUNCTION



# searchInformation = input("Select and enter text to begin search: ") REPLACED BY UPDATED searchInformation FUNCTION
# num=0
# listCode="p"
# if listCode == "p":
#     l="transaction.txt"
# elif listCode=="a":
#     l="apartment.txt"
# elif listCode=="t":
#     l="apartment.txt"    
# with open (l,"r") as Xhandler:
#     for record in Xhandler:
#         strippeditem = record.rstrip(",").rstrip("NEWLINE")
#         data = strippeditem.split(",")
#         if searchInformation in data[num:
#             print("\n Results: \n",record)

#def apartmentSearch(num):      REPLACED BY UPDATED searchInformation FUNCTION
#    displaylist=[]
#    with open ("Apartment.txt", "r") as Tread:
#        acheck = Tread.readlines()
#        for record in acheck:
#            listrec = record.split(",")
#            displaylist.append(listrec[num])
#        print(displaylist)
#with open("Apartment.txt","r") as Ahandler:
#    for item in record:
#        for data in item:
#            print(data.rstrip().rstrip(","))
#a = "0,1,2,3,4,5,6,7,8"
#
#list= a.split(",")
#print(list)

#def apartmentExitProgram(code): SCRAPPED BECAUSE UNUSABLE
#   if code:
#      return True
#   else:
#      print("We are about to exit the program.\n[C]-Continue\nOther keys to exit")
#      exit=input("Do you want to exit?\n")
#      if exit in ["C","c"]:
#         print("\Rerunning\n")
#         return True
#      else:
#         print("\nExiting\n")
#         return False
def gettenantID(masterKey):
   if masterKey == False:
    #fetch existing UID
      with open("user.txt","r") as uRead:
         userRecord = uRead.read().split(",")
         return userRecord[2]
   else:
    # generate new UID
      UID = dt.datetime.now().strftime("%d%m%Y%H%M%S%f")
      return UID

def getname(code):                  #define getname()
    specials = specialCharacterList(None)
    while True:
        name = input("Format: Name Name.....\nEnter tenant fullname:\n")
        if not name.isnumeric:
            nameList = name.split(" ")
            if len(nameList) >= 2:
                for words in nameList:
                    print("Checking",words)
                    if words[0].isupper() and (words.isalpha() or [character for character in words if(character in specials[16]) or (character in specials[19])]):
                        code = None
                        continue
                    else:
                        code = 2
                        message(code)
                        break
            else:
                code = 3
                message(code)
        else:
            code = 1
            message(code)
        if code:
            print("ATTENTION||Error detected.||ATTENTION")
        else:
            print("No errors detected.")
        retry = input("[R]-Retry,[Any other key]-Exit using "+name+"\n")
        if retry in ["R","r"]:
            continue
        else:
            return name

def getgender(code):
    while True:
        gender = input("Format: M/F\nEnter tenant gender:\n")
        if len(gender)== 1:
            if gender.isalpha():
                code = None
            else:
                code = 2
                message(code)
        else: 
            code = 3
            message(code)
        if code:
            print("ATTENTION||Error detected.||ATTENTION")
        else:
            print("No errors detected.")
        retry = input("[R]-Retry,[Any other key]-Exit using "+gender+"\n")
        if retry in ["R","r"]:
            continue
        else:
            return gender.upper()

def getpNum(code):
    while True:
        pNum = input("Format: ############\nEnter tenant phone number:\n")
        if 6 > len(pNum) > 16:
            for digit in pNum:
                if digit.isdigit():
                    code = None
                    continue
                else:
                    code = 1
                    message(code)
                    break
        else:
            code = 3
            message(code)
        if code:
            print("ATTENTION||Error detected.||ATTENTION")
        else:
            print("No errors detected.")
        retry = input("[R]-Retry,[Any other key]-Exit using "+pNum+"\n")
        if retry in ["R","r"]:
            continue
        else:
            return pNum

def getnationality(code):
    while True:
        nationality = input("Enter tenant nationality: (M: Malaysian/N: non-Malaysian):\n")
        if len(nationality) == 1:
            if nationality.isdigit():
                code = None
            else:
                code = 1
                message(code)
        else: 
            code = 3
            message(code)
        if code:
            print("ATTENTION||Error detected.||ATTENTION\n")
        else:
            print("No errors detected.\n")
        retry = input("[R]-Retry,[Any other key]-Exit using "+nationality.upper()+"\n")
        if retry in ["R","r"]:
            continue
        else:
            return nationality.upper()

def getstartDate(code):
    while True:
        specials = specialCharacterList(None)
        path = input("Use current date as rental start date?\n[Y]-Yes\n[Any Other Key]-No\n")
        if path in ["Y","y"]:
            startDate = dt.date.today().strftime("%Y/%m/%d")
            print("Current date:",startDate)
        else:
            startDate = input("Format: YYYY/MM/DD\nEnter Rental start date:\n")
            if len(startDate) == 10:
                if (startDate[:4]+startDate[5:7]+startDate[8:10]).isnumeric():
                    if startDate[4] == startDate[7] == specials[23]:
                        code = None
                    else:
                        code = 2
                        message(code)
                else:
                    code = 1
                    message(code)
            else:
                code = 3
                message(code)
        if code:
            print("ATTENTION||Error detected.||ATTENTION\n")
        else:
            print("No errors detected.\n")
        retry = input("[R]-Retry,[Any other key]-Exit using "+startDate+"\n")
        if retry in ["R","r"]:
            continue
        else:    
            return startDate

def getincome():
    while True:
        income = input("[1]-RM 350~449\n[2]-RM 450~549\n[3]-RM 550~649\n[4]-RM 650~749\n[5]-RM 750~849\n[6]-RM 850~949\n[7]-RM 950~1049\n[8]-RM 1050~1249\n[9]-RM 1250~1500\n[0]-RM > 1500\nChoose tenant income range in Ringgit Malaysia: ")
        if income == 1:
            income = "RM 1500~1599"
        elif income == 2:
            income = "RM 1600~1699"
        elif income == 3:
            income = "RM 1700~1799"
        elif income == 4:
            income = "RM 1800~1899"
        elif income == 5:
            income = "RM 1900~1999"
        elif income == 6:
            income = "RM 2000~2099"
        elif income == 7:
            income = "RM 2100~2199"
        elif income == 8:
            income = "RM 2200~2499"
        elif income == 9:
            income = "RM 2500~3000"
        elif income == 0:
            income = "RM > 3000"
        else:
            code = 0
            message(code)
            continue

        retry = input("[R]-Retry,[Any other key]-Exit using "+income+"\n")
        if retry in ["R","r"]:
            continue
        else:    
            return income

def getrental():
   rental = input("Enter tenant rental status(current/past)\n")
   return rental

def message(code):
   x,y,z = "Error,","Incorrect ","Please try again."
   if code == 0:
      print(x+y+"input."+z)
   elif code == 1:
      print(x+y+"data type present.")
   elif code == 2:
      print(x+y+"Format.")
   elif code == 3:
      print(x+y+"Length.")
   elif code == 4:
      print(x+"data not found.")
   elif code == 5:
      print(x+"zero input")

def specialCharacterList(SCI):
    if SCI == None:
        return ["~","`","!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]","|",",","\'","/","<",">","?",";",":","'",'"'] #0-30
    elif SCI == "SCL1":
        return ['~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|',',','\\','\'','\"','.','/','<','>','?',';',':'] #0-31
    elif SCI == "SCL2":
        return ['~','`','!','@','#','$','%','^','&','*','_','=','+','{','}','[',']','|','\\','\'','\"',',','.','/','<','>','?',':',';'] #0-28

def tenantEntryForm(tenantList,n):           #Define tenantEntryForm function
    errorCode = None
    for tenantList in range(n):
        #Get input for tenant data
        UID  = gettenantID(masterKey)
        name = getname(errorCode)
        gender = getgender(errorCode)
        pNum = getpNum(errorCode)
        nationality = getnationality(errorCode)
        startDate = getstartDate()
        income = getincome(errorCode)
        rental = getrental(errorCode)
        #Apply data to end of list 
        tenantList = [name,gender,pNum,nationality,startDate,income,rental]
    #Return the list
    return tenantList

import datetime as dt
masterKey=True
code=None
#n=2
#tenantEntryForm(list,n)
#print(list)
print(getstartDate(code))