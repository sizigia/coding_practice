"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    values = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 1,
    }

    if card in ['J', 'Q', 'K', 'A']:
        return values[card]

    return int(card)


def higher_card(card_one, card_two) -> str or tuple:
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    hand = [card_one, card_two]
    values = [value_of_card(card) for card in hand]

    if card_one == card_two or values[0] == values[1]:
        return (card_one, card_two)

    return hand[values.index(max(values))]


def value_of_ace(card_one, card_two) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    change_ace_val = lambda card: 11 if card == 'A' else value_of_card(card)
    values = [change_ace_val(card) for card in (card_one, card_two)]

    return 11 if sum(values) + 11 <= 21 else 1


def is_blackjack(card_one, card_two) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    change_ace_val = lambda card: 11 if card == 'A' else value_of_card(card)
    values = [change_ace_val(card) for card in (card_one, card_two)]

    return sum(values) == 21


def can_split_pairs(card_one, card_two) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    values = [value_of_card(card) for card in (card_one, card_two)]

    return all(card == values[0] for card in values)


def can_double_down(card_one, card_two) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    values = [value_of_card(card) for card in (card_one, card_two)]

    return sum(values) >= 9 and sum(values) <= 11
