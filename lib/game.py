import console
import player_input
import computer_input
from choice import Choice

class Game():
   @classmethod
   def play(cls):
      console.display("Rock (r), Paper (p) or Scissors (s):")

      player_choice = Choice(player_input.read_choice())
      computer_choice = Choice(computer_input.read_choice())

      console.display("You played " + str(player_choice) + "!")
      console.display("Computer played " + str(computer_choice) + "!")

      console.display(player_choice.winning_message(computer_choice))

if __name__ == "__main__":
   Game.play()
