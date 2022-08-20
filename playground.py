#with open("user.txt","r") as user:
#    rd = user.readlines()
#    for columns in rd:
#        print(columns.rstrip(",").rstrip("\n"))

#Adminkey=False

#def search():
#   while True:
#      category = input("[T]-Tenant\n[A]-Apartment\n[P]-Transaction\n[L]-Leave\nChoose a category:")
#      if category in ["T","t"]:
#         tenantsearch()
#      elif category in  ["A","a"]:
#         searchbox()
#      elif category in  ["P","p"]:
#         transactionsearch()
#      elif category in  ["L","l"]:
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

searchInformation = input("Select and enter text to begin search: ")
num=0
listCode="p"
if listCode == "p":
    l="transaction.txt"
elif listCode=="a":
    l="apartment.txt"
elif listCode=="t":
    l="apartment.txt"    
with open (l,"r") as Xhandler:
    for record in Xhandler:
        strippeditem = record.rstrip(",").rstrip("NEWLINE")
        data = strippeditem.split(",")
        if searchInformation in data[num]:
            print("\n Results: \n",record)