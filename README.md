# NaiveBayesClassifier

Here, we will demonstrate how Naive Bayes solves an age old internet problem - "Spams". To solve this, we will follow 
a few easy steps. Before you read this, I'm assuming you have a basic understanding of Naive Bayes Classifiers, if 
you don't - NB Classifiers is a classification algorithm used to certain classification problems. 
By 'certain' meaning Naive Bayes is limited in usage, Naive Bayes Classifier would be the wrong algorithm to use 
in a scenario whereby your dataset points are dependent, NBC makes an assumption about your data, each features would be 
scaled equally, thus the name.

    What do we need?
    - A sample dataset of Spam and legitimate email subjects, to narrow down our word list. Since this is basically a demonstration
	we won't be working with large datasets, rather popular spam mails subjects, do note when working on a large scaled projects 
	the datasets should be robust.
    - Python3.x Intepreter
    - In depth knowledge of Multinomial Naive Bayes Classification.

    How we go about this?v
    We have samples of popular spam email subjects from wordsthatclick.com
	- save big on all ehicles
	- melt fat away
	- you were recommended into the global professional network
	- how to grow 3+ inches taller in just a matter of weeks
	- you've won a lottery
    We also have samples of non spam emails
	- thanks for signing up for our newsletter
	- your profile was recently changed
	- confirm you new account
	- recommended courses for you
	- customer invoice
    But do keep it in mind that spammers are not stupid, they are getting better to bypass spam detection services, which means the better
	the datasets, the better the algorithm.

    Technicality?
	1. Convert the data(both the spam and non spam) into a frequency table, this will be done in code and here, the Artificial Intelligence favorite pet - Python;
	 The code to this is titled frequencytable.py in this repository.
