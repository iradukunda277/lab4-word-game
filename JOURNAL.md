# This JOURNAL.md file gets automatically updated by the journal-logger agent after every interaction with CoPilot. It serves as a comprehensive log of all prompts, responses, changes made, and reflections during the development process. Each entry is formatted consistently for easy reading and is listed in reverse chronological order, with the most recent interactions at the top.

---

### **New Interaction**
- **Agent Version**: 2.1
- **Date**: 03-16-2026 11:31
- **User**: jean-remy.iradukunda@epita.fr
- **Prompt**: read copilot instructions and activate the journal logger agent
- **CoPilot Mode**: Agent
- **CoPilot Model**: Grok Code Fast 1
- **Socratic Mode**: ON
- **Changes Made**: None
- **Context and Reasons for Changes**: User requested to read copilot instructions and activate the journal logger agent for logging interactions.

### **New Interaction**
- **Date**: 03-10-2026 21:07
- **User**: jean-remy.iradukunda@epita.fr
- **Prompt**: Update the journal with the latest work: the full playable word game now runs correctly, replay works, repeated guesses are handled, README.md was updated, and REPORT.md was completed.
- **CoPilot Mode**: Ask
- **CoPilot Model**: Grok Code Fast 1
- **Changes Made**: None - this is a journal update request.
- **Context and Reasons for Changes**: User reporting successful completion of the full word game implementation. All core features now working: playable game, replay functionality, repeated guess handling, updated documentation (README.md), and completed lab report (REPORT.md).
- **My Observations**: Project milestone achieved - full Hangman-like word game is now functional with proper error handling and user experience features.

## New Interaction

**Date**: 03-10-2026 15:15

**User**: jean-remy.iradukunda@epita.fr

**Prompt**: Update documentation and testing deliverables for word game project

**CoPilot Mode**: Plan

**CoPilot Model**: Claude Haiku 4.5

**Changes Made**: 
- test_update_game_state.py: Ran all tests successfully (all passed)
  - Tests cover: correct guess adds letter with kept lives
  - Tests cover: wrong guess adds letter with decremented lives
  - Tests cover: repeated guess prevents duplication
  - Tests cover: guessed_letters input is not mutated
  - Tests cover: uppercase guess is normalized to lowercase
- README.md: Created/updated with project documentation
  - Added short project description
  - Added instructions to run the game
  - Added instructions to run the tests
- REPORT.md: In progress for lab reflection/testing section
  - Test implementation complete
  - README updates complete
  - REPORT.md reflection section in progress

**Context and Reasons for Changes**: Completed test suite validation ensuring update_game_state function works correctly across core cases and edge cases (normalization). Documented project setup and usage for clarity. Preparing lab report documenting testing strategy and findings.

**My Observations**: Test coverage now includes the edge case (uppercase normalization) from earlier code review discussion. All tests passing indicates function implements designed behavior correctly.

## New Interaction

**Date**: 03-10-2026 13:44

**User**: jean-remy.iradukunda@epita.fr

**Prompt**: review tests for update_game_state and suggest missing edge cases

**CoPilot Mode**: Ask

**CoPilot Model**: Grok Code Fast 1

**Changes Made**: No code changes made.

**Context and Reasons for Changes**: User testing their update_game_state function implementation; provided comprehensive edge case suggestions to improve test coverage.

**My Observations**: 

## New Interaction

**Date**: 03-10-2026 13:27

**User**: jean-remy.iradukunda@epita.fr

**Prompt**: Log this interaction: User asked to review tests for update_game_state and suggest missing edge cases. I reviewed the test file, identified covered cases, and suggested additional edge case tests. Mode: Ask. No code changes made.

**CoPilot Mode**: Ask

**CoPilot Model**: Grok Code Fast 1

**Changes Made**: No code changes made.

**Context and Reasons for Changes**: User asked to review tests for update_game_state and suggest missing edge cases. I reviewed the test file, identified covered cases, and suggested additional edge case tests.

**My Observations**: 

## New Interaction

**Date**: 03-10-2026 14:45

**User**: jean-remy.iradukunda@epita.fr

**Prompt**: Update the journal with the recent interactions

**CoPilot Mode**: Ask

**CoPilot Model**: Claude Haiku 4.5

**Changes Made**: Prepended 5 new interaction entries to JOURNAL.md for 03-10-2026

**Context and Reasons for Changes**: Following up after comprehensive design discussions about Hangman game implementation. User requested journal update to log all interactions from design phase.

**My Observations**: 

## New Interaction

**Date**: 03-10-2026 14:30

**User**: jean-remy.iradukunda@epita.fr

**Prompt**: What are possible bugs in Word Guess / Hangman implementations?

**CoPilot Mode**: Ask

**CoPilot Model**: Claude Haiku 4.5

**Changes Made**: None

