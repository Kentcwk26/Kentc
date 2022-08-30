def message(code):                                                   #define message function
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
      print("\n"+x+"zero input."+z)

def apartmentSearch(num):
   while True:
      displaylist=[]
      with open ("Apartment.txt", "r") as Tread:
         acheck = Tread.readlines()
         for record in acheck:
            listRecord = record.split(",")
            displaylist.append(listRecord[num])
         print("\n",displaylist)
         break

selectedrow = int(input("Which row you want to edit: "))
selecteddata = input("\nPlease enter the exact data that you want to edit: ")
newdata = input("Last step, please insert the new data with the correct format: ")

with open("Apartment.txt","r") as f:
    reads = f.readlines()[selectedrow-1]
    print("\n",reads)
    strippeditem = reads.rstrip().rstrip(",").split(",")
    print(strippeditem)
    if selecteddata in strippeditem:
        strippeditem[0].replace(selecteddata,newdata)
    else:
        code = 4
        message(code)
        print("- The record(s) that you want to edit might not in the file. Please try again. -")
