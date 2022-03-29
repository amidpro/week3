trials = 3
# number of trials/attempts to get correct pin

correct_pin = 1234
# correct pin as int variable

while trials != 0:
# while trials are 0,
    supplied_pin = int(input ("Enter your PIN:"))
# display "Enter your PIN:" for user, user input int, could be more specific with rules, but for now it works
    if supplied_pin != correct_pin:
        trials -= 1
        # if supplied_pin does not equal correct_pin, -1 trial
        print('wrong pin number, you have', trials, 'trials left')
        # print statement if user does not get pin correct

    else:
        print('Success!')
        break
        # if correct - "Success!" will print
