"""The island world: rooms, items and puzzles as plain data."""

START = "beach"

ROOMS = {
    "beach": {
        "name": "Rocky Beach",
        "description": "Waves hiss over black stones. A path climbs north toward a dark lighthouse.",
        "exits": {"north": "path", "east": "wreck"},
        "items": ["driftwood"],
    },
    "wreck": {
        "name": "Shipwreck",
        "description": "The splintered hull of a fishing boat lies on its side.",
        "exits": {"west": "beach"},
        "items": ["oil can"],
    },
    "path": {
        "name": "Cliff Path",
        "description": "Gorse scratches at your legs. The lighthouse door is north; a shed stands to the west.",
        "exits": {"south": "beach", "north": "lighthouse", "west": "shed"},
        "items": [],
    },
    "shed": {
        "name": "Keeper's Shed",
        "description": "Rusty tools hang from nails. Something glints on the workbench.",
        "exits": {"east": "path"},
        "items": ["brass key", "matches"],
    },
    "lighthouse": {
        "name": "Lighthouse Base",
        "description": "A spiral staircase winds up into the dark.",
        "exits": {"south": "path", "up": "lamp room"},
        "items": [],
    },
    "lamp room": {
        "name": "Lamp Room",
        "description": "The great lamp sits cold and dry, its glass streaked with salt.",
        "exits": {"down": "lighthouse"},
        "items": [],
    },
}

ITEMS = {
    "driftwood": "A bleached, twisted branch. Not much use.",
    "oil can": "A dented can, still half full of lamp oil.",
    "brass key": "A heavy key stamped with a tiny lighthouse.",
    "matches": "A tin of matches, miraculously dry.",
}
