answer  = 5

print("please guess a number between 1 - 10: ")
guess = int(input())

# if guess < answer:
#     print('your guess is too low')
#     guess = int(input())
#     if guess == answer:
#         print("well done, you guessed it")
#     else:
#         print('sorry, you guessed wrong')
# elif guess > answer:
#     print('your guess is too high')
#     guess = int(input())
#     if guess == answer:
#         print("well done, you guessed it!")
#     else:
#         print('sorry, you guessed wrong')
# else:
#     print('you got the answer!')

###############################   Same code, written differntly

if guess != answer:
    if guess < answer:
        print("please guess higher")
    else:
        print('Please guess lower')
    guess = int(input())
    if guess == answer:
        print('well done, you got the answer')
    else:
        print('sorry, you didnt get the answer')
else:
    print('you got it the first time!')