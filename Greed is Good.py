#
# Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it,
# is to score a throw according to these rules. You will always be given an array with five six-sided
# dice values.
# Three 1's => 1000 points ;  Three 6's =>  600 points
# Three 5's =>  500 points ; Three 4's =>  400 points
# Three 3's =>  300 points ; Three 2's =>  200 points
# One   1   =>  100 points ; One   5   =>   50 point
# A single die can only be counted once in each roll. For example, a given "5" can only count as
# part of a triplet (contributing to the 500 points) or as a single 50 points,
# but not both in the same roll.

def score(dice):
    number_dice = [0,0,0,0,0,0]
    score = 0
    for i in dice:
        number_dice[i-1] +=1
        if i == 1:
            score += 100
        if i == 5:
            score += 50
    if any(n >= 3 for n in number_dice):
        if number_dice[0] >= 3:
            score += 700
        elif number_dice[4] >= 3:
            score += 350
        else:
            for i in range(0,len(number_dice)):
                if number_dice[i] >= 3:
                    score += 100* (i+1)
    return score

# Others solution:

def score(dice): 
  sum = 0
  counter = [0,0,0,0,0,0]
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice: 
    counter[die-1] += 1
  
  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

  return sum
#
def score(dice):
    # dice scores  [1   ,   2,   3,   4, 5,   6]
    scores_3same = [1000, 200, 300, 400, 500, 600]
    scores_single = [100 ,   0,   0,   0,  50,   0]
    
    sum = 0
    for i in range(1,7):
        count_i = dice.count(i)
        sum += (count_i // 3) * scores_3same[i-1] + (count_i % 3) * scores_single[i-1]
            
    return sum
#
