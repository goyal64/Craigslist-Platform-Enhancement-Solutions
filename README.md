# Craigslist-Platform-Enhancement-Solutions
Developed Python scripts to scrape data &amp; provided a lean product search system for Craigslist implementing deep learning models &amp; NLP; also implemented classification models to identify misclassified advertisements

Part 1: Flagging expired event tickets
1. Run the spider "notsonaivebayespart1scraper.py" from the terminal and extract the scraped ticket information in a csv
2. Run "notsonaivebayespart1_2processing.py" in pycharm after loading the csv in the dataframe and the processing file generates a flag for expired event

Part 2: Flagging old listings
1. Run the spider "notsonaivebayespart2scraper.py" from the terminal and extract the scraped listing information in a csv
2. Run "notsonaivebayespart1_2processing.py" in pycharm after loading the csv in the dataframe and the processing file generates a flag for old tickets based on the user input for the duration

Part 3: Keyword Extraction
1. Run the spider "notsonaivebayespart3scraper.py" and extract the data in a csv
2. Load the csv file in "notsonaivebayespart3processing.py" and execute the code to get the top 5 matching advertisements based on user selection.

Part 4: Misclassified Advertisements
1. Run the spider "notsonaivebayespart4scraper.py" and extract the data in a csv
2. Load the csv file in "notsonaivebayespart4model.py" and run the models to view the accuracy of the models
