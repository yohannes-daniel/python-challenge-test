# PyBank budget data

import os
import csv

# Prompt user for title lookup
book = input("What title are you looking for? ")

# Set path for file
print(os.path.abspath("."))
csvpath = os.path.join("Starter_Code", "PyBank", "Resources", "budget_data.csv")
print("File path is " + csvpath)

