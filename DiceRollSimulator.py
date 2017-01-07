"""
Author: 		Emma Kimlin
Date:   		6 January 2017
Title: 			DiceRollSimulator
Purpose: 		Determines number of times a person would have to roll 2 dice to get expected
				distribution of results. Appends this number into text file (results.txt). 
Run: 			python3 DiceRollSimulator.py [max_difference]
					max_difference: allowable error between actual result and expected result 
						for reach possible result 2-12 (positive int or double)
"""
import random
import sys

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
	expectedDistibution = [.0277, .0555, .0833, .1111, .1388, .1666, .1388, .1111, .0833, .0555, .0277]	# Store the 
									# expected distribution of results in expectedDistribution. Each successive value 
									# corresponds to a possible result such that expectedDistribution[i] = the expected 
									# percentage of times result i+1 will appear.			
	actualDistribution = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # Store the actual distribution of resuts. 
	actualResults = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Store cumulative number of times each result appears. 
													  # Initialize total to zero. 
	num_rolls = 0 									  # Total number of rolls across entire program execution. 									
	reachedExpectedDistribution = False;			  # Indicates whether actual results equal expected results within
												  	  # maximum boundary of difference. 													 
	
	die1Result = 0 									  # Store result of first die roll 																
	die2Result = 0 									  # Store result of second die roll 																 
	result = 0	   									  # Total of both rolls 																			
	# Parse command line arguments: 
	if len(sys.argv) == 1: # Case 1: No arguments provided. Set default values.
		max_difference = .1 
	elif len(sys.argv) > 2: # Case 2: Too many arguments provided. Output error and exit. 
		print("Usage: python3 DiceRollSimulator.py [max_difference]")
		exit(0)
	else: # Case 3: User provided one argument
		try: # Try to convert argument to integer and store in max_difference
			max_difference = float(sys.argv[1])
			if max_difference < 0: # max_difference can't be negative
				print("max_difference cannot be negative")
				exit(0)
		except ValueError: # User did not enter an double as argument. 
			print("max_difference must be a number.")
			exit(0)
	# Roll die:
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







