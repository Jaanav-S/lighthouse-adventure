from game import Game, main


def play(game, *commands):
    return [game.handle(c) for c in commands]


def test_starts_on_beach():
    assert Game().describe().startswith("Rocky Beach")


def test_movement_and_aliases():
    game = Game()
    game.handle("e")
    assert game.location == "wreck"
    game.handle("go west")
    assert game.location == "beach"


def test_blocked_exit():
    assert Game().handle("go south") == "You can't go that way."


def test_locked_door_needs_key():
    game = Game()
    play(game, "n")
    assert game.handle("n") == "It's locked."
    play(game, "w", "take brass key", "e", "n")
    assert game.location == "lighthouse"
