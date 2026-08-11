password = input ("Enter your password") . strip()
length = len(password)
print("password length:", length)
if length >= 7:
    print("Password is long enough.")
else:
    print("password is too short.")
 
has_uppercase = any(char.isupper() for char in password)
print("Contains uppercase:" , has_uppercase)
has_number = any(char.isdigit() for char in password)
print("Contains number:", has_number)
has_special = any(not char.isalnum() for char in password)
print("Contains special character:", has_special)
score = 0 
if length >= 7:
    score +=1
if has_uppercase:
    score += 1
if has_number:
    score += 1
if has_special:
    score += 1
print("Password score:", score, "/4")
if score <= 1:
    print("Password strength: Weak")
elif score <= 3:
    print("Password strength: Medium")
else :
     print("Password strength: Strong")
if not has_uppercase:
    print(" Tip: Add an uppercase letter.")
if not has_number:
     print(" Tip: Add a number.")
if not has_special:
     print(" Tip: Add a Special.")
if length < 7:
     print(" Tip: Darling use at least 7 characters!!!!.")
