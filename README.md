# bfb-demo — bug factory for BangkahFixBot

A tiny, deliberately buggy utility package used as the **demo/eval target** for
[BangkahFixBot](https://github.com/Bangkah/BangkahFixBot) (Nebius x NVIDIA Global AI
Hackathon, Coding & Agentic Engineering track).

Each GitHub issue in this repository describes one localized bug in `src/bfbutils/`.
The baseline suite in `tests/` passes today (it does not cover the bugs) — the bot's
job is to fix the issue, write its own regression test, and keep the baseline green.

Run locally:

```bash
pip install pytest
pytest -q
```
