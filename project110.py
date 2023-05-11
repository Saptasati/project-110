import random


response = "y"
while response == "y":
    no = random.randint(1, 6)
    

    if no == 1 :
      print("[-----]") 
      print("[     ]")
      print("[  0  ]")
      print("[     ]")  
      print("[-----]") 
      input("Enter y to roll again and n to exit:")

    elif no == 2:
      print("[-----]") 
      print("[     ]")
      print("[ 00  ]")
      print("[     ]")  
      print("[-----]") 
      input("Enter y to roll again and n to exit:")

    elif no == 3:
      print("[-----]") 
      print("[     ]")
      print("[ 000 ]")
      print("[     ]")  
      print("[-----]")
      input("Enter y to roll again and n to exit:")

    elif no == 4:
      print("[-----]") 
      print("[0   0]")
      print("[     ]")
      print("[0   0]")  
      print("[-----]")
      input("Enter y to roll again and n to exit:")

    elif no == 5:
      print("[-----]") 
      print("[0   0]")
      print("[  0  ]")
      print("[0   0]")  
      print("[-----]")
      input("Enter y to roll again and n to exit:")

    else:
      print("[-----]") 
      print("[0   0]")
      print("[0   0]")
      print("[0   0]")  
      print("[-----]") 
      input("Enter y to roll again and n to exit:")


