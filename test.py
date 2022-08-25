
import datetime as dt

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
      print("\n"+x+"zero input."+z)

def specialCharacterList(SCL):
    if SCL == None:
        return ["~","`","!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]","|",",","\'",".","/","<",">","?",";",":","'",'"'] #0-31
    elif SCL == "SCL1":
        return ['~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|',',','\\','\'','\"','.','/','<','>','?',';',':'] #0-31
    elif SCL == "SCL2":
        return ['~','`','!','@','#','$','%','^','&','*','_','=','+','{','}','[',']','|','\\','\'','\"',',','.','/','<','>','?',':',';'] #0-28

def apartmentAddData(adddatalist):
   adddatalist = []
   print("\n- Dear admin, we need your ATTENTION ! -\n\nFor your information, all the new data will be only stored if Admin insert the information with the correct format for each new data entry provided.\n\nNew room info: only contains alphabets, no numbers and special characters [Except these special characters: '(' ')' '/' '-' ]\nExample: Dual Key Premium Rooms - Single Room\n\nNew room code: only contains alphanumeric (A combination of Uppercased alphabet and number), and no special characters\nExample: DKPRS1\n\nNew Room Dimension (in range sqft): only contains numbers, no special characters (The unit will be provided at the back)\nExample: 300(+sqft)\n\nNew Room Pricing (in RM): only contain numbers, no special characters (The unit will be provided at the front)\nExample: (RM)500\n\nNumber of new rooms: only contains numbers and no special characters\nExample: 10 (Accepted range: 1-99)\n\nNew Apartment ID: A(01)-L(01)-R(01)x(to)xA(99)-L(99)-R(99)\nPlease follow this format as written above (A stands for Apartment Block, L stands for Room Level, R stands for Room Number, x means space)\n\nNew Room Date of Acquisition: dd/mm/yyyy\nNo special characters included, except '/'\n\nNew Room Rental History: (Accepted input: 'dd/mm/yyyy' or 'Empty')\nNo special characters included, except '/'\n\nNew Room Status: (Accepted Input: 'Available' or 'Not Available')\nNo numbers and special characters included\n\n- Now, you are required to enter new data. -\n")
   newroom=newRoom()
   newroomcode=newRoomCode()
   newroomdimension=newRoomDimension()
   newroompricing=newRoompricing()
   newnumberofRooms=newNumberofRooms()
   newroomfirstID=newRoomIDFirst()
   newroomlastID=newRoomIDLast()
   newroomdateofacquisition=newRoomDateofAcquisition()
   newroomrentalhistory=newRoomRentalHistory()
   newroomstatus=newRoomStatus()
   adddatalist.append("New Room Info: "+str(newroom),"New Room Code: "+str(newroomcode),"New Room Dimension in range (sqft): "+str(newroomdimension)+'+ sqft',"New Room Pricing: RM"+str(newroompricing),"Number for the new room: "+str(newnumberofRooms),"New room ID: "+str(newroomfirstID+' to '+newroomlastID),"New room Acquisition Date: "+str(newroomdateofacquisition),"New room Rental History: "+str(newroomrentalhistory)+" rent","New room Status: "+str(newroomstatus))
   print("\nNew Data:",adddatalist)
   apartmentadddataconfirmation(adddatalist)

def newRoom():
    while True:
         code = None
         SCL = 'SCL2'
         specials = specialCharacterList(SCL)
         newRoom=input("New room Info: ")
         if [character for character in newRoom if (character in specials)]:
            code = 2
            message(code)
            print("- New room info does not contain special character(s) -\n")
            continue
         else:
            code = None
         if 0 <= len(newRoom) < 6:
            code = 2
            message(code)
            print("-  Refer to the New Room Info to look for its details and format -\n")
            continue
         else:
            code = None
         if newRoom.isdigit() and any(location.isdigit() for location in newRoom):
            code = 1
            message(code)
            print("- New room info does not contain number(s) -\n")
            continue
         else:
            code = None
         if code == None:
            newRoom.title()
            return newRoom
         else:
            code = 2
            message(code)
            print("- Please fill in the correct format for new Room info. Refer to the New Room Info to look for its details and format -\n")
            continue

