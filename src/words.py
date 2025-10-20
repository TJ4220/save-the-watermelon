from pathlib import Path
import random
DEFAULT_WORDS = ["melon","water","python","slice","guess","fruit"]
def load_words():
    path = Path(__file__).resolve().parents[1] / "data" / "words.txt"
    if path.exists():
        words = [w.strip().lower() for w in path.read_text().splitlines() if w.strip()]
        return words or DEFAULT_WORDS
    return DEFAULT_WORDS
def select_secret_word(words=None):
    words = words or load_words()
    return random.choice(words)
