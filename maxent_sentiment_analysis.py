# Python Sentiment Analysis Tool
# Uses NLTK and Twitter Data to 
# train a maximum entropy classifier.
# More on MaxEnt Classifiers:
# http://blog.datumbox.com/machine-learning-tutorial-the-max-entropy-text-classifier/

# Created by Dan Adler on 08/31/2016
# Last edited by Dan Adler on 09/09/2016

# Input: training text file where each row is a tweet
# Input: training text file where each row is the category of the tweet
# Input: test data

# Output: the classification of each row of test data

# Command:
# python maxent_sentiment_analysis.py training_tweets.txt training_categories.txt test_data.txt

# Imports
from nltk.classify import MaxentClassifier as maxent
from collections import Counter
import ftfy
import sys, re, string

class MaxEntSentimentClassifier:

    # Main 
    # Simply define variables
    def __init__(self):
        self.train_toks = None
        self.tweets = None
        self.classes = None
        self.test_data = None
        self.classifier = None

    # Upload Tweets
    # tweet_file is the file containing line by line
    # tweets
    def add_tweets(self, tweet_file):
        self.tweets = self.__upload_file(open(tweet_file, "r"))

    # Upload a classifier for each tweet
    # class_file is the file with a classification
    # for each tween in training data
    def add_classification_data(self, class_file):
        self.classes = self.__upload_file(open(class_file, "r"))

    def add_test_data(self, test_file):
        self.test_data = self.__upload_file(open(test_file, "r"))

    # Train
    def train_data(self):
        # Organize data
        self.__organize_data()
        self.classifier = maxent.train(self.train_toks)

    # Classify
    def classify_test_data(self):
        # Make output list
        test_classes = [None] * len(self.test_data)
        for i  in range(len(self.test_data)):
            test_classes[i] = self.classifier.classify(self.__make_feature(self.test_data[i]))
        print(test_classes)
        return test_classes

    # Upload a file
    def __upload_file(self, file):
        return file.read().split('\n')

    # Organizes data for the classifier
    def __organize_data(self):
        try:
            # Initialize array
            self.train_toks = [None] * len(self.tweets)
            # Now actually create data
            for i in range(len(self.tweets)):
                self.train_toks[i] = (self.__make_feature(self.tweets[i]), self.classes[i])
        except:
            raise Exception("Number of tweets/classficiations do not match.")

    # Makes a feature counter from a string, i.e.
    def __make_feature(self, s):
        # Clean the tweet
        s = self.__clean_data(s)
        # Split and return a counter
        return Counter(s.split())

    # Cleans the data
    def __clean_data(self, s):
        # Fix and make sure unicode
        s = ftfy.fix_text(s)
        # Lower case
        s = s.lower()
        # Remove URLs
        s = re.sub(r"http\S+", "", s)
        # Remove reptitive characters
        s = re.sub(r'(.)\1+', r'\1\1', s)
        # Remove all usernames and split
        s = ' '.join(filter(lambda x:x[0]!='@', s.split()))
        # Regex punctuation prep
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        # Remove punctuation
        s = regex.sub('', s)
        return s


if __name__ == "__main__":
    # Create object
    classifier = MaxEntSentimentClassifier()
    # Add training tweets
    classifier.add_tweets(sys.argv[1])
    # Add classification for each tweet
    classifier.add_classification_data(sys.argv[2])
    # Train the data
    classifier.train_data()
    # Upload test data
    classifier.add_test_data(sys.argv[3])
    # Classify test data
    test_classes = classifier.classify_test_data()
    print(test_classes)