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



#selecteddata = input("\nPlease enter the exact data that you want to edit: ")
#newdata = input("Last step, please insert the new data with the correct format: ")

#with open(listIdentifier(listCode),"r") as Xhandler:
#    dataRead = Xhandler.readlines()
    # for record in dataRead[editDatatype]:
    #     strippeditem = record.rstrip(" ").split(",")
    #     if selecteddata == strippeditem[editDatatype] :
    #         record.replace(selecteddata,newdata)
    #     Xhandler.append(record)
display=[]
with open("currentUser.txt","r") as f:
    bulkData = f.readlines()
    print("raw data: ",bulkData)
    for line in bulkData:
        strippedLine = line.strip(", \n")
        list = strippedLine.split(", ")
        print(list)
        number = input("choose location")#editDatatype = ApartmentDataInfo()
        display.append(list[int(number)])
        print(display)#apartmentSearch(editDatatype)
        
