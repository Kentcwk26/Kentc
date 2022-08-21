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

#FUNCTION tenantSearch(details):
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
#FUNCTION tenantRead()
#    OPEN (tenant.txt) IN READ AS fTenant
#        tenantList = READ fTenant LINE-BY-LINE
#        FOR record IN tenantList
#            PRINT(record RIGHTSTRIP(",") RIGHTSTRIP("NEWLINE"))
#        ENDFOR
#    CLOSEFILE
#ENDFUNCTION



# searchInformation = input("Select and enter text to begin search: ")
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

#def apartmentSearch(num):
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

def getname():
    while True:
        name = input("Enter tenant name: Firstname Familyname Lastname \n")
        nameCheck = name
        nameCheck.split(" ")
        for words in nameCheck:
            if words[0].isupper():
                break
        else:
            code = 2
            message(code)
        return name
        return False

def getgender():
    gender = input("Enter tenant gender: (m/f):\n")
    genderCheck = gender
    if len(genderCheck)== 1:
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
        if type(digit) == int:
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
                return False
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
      print("Incorrect input.")
   elif code == 1:
      print("Incorrect data type present.")
   elif code == 2:
      print("Format error.")
   elif code == 3:
      print("Length error.")
   elif code == 4:
      print("Data not found.")
   print("Please try again.")

def tenantEntryForm(tenantList,n):           #Define tenantEntryForm function
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
        tenantList.append([name,gender,pNum,nationality,startDate,income,rental])
    #Return the list
    return tenantList

#import datetime as dt
#list = []
#n=2
#tenantEntryForm(list,n)
#print(list)

v=getname()
print(v)