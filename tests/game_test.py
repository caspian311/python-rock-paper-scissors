from lib.game import Game
import lib.console

def test_play_prompts_for_users_option(mocker):
   mocker.patch('lib.console.display')
   mocker.patch('lib.player_input.read_choice')

   Game.play()

   lib.console.display.assert_any_call("Rock (r), Paper (p) or Scissors (s):")

def test_play_players_choice_is_displayed(mocker):
   mocker.patch('lib.console.display')
   mocker.patch('lib.player_input.read_choice', return_value="r")

   Game.play()

   lib.console.display.assert_any_call("You played Rock!")

def test_play_players_choice_is_displayed_if_user_picks_other_option(mocker):
   mocker.patch('lib.console.display')
   mocker.patch('lib.player_input.read_choice', return_value="s")

   Game.play()

   lib.console.display.assert_any_call("You played Scissors!")
