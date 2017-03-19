#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print("SIZE: {}".format(len(enron_data)))

names = enron_data.keys()
pois = [1 for name in names if enron_data[name]["poi"]==1]
print("POI count: {}".format(len(pois)))

print("known salary: {}".format(sum([1 for p in names if enron_data[p]["salary"] != 'NaN'])))
print("known email: {}".format(sum([1 for p in names if enron_data[p]["email_address"] != 'NaN'])))
