
# account = {
#     "name": "Ayush",
#     "Balance": 100000,
#     "pin": "123456",
#     "Type": "Saving account"
# }

# print("== MINI ATM ==")
# pin = input("Enter your pin: ")
# if pin == account["pin"]:

#     while True:
#         print("\n*** ATM MENU ***")
#         print("1. Check balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Account details")
#         print("5. Exit")

#         choice = input("Enter your choice: ")

#         # Check Balance
#         if choice == "1":
#             print("Your balance is:", account["Balance"])

#         # Deposit Money
#         elif choice == "2":
#             amount = int(input("Enter your amount: "))

#             if amount > 0:
#                 account["Balance"] = account["Balance"] + amount
#                 print("Money deposited successfully.")
#                 print("New balance:", account["Balance"])
#             else:
#                 print("Amount must be greater than 0.")

#         # Withdraw Money
#         elif choice == "3":
#             amount = int(input("Enter your amount: "))

#             if amount > 0:
#                 if amount <= account["Balance"]:
#                     account["Balance"] = account["Balance"] - amount
#                     print("Money withdrawn successfully.")
#                     print("Collect your cash.")
#                     print("New balance:", account["Balance"])
#                 else:
#                     print("Insufficient balance.")
#             else:
#                 print("Amount must be greater than 0.")

#         # Account Details
#         elif choice == "4":
#             print("\nAccount Name:", account["name"])
#             print("Account Balance:", account["Balance"])
#             print("Account Type:", account["Type"])

#         # Exit
#         elif choice == "5":
#             print("Thank you for using Mini ATM!")
#             break

#         # Invalid Choice
#         else:
#             print("Invalid choice.")

# else:
#     print("Invalid PIN")
#     print("Access denied")    


# print("===Student marks calculator")

# name = input("Enter your name:")

# marks = []

# for i in range(5):
#     mark = int(input("Enter your marks:"))
#     marks.append(mark)

# total = sum(marks)

# percentage = total/ 500*100

# if percentage>= 90:
#     Grade = "A"
# elif percentage>=80:
#     Grade = "B"
# elif percentage>=70:
#     Grade = "C"
# elif percentage>=60:
#     Grade = "D"
# elif percentage>=50:
#     Grade = "E"
# else:
#     Grade = "F"

# if percentage>=40:
#     result = "PASS"
# else:
#     result = "FAIL"

# print("\n===RESULT===")
# print("Name:",name)
# print("Marks:",marks)
# print("Total",total)
# print("percentage",percentage,"%")
# print("Grade:",Grade)
# print("Result:",result)

# import random

# number = random.randint(1,50)

# print("Guess the number(1,50)")
# print("YOu have 5 chances")

# for i in range(5):
#     guess = int(input("Enter your guess:"))

#     if guess == number:
#         print("You win!")
#         break
#     elif guess > number:
#         print("too high")

#     elif guess < number:
#         print("Too low")

# else:
#     print("You lost")
#     print("Number was:",number)


# import random

# print("***ROCK PAPER SCISSOR***")

# choice = random.choice(["rock","paper","scissor"])

# computer = random.choices(choice)

# player = input("Enter rock,paper,scissor:").lower()

# if player not in choice:
#     print("INVALID CHOICE")

# elif player == computer:
#     print("It's a tie!")

# elif(player == "rock" and computer == "scissor") or \
#     (player == "paper" and computer == "rock") or \
#     (player == "scissor" and computer == "paper"):
#     print("You win!")

# else:
#     print("Computer win!")

# print("You chose:",player)
# print("Computer chose:",computer)


