import pandas as pd
import numpy as np

class Die :
    """
    A Die class representing a die with customizable sides and weights.
    """
    def __init__(self,sides,weights=None):

        """
        Initialize a Die.

        Args:
            sides (np.ndarray): A NumPy array of unique face values.
            weights (list, optional): A list of weights corresponding to each side.
                Defaults to equal weights of 1.0 for each side.

        Raises:
            TypeError: If sides is not a NumPy array.
            ValueError: If sides are not unique or if sides and weights lengths mismatch.
        """

        """
        Takes a NumPy array of faces as an argument. Throws a TypeError if not a NumPy array
        """
        if not isinstance(sides, np.ndarray):
            raise TypeError("Sides must be a NumPy array.")
        """
        Ensure all face values are unique
        """
        if len(np.unique(sides)) != len(sides):
            raise ValueError("All face values must be unique.")   

        self.sides= sides
        """
        Initializes the weight to 1.0 for each face
        """
        self.weights = weights if weights is not None else[1.0]* len(sides)
        if len(self.weights) != len(self.sides):
            raise ValueError("Weights and sides must be the same length.")
        #Initialize DataFrame
        self.dice_df = pd.DataFrame({'weight': self.weights}, index=self.sides) 
    
#|-------------------------------------------------------------------------------------------|
    def weight_change(self,sides,new_weight):
        """
        Change the weight of a specific side.

        Args:
        sides (str): The side whose weight is to be changed.
        new_weight (int or float): The new weight for the side.

        Raises:
        IndexError: If the side is not found.
        TypeError: If the new weight is not a positive number.
        """
        #to check if sides is a valid value
        if sides not in self.dice_df.index:
            raise IndexError("Side not valid.")
        #to check if weigh is a valid type
        if not isinstance(new_weight,(int,float)) or new_weight < 0:
            raise TypeError("Weight must be numeric")
        self.dice_df.at[sides,'weight'] = new_weight
#|-------------------------------------------------------------------------------------------|
    def roll(self,nrolls=1):
        """
        to roll the die N times and return an outcome
        """
        if not isinstance(nrolls, int) or nrolls < 1:
            raise ValueError("Number of rolls must be a positive integer.")
        
        sides = self.dice_df.index.to_list()
        weights = np.array(self.dice_df['weight'])
        probability = weights/weights.sum()
        return list(np.random.choice(sides, size=nrolls, p=probability))
#|-------------------------------------------------------------------------------------------| 
    def show_die(self):
        return self.dice_df.copy()
#|-------------------------------------------------------------------------------------------|

class Game:
    """
    A Game class to simulate rolling multiple dice.
    """

    def __init__(self, dice):
        """
        Initialize a Game with a list of dice.

        Args:
        dice (list): List of Die objects.
        """

        self.dice = dice  # List of Die objects
        self.results = pd.DataFrame()
#|-------------------------------------------------------------------------------------------|
    def play(self, nrolls):
        """
        Rolling all dice N times.
        """
        rolls = []
        for i, die in enumerate(self.dice):
            roll_result = pd.DataFrame(die.roll(nrolls), columns=[f'Die {i+1}'])
            rolls.append(roll_result)

        self.results = pd.concat(rolls, axis=1)
        self.results.index = pd.RangeIndex(start=1, stop=nrolls + 1, name="Roll Number")
        self.results.columns.name = "Die Number" 
#|-------------------------------------------------------------------------------------------|
    def show_results(self, format='wide'):
  
        """
        Show results of the play in 'wide' or 'narrow' format.
        """
    
        if self.results.empty:
            raise ValueError("No results to show. Please run play() first.")

        if format == 'wide':
            return self.results.copy()

        elif format == 'narrow':
            narrow_df = self.results.stack()
            narrow_df.name = "Outcome"  # Set the name directly
            narrow_df = narrow_df.reset_index()  # Now columns will be Roll Number, Die Number, Outcome
            return narrow_df

        else:
            raise ValueError("Invalid format. Choose 'wide' or 'narrow'.")

#|-------------------------------------------------------------------------------------------|       
# Assuming Die class has a roll(n) method returning a list of face outcomes
class Analyzer:
    """
    An Analyzer class to analyze the results of a Game.
    """
    def __init__(self, game):

        """
        Initialize an Analyzer with a Game object.

        Args:
            game (Game): A completed Game object.

        Raises:
            ValueError: If the input is not a Game instance.
        """
        if not isinstance(game, Game):
            raise ValueError("Input must be a Game object.")
        
        self.game = game
        self.results = game.show_results('wide')  # Ensure we always work in wide format
#|-------------------------------------------------------------------------------------------|
      
    def jackpot(self):
        """
        Number of jackpots (all dice showing the same face in a roll)
        """ 
        return int((self.results.nunique(axis=1) == 1).sum())

#|-------------------------------------------------------------------------------------------|
    def counts_per_roll(self):
        """
        Computes how many times a given face is rolled
        """        
        unique_faces = np.unique(self.results.values)
        side_count = self.results.apply(lambda row: pd.Series({face: (row == face).sum() for face in unique_faces}), axis=1)
        side_count.index = self.results.index
        return side_count
#|-------------------------------------------------------------------------------------------|
    def combo_count(self):
        """
        Computes distinct combinations of faces rolled
        """
        combinations = self.results.apply(lambda row: tuple(sorted(row)), axis=1)
        counts = combinations.value_counts().rename_axis(["Combination"]).to_frame('Count')
        return counts
#|-------------------------------------------------------------------------------------------|

    def permutations(self):
        """
        Calculate the frequency of each permutation of rolled faces
        """
        permutations = self.results.apply(lambda row: tuple(row), axis=1)
        counts = permutations.value_counts().to_frame('Count')
        return counts

#||-----------------------------------------------------------------------------------------||

