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


if __name__ == "__main__":
    pass