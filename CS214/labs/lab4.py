import random

nums = []
wins = 0
losses = 0
winrate = 0

while True:
    try:
        max_num = int(input("Enter the maximum number: "))
        min_num = int(input("Enter the minimum number: "))
        
        if min_num >= max_num:
            print("Minimum number must be less than maximum number")
            continue
            
        answer = random.randint(min_num, max_num)
        nums.append(answer)
        
        guess = int(input("Guess the number: "))
        if guess == answer:
            print("You guessed right!")
            wins += 1
        else:
            print("You guessed wrong!")
            print("The number was", answer)
            losses += 1

        total_games = wins + losses
        winrate = (wins / total_games) * 100 if total_games > 0 else 0
        
        print("\nStats:")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Winrate: {winrate:.1f}%")

        reset_stats = input("\nWould you like to reset your stats? (yes/no) ").lower()
        if reset_stats == "yes":
            wins = 0
            losses = 0
            winrate = 0
            nums = []
            print("Stats have been reset")
        
        play_again = input("\nWould you like to play again? (yes/no) ").lower()
        if play_again == "no":
            break
            
    except ValueError:
        print("Please enter valid numbers")