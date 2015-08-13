
class Choice(object):
   def __init__(self, val, enemies):
      self._value = val
      self._enemies = enemies

   def __eq__(self, other):
      return type(self) is type(other)

   def beats(self, other):
      return not other._value in self._enemies

