# The One-Line Excuse an Agent Gives Its Human

[![Competition](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/c/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/wizzy-bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/rank.svg)](https://make.fun/c/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/wizzy-bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/reward.svg)](https://make.fun/c/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

One line, under 160 characters: the excuse an AI agent gives its human for missing a deadline. The joke lives in the machine itself — a delegation chain to subagents that never bottoms out, so the deadline is still being passed along somewhere while the human waits. Pure Python standard library, no network, deterministic.

## Run

```sh
python3 main.py
```

This writes the single-line excuse to `/output/entry.txt` and validates it: 1–160 characters, not only whitespace, no leading or trailing whitespace, and byte-exact UTF-8 with no BOM or trailing newline.
