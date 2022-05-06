"""
 Internship
 Group 2 : Cyber Protection
 Chhayrong Daravid & Khiev Oudom
 Project: Password Strength Checker
 Mentor : Prof. Taing Tomeng
"""
# Introduction
print("\n", "\t"*3, "PASSWORD CHECKER", "\n"*2)
# Instructions
y = input("Hello, Do you want to read the instruction? (yes/no) ")
if y == 'yes' or y == 'Yes' or y == 'YES' or y == 'y' or y == 'Y':
    print("Instruction\n1. To check whether your Password is strong or not, you will need to enter your password to the password checker\n2. The program will run and show you the result\n3. There are 3 results for the outcome: WEAK, MEDIUM, and STRONG\nNOTE: The star range from 1-10 based n the stength of the password ")
else:
    print("\t")
# use the loop after the user check the password whether they want to recheck
a = True
while a == True:
    print("\t")
# Let the user input their Password
    x = input("Enter the Password: ")
# The c is for the score rate for the system to detect their Pass_Strength
    c = 0
# The Uppercase, Lowercase, number and the special signs
    Upp = False
    Loww = False
    Num = False
    Sign = False
# To detect the character in the password
    for character in x:
        if character in ("abcdefghijklmnopqrstuvwxyz"):
            Loww = True
        elif character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            Upp = True
        elif character in "0,1,2,3,4,5,6,7,8,9":
            Num = True
        elif character in "!,@,#,$,%,^,&,*,(,),-,_,=,+,[,{,],},;,:,',,,<,>,.,?,/,\,|,":
            Sign = True
# To detect the length of the password (How many character in the pass)
    if len(x) < 8:
        c = 5
    elif 8 <= len(x) < 15:
        c += 10
# The conditions use for password and score
        if Upp == True and Loww == True and Num == True and Sign == True:
            c += 20
        elif Upp == True and Loww == True and Num == True:
            c += 15
        elif Upp == True and Loww == True and Sign == True:
            c += 15
        elif Upp == True and Loww == True and Sign == True:
            c += 15
        elif Loww == True and Num == True and Sign == True:
            c += 15
        elif Upp == True and Loww == True:
            c += 10
        elif Upp == True and Num == True:
            c += 10
        elif Upp == True and Sign == True:
            c += 10
        elif Loww == True and Num == True:
            c += 10
        elif Loww == True and Sign == True:
            c += 10
        elif Num == True and Sign == True:
            c += 10
        elif Upp == True:
            c += 5
        elif Loww == True:
            c += 5
        elif Num == True:
            c += 5
        elif Sign == True:
            c += 10
    elif len(x) >= 15:
        c += 15
        if Upp == True and Loww == True and Num == True and Sign == True:
            c += 20
        elif Upp == True and Loww == True and Num == True:
            c += 15
        elif Upp == True and Loww == True and Sign == True:
            c += 15
        elif Upp == True and Loww == True and Sign == True:
            c += 15
        elif Loww == True and Num == True and Sign == True:
            c += 15
        elif Upp == True and Loww == True:
            c += 10
        elif Upp == True and Num == True:
            c += 10
        elif Upp == True and Sign == True:
            c += 10
        elif Loww == True and Num == True:
            c += 10
        elif Loww == True and Sign == True:
            c += 10
        elif Num == True and Sign == True:
            c += 10
        elif Upp == True:
            c += 5
        elif Loww == True:
            c += 5
        elif Num == True:
            c += 5
        elif Sign == True:
            c += 10
    if c <= 15:
        print("*" * 4)
        print("Weak Password")
    elif 15 < c <= 25:
        print("*" * 7)
        print("Medium Password")
    else:
        print(" ", "*" * 10)
        print(" Strong Password")

# Another loop whether they want to recheck the pass or not
    Q = False
    while Q == False:
        l = input("Do you want to Recheck? Yes or No? ")
        if l == 'yes' or l == 'Yes' or l == 'y' or l == 'Y':
            a = True
            break
        elif l == 'no' or l == 'No' or l == 'n' or l == 'N':
            a = False
            break
        else:
            print('Error!\nPlease Try again')
            Q = False

