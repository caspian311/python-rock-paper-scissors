import console
import player_input
import computer_input

class Game():
   @classmethod
   def play(cls):
      console.display("Rock (r), Paper (p) or Scissors (s):")

      player_choice = player_input.read_choice()
      computer_choice = computer_input.read_choice()

      console.display("You played " + cls._translate_choice(player_choice) + "!")
      console.display("Computer played " + cls._translate_choice(computer_choice) + "!")

      if player_choice == computer_choice:
         console.display("It's a tie!")
      elif player_choice == "p":
         console.display("Player wins!")
      else:
         console.display("Computer wins!")

   @classmethod
   def _translate_choice(cls, choice):
      return "Rock" if choice == "r" else "Scissors" if choice == "s" else "Paper"

if __name__ == "__main__":
   Game.play()
