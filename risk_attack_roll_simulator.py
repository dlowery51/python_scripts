import random
import argparse
"""
This program is a multi-attack simulator for the game of risk.
It simply asks for the number of attackers, the number of defenders, and a stop number which 
represents the number of attackers, that should the attacking number be reduced to or below,
the program will stop as a safety measure. This program speeds up the process for long engagements
by conducting any series of attacking rolls in rapid succession, thus saving considerable time.
"""

# Set up argument parser
parser = argparse.ArgumentParser(description="Risk battle simulation")

# Define expected arguments
parser.add_argument('--attacker', type=int, required=True, help='Number of attacking units')
parser.add_argument('--defender', type=int, required=True, help='Number of defending units')
parser.add_argument('--stop', type=int, required=True, help='Number of units attacker will stop at')

# Parse the arguments
args = parser.parse_args()
attackers = args.attacker
defenders = args.defender
stop = args.stop  # or call it attacker_stops_at if clearer

# Conduct attacking rolls until one of the following conditions is met
# 1) The number of attackers is zero
# 2) The number of defenders is zero
# 3) The number of attackers is less than or equal to the provided stop number
def attack(attackers, defenders, stop):
  while (attackers > stop):
    diceA = [0,0,0]
    diceD = [0,0]
    for i in range(0, 3):
      if attackers > i:
        diceA[i] = random.randint(1, 6)
    for i in range(0, 2):
      if defenders > i:
        diceD[i] = random.randint(1, 6)
    diceA.sort(reverse=True)
    diceD.sort(reverse=True)

    for i in range(0, 2):
      if diceD[i] >= diceA[i]:
        attackers -= 1
        if attackers <= 0:
          #attackers lose battle
          break;
      else:
        defenders -= 1
        if attackers <= 0:
          #attackers lose battle
          break;
  print(f"Attacker: {attackers} remaining; Defender: {defenders} remaining")

attack(attackers, defenders, stop)

