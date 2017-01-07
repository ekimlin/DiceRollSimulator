"""
Author: 		Emma Kimlin
Date:   		6 January 2017
Title: 			DiceRollSimulator
Purpose: 		Determines number of times a person would have to roll 2 dice to get expected
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

"""
import random

def checkIfReachedExpectedDistro(expectedDistro, actualDistro, max_difference):
	difference = 0
	for i in range(11): 
		difference = abs(expectedDistro[i] - actualDistro[i]) # Find the difference between what we expected to roll 
															  # and what we actually rolled for each possible result
		if difference > max_difference:	# If that difference is greater than preset maximum difference, we have not 
										# reached the expected distribution. Return False
			return False
	return True # Reached expected distro. Return True.

def main():
	# Store the expected distribution of results in expectedDistribution. Each successive value 
	# corresponds to a possible result such that expectedDistribution[i] = the expected percentage 
	# of times result i+1 will appear.
	expectedDistibution = [.0277, .0555, .0833, .1111, .1388, .1666, .1388, .1111, .0833, .0555, .0277]
			
	actualDistribution = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # Store the actual distribution of resuts. 
	actualResults = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Store cumulative number of times each result appears. 
													  # Initialize total to zero. 
	num_rolls = 0 									  # Total number of rolls across entire program execution. 									
	max_difference = .1							  # Maxmimum difference the actual result and expected result 
													  # for each possible result.
	reachedExpectedDistribution = False;			  # Indicates whether actual results equal expected results within
												  	  # maximum boundary of difference. 													 
	# min_num_rolls = 11 Minimum number of times to roll before checking whether results match expected results.	
	die1Result = 0 									  # Store result of first die roll 																
	die2Result = 0 									  # Store result of second die roll 																 
	result = 0	   									  # Total of both rolls 																			

	while reachedExpectedDistribution == False:
		num_rolls += 1
		die1Result = random.randint(1, 6) # Roll the first dice
		die2Result = random.randint(1, 6) # Roll the second dice
		result = die1Result + die2Result  # Add die rolls to get result
		actualResults[result-2] += 1 	  # Add this result to tally of results
		actualDistribution[result-2] = actualResults[result-2]/num_rolls # Update the distribution of actual results to reflect
										  								 # this die roll.
		reachedExpectedDistribution = checkIfReachedExpectedDistro(expectedDistibution, actualDistribution, max_difference)

	print ("Number of rolls needed to reach expected distribution of results:", num_rolls)

if __name__ == "__main__": main()







