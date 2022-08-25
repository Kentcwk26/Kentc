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
      print("\n"+x+"zero input"+z)

def specialCharacterList(SCL):
    if SCL == None:
        return ["~","`","!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]","|",",","\'","/","<",">","?",";",":","'",'"'] #0-30
    elif SCL == "SCL1":
        return ['~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|',',','\\','\'','\"','.','/','<','>','?',';',':'] #0-31
    elif SCL == "SCL2":
        return ['~','`','!','@','#','$','%','^','&','*','_','=','+','{','}','[',']','|','\\','\'','\"',',','.','/','<','>','?',':',';'] #0-28
    elif SCL == "SCL3":
        return ["~","`","!","@","#","$","%","^","&","*","(",")","_","=","+","{","}","[","]","|",",","\'","/","<",">","?",";",":","'",'"'] #0-29

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
        
print("\n",newRoomStatus())
# SCL = None
# specials = specialCharacterList(SCL)
# print(specials.index('"'))