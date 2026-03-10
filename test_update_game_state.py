from main import update_game_state


def test_correct_guess_adds_letter_and_keeps_lives() -> None:
    guessed_letters = []
    new_letters, new_lives = update_game_state("apple", guessed_letters, "a", 6)

    assert new_letters == ["a"]
    assert new_lives == 6


def test_wrong_guess_adds_letter_and_decreases_lives() -> None:
    guessed_letters = ["a"]
    new_letters, new_lives = update_game_state("apple", guessed_letters, "z", 6)

    assert new_letters == ["a", "z"]
    assert new_lives == 5


def test_repeated_guess_does_not_duplicate_letter() -> None:
    guessed_letters = ["a"]
    new_letters, new_lives = update_game_state("apple", guessed_letters, "a", 6)

    assert new_letters == ["a"]
    assert new_lives == 6


def test_original_guessed_letters_is_not_mutated() -> None:
    guessed_letters = ["a"]
    _new_letters, _new_lives = update_game_state("apple", guessed_letters, "z", 6)

    assert guessed_letters == ["a"]


def run_all_tests() -> None:
    test_correct_guess_adds_letter_and_keeps_lives()
    test_wrong_guess_adds_letter_and_decreases_lives()
    test_repeated_guess_does_not_duplicate_letter()
    test_original_guessed_letters_is_not_mutated()
    print("All tests passed.")


if __name__ == "__main__":
    run_all_tests()


def test_uppercase_guess_is_normalized() -> None:
    guessed_letters = []
    new_letters, new_lives = update_game_state("apple", guessed_letters, "A", 6)

    assert new_letters == ["a"]
    assert new_lives == 6


def test_mixed_case_secret_word_still_works() -> None:
    guessed_letters = []
    new_letters, new_lives = update_game_state("Apple", guessed_letters, "a", 6)

    assert new_letters == ["a"]
    assert new_lives == 6
