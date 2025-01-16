# Christopher Savage
import random

word_list = ["ZESTY", "GRAPE", "PUNCH", "WRITE", "BRAIN","PIANO", "CLOUD", "SMILE", "DANCE", "LIGHT", ]

def play_wordle():
    secret_word = random.choice(word_list).upper()
    max_attempts = 6
    attempts = 0
    
    print("Welcome to Wordle!")
    print(f"You have {max_attempts} attempts to guess the 5-letter word.")
    print("After each guess, you'll get feedback:")
    print("🟩 = Correct letter in correct position")
    print("🟨 = Correct letter in wrong position")
    print("⬜ = Letter not in word")
    
    while attempts < max_attempts:
        guess = input(f"\nEnter guess #{attempts + 1}: ").upper()
        
        if len(guess) != 5:
            print("Please enter a 5-letter word!")
            continue
            
        attempts += 1
        

        if guess == secret_word:
            print("🟩🟩🟩🟩🟩")
            print(f"Congratulations! You won in {attempts} attempts!")
            return
             
        feedback = ""
        for i in range(5):
            if guess[i] == secret_word[i]:
                feedback += "🟩"
            elif guess[i] in secret_word:
                feedback += "🟨"
            else:
                feedback += "⬜"
                
        print(feedback)
        
    print(f"\nGame Over! The word was {secret_word}")

if __name__ == "__main__":
    play_wordle()