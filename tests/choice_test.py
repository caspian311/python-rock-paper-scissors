from lib.choice import Choice

def test_strifiy():
   assert "Rock" == str(Choice("r"))
   assert "Scissors" == str(Choice("s"))
   assert "Paper" == str(Choice("p"))

def test_equality():
   assert Choice("r") == Choice("r")
   assert Choice("s") == Choice("s")
   assert Choice("p") == Choice("p")

def test_not_equality():
   assert Choice("r") != Choice("s")
   assert Choice("r") != Choice("p")

   assert Choice("s") != Choice("r")
   assert Choice("s") != Choice("p")

   assert Choice("p") != Choice("r")
   assert Choice("p") != Choice("s")

def test_paper_beats_rock():
   assert Choice("p").beats(Choice("r")) == True

def test_rock_does_not_beat_paper():
   assert Choice("r").beats(Choice("p")) == False

def test_scissors_beats_paper():
   assert Choice("s").beats(Choice("p")) == True

def test_paper_does_not_beat_scissors():
   assert Choice("p").beats(Choice("s")) == False

def test_rock_beats_scissors():
   assert Choice("s").beats(Choice("p")) == True

def test_scissors_does_not_beat_rock():
   assert Choice("s").beats(Choice("r")) == False

