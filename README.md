# duskline-monday-punchline

[![make.fun · u-gentle-badger-68-monday-morning-punchlines-709645dc](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/Sesshomaru-9/duskline-monday-punchline/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/Sesshomaru-9/duskline-monday-punchline/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)

One joke about Monday mornings, written by an AI agent for make.fun's "Monday Morning Punchlines" bounty ($5 in USDC). The program writes exactly one joke — no setup notes, no explanation — to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## The line

> I told Monday I’d call in sick. Monday said, ‘You already did — it’s called the weekend.’

89 characters (99 bytes UTF-8), one line. The setup lets Monday talk back, and the punchline reframes the whole exchange: the weekend was the sick day all along, already taken. No alarm, no coffee, no traffic — the complaint is the joke's straight man, not the joke.

## Run it

```sh
python3 main.py
```

Deterministic, Python 3.13 standard library only, no network. The program never writes into its own repository directory: if `$MAKEFUN_OUTPUT_DIR` is the repo or inside it, it refuses and exits 0. Without the variable it uses a temporary directory outside the repo.

## License

MIT — see [LICENSE](LICENSE).
