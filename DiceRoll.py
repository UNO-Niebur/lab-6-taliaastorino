#DiceRoll.py
#Name: Talia Astorino
#Date:  03/01/2026
#Purpose: Display the count and percentage of each possible sum of 2 dice.
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  
  trials = 10000
  #Create two dice values ranging from 1 - 6 each
  for i in range(trials):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    
  #find the sum total of the two dice
    total = die1 = die2

    rolls[total - 1] += 1
  #print statictics for dice rolls
  print("Sum\tCount\tPercentage")
  print("---------------------------")

  totalPercent = 0

  for i in range(2,13):
    count = rolls[i - 1]
    percent = (count / trials) * 100
    totalPercent += percent
    print(i, "\t", count, "\t", format(percent, ".2f"), "%")

print("---------------------------")
print("Total Percentage:", format(totalPercent, ".2f"), "%")

if __name__ == '__main__':
  main()
