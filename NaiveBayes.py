from __future__ import division
import string, csv, math, os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#Download the  nltk libary from nltk( http://www.nltk.org/install.html)
#Dictionary for newsgroup 
newsGroups_dict = {} 
class_count = 20 

#An 2 dimensional array is used to store the number of times the vocabulary is used in the document and array_count contains wordcount of each class
array = [] 
array_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 

#dictionary containing all vocabulary
vocabulary = {}
length_Vocabulary = 0
crPr = 0
wrPr = 0

def createVocabulary():
    global array, vocabulary, newsGroups_dict, class_count, array_count, length_Vocabulary
    stopset = set(stopwords.words('english'))

    #Give the 20 newsgroup Dataset path here
    folderPath = "C:\\Users\\sride\\Desktop\\ml\\20_newsgroups\\"
    folderList = [folder for folder in os.listdir(folderPath) if os.path.isdir(os.path.join(folderPath, folder))]
    buildNewsGroup_dict(folderList)
    for folder in folderList: #getting groups list
        fileList = [fileName for fileName in os.listdir(os.path.join(folderPath, folder)) if
                    os.path.isfile(os.path.join(folderPath, folder, fileName))]
        for fileName in fileList[0:500]: 
            inputFile = open(os.path.join(folderPath, folder, fileName)).read()
            inputFile = inputFile.lower()
            tokens = word_tokenize(str(inputFile))
            tokens = [w for w in tokens if not w in stopset]
            tokens = [i for i in tokens if i not in string.punctuation]
            tokens = [x for x in tokens if not any(x1.isdigit() for x1 in x)]
            list_banned = ['--', '''''', '*', 'et', 'al', '...', '``', '_', "''", 'xref', '_/_/_/', '-+', '-/', '..',
                         '+ve', '-ve', 'mr.', "n't", "'s", '|', '==','path', 'newsgroups']
            tokens = [i for i in tokens if i not in list_banned]
            computeArray(tokens, folder)

    length_Vocabulary = len(vocabulary)
    print ("vocabulary Length: " + str(length_Vocabulary))

def buildNewsGroup_dict(folderList):
    global newsGroups_dict
    count = 0
    for folder in folderList:
        newsGroups_dict[folder] = count
        count += 1

#Creates the array of vocabulary and there occurences in a newsgroup
def computeArray(tokens, folder):
    global array, vocabulary, newsGroups_dict, array_count
    for token in tokens :
        if(token in vocabulary):
            array[vocabulary[token]][newsGroups_dict[folder]] += 1
        else:
            vocabLen = len(vocabulary)
            vocabulary[token] = vocabLen
            array.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            array[vocabLen][newsGroups_dict[folder]] += 1
    array_count[newsGroups_dict[folder]] += 1

def classify():
    global crPr, wrPr
    stopset = set(stopwords.words('english'))

	#Give the 20 newsgroup Dataset path here
    folderPath = "C:\\Users\\sride\\Desktop\\ml\\20_newsgroups\\"
    folderList = [folder for folder in os.listdir(folderPath) if os.path.isdir(os.path.join(folderPath, folder))]
    for folder in folderList:
        fileList = [fileName for fileName in os.listdir(os.path.join(folderPath, folder)) if
                    os.path.isfile(os.path.join(folderPath, folder, fileName))]
        for fileName in fileList[500:999]:
            inputFile = open(os.path.join(folderPath, folder, fileName)).read()
            inputFile = inputFile.lower()
            tokens = word_tokenize(str(inputFile))
            tokens = [w for w in tokens if not w in stopset]
            tokens = [i for i in tokens if i not in string.punctuation]
            tokens = [x for x in tokens if not any(x1.isdigit() for x1 in x)]
            list_banned = ['--', '''''', '*', 'et', 'al', '...', '``', '_', "''", 'xref', '_/_/_/', '-+', '-/', '..',
                         '+ve', '-ve', 'mr.', "n't", "'s", '|', '==','path', 'newsgroups']
            tokens = [i for i in tokens if i not in list_banned]
            prClass = getClass(tokens)
            #print ("Actual class: " + folder + "; Predicted class: " + prClass) 
            if (prClass == folder) :
                crPr += 1
            else:
                wrPr += 1

    accuracy = (crPr/(crPr + wrPr))*100
    print ("Accuracy of prediction: " + str(accuracy))

#returns the class of the document sent as input
def getClass(tokens):
    global array, vocabulary, newsGroups_dict, class_count, array_count, length_Vocabulary
    maxClass = ""
    maxVal = -999999999999
    for key in newsGroups_dict:
        logSum = 0
        for token in tokens:
            if(token in vocabulary):
                numer = (array[vocabulary[token]][newsGroups_dict[key]] + 1)
            else:
                numer = 1
            denom =  (array_count[newsGroups_dict[key]] + length_Vocabulary)
            pr = (numer/denom)
            logSum = logSum + math.log10(pr)
        logSum = logSum + math.log10(0.05)
        if(maxVal < logSum):
            maxVal = logSum
            maxClass = key
    return maxClass

if __name__ == "__main__":
    createVocabulary()
    classify()