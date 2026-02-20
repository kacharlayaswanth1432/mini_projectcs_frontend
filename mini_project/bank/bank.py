import json
from random import randint
import os

FILE_NAME = "bank_data.json"

# -------------------------
# Load Data From File
# -------------------------
if os.path.exists(FILE_NAME) and os.path.getsize(FILE_NAME) > 0:
    with open(FILE_NAME, "r") as file:
        bank_account = json.load(file)
else:
    bank_account = {}

# -------------------------
# Save Data To File
# -------------------------
def save_data():
    with open(FILE_NAME, "w") as file:
        json .dump(bank_account, file, indent=4)

def create_account():
    choic=input("Do You Have An Account Yes/No:")
    if choic.lower()== 'yes':
        user_acc_no = input("Enter Account No:")
        if user_acc_no in bank_account:
            print(f"""
                        Account Details
                        ---------------
                        Account Number : {user_acc_no}
                        Name           : {bank_account[user_acc_no]['name']}
                                                                    """)  
        else:
            print("Account Not Found!")
    else:
        print("Please Create New Account:")
        name = input("Enter Your Name:")
        acc_no ="9640" + str(randint(99999,1000000))
        bank_account[acc_no] ={'Account number':acc_no,'name':name,'balance':0}
        save_data()
        print("Account Created Successfully!")
        print("Your Account Number:", acc_no)

def deposite():
    user_acc_no = input("Enter Account No:")
    if user_acc_no in bank_account:
        print(f"""
                        Account Details
                        ---------------
                        Account Number : {user_acc_no}
                        Name           : {bank_account[user_acc_no]['name']}
                                                                    """) 
        amount = float(input("Enter Deposite Amount:"))
        if amount > 0:
                bank_account[user_acc_no]['balance']+=amount
                print("Your Amount will be Successfully Deposited")
                print("Current Balance:",bank_account[user_acc_no]['balance'])
                save_data()
        else:
            print("Amount Should be Always Above 0")
    else:
        print("Account Number is Not Exists ! Please Enter Correct Number")
        
def withdraw():
    user_acc_no = input("Enter Account No:")
    if user_acc_no in bank_account:
        otp = randint(100000,999999)
        print(f"Your OTP:{otp}")
        for i in range(3,0,-1):
            user_otp = int(input("Enter 6 Digit OTP:"))
            if otp == user_otp:
                print(f"""
                            Account Details
                            ---------------
                            Account Number : {user_acc_no}
                            Name           : {bank_account[user_acc_no]['name']}
                                                                        """) 
                amount = float(input("Enter Withdrawal Amount:"))
                if amount > 0:
                    if amount<=bank_account[user_acc_no]['balance']:
                        bank_account[user_acc_no]['balance']-=amount
                        print("Please Collect Your cash!")
                        print("Current Balance:",bank_account[user_acc_no]['balance'])
                        save_data()
        
                    else:
                        print("Insufficient Balace")
                else:
                    print("Amount Should be Always Above 0")
                break
            else:
                print("Wrong OTP Please Correct One")
                print(f"Please Try Again You Have {i-1} attempts left")
    else:
        print("Account Number is Not Exists ! Please Enter Correct Number")

def Check_balance():
    user_acc_no = input("Enter Account No:")
    if user_acc_no in bank_account:
        otp = randint(100000,999999)
        print(f"Your OTP:{otp}")
        for i in range(3,0,-1):
            user_otp = int(input("Enter 6 Digit OTP:"))
            if otp == user_otp:
                print(f"""
                            Account Details
                            ---------------
                            Account Number : {user_acc_no}
                            Name           : {bank_account[user_acc_no]['name']}
                            Balance        : {bank_account[user_acc_no]['balance']}
                                                                     """) 
                break
            else:
                print("Wrong OTP Please Correct One")
                print(f"Please Try Again You Have {i-1} attempts left")     
    else:
        print("Please Enter Correct Account Number")


# Bank Services
def choice():
    while True:
        print("Choose Which Service You need:\n 1:Creat Account \n 2:Deposite Amount \n 3:Withdraw Money \n 4:Check Balance \n 5:Exit")
        try:
            service = int(input("Enter Your Service: "))
        except ValueError:
            print("Please Enter a Valid Number")
            continue
        if service == 1:
            create_account()
        elif service == 2: 
            deposite()
        elif service == 3:
            withdraw()
        elif service == 4:
            Check_balance()
        elif service == 5:
            print("Thank You for Using Our Bank Services")
            break
        else:
            print("Please Enter Correct Option")
choice()




