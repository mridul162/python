# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
#
# count = 0
# for item in result:
#     if item == "heads":
#         count = count + 1
#
# print(count)

###########################################

# for i in range(1,11):
#     if i%2!=0:
#         print(i**2)

############################################

# expense_list = [2340, 2500, 2100, 3100, 2980]
# month = ["jan", "feb", "march", "april", "may"]
# exp = int(input("Enter your expense: "))
#
# for i in range(len(expense_list)):
#     if expense_list[i] == exp:
#         print(f'You spent {exp} in {month[i]}')
#
# if exp not in expense_list:
#     print(f'You didn\'t spend {exp} in any month')

############################################

# count =0
# for i in range(5):
#     ask = input("Are you tired?")
#     if ask == "yes" or ask == "Yes" or ask == "YES":
#         print("You didn't finish the race.")
#         break
#     elif ask == "no" or ask == "No" or ask == "NO":
#         count = count +1
#         continue
#
# if count == 5:
#     print("Congratulations, you've completed the race!")

############################################

n = int(input("Enter N:"))

for i in range(n):
    s = '*'
    for j in range(i):
        s+='*'
    print(s)