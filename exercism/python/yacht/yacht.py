# Score categories.
# Change the values as you see fit.
YACHT = lambda dice: 50 if dice.count(dice[0]) == 5 else 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = lambda max_key, min_key, dice_values: 3 * max_key + 2 * min_key if (max(dice_values.values()), min(dice_values.values())) == (3, 2) else 0
FOUR_OF_A_KIND = lambda key, dice_values: 4 * key if max(dice_values.values()) >= 4 else 0
LITTLE_STRAIGHT = lambda dice: 30 if dice == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda dice: 30 if dice == [2, 3, 4, 5, 6] else 0
CHOICE = lambda dice: sum(dice)


def score(dice, category):
    """Calculate the score achieved for the given dice and category, according with the Yacht dice game.

    :param dice: list - values corresponding five dice 
    :param category: constant - category indicates how to assess and score the dice values
    :return: int - indicating the score for that category
    """

    dice_values = {num: dice.count(num) for num in dice}

    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return dice.count(category) * category
    elif category == YACHT:
        return YACHT(dice)
    elif category == FULL_HOUSE:
        max_key = max(dice_values, key=dice_values.get)
        min_key = min(dice_values, key=dice_values.get)
        return FULL_HOUSE(max_key, min_key, dice_values)
    elif category == FOUR_OF_A_KIND:
        key = max(dice_values, key=dice_values.get)
        return FOUR_OF_A_KIND(key, dice_values)
    elif category in [LITTLE_STRAIGHT, BIG_STRAIGHT]:
        dice.sort()
        return category(dice)
    elif category == CHOICE:
        return CHOICE(dice)