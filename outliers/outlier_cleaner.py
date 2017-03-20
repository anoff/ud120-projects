#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    tuples = [(ages[i], net_worths[i], abs(predictions[i] - net_worths[i])) for i in range(len(predictions))]
    ordered = sorted(tuples, key=lambda elm: elm[2][0])
    total = len(ordered)
    return ordered[0:int(total-1-0.1*total)]

