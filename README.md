# Python-Guessing-Game

> If you wanna use Python editor, please make sure Python version 3x is installed on your system.  
> Alternatively, you can use Visual Code Studio/VScodium and run this file. Python extensions are also available. 

## Description
This is a simple Python game that allows you to guess a random number between 1 - 10. The following are the conditions of the game: 
* It will prompt the user to guess a number between 1 - 10.
```
  while True: # count how many attempts will be done 
    guess_number = int(input('Enter your guess number between 1 and 10: '))
    attempts += 1
```
* If it's right, it will show the compliment message and the number of attempts the user had made to guess it correctly.
```
    if guess_number == true_number: # If it's correct
        print('Good job!  Are you a wizard? Keep it up, Harry! You guessed it in' , attempts, 'attempts.')
        break
```
* If it's wrong, it will show a specific message (the number is higher or lower) and the number of attempts the user had made so far. <br>
When the guess number is lower than the random number. 
```    
    elif guess_number < true_number: # The second option if it's too low 
        print('Not quite right. Please do not aim so low. The sky is the limit! Please spread your wings! So far, you have made', attempts, 'attempts.')
        true_number = random.randint(1,10) # Regenerate a new random number
```
When the guess number is higher than the random number. 
```
    else: # The last option if it's too high
        print('Not quite right. You aimed too high. Though it is reasonable, sometimes the solution is just in front of our eyes. Keep looking! So far, you have made', attempts, 'attempts.')
        true_number = random.randint(1,10) # Regenerate a new random number
```
