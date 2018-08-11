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
	 2. Create a Likelihood table 
	 3. Use Naive Bayes equation to calculate the posterior probability for each class(spam or no spam), The class with the highest posterior probability is the 
 the outcome of prediction, given a mail with subject line “new professional courses is recommneded for you”
	4. Step 3 and 4 are solved simultaneously, by computing the posterior probability of each word in the new subject line, and we will be applying Laplace 
 smoothing to fix the missing words in our datasets. We then add the results of each of these words. The class with the highest posterior probability
 is the category this new mail belongs to.
 First, we compute the posterior probability of the class spam given the predictor(word).
 	The posterior probability of class ‘spam’ given the predictor(new mail subject line) is found to be 0.8839285714285714(nn). Next, we compute the posterior probability of class ‘non spam’ given the same predictor.
	The posterior probability hereby is given as 1.4375(mm). Finally since it’s a universal truth that 1.4375 > 0.8839285714285714, the new mail in our inbox with the subject line, “new professional courses recommended for you” has been classified as a “non spam” email by the algorithm. We are safe. :).
	
