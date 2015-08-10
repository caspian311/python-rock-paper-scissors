
class Choice():
   def __init__(self, val):
      self._value = val

   def __str__(self):
      return "Rock" if self._value == "r" else "Scissors" if self._value == "s" else "Paper"

   def __eq__(self, other):
      return self._value == other._value

   def _beats(self, other):
      return self._value == "p"

   def winning_message(self, computer_choice):
      if self == computer_choice:
         return "It's a tie!"
      elif self._beats(computer_choice):
         return "Player wins!"
      else:
         return "Computer wins!"
