from datetime import date



bank = {}

'''
bank = {
   account_no : {
       username ,
       pin,
       balance,
       transactions : [('date','status','amount')]
   }
}
'''


print("============= MINI-BANK====================")
print("[1] Create account")
print("[2] Login & Deposit")
print("[3] Login & Withdraw")
print("[4] Check balance")
print("[5] View Transactions")
print("[6] Show all accounts")
print("[7] Exit")
print("===============================================")


while(True):
    option = int(input("enter you option : "))
    if(option==1):
      account_no = int(input("enter your account number : "))
      if(account_no in bank):
         print("Account number already given...")
      else:
         username = input("enter your username : ")
         pin = int(input("enter your pin number : "))

         bank[account_no] = {
            "username" : username,
            "pin" : pin,
            "balance" : 0,
            "transactions" : []
         }
         print("Account created")
         #print(bank)

    elif(option==2):
      account_no = int(input("enter your account number : "))
      pin = int(input("enter your pin number : "))
      if(account_no in bank and pin == bank[account_no]['pin']):
         amount = int(input("enter amount : "))
         bank[account_no]['balance'] += amount
         bank[account_no]["transactions"].append((date.today(),'deposit',amount))
      else:
         print("account_no or pin number is wrong")

    elif(option==3):
      account_no = int(input("enter your account number : "))
      pin = int(input("enter your pin number : "))
      if(account_no in bank and pin == bank[account_no]['pin']):
         amount = int(input("enter amount : "))
         current_balance = bank[account_no]['balance']
         if(amount<current_balance):
            bank[account_no]['balance'] -= amount
            bank[account_no]["transactions"].append((date.today(),'withdraw',amount))
         else:
            print("insufficiet balance")
      else:
         print("account_no or pin number is wrong")

    elif(option==4):
      account_no = int(input("enter your account number : "))
      pin = int(input("enter your pin number : "))
      if(account_no in bank and pin == bank[account_no]['pin']):
        print(f"your balance is : {bank[account_no]['balance']}")
      else:
         print("account_no or pin number is wrong") 

    elif(option==5):
      account_no = int(input("enter your account number : "))
      pin = int(input("enter your pin number : "))
      if(account_no in bank and pin == bank[account_no]['pin']):
         print("your transaction statement here....")
         for transaction in bank[account_no]["transactions"]:
            print(transaction)
      else:
         print("account_no or pin number is wrong")   

    elif(option==6):
       for account_number in bank.keys():
          print(f"{account_number}   :  {bank[account_number]['username']}")     

    elif(option==7):
        print("Thank")
        break

        