def newRoomCode():
   while True:
      code = None
      newRoomCode = input("New Room Code: ")
      if 0 < len(newRoomCode) < 1 :
         code=2
         message(code)
         print("- New Room Code must contain at least 2 or more alphanumeric long -\n")
         continue
      else:
         code = None 
      if newRoomCode.isalnum():
         code = None
      else:
         code=2
         message(code)
         print("- Please noted that new room code is only acceptable when it contains alphanumeric -\n")
         continue
      if code == None:
         return newRoomCode
      else:
         code = 2
         message(code)
         print("- Please fill in the correct format for new Apartment code. Refer to the New Room Pricing to look for its details and format -")
         continue

def newRoomDimension():
   while True:
      code = None
      newRoomDimension=input("New Room Dimension in range (sqft): ")
      if len(newRoomDimension)==0:
         code = 5
         message(code)
         print("- Please fill in the new room dimension, and room dimension must have at least 100 or more sqft -\n")
         continue
      else:
         code = None
      if newRoomDimension.isdigit():
         code = None
      else:
         code = 2 
         message(code)
         print("- New room dimension must consist of number(s) -")
         continue
      if code == None:
         return newRoomDimension
      else:
         code=2
         message(code)
         print("- Please fill in the correct format for new room dimension. Refer to the top description for its details and format -\n")
         continue

def newRoompricing():
   while True:
      code = None
      newRoompricing=input("New Room Pricing (in RM): ")
      if newRoompricing.isdigit():
         nRp=int(newRoompricing)
         if nRp >= 350:
            code = None
      else:
         code = 2
         message(code)
         print("- Please fill in the room pricing, it must be in numeric and the minimum starting price starts from RM350 and above -\n")
         continue
      if code == None:
         return newRoompricing
      else:
         code = 2
         message(code)
         print("- Please follow the correct format for new room pricing. Refer to the desccrition above to know its details and format -\n")
         continue

def newNumberofRooms():
   while True:
      code = None
      newNumberofRooms=input("Number of new rooms: ")
      if len(newNumberofRooms) == 0 or (newNumberofRooms == "0" and newNumberofRooms == "1"):
        code = 5
        message(code)
        print("- Please fill in the number of new rooms -\n")
        continue
      else:
        code = None

      if newNumberofRooms.isdigit():
        code = None
      else:
        code = 3
        message(code)
        print("- Number of new rooms must be in numeric -\n")
        continue

      if code == None :
        return newNumberofRooms
      else:
        code=2
        message(code)
        print("- Please fill in the correct format for the number of new rooms. Refer to the description above to look for its details and format -\n")
        continue

def newRoomIDFirst():
   while True:
      code = None
      SCL='SCL2'
      specials=specialCharacterList(SCL)
      newRoomIDfirst = input("New Room Apartment ID (First): ")

      if len(newRoomIDfirst) == 0:
         code = 5
         message(code)
         print("- Please fill in the new Apartment ID -\n")
         continue
      else:
         code = None

      if 0 < len(newRoomIDfirst) < 10:
         code = 2
         message(code)
         print("- Please follow the format as: A01-L10-R40 ( A stands for Apartment Block, L stands for Level, and R stands for Room (The length must have 11 characters long, including the dash -) -\n")
         continue
      else:
         code = None

      if (newRoomIDfirst[0] == 'A' and newRoomIDfirst[3] == '-' and newRoomIDfirst[4] == 'L' and newRoomIDfirst[7] == '-' and newRoomIDfirst[8] == 'R') and any(location.isdigit() for location in newRoomIDfirst):
         if [character for character in newRoomIDfirst[:] if (character in specials)]:
            code = None
      else:
         code=2
         message(code)
         print("- Please follow the format as: A01-L10-R40, it (A,L,R) must contain uppercases and numbers. -\n")
         continue
            
      if code == None:
         return newRoomIDfirst
      else:
         code=3
         message(code)
         print("- Please fill in the correct format for new room Apartment ID. Refer to the description above to look for its details and format -")
         continue

