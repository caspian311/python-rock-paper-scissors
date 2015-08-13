#Python: Rock, Paper, Scissors#

Just to keep my Python skills up. A rock, paper, scissors console game.


###Dependencies:###

    pip install -U pytest mock pytest-mock
    
###Run tests:###

    py.test
    
###Run game:###

    ./bin/play.sh


Tring to avoid embedded if/else blocks like this:

    if self is rock:
       if other is paper:
          lose
       if other is scissors:
		  win
       if other is rock:
          tie
    if self is scissors:
	   if other is paper:
		 lose
       if other is rock
	      win
       if other is scissors:
          tie
    if self is paper:
       if other is scissors:
          lose
       if other is rock:
          win
       if other is paper:
          tie

