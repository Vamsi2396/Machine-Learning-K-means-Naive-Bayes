Yalamanchili Vamsi krishna
1001554490

->Performed using Python.

->Files Submitted
 	-NaiveBayes.py
 	-ReadMe.txt

->Code Structure:
	-We iterates each newsgroup and reads first 500 files.
	-Then it cleans and tokenizes the data.(Using the nltk library) 
	-It then creates a two dimensional array. Rows are vocabulary and columns are the 20 newsgroup class.
	-Each cell represents the count of that vocabulary in that class.
	-Based on the array we classify each document(naive bayes classifier).
	-Logarithmic Probability for each word is calculated for each class and added.
	-Highest probabilty class will be assigned as the class.
	-We check original class to predicted class for accuracy measurement.

->Packages required:
	-nltk( http://www.nltk.org/install.html)

->To Run:
	-Set the path of newsgroupdata in files (Lines 23, 78)
	-python NaiveBayes.py

	Note:nltk works in Python 2.7, 3.4, 3.5, or 3.6
	For any errors : To run from cmd:( Change path\\pip install nltk\\import nltk\\nltk.download('stopwords')\\nltk.download('punkt') )
 
-> Note:It takes 3-4 minutes to execute

-> Accuracy:
	-It provides 80.467% accuracy.

