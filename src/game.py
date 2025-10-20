from .words import select_secret_word, load_words
from .logic import MAX_SLICES, normalize_guess, apply_guess, is_win, mask_word
def play_once():
    secret = select_secret_word(load_words())
    guessed = set()
    slices = MAX_SLICES
    print("\n🍉 Save the Watermelon!")
    while slices > 0 and not is_win(secret, guessed):
        print("Word:", " ".join(mask_word(secret, guessed)))
        guess = normalize_guess(input("Guess a letter: "))
        if guess is None:
            print("Enter ONE letter (a-z)."); continue
        guessed, slices, hit = apply_guess(secret, guessed, guess, slices)
        print("Nice!" if hit else f"Sliced! Remaining: {slices}")
    if is_win(secret, guessed):
        print(f"You saved it! The word was {secret}")
    else:
        print(f"Game over. The word was {secret}")
def main():
    while True:
        play_once()
        if input("Play again? (y/n): ").lower() != "y":
            break
if __name__ == "__main__":
    main()