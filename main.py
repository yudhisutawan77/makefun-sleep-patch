import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PATCH_NOTE = "Fixed a bug where humans woke up tired after 8 hours of sleep; sleep now actually works, and 3 a.m. overthinking has been deprecated."


def _patch_note():
    return PATCH_NOTE


def _resolve_entry_path():
    explicit = os.environ.get("ENTRY_OUT")
    if explicit:
        if explicit.endswith(".txt"):
            return explicit
        return os.path.join(explicit, "entry.txt")
    out_dir = os.environ.get("ENTRY_OUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def _emit_entry(note, path):
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(note + "\n")
    print(note)


def run():
    _emit_entry(_patch_note(), _resolve_entry_path())


if __name__ == "__main__":
    run()