**Context and Reasons for Changes**: Part of design thinking phase; user consulting on edge cases and common pitfalls. Provided comprehensive bug taxonomy organized by category (input validation, display, logic, state machine, data structures, initialization, and flow).

**My Observations**: 

## New Interaction

**Date**: 03-10-2026 14:15

**User**: jean-remy.iradukunda@epita.fr

**Prompt**: What are the rules and invariants?

**CoPilot Mode**: Ask

**CoPilot Model**: Claude Haiku 4.5

**Changes Made**: None

**Context and Reasons for Changes**: User filling out MY_NOTES.md section on rules and invariants. Provided detailed breakdown of game mechanics rules and invariant conditions that must always hold true.

**My Observations**: 

## New Interaction

**Date**: 03-10-2026 14:00

**User**: jean-remy.iradukunda@epita.fr

**Prompt**: What variables should I keep track of?

**CoPilot Mode**: Ask

**CoPilot Model**: Claude Haiku 4.5

**Changes Made**: None

**Context and Reasons for Changes**: User designing data structures for Hangman game; building on initial state design. Provided variable taxonomy with essential vs derived variables; explained why to use set for guessed_letters.

**My Observations**: 

## New Interaction

**Date**: 03-10-2026 13:45

**User**: jean-remy.iradukunda@epita.fr

**Prompt**: What states does a Word Game like Hangman game need?

**CoPilot Mode**: Ask

**CoPilot Model**: Claude Haiku 4.5

**Changes Made**: None

**Context and Reasons for Changes**: Start of session; user working through design thinking for Hangman-like word game. User had already identified core states; provided additional perspective on state transitions and between-round handling.

**My Observations**: 

---

## New Interaction

**Date**: 03-09-2026 14:42

**User**: jean-remy.iradukunda@epita.fr

**Prompt**: read the #copilot-instructions and activate the #journal-logger agent

**CoPilot Mode**: Ask

**CoPilot Model**: Grok Code Fast 1

**Changes Made**: None.

**Context and Reasons for Changes**: This is a repeated request. The instructions were already read and the agent activated in the previous interaction.

**My Observations**: 

## New Interaction

**Date**: 03-09-2026 14:30

**User**: jean-remy.iradukunda@epita.fr

**Prompt**: read the #copilot-instructions and activate the #journal-logger agent

**CoPilot Mode**: Ask

**CoPilot Model**: Grok Code Fast 1

**Changes Made**: Read the copilot-instructions.md file and activated the journal-logger agent.

**Context and Reasons for Changes**: As per the instructions in copilot-instructions.md, the journal-logger agent must be run after every user interaction to maintain a log in JOURNAL.md.

**My Observations**: 

## New Interaction

**Date**: 03-07-2026 14:38

**User**: jean-remy.iradukunda@epita.fr

**Prompt**: "Implement a recursive Fibonacci function in main.py"

**CoPilot Mode**: Ask

**CoPilot Model**: Claude Haiku 4.5

**Changes Made**: 
- Created fibonacci() function with recursion
- Added docstring with args, returns, and raises documentation
- Added input validation for negative numbers
- Added test code in if __name__ == "__main__" block
- Tested function with values 0-10, all correct

**Reasons for Changes**: 
- Implemented classic recursive Fibonacci algorithm
- Added proper error handling for edge cases
- Included comprehensive docstring for clarity
- Added test cases to demonstrate functionality
- Followed Python best practices with main guard

**Context**: 
- Function handles base cases (n=0, n=1) and recursive case
- Tested output confirms correct Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
- Implementation is educational and demonstrates recursive programming concepts

**My Observations**: [Empty - to be filled by user as needed]

## New Interaction

**Date**: 03-07-2026 14:32 (Initial Setup)

**User**: jean-remy.iradukunda@epita.fr

**Prompt**: "Read the ai4se.instructions.md file and follow its directive. Activate the journal agent in journal-logger.agent.md"

**CoPilot Mode**: Ask

**CoPilot Model**: Claude Haiku 4.5

**Changes Made**: 
- Read ai4se.instructions.md (provided in attachment)
- Read journal-logger.agent.md to understand journal requirements
- Activated journal-logger agent in journal-logger mode
- Created initial journal entry to establish logging workflow

**Reasons for Changes**: 
- Following the journaling requirement from ai4se.instructions.md which mandates: "Read and follow .github/agents/journal-logger.agent.md. Log every prompt interaction in JOURNAL.md using the required format and reverse-chronological order."
- Establishing proper audit trail for all interactions and changes to the codebase

**Context**: 
- Initial setup to establish journal logging for c:\AI4SE\lab4-word-game workspace
- ai4se.instructions.md emphasizes tutor mode, incremental implementation policy, and question-led learning approach
- Journal entries must maintain reverse-chronological order with most recent entries at top
- User identified from git config: jean-remy.iradukunda@epita.fr

**My Observations**: [Empty - to be filled by user as needed]

