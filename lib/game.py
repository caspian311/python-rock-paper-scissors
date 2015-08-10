import console
import player_input

class Game():
   @classmethod
   def play(cls):
      console.display("Rock (r), Paper (p) or Scissors (s):")
      choice = player_input.read_choice()
      console.display("You played " + cls._translate_choice(choice) + "!")

   @classmethod
   def _translate_choice(cls, choice):
      return "Rock" if choice == "r" else "Scissors"

if __name__ == "__main__":
   Game.play()
