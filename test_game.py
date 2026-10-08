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


def test_take_and_drop():
    game = Game()
    game.handle("take driftwood")
    assert "driftwood" in game.inventory
    game.handle("drop driftwood")
    assert "driftwood" in game.room["items"]


def test_matches_need_oil_first():
    game = Game()
    play(game, "n", "w", "take brass key", "take matches", "e", "n", "up")
    assert "smoulders" in game.handle("use matches")
    assert not game.over


def test_full_walkthrough_wins():
    game = Game()
    play(game, "e", "take oil can", "w", "n", "w", "take brass key", "take matches",
         "e", "n", "up", "use oil can", "use matches")
    assert game.over
    assert "lit" in game.flags


def test_main_loop_stops_on_quit():
    out = []
    commands = iter(["look", "quit"])
    main(input_fn=lambda _: next(commands), output_fn=out.append)
    assert out[-1] == "Goodbye."
