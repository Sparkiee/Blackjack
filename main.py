import resources
import random

player_deck = []
computer_deck = []


def start_game():
    if input("Would you like to start a game of blackjack?: Type 'y' to confirm: ") == "y":
        # clear screen
        deal_start_deck()
    print("Goodbye")


def deal_start_deck():
    player_deck.append(grab_card(player_deck))
    player_deck.append(grab_card(player_deck))
    computer_deck.append(grab_card(computer_deck))
    play_game()


def play_game():
    resume = True
    print(resources.logo)
    while True:
        print(f"Your {print_deck(player_deck)}")
        print(f"Computer {print_deck(computer_deck)}")
        hit = input("Would you like to 'hit' or 'stay'?: ").lower()
        if hit == 'stay':
            find_winner()
        if hit == 'hit':
            card = grab_card(player_deck)
            player_deck.append(card)
            if sum_deck(player_deck) >= 21:
                print(f"Your {print_deck(player_deck)}")
                find_winner()


def sum_deck(deck):
    sum = 0
    for card in deck:
        if isinstance(card, int):
            sum += card
        else:
            sum += resources.deck_value[card]
    return sum


def grab_card(deck):
    card = random.choice(resources.deck)
    if card == "A":
        if sum_deck(deck) + 11 <= 21:
            return 11
        return 1
    return card


def find_winner():
    computer_value = sum_deck(computer_deck)
    player_value = sum_deck(player_deck)
    if player_value > 21:
        print("Your " + print_deck(player_deck) + f" went over!\nComputer won");
    while computer_value < player_value:
        card = grab_card(computer_deck)
        print(f"Computer drew the card {card}")
        computer_deck.append(card)
        computer_value = sum_deck(computer_deck)
        if 21 >= computer_value > player_value:
            print("Comuter " + print_deck(computer_deck) + " is higher than yours\nComputer win")
            pass
        if computer_value > 21:
            print("Computer " + print_deck(computer_deck) + f" went over!\nYOU WON!");
            break
        if computer_value == player_value:
            print("It's a draw!")
            break
    input("Press 'Enter' to continue")
    computer_deck.clear()
    player_deck.clear()
    deal_start_deck()


def print_deck(deck):
    return f"deck: {deck}, value of deck: {sum_deck(deck)}"


start_game()
