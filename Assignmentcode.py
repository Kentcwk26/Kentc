def login():  #define the login function
   print("Welcome to Tenant Management System.\nPlease enter username and password to proceed.\n")   
   chance=3
   while chance>0:
      #input login credentials
      username=input("Enter username:")
      password=input("Enter password:")
      #open file and match for correct login
      with open("user.txt",'r') as userInfo:
         userCheck=userInfo.readlines()
         for record in userCheck:
            listRecord = record.split(",")
            if username == listRecord[0]:
               if password == listRecord[1]:
                  print("\nLogin successful\n")
                  #check for admin credentials
                  if (username == "john" and password == "1234u-78") or (username == "Dave" and password == "55467913"):
                     adminMenu()
                     chance=0
                     break
                  else:
                     menu()
                     chance=0
                     break            
         else:
            chance-=1
            print("\nError, incorrect username or password.\n",chance,"chances remaining.\n")


#Define tenant_entry form function
def tenant_entry_form(bulklist,n):
   newForm=[]
   for i in range(n):
      #Get input for tenant data
      name = input("Enter tenant name:\n")
      age = input("Enter tenant age: (##)\n")
      gender = input("Enter tenant gender: (m/f)\n")
      pnum = input("Enter tenant phone number: (############)\n")
      nationality = input("Enter tenant nationality: (Malaysian/non-Malaysian)\n")
      date1 = input("Enter Rental start date: (YYYY/MM/DD)\n")
      income = input("Enter tenant income range(RM)\n")
      rental = input("Enter tenant rental status(current/past)\n")
      #Apply data to end of list
      newForm.append(name)
      newForm.append(age)
      newForm.append(gender)
      newForm.append(pnum)
      newForm.append(nationality)
      newForm.append(date1)
      newForm.append(income)
      newForm.append(rental)
      bulklist.append(newForm)
   #Return the list
   return newForm

#Define apartment function
def apartment():
   
   print("\nApartment info:\n")
   record=[]

   #Put sample data
   list1=[["Standard Room (Triple)"],["Code: SR1"],["Dimensions: 140+ sqft"],["Pricing: RM350"],["Number of Rooms: 20"],["Apartment ID: A01-L1-R1 to A01-L1-R21"]]
   list2=[["Standard Room (Twin)"],["Code: SR2"],["Dimensions: 120+ sqft"],["Pricing: RM450"],["Number of Rooms: 20"],["Apartment ID: A01-L1-R22 to A01-L1-R41"]]
   list3=[["Standard Room A/C (Triple)"],["Code: SR3"],["Dimensions: 150+ sqft"],["Pricing: RM550"],["Number of Rooms: 20"],["Apartment ID: A01-L2-R1 to A01-L2-R21"]]
   list4=[["Standard Room A/C (Twin)"],["Code: SR4"],["Dimensions: 130+ sqft"],["Pricing: RM650"],["Number of Rooms: 20"],["Apartment ID: A01-L2-R22 to A01-L2-R41"]]
   list5=[["Deluxe Room (Triple)"],["Code: DR1"],["Dimensions: 170+ sqft"],["Pricing: RM750"],["Number of Rooms: 20"],["Apartment ID: A01-L4-R1 to A01-L4-R21"]]
   list6=[["Deluxe Room (Twin)"],["Code: DR2"],["Dimensions: 160+ sqft"],["Pricing: RM840"],["Number of Rooms: 20"],["Apartment ID: A01-L4-R22 to A01-L4-R41"]]
   list7=[["Deluxe Room A/C with shared attached bath / toilet (Triple)"],["Code: DR3"],["Dimensions: 180+ sqft"],["Pricing: RM950"],["Number of Rooms: 20"],["Apartment ID: A01-L3-R1 to A01-L3-R21"]]
   list8=[["Deluxe Room A/C with shared attached bath / toilet"],["Code: DR4"],["Dimensions: 170+ sqft"],["Pricing: RM1040"],["Number of Rooms: 20"],["Apartment ID: A01-L3-R22 to A01-L3-R41"]]
   list9=[["Compact Premium Single"],["Code: CPS"],["Dimensions: 130+ sqft"],["Pricing: RM690"],["Number of Rooms: 20"],["Apartment ID: A01-L5-R1 to A01-L5-R41"]]
   list10=[["Medium Premium Single"],["Code: MPS"],["Dimensions: 150+ sqft"],["Pricing: RM750"],["Number of Rooms: 20"],["Apartment ID: A02-L1-R1 to A02-L1-R21"]]
   list11=[["Medium Premium Twin"],["Code: MPT"],["Dimensions: 180+ sqft"],["Pricing: RM890"],["Number of Rooms: 20"],["Apartment ID: A02-L2-R1 to A02-L2-R21"]]
   list12=[["Medium Premium with attached bath / toilet (Twin)"],["Code: MP1"],["Dimensions: 180+ sqft"],["Pricing: RM940"],["Number of Rooms: 20"],["Apartment ID: A02-L3-R1 to A02-L3-R21"]]
   list13=[["Medium Premium with attached bath / toilet (Single)"],["Code: MP2"],["Dimensions: 160+ sqft"],["Pricing: RM1050"],["Number of Rooms: 20"],["Apartment ID: A02-L3-R22 to A02-L3-R41"]]
   list14=[["En-Suite Single (Super Premium - Triple)"],["Code: ESS3"],["Dimensions: 160+ sqft"],["Pricing: RM700"],["Number of Rooms: 20"],["Apartment ID: A02-L4-R1 to A02-L4-R41"]]
   list15=[["En-Suite Single (Super Premium - Twin)"],["Code: ESS2"],["Dimensions: 140+ sqft"],["Pricing: RM800"],["Number of Rooms: 20"],["Apartment ID: A02-L4-R1 to A02-L4-R41"]]
   list16=[["En-Suite Twin (Super Premium)"],["Code: EST2"],["Dimensions: 200+ sqft"],["Pricing: RM900"],["Number of Rooms: 20"],["Apartment ID: A02-L5-R1 to A02-L5-R41"]]

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
   
   with open("Apartment.txt","w") as Ahandler:
      for item in record:
         for data in item:
            for element in data:
               Ahandler.write(element)
            Ahandler.write(", ")
         Ahandler.write("\n")
       
   with open("Apartment.txt","r") as Ahandler:
      for item in Ahandler:
         print(item.rstrip().rstrip(","))

