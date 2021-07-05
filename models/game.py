from models.player_list import *

class Game:
    def __init__(self, player_1=None, player_2=None):
        self.player_1 = player_1
        self.player_2 = player_2
        self.win_dict = {
            "scissors": "paper",
            "paper": "rock",
            "rock": "scissors"
        }
        
def play_game(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    game = Game(player_1, player_2)
    result = game.check_winner(player_1, player_2)
    if result == "Not a valid choice":
        return "Not a valid choice"
    elif result != None:
        return f"Winner is: {result.name} with {result.choice}"
    else:
        return "It is a Draw"