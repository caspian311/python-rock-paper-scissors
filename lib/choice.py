
class Choice():
   def __init__(self, val, enemies):
      self._value = val
      self._enemies = enemies

   def __str__(self):
      return "Rock" if self._value == "r" else "Scissors" if self._value == "s" else "Paper"

   def __eq__(self, other):
      return self._value == other._value

   def beats(self, other):
      return not other._value in self._enemies

