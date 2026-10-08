"""A tiny data-driven text adventure engine."""

import copy

import world as default_world

ALIASES = {
    "n": "go north", "s": "go south", "e": "go east", "w": "go west",
    "u": "go up", "d": "go down", "up": "go up", "down": "go down",
    "l": "look", "i": "inventory", "inv": "inventory", "get": "take", "q": "quit",
}
