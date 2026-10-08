from game import Game, main


def play(game, *commands):
    return [game.handle(c) for c in commands]
