This program determines number of times a person would have to roll 2 dice to get expected
distribution of results. In other words, given the probability of each possible
result:
					Result 		Probability 	Expected distribution of results (%)
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
	FindAverage results.txt

INTERPRETING OUTPUT:
	Say the following is run: 
		python3 DiceRollSimulator.py -1 1000
		FindAverage results.txt	
	And the output on stdout is "Average = 59"

	This means that on average, you need to roll 59 times in order to achieve a difference of 10%
	between expected and actual results for each possible result. For example, if you roll 59 times, 
	you would expect about 8.3% of the rolls to sum to 10 (around 5 tens). However your actual results 
	will differ by 10%, meaning that you could actually see between 0 and 10 tens. 

	The lower your maximum difference between actual and expected results, the higher number of average 
	rolls you will need. 





