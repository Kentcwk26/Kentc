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
    
   print()
   print("Apartment info:")
   print()
   masterlist=[]

   #Put sample data
   list1=["Standard Room","Code: SR1(Triple),SR2(Twin)","Dimensions: 120+ sqft - 140+ sqft","Pricing: RM350(Triple),RM450(Twin)","Number of Rooms: 40","Apartment ID: A01-L1-R1 to A01-L1-R41"]
   list2=["Standard Room A/C","Code: SRAC3(Triple),SRAC4(Twin)","Dimensions: 130+ sqft - 150+ sqft","Pricing: RM450(Triple),RM550(Twin)","Number of Rooms: 40","Apartment ID: A01-L2-R1 to A01-L2-R41"]
   list3=["Deluxe Room","Code: DR1(Triple),DR2(Twin)","Dimensions: 140+ sqft - 170+ sqft","Pricing: RM650(Triple),RM740(Twin)","Number of Rooms: 40","Apartment ID: A01-L4-R1 to A01-L4-R41"]
   list4=["Deluxe Room A/C with shared attached bath / toilet","Code: DRAC3(Triple),DRAC4(Single)","Dimensions: 150+ sqft - 180+ sqft","Pricing: RM750(Triple),RM840(Single)","Number of Rooms: 40","Apartment ID: A01-L3-R1 to A01-L3-R41"]
   list5=["Compact Premium Single","Code: CPS","Dimensions: 130+ sqft","Pricing: RM690","Number of Rooms: 20","Apartment ID: A01-L5-R1 to A01-L5-R41"]
   list6=["Medium Premium Single","Code: MPS","Dimensions: 150+ sqft","Pricing: RM700","Number of Rooms: 20","Apartment ID: A02-L1-R1 to A02-L1-R41"]
   list7=["Medium Premium Twin","Code: MPT1(Twin),MPT2(Single)","Dimensions: 180+ sqft","Pricing: RM690(Twin),RM1150(Single)","Number of Rooms: 40","Apartment ID: A02-L2-R1 to A02-L2-R41"]
   list8=["Medium Premium with attached bath / toilet","Code: MPA1(Twin),MPA2(Single)","Dimensions: 160+ sqft - 180+ sqft","Pricing: RM740(Twin),RM1250 (Single)","Number of Rooms: 40","Apartment ID: A02-L3-R1 to A02-L3-R41"]
   list9=["En-Suite Single (Super Premium)","Code: SR1(Triple),SR2(Twin)","Dimensions: 140+ sqft","Pricing: RM1200","Number of Rooms: 20","Apartment ID: A02-L4-R1 to A02-L4-R41"]
   list10=["En-Suite Twin (Super Premium)","Code: SR1(Triple),SR2(Twin)","Dimensions: 200+ sqft","Pricing: RM920(per person)","Number of Rooms: 20","Apartment ID: A02-L5-R1 to A02-L5-R41"]

   #Apply data at the list
   masterlist.append(list1)
   masterlist.append(list2)
   masterlist.append(list3)
   masterlist.append(list4)
   masterlist.append(list5)
   masterlist.append(list6)
   masterlist.append(list7)
   masterlist.append(list8)
   masterlist.append(list9)
   masterlist.append(list10)

   with open("apartment.txt","w") as Ahandler:
      for record in masterlist:
         for item in record:
            Ahandler.write(item)
            Ahandler.write("\n")
         Ahandler.write("\n")

   with open("apartment.txt","r") as Ahandler:
      for record in Ahandler:
         print(record.rstrip().rstrip(","))

#return the list
   return menu()

#define search function
def search():

   print("\nWelcome to search box!")
   print("\n1. Search room specific details")
   print("2. Search specific tenant details")
   print("3. Search both tenant and room details")
   print("4. Exit")
   option=int(input("\nPlease select a number to start the program: "))

   if option==1:
      print("Room")
   elif option==2:
      print("Tenant")
   elif option==3:
      print("Room and Tenant")
   elif option==4:
      print("\nReturn to main menu")
      return menu()
   else:
      print("\nError! Please try again")
      return search()

#Return the list
   return menu()

#define menu function:
def menu():
   
   print("\nTenant Management System")
   print("\n1. Review all apartment information\n2. Search box\n3. Register new tenant\n4. Exit")

   opt=int(input("\nPlease select which operation that you want to do: "))

   if opt==1:
      apartment()

   elif opt==2:
      search()
      
   elif opt==3:
      bulklist=[]
      bulklist = tenant_entry_form()
      print(bulklist)

   elif opt==4:
      print("\nThank you for using, have a nice day~")

   else:
      print("\nError! Please try again")
      return menu()

menu()

print("1. r\n2. e")
