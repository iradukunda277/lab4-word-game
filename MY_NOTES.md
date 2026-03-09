# My Original Thinking

## States of a Hangman-like game
- Setup:
- Playing:
- Won:
- Lost:
- Quit/Exit (optional):

## Variables required
- secret_word:
- guessed_letters:
- wrong_guesses:
- max_wrong_guesses:
- display_word / masked_word:
- remaining_attempts:
- input_guess:
- game_state:

## Rules and invariants
- Rules:
- Invariants (must always be true):
  - secret_word never changes during a round
  - guessed_letters contains unique letters
  - remaining_attempts = max_wrong_guesses - wrong_guesses
  - masked_word matches secret_word length

## Bugs / edge cases to be careful about
- Repeated guesses
- Upper/lowercase handling
- Non-letter input (numbers, symbols, empty input)
- Guessing more than 1 character
- Words with hyphen/space (if allowed)
- End condition: win/loss detected correctly
- Clearing state between rounds

# CoPilot Suggestions
(To be filled after you ask Copilot for suggestions)