def newApartmenttype(code,specials):
   nonumber=0 ; nospecialcharacter=0 
   while True:
      Newapartmentinfo=input("New apartment Info:")
      for validinput in Newapartmentinfo:
         if len(Newapartmentinfo) < 0:
            if type(Newapartmentinfo)!= str:
               code = 1
               message(code)
               print("- Please enter the correct input -")
         else:
            code = 3 
            message(code)
            print("- Pleasse insert the correct format -")
            continue
         if Newapartmentinfo.isalpha():
            nonumber=1
         else:
            code = 2
            message(code)
            print("- Apartment info does not contain number -")
            continue
         if any (c in specials for c in Newapartmentinfo[:]):
            code = 0
            message(code)
            print("- Apartment info does not contain special character -")
         else:
            nospecialcharacter=1
         if nonumber == 1 and nospecialcharacter == 1:
            return False
         else:
            code=1
            message(code)
            print("- Please enter the correct data type -")
            continue

def ApartmentID(code,specials):
   while True:
      lenAparID = None ; notlowercase = None ; AparIDdash = None
      ApartmentID = input("Apartment ID: ")
      if len(ApartmentID)>26:
         code = 2
         message(code)
         print("\nPlease follow the format as: A01-L10-R40 to A02-L01-R09,\nA stands for Apartment Block, L stands for Level, and R stands for Room (The length must have 11 characters long, including the dash -)")
         continue
      else:
         lenAparID = 1
      if ApartmentID[0:4:8].islower():
         code=2
         message(code)
         print("\nMust contain uppercase, not lower case")
         continue
      else:
         notlowercase = 3
      if (ApartmentID[3] and ApartmentID[7] and ApartmentID[18] and ApartmentID[22]) == specials[20]:
         AparIDdash = 4 
      else:
         code=2
         message(code)
         print("\nPlease include the dash inside the apartment ID")
         continue
      if lenAparID == 1 and notlowercase == 3 and AparIDdash == 4:
         return ApartmentID
      else:
         continue

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
   specials = ["{","}","<",">","!","@","#","$","%","^","&","*","?",":",";","'","+","=","-","_","]","["]
   specials.append('"')
   return specials

newApartmenttype(code,specials)
ApartmentID(code,specials)