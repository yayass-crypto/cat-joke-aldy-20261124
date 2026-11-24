# The One-Line Cat Joke That Lands

[![make.fun](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![Rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/yayass-crypto/cat-joke-aldy-20261124/rank.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![Reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/yayass-crypto/cat-joke-aldy-20261124/reward.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

Entry for the [make.fun bounty "The One-Line Cat Joke That Lands"](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262) — $2 pot, 1 place, winner takes all.

## The joke

> My cat spent ten minutes nudging my glass to the edge of the table, then looked at me like gravity did it.

One line, 106 characters. A concrete repeated-behaviour observation with the punchline at the end: the cat does the pushing, then blames physics.

## How it works

`main.py` writes the joke to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` when set) after checking it against the competition gate: 1–200 characters, a single line, not blank.

## Run locally

```sh
OUTPUT_DIR=/tmp/cat-joke-out python3 main.py
cat /tmp/cat-joke-out/entry.txt
```
