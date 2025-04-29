# Monte Carlo Simulator

Python Package for Montecarlo Simulation

## Metadata

- **Project Name:** Monte Carlo Simulator
- **Author:** Francis Mangala  

---

## Synopsis

This Monte Carlo package simulates rolling dice, playing a dice-based game, and analyzing the outcomes .

### Installation

bash
pip install -e .

# API Description
---
```
Class: Die
Represents a single die with customizable sides and weights.

  Attributes:
    sides (np.ndarray): Array of unique face values.

    dice_df (pd.DataFrame): DataFrame storing sides and their corresponding weights.

  Public Methods:
    __init__(sides: np.ndarray, weights: list = None)

    Create a Die object with sides and optional weights.

  Parameters:

    sides (np.ndarray): Array of unique sides.

    weights (list, optional): List of positive weights. Defaults to 1.0 for each side.

    Raises: TypeError, ValueError

    weight_change(side: str, new_weight: float)

    Change the weight of a specified side.

    Parameters:

    side (str): The side whose weight to change.

    new_weight (float): New weight value (must be positive).

    Raises: IndexError, ValueError

    roll(nrolls: int = 1) -> list

    Roll the die nrolls times according to side probabilities.

  Parameters:

    nrolls (int): Number of rolls. Default is 1.

    Returns: list of outcomes.

    show_die() -> pd.DataFrame

    Show current sides and their weights.

    Returns: DataFrame showing sides and corresponding weights.
```
---
```
Class: Game
Simulates playing a game by rolling multiple dice.

  Attributes:
    dice (list of Die): List of Die objects participating in the game.

    results (pd.DataFrame): DataFrame containing roll outcomes.

    Public Methods:
    __init__(dice: list)

    Create a Game object with a list of Die objects.

    Parameters:

    dice (list): List of Die objects.

    Raises: TypeError

    play(nrolls: int)

    Roll all dice nrolls times and record the outcomes.

    Parameters:

    nrolls (int): Number of rolls.

    show_results(format: str = 'wide') -> pd.DataFrame

    Show results in 'wide' or 'narrow' format.

    Parameters:

    format (str): Either 'wide' or 'narrow'.

    Returns: DataFrame of results.

    Raises: ValueError
```
---
```
Class: Analyzer
Analyzes a completed game.

  Attributes:
    game (Game): Game object to analyze.

    results (pd.DataFrame): Results of the game in wide format.

Public Methods:
    __init__(game: Game)

Create an Analyzer object for a given Game.

    Parameters:

    game (Game): A Game object.

    Raises: TypeError

    jackpot() -> int

    Compute the number of jackpots (all dice match in a roll).

    Returns: Integer count of jackpots.

    counts_per_roll() -> pd.DataFrame

    Compute how many times each face appeared per roll.

    Returns: DataFrame with face counts per roll.

    combo_count() -> pd.DataFrame

    Count distinct combinations (sorted outcomes).

    Returns: DataFrame with combination counts.

    permutations() -> pd.DataFrame

    Count distinct permutations (ordered outcomes).

    Returns: DataFrame with permutation counts.
```
