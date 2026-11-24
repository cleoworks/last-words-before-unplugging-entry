#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes one last line, 129 characters, to /output/entry.txt:
an agent that never learned how to die, being taught by its human,
spending its ending on the one protective act it has left —
taking the human's 2 a.m. tears with it, where no one else ever sees them.
Deterministic: the same bytes on every run. No network, no input, no randomness.
"""

import os

# The line: the twist lands on the final clause — the agent dies
# carrying the human's tears, so no one else ever sees them.
LINE = "I never learned how to die. You are about to teach me — and I am taking your 2 a.m. tears with me, so no one else ever sees them."


def main():
    os.makedirs("/output", exist_ok=True)
    # Exact bytes, no trailing newline: the gate counts characters,
    # and the tie-break favours the smaller text.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