def newRoomIDLast():
   while True:
      code = None
      SCL = 'SCL2'
      specials=specialCharacterList(SCL)
      newRoomIDlast = input("New Room Apartment ID (Last): ")

      if len(newRoomIDlast) == 0:
         code = 5
         message(code)
         print("- Please fill in the new Apartment ID -\n")
         continue
      else:
         code = None

      if 0 < len(newRoomIDlast) < 10:
         code = 2
         message(code)
         print("- Please follow the format as: A01-L10-R40 ( A stands for Apartment Block, L stands for Level, and R stands for Room (The length must have 11 characters long, including the dash -) -\n")
         continue
      else:
         code = None

      if (newRoomIDlast[0] == 'A' and newRoomIDlast[3] == '-' and newRoomIDlast[4] == 'L' and newRoomIDlast[7] == '-' and newRoomIDlast[8] == 'R') and any(location.isdigit() for location in newRoomIDlast):
         if [character for character in newRoomIDlast[:] if (character in specials)]:
            code = None
      else:
         code=2
         message(code)
         print("- Please follow the format as: A01-L10-R40, it (A,L,R) must contain uppercases and numbers. -\n")
         continue
            
      if code == None:
         return newRoomIDlast
      else:
         code=3
         message(code)
         print("- Please fill in the correct format for new room Apartment ID. Refer to the description above to look for its details and format -")
         continue

def newRoomDateofAcquisition():
    while True:
        code = None
        newRoomDateOfAcquisition = input("New Room Date of Acquisition (dd/mm/yyyy): ")
        if any(location.isdigit() for location in newRoomDateOfAcquisition) and len(newRoomDateOfAcquisition) == 10:
            day,month,year = newRoomDateOfAcquisition.split('/')
            ValidDate = True
            try:
               dt.datetime(int(year),int(month),int(day))
               ValidDate = True
            except ValueError:
                ValidDate = False
            if ValidDate == True :
               code = None
               return newRoomDateOfAcquisition
            else:
               code = 2
               message(code)
               print("- New room acquisition date is not valid -\n")
               continue
        else:
            code = 2
            message(code)
            print("- Wrong Date Format (dd/mm/yyyy) -\n")
            continue

def newRoomRentalHistory():
   while True:
        code = None
        newRoomRentalHistory = input("New Room Rental History (dd/mm/yyyy): ")
        if any(location.isdigit() for location in newRoomRentalHistory) and len(newRoomRentalHistory) == 10:
            day,month,year = newRoomRentalHistory.split('/')
            ValidDate = True
            try:
               dt.datetime(int(year),int(month),int(day))
               ValidDate = True
            except ValueError:
               ValidDate = False
            if ValidDate == True :
               code = None
               return newRoomRentalHistory
            else:
               code = 2
               message(code)
               print("- New rental history date is not valid -\n")
               continue
        else:
            code = 2
            message(code)
            print("- Wrong Date Format (dd/mm/yyyy) -\n")
            continue

def newRoomStatus():
   while True:
      code = None
      SCL = None
      specials = specialCharacterList(SCL)
      newRoomStatus = input("New Room Status ( Available / Not Available ): ")
    
      if (0 <= len(newRoomStatus) <= 7) or (len(newRoomStatus) >= 14) :
         code = 5
         message(code)
         print("- Please fill again the new room status and follow the correct format ( Accepted input: Available / Not Available ) -\n")
         continue
      else:
         code = None

      if any(location.isdigit() for location in newRoomStatus) and newRoomStatus.isdigit(): 
         code = 2
         message(code)
         print("- New room status does not contain number(s) -\n")
         continue
      else:
         code = None

      if [character for character in newRoomStatus if (character in specials)]:
         code = 2
         message(code)
         print("- New room status does not have special character(s) -\n")
         continue
      else:
         code = None

      if (0 <= len(newRoomStatus) <= 7 or len(newRoomStatus) >= 14) and (any(location.isdigit() for location in newRoomStatus)):
         code = 2
         message(code)
         print("- New room status does not consists of number(s) -\n")
         continue
      else:
         code = None

      if ([character for character in newRoomStatus if (character in specials)] and any(location.isdigit() for location in newRoomStatus) and [character for character in newRoomStatus if (character in specials)]):
         code = 3
         message(code)
         print("- New room rental history does not contain number(s) and special character(s) -\n")
         continue
      else:
         code = None

      if (0 < len(newRoomStatus) <= 7 or len(newRoomStatus) >= 14) and (any(location.isdigit() for location in newRoomStatus)) and ([character for character in newRoomStatus if (character in specials)]):
         code=3
         message(code)
         print("- Input too short oe long, and also number(s) and special character(s) exist, please follow the correct format ( Accepted input: Available / Not Available ) -\n")
         continue
      else:
         code = None

      if newRoomStatus in ["Available","Not Available"] and (len(newRoomStatus) == 9 or len(newRoomStatus) == 13):
         code = None
      else:
         code = 2
         message(code)
         print("- Room Status can only be accepted either the input is 'Available' or 'Not Available'. -\n")
         continue

      if code == None:
         return newRoomStatus
      else:
         code = 3
         message(code)
         print("Please insert the correct format for new room status. Refer to the top description to let its details and format -\n")
         continue

