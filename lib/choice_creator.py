from choice import Choice

class ChoiceCreator():
   @classmethod
   def create(cls, val):
      enemies = []
      if val == "r":
         enemies.append("p")
      elif val == "p":
         enemies.append("s")
      elif val == "s":
         enemies.append("r")

      return Choice(val, enemies)
