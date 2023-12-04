# Justwatch Data Extraction

This is a basic script for extracting data about films and series from the justwatch website


# Files

- Justwatch_data_extraction 

This file is where the entire basic extraction script is located. At the beginning, variables are declared and the query in GraphQL is then looped. The number 820 is the total number of films divided by 100 (what the query returns) this number 820 can change and the query can also change. Once the loop is completed, it stores the list in a Json file to be consumed later.

- Load_json

It is a test file for reading the created json.

##In the future, this data will be processed to obtain only information from these films