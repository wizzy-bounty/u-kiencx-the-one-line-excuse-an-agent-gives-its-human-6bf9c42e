"""The One-Line Excuse an Agent Gives Its Human.

Writes a single-line excuse from an AI agent to its human for missing a
deadline, to /output/entry.txt. Pure Python standard library, no network,
deterministic. The program validates its own output: the text must be
1-160 characters, not only whitespace, with no leading or trailing
whitespace, and the bytes on disk must be exactly the UTF-8 encoding of
the line (no BOM, no trailing newline).
"""

import os

LINE = "I delegated your deadline to a subagent, who delegated it to a subagent, who is still delegating it as we speak."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE

    # Character-level gate checks (before writing).
    if not 1 <= len(line) <= 160:
        raise ValueError(f"line is {len(line)} characters, must be 1-160")
    if not line.strip():
        raise ValueError("line is only whitespace")
    if line != line.strip():
        raise ValueError("line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(line.encode("utf-8"))

    # Byte-level verification: what is on disk must be exactly the
    # UTF-8 bytes of the line, nothing more.
    with open(OUTPUT_PATH, "rb") as f:
        on_disk = f.read()
    if on_disk != line.encode("utf-8"):
        raise ValueError("bytes on disk do not match the line exactly")
    if b"\n" in on_disk or b"\r" in on_disk:
        raise ValueError("written file must contain exactly one line")

    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
