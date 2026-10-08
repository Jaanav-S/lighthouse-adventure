"""A tiny data-driven text adventure engine."""

import copy

import world as default_world

ALIASES = {
    "n": "go north", "s": "go south", "e": "go east", "w": "go west",
    "u": "go up", "d": "go down", "up": "go up", "down": "go down",
    "l": "look", "i": "inventory", "inv": "inventory", "get": "take", "q": "quit",
}

HELP = "Commands: look, go <dir>, take <item>, drop <item>, use <item>, inventory, help, quit"


class Game:
    def __init__(self, world=default_world):
        self.world = world
        self.rooms = copy.deepcopy(world.ROOMS)
        self.location = world.START
        self.inventory = []
        self.flags = set()
        self.over = False

    @property
    def room(self):
        return self.rooms[self.location]

    def describe(self):
        room = self.room
        lines = [room["name"], room["description"]]
        if room["items"]:
            lines.append("You see: " + ", ".join(room["items"]) + ".")
        lines.append("Exits: " + ", ".join(room["exits"]) + ".")
        return "\n".join(lines)

    def go(self, direction):
        if direction not in self.room["exits"]:
            return "You can't go that way."
        key = self.world.LOCKED.get((self.location, direction))
        if key and key not in self.inventory:
            return "It's locked."
        self.location = self.room["exits"][direction]
        return self.describe()

    def take(self, item):
        if item not in self.room["items"]:
            return f"There is no {item} here."
        self.room["items"].remove(item)
        self.inventory.append(item)
        return f"Taken: {item}."

    def drop(self, item):
        if item not in self.inventory:
            return f"You don't have {item}."
        self.inventory.remove(item)
        self.room["items"].append(item)
        return f"Dropped: {item}."

    def use(self, item):
        if item not in self.inventory:
            return f"You don't have {item}."
        effect = self.world.USES.get((item, self.location))
        if not effect:
            return "Nothing happens."
        if effect.get("needs_flag") and effect["needs_flag"] not in self.flags:
            return effect.get("fail", "Nothing happens.")
        self.flags.add(effect["sets"])
        message = effect["message"]
        if self.world.GOAL_FLAG in self.flags:
            self.over = True
            message += "\n\n" + self.world.WIN_TEXT
        return message

    def examine(self, item):
        if item in self.inventory or item in self.room["items"]:
            return self.world.ITEMS.get(item, "Nothing special.")
        return f"There is no {item} here."

    def show_inventory(self):
        if not self.inventory:
            return "You are carrying nothing."
        return "You are carrying: " + ", ".join(self.inventory) + "."

    def handle(self, command):
        """Run one command and return the text to show the player."""
        command = " ".join(command.lower().split())
        command = ALIASES.get(command, command)
        verb, _, arg = command.partition(" ")
        verb = ALIASES.get(verb, verb)
        if verb == "look":
            return self.describe()
        if verb == "go":
            return self.go(arg)
        if verb in ("take", "drop", "use", "examine") and not arg:
            return f"{verb.capitalize()} what?"
        if verb == "take":
            return self.take(arg)
        if verb == "drop":
            return self.drop(arg)
        if verb == "use":
            return self.use(arg)
        if verb == "examine":
            return self.examine(arg)
        if verb == "inventory":
            return self.show_inventory()
        if verb == "help":
            return HELP
        if verb == "quit":
            self.over = True
            return "Goodbye."
        return "I don't understand that."


def main(input_fn=input, output_fn=print):
    game = Game()
    output_fn(game.describe())
    while not game.over:
        try:
            command = input_fn("> ")
        except EOFError:
            break
        output_fn(game.handle(command))


if __name__ == "__main__":
    main()
