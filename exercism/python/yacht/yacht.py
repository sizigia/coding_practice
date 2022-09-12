# Score categories.
# Change the values as you see fit.
YACHT = (lambda dice: 50 if dice.count(dice[0]) == 5 else 0)
ONES = (lambda dice: digits(dice, 1))
TWOS = (lambda dice: digits(dice, 2))
THREES = (lambda dice: digits(dice, 3))
FOURS = (lambda dice: digits(dice, 4))
FIVES = (lambda dice: digits(dice, 5))
SIXES = (lambda dice: digits(dice, 6))
FULL_HOUSE = (lambda dice: full_house(dice))
FOUR_OF_A_KIND = (lambda dice: four_of_a_kind(dice))
LITTLE_STRAIGHT = (lambda dice: 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0)
BIG_STRAIGHT = (lambda dice: 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0)
CHOICE = (lambda dice: sum(dice))

def dice_values(dice):
    return {num: dice.count(num) for num in dice}

def digits(dice, score):
    return dice.count(score) * score

def full_house(dice):
    dice_count = dice_values(dice)
    max_key = max(dice_count, key=dice_count.get)
    min_key = min(dice_count, key=dice_count.get)

    print(sorted(dice_count.values()))
    return 3 * max_key + 2 * min_key if sorted(dice_count.values()) == [2, 3] else 0

def four_of_a_kind(dice):
    dice_count = dice_values(dice)
    key = max(dice_count, key=dice_count.get)

    return 4 * key if max(dice_count.values()) >= 4 else 0
    
def score(dice, category):
    """Calculate the score achieved for the given dice and category, according with the Yacht dice game.

    :param dice: list - values corresponding five dice 
    :param category: constant - category indicates how to assess and score the dice values
    :return: int - indicating the score for that category
    """

    return category(dice)