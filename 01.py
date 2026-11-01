import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!','@','#','$','%','&','*','(',')','+']

print("!Welcome To Password Genaretor!")
n_letter=int(input("How many letters you want in your password?\n:-"))
n_number=int(input("How many number you want in your password?\n:-"))
n_symbol=int(input("How many symbol you want in your password?\n:-"))

password_list=[]
for i in range(0,n_letter):
    l=random.choice(letters)
    password_list += l
for i in range(0,n_number):
    n=random.choice(numbers)
    password_list += n
for i in range(0,n_symbol):
    s=random.choice(symbols)
    password_list += s

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password=""
for f in password_list:
    password += f
print(password)