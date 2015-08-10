
class Choice():
   def __init__(self, val):
      self._value = val

   def __str__(self):
      return "Rock" if self._value == "r" else "Scissors" if self._value == "s" else "Paper"

   def __eq__(self, other):
      return self._value == other._value

   def beats(self, other):
      if self._value == "s":
         return True if other._value == "p" else False
      elif self._value == "p":
         return True if other._value == "r" else False
      else:
         return True if other._value == "s" else False

