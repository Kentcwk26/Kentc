
def getdecimal(code):                                                #define getdecimal function
   specials = specialCharacterList(None)
   while True:
      decimal = input("Format: ########.##\nEnter the transaction amount in Ringgit Malaysia:\n")
      if specials[23] in decimal:
         money = decimal.split(".")
         for numbers in money:
            try:
               numbers[1] in money[1]
               if (digits.isnumeric() for digits in numbers):
                  code = None
                  continue
               else:
                  code = 1
                  break
            except IndexError:
               code = 2
      else:
         message(2)
         code = 2
         print(specials[23])
      if code:
         message(code)
         print("ATTENTION||Error detected.||ATTENTION\n")
      else:
         print("No errors detected.\n")
      retry = input("[R]-Retry,[Any other key]-Exit using "+decimal+"\n")
      if retry in ["R","r"]:
         continue
      else:    
         retry = input("[R]-Retry,[Any other key]-Exit using "+decimal+"\n")
         if retry in ["R","r"]:
            continue
         else:    
            return decimal
