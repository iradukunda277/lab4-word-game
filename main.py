import random


def update_game_state(
    secret_word: str, guessed_letters: list[str], guess: str, lives: int
) -> tuple[list[str], int]:
    """
    Update the guessed letters and remaining lives after one player guess.

    Args:
        secret_word: Word to guess.
        guessed_letters: Letters already guessed in the current round.
        guess: The player's guessed letter.
        lives: Remaining incorrect attempts.

    Returns:
        A tuple containing the updated guessed letters and updated lives.

    Note:
        This function assumes the input guess has already been validated.
    """
    normalized_guess = guess.lower()

    if normalized_guess in guessed_letters:
        return guessed_letters.copy(), lives

    new_guessed_letters = guessed_letters + [normalized_guess]

    if normalized_guess in secret_word.lower():
        return new_guessed_letters, lives

    return new_guessed_letters, lives - 1

    


def get_masked_word(secret_word: str, guessed_letters: list[str]) -> str:
    masked_characters = []

    for letter in secret_word.lower():
        if letter in guessed_letters:
            masked_characters.append(letter)
        else:
            masked_characters.append("_")

    return " ".join(masked_characters)


def has_won(secret_word: str, guessed_letters: list[str]) -> bool:
    for letter in secret_word.lower():
        if letter not in guessed_letters:
            return False
    return True


def is_valid_guess(guess: str, guessed_letters: list[str]) -> bool:
    normalized_guess = guess.lower().strip()

    if len(normalized_guess) != 1:
        return False
    if not normalized_guess.isalpha():
        return False
    if normalized_guess in guessed_letters:
        return False

    return True


def choose_secret_word(word_list: list[str]) -> str:
    return random.choice(word_list).lower()


def show_game_status(masked_word: str, guessed_letters: list[str], lives: int) -> None:
    print("\nWord:", masked_word)
    print("Guessed letters:", " ".join(guessed_letters) if guessed_letters else "None")
    print("Lives left:", lives)


def prompt_guess() -> str:
    return input("Enter a letter: ").strip()


def show_result(won: bool, secret_word: str) -> None:
    if won:
        print(f"\nYou won! The word was '{secret_word}'.")
    else:
        print(f"\nYou lost! The word was '{secret_word}'.")


def play_round(word_list: list[str], max_lives: int) -> None:
    secret_word = choose_secret_word(word_list)
    guessed_letters: list[str] = []
    lives = max_lives
    game_state = "PLAYING"

    while game_state == "PLAYING":
        masked_word = get_masked_word(secret_word, guessed_letters)
        show_game_status(masked_word, guessed_letters, lives)

        guess = prompt_guess()

        if not is_valid_guess(guess, guessed_letters):
            print("Invalid guess. Enter one new letter only.")
            continue

        guessed_letters, lives = update_game_state(
            secret_word, guessed_letters, guess, lives
        )

        if has_won(secret_word, guessed_letters):
            game_state = "WON"
        elif lives <= 0:
            game_state = "LOST"

    show_result(game_state == "WON", secret_word)


def play_auto_round(word_list: list[str], max_lives: int) -> None:
    secret_word = choose_secret_word(word_list)
    guessed_letters: list[str] = []
    lives = max_lives
    game_state = "PLAYING"

    while game_state == "PLAYING":
        masked_word = get_masked_word(secret_word, guessed_letters)
        show_game_status(masked_word, guessed_letters, lives)

        guess = get_auto_guess(guessed_letters)

        if guess == "":
            print("No more available letters.")
            game_state = "LOST"
            continue

        print("Auto guess:", guess)

        guessed_letters, lives = update_game_state(
            secret_word, guessed_letters, guess, lives
        )

        if has_won(secret_word, guessed_letters):
            game_state = "WON"
        elif lives <= 0:
            game_state = "LOST"

    show_result(game_state == "WON", secret_word)


def ask_play_again() -> bool:
    answer = input("Play again? (y/n): ").strip().lower()
    return answer == "y"


def main() -> None:
    word_list = ["apple", "banana", "python", "school", "planet"]
    max_lives = 6
    play_again = True

    while play_again:
        mode = choose_game_mode()

        if mode == "MANUAL":
            play_round(word_list, max_lives)
        elif mode == "AUTO":
            play_auto_round(word_list, max_lives)
        else:
            print("Invalid mode. Please choose 1 or 2.")
            continue

        play_again = ask_play_again()

    print("Thanks for playing!")



def choose_game_mode() -> str:
    mode = input("Choose mode: (1) Manual  (2) Auto : ").strip()

    if mode == "1":
        return "MANUAL"
    if mode == "2":
        return "AUTO"

    return "INVALID"



def get_auto_guess(guessed_letters: list[str]) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        if letter not in guessed_letters:
            return letter

    return ""

if __name__ == "__main__":
    main()

