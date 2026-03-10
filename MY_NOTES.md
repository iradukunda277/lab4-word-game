# My Original Thinking

## States of a Hangman-like game
- **Setup**: choose the secret word, reset variables, and prepare the game
- **Playing**: player enters guesses and the game updates the display
- **Won**: player reveals the whole word before running out of attempts
- **Lost**: player runs out of attempts before guessing the word
- **Quit/Exit (optional)**: player chooses to stop the game

## Variables required
- **secret_word**: the hidden word to guess
- **guessed_letters**: letters already guessed by the player
- **wrong_guesses**: number of incorrect guesses
- **max_wrong_guesses**: maximum wrong attempts allowed
- **display_word / masked_word**: what the player currently sees
- **remaining_attempts**: attempts left before losing
- **input_guess**: the current user input
- **game_state**: current state of the game

## Rules and invariants
- **Rules**:
  - The player guesses one letter at a time
  - Correct guesses reveal letters in the word
  - Wrong guesses reduce remaining attempts
  - The game ends when the word is guessed or attempts run out
- **Invariants (must always be true)**:
  - `secret_word` never changes during a round
  - `guessed_letters` contains unique letters
  - `remaining_attempts = max_wrong_guesses - wrong_guesses`
  - `masked_word` matches `secret_word` length

## Bugs / edge cases to be careful about
- Repeated guesses
- Upper/lowercase handling
- Non-letter input (numbers, symbols, empty input)
- Guessing more than 1 character
- Words with hyphen/space (if allowed)
- End condition: win/loss detected correctly
- Clearing state between rounds

# Copilot Suggestions

## App States
- **SETUP**: initialize the game, choose the secret word, reset variables and counters
- **PLAYING**: main game loop where the player enters guesses
- **WON**: all letters in the word have been guessed before attempts run out
- **LOST**: the player has no attempts left before guessing the word
- **QUIT**: player chooses to exit the game
- **INVALID_INPUT** (optional): temporary handling for bad input, then return to PLAYING

## App Variables
- **secret_word**: the word the player must guess
- **guessed_letters**: letters already guessed by the player
- **wrong_guesses**: number of incorrect guesses made
- **max_wrong_guesses**: maximum number of wrong guesses allowed
- **game_state**: current state of the game (SETUP, PLAYING, WON, LOST, QUIT)
- **remaining_attempts**: attempts left, calculated from `max_wrong_guesses - wrong_guesses`
- **masked_word / display_word**: the version of the word shown to the player
- **word_list** (optional): source of possible secret words

## App Rules and Invariants

### Rules
- The player guesses one letter at a time.
- If the guessed letter is in the secret word, reveal it in all matching positions.
- If the guessed letter is not in the secret word, increase `wrong_guesses` by 1.
- A letter should not be counted twice if it was already guessed.
- Input must be a single letter; empty input, numbers, spaces, or symbols are invalid.
- Uppercase and lowercase letters should be treated the same.
- The player wins when all letters in the secret word have been revealed.
- The player loses when `wrong_guesses` reaches `max_wrong_guesses`.

### Invariants
- `secret_word` does not change during one round.
- `guessed_letters` should contain unique letters only.
- `0 <= wrong_guesses <= max_wrong_guesses`
- `len(masked_word) == len(secret_word)`
- `remaining_attempts = max_wrong_guesses - wrong_guesses`
- If the game state is `WON`, then all letters of the word have been guessed.
- If the game state is `LOST`, then no attempts remain.

## App Bugs
- Repeated guesses being accepted and counted again
- Uppercase/lowercase mismatch causing correct letters not to match
- Accepting invalid input such as empty input, multiple letters, numbers, symbols, or extra spaces
- Masked word having the wrong length or not revealing letters correctly
- Wrong guesses not being counted correctly
- Correct guesses being penalized by mistake
- Win condition not triggering when all letters are guessed
- Loss condition not triggering when attempts reach the maximum
- Off-by-one errors in remaining attempts
- Game continuing after `WON` or `LOST`
- Restart not resetting all variables properly
- Empty word list or uninitialized `secret_word` causing startup errors

## Observations
- Copilot gave a clear core set of states and made the win/loss/end states explicit.
- It was slightly over-detailed because it also suggested optional states like `INVALID_INPUT` and discussed transitions, which are useful but not all necessary for a simple version.
- Copilot identified the core variables clearly and helped separate essential variables from optional ones.
- It was helpful because it explained that `guessed_letters` should ideally be a set and that `remaining_attempts` can be derived instead of stored separately.
- Copilot gave clear rules and useful invariants that can help avoid logic bugs later.
- It was a bit over-detailed because it added implementation examples and extra edge-case discussion, but the core rules were still helpful.
- Copilot gave many possible bugs and edge cases, which was useful for thinking about testing.
- It was slightly over-detailed because it included implementation-level examples, but the common bug list was still very helpful.