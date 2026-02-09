
import random
import time
def spin_rows():
   rows=["🍒", "🍇","🥭", "🪙 ","🧸"]
   return [random.choice(rows) for _ in range(3)]
def print_row(row):
    print( " ".join(row))    
def win_payout(balance,bet,op):
    temp=balance
    if op=="1":
        balance+=bet*2
        win=balance-temp
        print(f'You have won ${win}!!')
    elif op=="2":
        balance+=bet*5
        win=balance-temp
        print(f'You have won ${win}!!')
    return balance
def main():
    print("************************")
    print("Welcome to Python Slots!")
    print("The symbols you are searching for are:🍒 🍇 🥭 🪙  🧸")
    print("************************")
    play=True
    sectry=False
    if sectry==False:
        balance=(input("What's your balance? "))
        while not(balance.isdigit()):
            balance=input("Wrong input,give us your balance(number). ")
    balance=int(balance)
    while balance>0 and play==True:
        bet=(input("Place your bet amount: "))
        if not(bet.isdigit()):
            continue
        if int(bet)>balance:
            print("Insufficient Funds")
            check=input("Do you want to keep playing? ")
            continue
        else:
          bet=int(bet)
          balance=balance-bet
          row=spin_rows()
          print("Spinning....")
          time.sleep(2)
          print_row(row)
          a=set(row)
          total=3-len(a)
          if total==1:
              balance=win_payout(balance,bet,op='1')
          elif total==2:
              balance=win_payout(balance,bet,op='2')
          else:
              print("No win :(")
        if balance>0: 
            print(f"Your balance is {balance}")
            check=input("Do you want to keep playing? ")
        else:
            while True: 
                check=input("Do you want to continue by adding money in your balance? ")
                if check.lower()=="yes":
                    sectry=True
                    balance=input("How much money do you want to add? ")
                    while not(balance.isdigit()):
                        balance=input("Wrong input,give us your balance(number). ")
                    balance=int(balance)
                    break
                elif check.lower()=="no":
                    play=False
                    break
                else:
                    print("Wrong answer,please say yes or no.")

        if check.lower()=="yes":
            play=True
        else:
            play=False
    
    print("Thank you for playing in our slots game!!!")
    
if __name__=="__main__":
    main()



