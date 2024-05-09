from random import choice
options = ["rock", "paper", "scissor"]

fail_message = """
=============================
you fail retry again
=============================
"""

win_message = """
=============================
you win play again
=============================
"""

draw_message = """
=============================
it is a draw retry again
=============================
"""


def get_choices():
    """
    get player choice and randomly selecting computer choice form options
    :return:
    player choice
    computer choice
    """
    pick = input("""
    choose from the options:
    1. rock
    2. paper
    3. scissor
    
    """)
    if int(pick) == 1:
        player_choice = "rock"
    elif int(pick) == 2:
        player_choice = "paper"
    else:
        player_choice = "scissor"

    computer_choice = choice(options)

    return {'player_choice': player_choice, 'computer_choice': computer_choice}


def check_win():
    """
    check if the player win or not
    :return:
    message
    """
    both_choice = get_choices()
    player_choice, computer_choice = both_choice['player_choice'], both_choice['computer_choice']
    print(player_choice, computer_choice)

    if (player_choice=="rock" and computer_choice=="scissor") or (player_choice=="paper" and computer_choice=="rock") or (player_choice=="scissor" and computer_choice=="paper"):
        return win_message
    elif (player_choice=="scissor" and computer_choice=="rock") or (player_choice=="rock" and computer_choice=="paper") or (player_choice=="paper" and computer_choice=="scissor"):
        return fail_message
    else:
        return draw_message


run = check_win()
print(run)