#return the list
   return menu()

#define search function
def searchbox():

   print("\nWelcome to search box!")
   print("\n1. Search room specific details.\n2. Search specific tenant details.\n\nEnter 'X' to EXIT search box \n")
   option=input("Select and insert input in order to start the program: ")

   if option=='1':
      print()
      opt=input("Room(r), Pricing(p)\nPlease type the keyword search based on the listing above: ")
      
      if opt=='r':
         print("\nSR1,SR2,SR3,SR4,DR1,DR2,DR3,DR4,CPS,MPS,MPT,MP1,MP2,ESS3,ESS2,EST2")
         num=1
         searchinformation(num)
      
      elif opt=='p':
         print("\nRM350,RM450,RM550,RM650,RM690,RM700,RM750,RM800,RM840,RM890,RM900,RM940,RM950,RM1040,RM1050")
         num=3
         searchinformation(num)
      else:
         print("Invalid input or no records")
   
   elif option=='2':
      options=input("\nName(N),Apartment Details(A)\nPlease type the keyword search based on the listing above: ")
      print()

   elif option=='X':
      print("\nReturn to main menu\n\n--------------------------------")
      #return menu function
      return menu()

   else:
      print("\nError! Please try again")
      #return searchbox function
      return searchbox()

#define searchinformation function:
def searchinformation(num):
   
   searchinformation=input("Select and enter text to begin search: ")
   print()
   with open("Apartment.txt","r") as Xhandler:
      for record in Xhandler:
         strippeditem=record.rstrip()
         data=strippeditem.split(", ")
         if searchinformation in data[num]:
            print("Results:\n",record)

   exitsearch=input("Exit program? Enter any key to exit, Enter 'C' to continue. ")
   if exitsearch == 'C':
      searchbox()
   else:
      menu()


#define menu function:
def adminmenu():
   while True:
      print("\n- Tenant Management System -")
      print("\n1. Review all apartment information\n2. Search box\n3. Register new tenant\n4. Exit")

      opt=int(input("\nPlease select which operation that you want to do: "))

      if opt==1:
         apartment()

      elif opt==2:
         searchbox()
         
      elif opt==3:
         bulklist=[]
         bulklist = tenant_entry_form()
         print(bulklist)

      elif opt==4:
         print("\nThank you for using, have a nice day~\n")
         return False

      else:
         print("\nError! Please try again\n")

#define menu function:
def tenantmenu():
   while True:
      print("\n- Tenant page -")
      print("\n1. Review all apartment information\n2. Search box\n3. Register new tenant\n4. Exit")

      opt=int(input("\nPlease select which operation that you want to do: "))

      if opt==1:
         apartment()

      elif opt==2:
         searchbox()
         
      elif opt==3:
         bulklist=[]
         bulklist = tenant_entry_form()
         print(bulklist)

      elif opt==4:
         print("\nThank you for using, have a nice day~\n")
         return False

      else:
         print("\nError! Please try again\n")

login()