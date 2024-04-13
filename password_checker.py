import re

def password_strength_checker(password):
    
    #Define password strength criteria
    
    length_criteria = len(password) >=8
    
    uppercase_criteria = any(char.isupper() for char in password) 
    
    lowercase_criteria = any(char.islower() for char in password)
    
    digit_criteria = any(char.isdigit() for char in password)
    
    special_char_criteria = re.search(r"[!@#%^$@%%#^^&()$%#]", password) is not None
    
    #check overall strength
    if all([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, 
    special_char_criteria]):
        return "strong"
    elif all([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria]):
        return "Moderate"
    else:
        return "Weak"
    
def main():
    user_password = input("Enter your password: ")
    strength_result = password_strength_checker(user_password)
    print(f"Password strength: {strength_result}")
if __name__ == "__main__":
        
    main()


        