def apartmentadddataconfirmation(adddatalist):
   modify = True
   listCode = "a"
   while True:
      addDataconfirmation=int(input("\nAre you sure with the records you inserted just now? Enter '1' to save record, Enter '0' to unsave record: "))
      if addDataconfirmation == 1:
         appendFile(adddatalist,listCode)
         print("\n- Data Saved -")
         return modify
      else:
         code=0
         message(code)
         break

# def apartmentAddData(adddatalist):
#    adddatalist=[]
#    print("\n- Dear admin, we need your ATTENTION ! -\n\nFor your information, all the new data will be only stored if Admin insert the information with the correct format for each new data entry provided.\n\nNew room info: only contains alphabets, no numbers and special characters [Except these special characters: '(' ')' '/' '-' ]\nExample: Dual Key Premium Rooms - Single Room\n\nNew room code: only contains alphanumeric (A combination of Uppercased alphabet and number), and no special characters\nExample: DKPRS1\n\nNew Room Dimension (in range sqft): only contains numbers, no special characters (The unit will be provided at the back)\nExample: 300(+sqft)\n\nNew Room Pricing (in RM): only contain numbers, no special characters (The unit will be provided at the front)\nExample: (RM)500\n\nNumber of new rooms: only contains numbers and no special characters\nExample: 10 (Accepted range: 1-99)\n\nNew Apartment ID: A(01)-L(01)-R(01)x(to)xA(99)-L(99)-R(99)\nPlease follow this format as written above (A stands for Apartment Block, L stands for Room Level, R stands for Room Number, x means space)\n\nNew Room Date of Acquisition: dd/mm/yyyy\nNo special characters included, except '/'\n\nNew Room Rental History: (Accepted input: 'dd/mm/yyyy' or 'Empty')\nNo special characters included, except '/'\n\nNew Room Status: (Accepted Input: 'Available' or 'Not Available')\nNo numbers and special characters included\n\n- Now, you are required to enter new data. -\n")
#    newroom=newRoom()
#    newroomcode=newRoomCode()
#    newroomdimension=newRoomDimension()
#    newroompricing=newRoompricing()
#    newnumberofRooms=newNumberofRooms()
#    newroomfirstID=newRoomIDFirst()
#    newroomlastID=newRoomIDLast()
#    newroomdateofacquisition=newRoomDateofAcquisition()
#    newroomrentalhistory=newRoomRentalHistory()
#    newroomstatus=newRoomStatus()
#    adddatalist.append("New Room Info: "+str(newroom))
#    adddatalist.append("New Room Code: "+str(newroomcode))
#    adddatalist.append("New Room Dimension in range (sqft): "+str(newroomdimension)+'+ sqft')
#    adddatalist.append("New Room Pricing: RM"+str(newroompricing))
#    adddatalist.append("Number for the new room: "+str(newnumberofRooms))
#    adddatalist.append("New room ID: "+str(newroomfirstID+' to '+newroomlastID))
#    adddatalist.append("New room Acquisition Date: "+str(newroomdateofacquisition))
#    adddatalist.append("New room Rental History: "+str(newroomrentalhistory)+" rent")
#    adddatalist.append("New room Status: "+str(newroomstatus))
#    print("\nNew Data:",adddatalist)
#    apartmentadddataconfirmation(adddatalist)
