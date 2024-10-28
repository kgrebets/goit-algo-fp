import random
import pandas as pd
import matplotlib.pyplot as plt

def roll_dice(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)} 

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sums_count[total] += 1

    probabilities = {sum_: count / num_rolls for sum_, count in sums_count.items()}
    return probabilities

def simulate_dice_rolls(num_rolls):
    probabilities = roll_dice(num_rolls)
    
    df = pd.DataFrame(list(probabilities.items()), columns=['Sum', 'Probability'])
    df['Probability'] = df['Probability'].round(4) 

    print(df)
    
    plt.bar(df['Sum'], df['Probability'], color='blue', alpha=0.7)
    plt.xlabel('Сума')
    plt.ylabel('Імовірність')
    plt.title(f'Імовірність сум при киданні двох кубиків {num_rolls} раз')
    plt.xticks(range(2, 13))
    plt.ylim(0, max(df['Probability']) + 0.05)
    plt.grid(axis='y')
    plt.show()

for num_roll in [100, 1000, 100000]:
    simulate_dice_rolls(num_roll)
