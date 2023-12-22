# Random means Bring code from one module into another, making it accessible for use. In this case it's generating random numbers and sequences in Python. 
# Bring "random" module into our current script, making its functions and constans available for use. 
import random 
true_number = random.randint(1,10) # Random integer: the lower bound (inclusive) and the upper bound (inclusive)
attempts = 0

while True: # count how many attempts will be done 
    guess_number = int(input('Enter your guess number between 1 and 10: '))
    attempts += 1

    if guess_number == true_number: # If it's correct
        print('Good job!  Are you a wizard? Keep it up, Harry! You guessed it in' , attempts, 'attempts.')
        break
    
    elif guess_number < true_number: # The second option if it's too low 
        print('Not quite right. Please do not aim so low. The sky is the limit! Please spread your wings! So far, you have made', attempts, 'attempts.')
        true_number = random.randint(1,10) # Regenerate a new random number

    else: # The last option if it's too high
        print('Not quite right. You aimed too high. Though it is reasonable, sometimes the solution is just in front of our eyes. Keep looking! So far, you have made', attempts, 'attempts.')
        true_number = random.randint(1,10) # Regenerate a new random number
