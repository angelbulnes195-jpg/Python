# if True:
#  # action will be executed if the condition is true
    
# if False:
# # action will not be executed if the condition is false 


age = 14

if age >= 18:
    print("Access granted")
else:
    print("Access denied")    
    
    
    
    
    saved_password = "password123"
    written_password = '''passwod123'''
    
    if saved_password == written_password:
        print("Access granted")
        
    else:
        print("Access denied")    
       
       
       
       
monthly_salary = 20000
monthly_expenses = 21000
       
if monthly_salary > 10000:
    print("You are strong economically in any part of the world")
    
    if monthly_salary - monthly_expenses < 0:
        print("You are strong economically in any part of the world but you have unmanageable expenses")
        
    elif monthly_salary - monthly_expenses >= 4000:
        print("You are strong economically in any part of the world and you have manageable expenses")
        
    else:
        print("You are strong economically in any part of the world but you have manageable expenses but not enough to save")

              
elif monthly_salary >= 5000:
     print("You are strong economically in Europe and North America")
     
elif monthly_salary >= 1000:
     print("You are strong economically in latin america")
     
elif monthly_salary >= 500:
     print("You are strong economically in Africa and some parts of central america")
     
elif monthly_salary >= 200:
     print("You are strong economically in Venezuela and some parts of Africa")
             
else:
    print("You are not strong economically")     
                  