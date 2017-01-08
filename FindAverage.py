"""
Author: 		Emma Kimlin
Date:   		7 January 2017
Title: 			FindAverage.py
Purpose: 		Given a file of numbers, each on its own line, find average of 
				all the numbers in the file. 
Usage: 			FindAverage -input_file.txt
					where input_file.txt is the file where the numbers that will
						will be averaged are stored. 			
"""
import sys

def main():
	# Check that user provided correct number of arguments
	if len(sys.argv) != 2:
		print("Usage: FindAverage -fi -input_file.txt")
		exit(0)
	# Open file where numbers are stored and read in data
	sum_numbers = 0 # Sum of all numbers in the file
	count_numbers = 0 # How many numbers are in the file
	try:
		with open(sys.argv[1], "r") as input_file:
			for each_number in input_file.readlines(): 
				count_numbers += 1
				try:
					sum_numbers += float(each_number.strip('\n')) 
				except ValueError:
					print("File must store numbers. ")
					exit(0)
	except IOError:
		print("Cannot open input file.")
		exit(0)	
	# Compute average and print to stdout:
	average = sum_numbers/count_numbers
	print("Average =", round(average, 2))

if __name__ == '__main__': main()