from lib.choice_creator import ChoiceCreator

def test_strifiy():
   assert "Rock" == str(ChoiceCreator.create("r"))
   assert "Scissors" == str(ChoiceCreator.create("s"))
   assert "Paper" == str(ChoiceCreator.create("p"))

def test_equality():
   assert ChoiceCreator.create("r") == ChoiceCreator.create("r")
   assert ChoiceCreator.create("s") == ChoiceCreator.create("s")
   assert ChoiceCreator.create("p") == ChoiceCreator.create("p")

def test_not_equality():
   assert ChoiceCreator.create("r") != ChoiceCreator.create("s")
   assert ChoiceCreator.create("r") != ChoiceCreator.create("p")

   assert ChoiceCreator.create("s") != ChoiceCreator.create("r")
   assert ChoiceCreator.create("s") != ChoiceCreator.create("p")

   assert ChoiceCreator.create("p") != ChoiceCreator.create("r")
   assert ChoiceCreator.create("p") != ChoiceCreator.create("s")

def test_paper_beats_rock():
   assert ChoiceCreator.create("p").beats(ChoiceCreator.create("r")) == True
   assert ChoiceCreator.create("r").beats(ChoiceCreator.create("p")) == False

def test_rock_beats_scissors():
   assert ChoiceCreator.create("s").beats(ChoiceCreator.create("p")) == True
   assert ChoiceCreator.create("s").beats(ChoiceCreator.create("r")) == False

def test_scissors_beats_paper():
   assert ChoiceCreator.create("s").beats(ChoiceCreator.create("p")) == True
   assert ChoiceCreator.create("p").beats(ChoiceCreator.create("s")) == False

