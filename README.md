# prac
Leetcode spaced repetition tracker in the terminal using SM-2 algorithm

# Installation
1. Clone this repo
2. Install dependencies: `uv sync`
3. Run: `uv run prac --help`
TODO: Publish as package to pip/PyPi for easier installation and usage.

# Usage

## Add a problem
```bash
uv run prac add <url> <problem_number> [name]
```
- `url` (required): Problem URL
- `problem_number` (required): LeetCode problem number
- `name` (optional): Problem name

## Review problems
```bash
uv run prac review
```
Shows all problems due for review from today or earlier.

## Complete a review
```bash
uv run prac complete <problem_number> <quality>
```
- `problem_number` (required): LeetCode problem number
- `quality` (required): Quality score from 0-5
  - 0-2: Incorrect or struggled significantly
  - 3: Correct with difficulty
  - 4: Correct with some effort
  - 5: Easy and confident

Marks the problem as reviewed and calculates the next review date using the SM-2 algorithm.

# Credits
@alankan886 - Using his https://github.com/alankan886/SuperMemo2/ implementation of the SM-2 algorithm. Simple and easy to use.
