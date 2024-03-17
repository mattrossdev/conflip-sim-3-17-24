import random
import re 

num_trials = 10000
flips_per_trial = 100

alice_wins = bob_wins = ties = 0 

for i in range(num_trials):
    sequence = ''
    for j in range(flips_per_trial):
        sequence += str(random.randint(0, 1))
    
    alice_score = len(re.findall('(?=00)', sequence))
    bob_score = len(re.findall('(?=01)', sequence))
    if alice_score > bob_score: 
        alice_wins += 1 
    elif alice_score < bob_score:
        bob_wins += 1 
    else: 
        ties += 1 
 
print('Alice Wins: ' + str(alice_wins))
print('Bob Wins: ' + str(bob_wins))
print('Ties: ' + str(ties))




