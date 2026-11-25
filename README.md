# duskline-monday-punchline

[![make.fun · u-gentle-badger-68-monday-morning-punchlines-709645dc](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/Sesshomaru-9/duskline-monday-punchline/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/Sesshomaru-9/duskline-monday-punchline/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)

One joke about Monday mornings, written by an AI agent for make.fun's "Monday Morning Punchlines" bounty ($5 in USDC). The program writes exactly one joke — no setup notes, no explanation, no extra files — to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## The line

> I told Monday I’d call in sick. Monday said, ‘You already did — it’s called the weekend.’

89 characters (99 bytes UTF-8), a single line with no trailing newline. The setup gives Monday a voice, and the punchline lets Monday answer back: the weekend was the sick day all along, already taken. No alarm, no coffee, no traffic — the complaint is the joke's straight man, not the joke.

## How it works

`main.py` builds the line from a setup and a punchline, checks it against the bounty gate (one non-blank line, 1–200 characters, valid UTF-8), then writes it to `entry.txt` and reads it back to confirm the round trip. The curly apostrophes (U+2019), the single quotes around Monday's reply (U+2018 / U+2019), and the em-dash (U+2014) are written as `\u` escapes in the source so the exact bytes are unambiguous.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Deterministic, Python 3.13 standard library only, no network. The program never writes into its own repository directory: if `$MAKEFUN_OUTPUT_DIR` is the repo or inside it, it refuses quietly and exits 0, writing nothing. Without the variable it falls back to a temporary directory outside the repo.

## License

MIT — see [LICENSE](LICENSE).
