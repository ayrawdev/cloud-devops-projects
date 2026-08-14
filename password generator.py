# welcome to password generator
import random
import string

print("="*70)
heading="Welcome to password generator"
print(heading.center(50).upper())
print("="*70)

attempts=3
while attempts>0:
# Handeling error
   try:
   # taking input(1) from user
        a=(int(input("Enter the length of Password(5-15):".upper())))
           # using conditional statement
        if a<5:
           print("password length should be greater than 5\n".capitalize())
           attempts=attempts-1
           print(f"you have {attempts} attempts left")
           if attempts == 0:
                 break
           continue

        elif a>=15:
           print("password length shouldn't be greater than 15\n".capitalize())
           attempts=attempts-1
           print(f"you have {attempts} attempts left")
           if attempts == 0:
                   break
           continue
        else:
           print(f"your password length is:{a}\n".title())
   
   except ValueError:
           print("invalid input\n".capitalize())
           attempts=attempts-1
           print(f"you have {attempts} attempts left")
           if attempts == 0:
                   break
           continue
   
   print("-"*70)
   
   REMAINDER="the password will be generated in form of (a-z,A-Z,0-9)"
   print(REMAINDER.capitalize().center(50))
   
   print("-"*70)
   
   
   # taking input(2) from user
   
   # String Validation using built-in methods
   b=(input("Enter Your Favourite one Alphabet :".upper()))
   if len(b)==1 and b.isalpha():
      print(f"your favourite alphabet is:{b}\n".title())
   else:
      print("invalid input\n".capitalize())
      attempts=attempts-1
      print(f"you have {attempts} attempts left")
      if attempts == 0:
              break
      continue
   
   print("-"*70)
   
   # taking input(3) from user
   try:
        c=int(input("Enter Your Favourite Number between 1-9:".upper()))
        if c > 9 or c < 1 :
           print("number should be between 1-9".capitalize())
           attempts=attempts-1
           print(f"you have {attempts} attempts left")
           if attempts == 0:
                   break
           continue
        else:
           print(f"your favourite number is:{c}\n".capitalize())
           
   except ValueError:
      print("invalid input\n".capitalize())
      attempts=attempts-1
      print(f"you have {attempts} attempts left")
      if attempts == 0:
              break
      continue
   
   print("-"*70)
        
   special_character = {
       1: ("!", "exclamation"),
       2: ("@", "at the rate"),
       3: ("#", "hash"),
       4: ("$", "dollar"),
       5: ("%", "percentage"),
       6: ("^", "caret"),
       7: ("&", "ampersand"),
       8: ("*", "asterisk"),
       9: ("?", "question mark"),
       10: ("_", "underscore")
   }      
   for key,value in special_character.items():
        print(f"{key}.{value[0]} {value[1]}")
# Variable Initialization
   symbol = ""
   name = ""
# Variable Initialization
   d=input("select any one special character from  list ;if no choice type exit:").lower()
   if d=="exit":
           print("your password will be generated without special character")
           symbol = "none"
           name = ""

   elif d.isdigit() and int(d) in special_character:
           d = int(d)
           symbol, name = special_character[d]
                   # tuple unpacking
           print(f"you selected special character => {symbol} {name}")
        # second method
        # print(f"you selected special character => {special_character[d][0]} {special_character[d][1]}")
                  
   else:
           print("invalid input\n".capitalize())
           attempts=attempts-1
           print(f"you have {attempts} attempts left")
           if attempts == 0:
                break
           continue

   print("-"*70)
  
   print("="*70)

   # 5. PASSWORD GENERATION LOGIC 
   try:
        pool = list(string.ascii_letters + string.digits)

        required = [b, str(c)]
        if symbol != "":
               required.append(symbol)

        remaining_length = a - len(required)

        random_chars = []
        for _ in range(remaining_length):
               random_chars.append(random.choice(pool))

        password_list = required + random_chars
        random.shuffle(password_list)

        password = "".join(password_list)

        print(f"Generated Password: {password}")

        print("="*70)
        
        print(f"Summary → Length:{a}, Alphabet:{b}, Number:{c}, Symbol:{symbol}")

        break
   except ValueError:
           print("Invalid input type\n")
           attempts -= 1
           print(f"Attempts left: {attempts}")
           if attempts == 0:
               break
           continue

print("="*70)
        

   
       
                   
           


                        
