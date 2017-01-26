"""
Author:         Emma Kimlin
Date:           6 January 2017
Title:          DiceRollSimulator
Purpose:        Determines number of times a person would have to roll 2 dice to get expected
                distribution of results. Appends this number into text file (results.txt).
Usage:          python3 DiceRollSimulator.py [-d max_difference] [-i num_iterations]
                    max_difference: allowable error between actual result and expected result
                        for reach possible result 2-12 (positive int or double)
                    num_iterations: user can run this multiple times. The results will all
                        be stored in results.txt
"""
import random
import argparse


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
    return True  # Reached expected distro. Return True.


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
    num_rolls = 0  # Total number of rolls across entire program execution.
    # Indicates whether actual results are equal expected results within
    # maximum boundary of difference.
    reached_expected_distribution = False
    result = 0  # Sum of both rolls
    num_iterations = 1
    max_difference = .1
    # Average number of rolls per iterations necessary to reach
    # maximum difference b/w expected and actual results:
    avg_num_rolls_needed = 0

    # Parse command line arguments:
    parser = argparse.ArgumentParser(usage="python3 DiceRollSimulator.py <-d num_rolls> <-i num_iterations>")
    parser.add_argument('-d', help="number of times to roll dice per iteration", type=int)
    parser.add_argument('-i', help="maximum number of times to simulate die-roll sequence", type=int)
    args = parser.parse_args()
    if args.d:
        max_difference = args.d
    if args.i:
        num_iterations = args.i
    if num_iterations < 0 or max_difference < 0:
        print("number of iterations or max_difference cannot be negative")
        exit(0)
    # Roll die:
    for i in range(num_iterations):
        while reached_expected_distribution == False:
            num_rolls += 1
            result = random.randint(1, 6) + random.randint(1, 6)  # Add 2 die rolls to get result
            actual_results[result - 2] += 1  # Add this result to tally of results
            # Update the distribution of actual results to reflect this die roll:
            actual_distribution[result - 2] = actual_results[result - 2] / num_rolls
            reached_expected_distribution = check_if_reached_expected_distro(expected_distibution, actual_distribution,
                                                                             max_difference)
        avg_num_rolls_needed += num_rolls
        # Reset for next iteration:
        actual_distribution = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        actual_results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        reached_expected_distribution = False
        num_rolls = 0
    avg_num_rolls_needed = int(avg_num_rolls_needed / num_iterations)
    print("On average, dice must be rolled", avg_num_rolls_needed, "times to reach expected variation.")

if __name__ == "__main__": main()
