import random
print(f"Welcome to the guess game!!")
players=input(f"How many are going to play? ")
max=-1
winners = 0 
for i in range(int(players)) :
 name=input("What's your name? ")
 print(f"OK {name} we will play a game!")
 secret_number = random.randint(1,10)
 try_again = True
 wins=0
 played=0
 while try_again == True:
  i=1
  while i<=3 :
    guess=input("Guess:")
    i+=1
    if int(guess)==secret_number :
        print(f"{name} you won!!")
        wins+=1
        break 
  else:
    print(f"Sorry,{name},you lost :(")
  played+=1  
  answer = input(f"{name} do you want to play again? (yes or no) " )
  if answer  == "yes":
        try_again = True
        secret_number = random.randint(1,10)
  else: 
       try_again = False 
 prc=(wins/played)*100
 if prc > max :
    max = prc
    winner = name
    winners=1
    sd = [name]
 elif prc==max :
    winners+=1
    sd.append(name)
 print(f"{name} you won {wins} out of {played},that's {prc}%, in {played} tries!") 
if winners== 1 :
 print(f"The winner is {winner}")
else:
   print(f"There are {winners} winners!!,we go to sudden death!")
   print("Welcome to sudden death,whoever finds the correct number first is going to be the winner!!")
   end=False
   while end==False :
         for x in range(winners):
          secret_number = random.randint(1,10)
          guess=input("Guess:")
         if int(guess)==secret_number :
            print(f"{sd[x]} you won!!")
            end=True
            break
print(f"Thank you for playing!")






