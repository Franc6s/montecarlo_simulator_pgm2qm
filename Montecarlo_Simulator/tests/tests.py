import unittest
import numpy as np
import pandas as pd
from montecarlo import Die, Game, Analyzer   

class TestDie(unittest.TestCase):

    def setUp(self):
        self.faces = np.array(['A', 'B', 'C'])
        self.die = Die(self.faces)

    def test_init(self):
        self.assertIsInstance(self.die.dice_df, pd.DataFrame)
        self.assertListEqual(list(self.die.dice_df.index), list(self.faces))

    def test_weight_change(self):
        self.die.weight_change('A', 2.0)
        self.assertEqual(self.die.dice_df.loc['A', 'weight'], 2.0)

    def test_roll(self):
        rolls = self.die.roll(5)
        self.assertIsInstance(rolls, list)
        self.assertEqual(len(rolls), 5)
        self.assertTrue(all(roll in self.faces for roll in rolls))

    def test_show_die(self):
        df = self.die.show_die()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue('weight' in df.columns)


class TestGame(unittest.TestCase):

    def setUp(self):
        die1 = Die(np.array(['1', '2', '3']))
        die2 = Die(np.array(['A', 'B', 'C']))
        self.game = Game([die1, die2])

    def test_play(self):
        self.game.play(5)
        self.assertIsInstance(self.game.results, pd.DataFrame)
        self.assertEqual(self.game.results.shape, (5, 2))  # 5 rolls, 2 dice

    def test_show_results_wide(self):
        self.game.play(3)
        wide_result = self.game.show_results('wide')
        self.assertIsInstance(wide_result, pd.DataFrame)
        self.assertEqual(wide_result.shape, (3, 2))

    def test_show_results_narrow(self):
        self.game.play(3)
        narrow_result = self.game.show_results('narrow')
        self.assertIsInstance(narrow_result, pd.DataFrame)
        self.assertTrue(set(narrow_result.columns) >= {"Roll Number", "Die Number", "Outcome"})


class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        die1 = Die(np.array(['1', '2', '3']))
        die2 = Die(np.array(['A', 'B', 'C']))
        self.game = Game([die1, die2])
        self.game.play(10)
        self.analyzer = Analyzer(self.game)

    def test_jackpot(self):
        jackpots = self.analyzer.jackpot()
        self.assertTrue(isinstance(jackpots, (int, np.integer)))
        self.assertGreaterEqual(jackpots, 0)

    def test_counts_per_roll(self):
        counts = self.analyzer.counts_per_roll()
        self.assertIsInstance(counts, pd.DataFrame)
        self.assertEqual(counts.shape[0], self.analyzer.results.shape[0])

    def test_combo_count(self):
        combo = self.analyzer.combo_count()
        self.assertIsInstance(combo, pd.DataFrame)
        self.assertIn('Count', combo.columns)

    def test_permutations(self):
        perms = self.analyzer.permutations()
        self.assertIsInstance(perms, pd.DataFrame)
        self.assertIn('Count', perms.columns)


if __name__ == '__main__':
    unittest.main()
