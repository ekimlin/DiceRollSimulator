"""
Author: 		Emma Kimlin
Date:   		6 January 2017
Title: 			DiceRollSimulator
Purpose: 		Determines number of times a person would have to roll 2 dice to get expected
				distribution of results. Appends this number into text file (results.txt). 
Usage: 			python3 DiceRollSimulator.py [-d max_difference] [-i num_iterations]
					max_difference: allowable error between actual result and expected result 
						for reach possible result 2-12 (positive int or double)
					num_iterations: user can run this multiple times. The results will all
						be stored in results.txt
"""
import random
import sys
import os
import time

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
	num_iterations = 1 		
	max_difference = .1																	
	# Parse command line arguments: 
	if len(sys.argv) == 3 or len(sys.argv) == 5: # Case 2: User provided max_difference and/or num_iterations
		if sys.argv[1] == "-d": # User provided max_difference
			try:
				max_difference = float(sys.argv[2])
			except ValueError: 
				print("max_difference must be a number.")
				exit(0)
			if len(sys.argv) == 5 and sys.argv[3] == "-i": # User also provided num_iterations
				try:
					num_iterations = int(sys.argv[4])
				except ValueError:  
					print("max_difference must be a number.")
					exit(0)
		elif sys.argv[1] == "-i":
			try: 
				num_iterations = int(sys.argv[2])
			except ValueError:
				print("max_difference must be a number.")
				exit(0)
		else: 
			print("Usage: python3 DiceRollSimulator.py [-d max_difference] [-i num_iterations]")
			exit(0)
	else: # Case 3: Invalid number of arguments provided.
		print("Usage: python3 DiceRollSimulator.py [-d max_difference] [-i num_iterations]")
		exit(0)

	if num_iterations < 0 or max_difference < 0:
		print("max_difference cannot be negative")
		exit(0)
	# Roll die:
	for i in range(num_iterations): 
		while reached_expected_distribution == False:
			num_rolls += 1
			die_1_result = random.randint(1, 6) # Roll the first dice
			die_2_result = random.randint(1, 6) # Roll the second dice
			result = die_1_result + die_2_result  # Add die rolls to get result
			actual_results[result-2] += 1 	  # Add this result to tally of results
			# Update the distribution of actual results to reflect this die roll:
			actual_distribution[result-2] = actual_results[result-2]/num_rolls 
			reached_expected_distribution = check_if_reached_expected_distro(expected_distibution, actual_distribution, max_difference)
		# Output result into file:
		try:
			with open("results.txt", "a") as output_file:
				output_file.write(str(num_rolls))
				output_file.write("\n")
		except IOError:
			print("Cannot open output file to print result.")	
			exit(0)
		# Reset for next iteration:
		actual_distribution = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
		actual_results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		reached_expected_distribution = False
		num_rolls = 0

if __name__ == "__main__": main()







