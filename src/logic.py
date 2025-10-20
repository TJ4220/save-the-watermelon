MAX_SLICES = 6
def mask_word(secret, guessed):
    return "".join(c if c in guessed else "_" for c in secret)
def is_win(secret, guessed):
    return all(c in guessed for c in secret)
def normalize_guess(raw):
    if not raw or len(raw.strip()) != 1 or not raw.isalpha():
        return None
    return raw.lower()
def apply_guess(secret, guessed, guess, slices):
    if guess in guessed:
        return guessed, slices, guess in secret
    guessed.add(guess)
    if guess in secret:
        return guessed, slices, True
    return guessed, slices - 1, False
