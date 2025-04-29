from Montecarlo_Simulator.montecarlo import Die, Game, Analyzer
import numpy as np

#SCENARIO 1

# #Task1
# #create a 2-headed coin (H=head, T=Tail)
# coin = np.array(['H','T'])

# #create a fair coin
# fair_coin =Die(sides=coin)
# #create unfair coing
# unfair_coin = Die(sides=coin)
# unfair_coin.weight_change('H',5)

# print(fair_coin.show_die())
# print(unfair_coin.show_die())

# #|------------------------------------------------------------|
# #Task 2

# #create 2 fair dice
# fair_dice1 =Die(coin)
# fair_dice2 =Die(coin)

# #create game
# Game1 = Game([fair_dice1,fair_dice2])
# Game1.play(1000)
# print(Game1.show_results('wide').head(10))

# #|------------------------------------------------------------|
#Task 3
#create 2 unfair dice and 1 fair dice
# unfair_dice = Die(coin)
# unfair_dice.weight_change('H',5)
# fair_dice = Die(coin)
# #create game and print results
# Game2 = Game([unfair_dice,unfair_dice,fair_dice])
# Game2.play(1000)
# print(Game2.show_results('wide').head(10))

# #|------------------------------------------------------------|
#Task 4
# #Analyzer dice_game
# Game1_analyzer = Analyzer(Game1)
# Game1_jackpot = Game1_analyzer.jackpot()
# #Raw frequency report
# print(f"Number of jackpots in Game Task 2 : {Game1_jackpot}")

# #Analyzer dice_game_2
# Game2_analyzer = Analyzer(Game2)
# Game2_jackpot = Game2_analyzer.jackpot()
# #Raw frequency report
# print(f"Number of jackpots in Game Task 3 : {Game2_jackpot}")

# #|-------------------------------------------------------------|
#Task 5

#number of rolls played by games
# nrolls = 1000

# #relative frequencies
# relative_freq_Game1 = Game1_jackpot / nrolls
# relative_freq_Game2 = Game2_jackpot / nrolls

# #|-------------------------------------------------------------|

# import matplotlib.pyplot as plt

# Games = ['Game1','Game2']
# relative_frequencies = [relative_freq_Game1,relative_freq_Game2]

# #create bar chart
# plt.bar(Games,relative_frequencies)
# plt.ylabel('Relative Frequency')
# plt.show()

#|---------------------------------------------------------------|
#SCENARIO 2
#Task 1

dice = np.array(['1','2','3','4','5','6'])

dice_1 = Die(dice)
dice_2 = Die(dice)
dice_3 = Die(dice)

#Task 2
dice_2.weight_change('6',5)

#Task 3
dice_3.weight_change('1',5)

#Task 4 

#create 5 fair dice

fair_dice_1 = Die(dice)
fair_dice_2 = Die(dice)
fair_dice_3 = Die(dice)
fair_dice_4 = Die(dice)
fair_dice_5 = Die(dice)

#set game
Game3 = Game([fair_dice_1,fair_dice_2,fair_dice_3,fair_dice_4,fair_dice_5])

#nrolls 10000
Game3.play(10000)
print(Game3.show_results('wide').head(10))

#Task 6

#create 2 unfair dice and 3 fair dice
fair_dice_1 = Die(dice)
unfair_dice_2 = Die(dice)
unffair_dice_3 = Die(dice)
fair_dice_4 = Die(dice)
fair_dice_5 = Die(dice)

unfair_dice_2.weight_change('6',5)
unffair_dice_3.weight_change('1',5)

#set game
Game4 = Game([fair_dice_1,unfair_dice_2,unffair_dice_3,fair_dice_4,fair_dice_5])

#nrolls 10000
Game4.play(10000)
print(Game4.show_results('wide').head(10))

#Task 6
#Analyzer dice_game

#Game3
Game3_analyzer = Analyzer(Game3)
Game3_jackpot = Game3_analyzer.jackpot()

#Game4
Game4_analyzer = Analyzer(Game4)
Game4_jackpot = Game4_analyzer.jackpot()

#Relative Fequencies

#number of rolls played by games
nrolls = 10000

#relative frequencies
relative_freq_Game3 = Game3_jackpot / nrolls
relative_freq_Game4 = Game4_jackpot / nrolls

#Chart
import matplotlib.pyplot as plt

Dice_Games = ['Game3','Game4']
relative_frequencies = [relative_freq_Game3,relative_freq_Game4]

#create bar chart
plt.bar(Dice_Games,relative_frequencies)
plt.ylabel('Relative Frequency')
plt.show()