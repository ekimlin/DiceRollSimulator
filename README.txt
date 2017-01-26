This program determines number of times a person would have to roll 2 dice to get expected
distribution of results. In other words, given the probability of each possible
result:
	Result 			Probability 		Expected distribution of results (%)
	2 			1/36				2.7777
	3 			2/36				5.5555
	4			3/36				8.3333
 	5			4/36				11.111
	6			5/36				13.888	
	7			6/36				16.6666
	8			5/36				13.888
	9			4/36				11.111
	10			3/36				8.3333
	11			2/36				5.5555
	12			1/36				2.7777

How many times do we have to roll the dice to see the results we expect?

NOTES: A Dice roll is simulated using the pseudo-random number generator command in python: random.randomint, 
	which uses the Mersenne Twister as its underlying generator. 

HOW TO RUN: 
	python3 DiceRollSimulator.py [-d max_difference] [-i num_iterations]




