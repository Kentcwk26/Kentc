with open("user.txt","r") as user:
    rd = user.readlines()
    for columns in rd:
        print(columns.rstrip(",").rstrip("\n"))