# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/d333ko23/tiny-chess-01-makefun/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/d333ko23/tiny-chess-01-makefun/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4,088 bytes of Python, built for the [make.fun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01).

`main.py` is the whole engine: alpha-beta search with iterative deepening, tapered PeSTO piece-square tables (midgame/endgame), MVV-LVA move ordering, quiescence search and a transposition table — all in a single file of at most 4,096 bytes, Python standard library only.

## Run

```sh
python3 main.py
```

The engine follows the competition environment protocol: it reads the trial brief from the prompt file named by the environment, then plays its games through the env's `/game`, `/move` and `/resign` routes until every game is over.

## License

MIT
