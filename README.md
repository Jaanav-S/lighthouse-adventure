# The Lighthouse

A short text adventure. You wash up on a rocky island at dusk and have to
get the old lighthouse lamp burning before the supply boat passes.

## Playing

```
python game.py
```

Commands: `look`, `go <direction>` (or just `n`, `s`, `e`, `w`, `up`,
`down`), `take <item>`, `drop <item>`, `use <item>`, `inventory`, `help`,
`quit`.

## How it is built

The world lives in `world.py` as plain dictionaries: rooms, their exits,
the items lying around and which exits are locked. `game.py` holds the
engine, which knows nothing about the island and could run any world with
the same shape.

## Writing your own world

Copy `world.py`, change the rooms and items, and point `Game` at it. Locked
exits list the item that opens them, and the `goal` entry says which item
has to be used where to win.

## Tests

```
python -m pytest
```
