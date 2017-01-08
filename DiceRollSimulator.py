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
import os

def check_if_reached_expected_distro(expected_distro, 
									actual_distro, 
									max_difference):
	difference = 0
	for i in range(11): 
		# Find the difference between what we expected to roll 
		# and what we actually rolled for each possible result
		difference = abs(expected_distro[i] - actual_distro[i])
		# If that difference is greater than preset maximum difference, 
		# we have reached the expected distribution. Return False
		if difference > max_difference:	
			return False
	return True # Reached expected distro. Return True.

def main():
	# Store the expected distribution of results in expectedDistribution. 
	# Each successive value corresponds to a possible result such that 
	# expectedDistribution[i] = the expected percentage of times result 
	# i+1 will appear.	
	expected_distibution = [.0277, .0555, .0833, .1111, .1388, .1666, 
							.1388, .1111, .0833, .0555, .0277]	
	# Store the actual distribution of results in actual_distribution. 
	# This is updated each time dice are rolled.		
	actual_distribution = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	# actual_results stores cumulative number of times each result appears: 
	actual_results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	num_rolls = 0 # Total number of rolls across entire program execution. 	
	# Indicates whether actual results equal expected results within
	# maximum boundary of difference. 								
	reached_expected_distribution = False;													 	
	die_1_result = 0 							  	 																
	die_2_result = 0 								  																 
	result = 0 # Sum of both rolls 																			
	# Parse command line arguments: 
	if len(sys.argv) == 1: # Case 1: No arguments provided. Set default values.
		max_difference = .1 
	elif len(sys.argv) > 2: # Case 2: Too many arguments provided.
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
	while reached_expected_distribution == False:
		num_rolls += 1
		die_1_result = random.randint(1, 6) # Roll the first dice
		die_2_result = random.randint(1, 6) # Roll the second dice
		result = die_1_result + die_2_result  # Add die rolls to get result
		actual_results[result-2] += 1 	  # Add this result to tally of results
		# Update the distribution of actual results to reflect this die roll:
		actual_distribution[result-2] = actual_results[result-2]/num_rolls 
		reached_expected_distribution = check_if_reached_expected_distro(expected_distibution, 
																		 actual_distribution, 
																		 max_difference)
	# Output result into file:
	try:
		with open("results.txt", "a") as output_file:
			output_file.write(str(num_rolls))
			output_file.write("\n")
	except IOError:
		print("Cannot open output file to print result. Will print to standard", 
				"output. \n Total number of rolls:", num_rolls)	

if __name__ == "__main__": main()







