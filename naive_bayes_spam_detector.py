spamdata = ['save', 'big', 'on', 'all', 'vehicles', 'melt', 'fat', 'away',
           'you', 'were', 'recommended', 'into', 'the', 'global', 'professional',
           'network', 'how', 'to', 'grow', '3+', 'inches', 'taller', 'in', 'just','a',
           'matter', 'of', 'weeks', 'you', 'have', 'won', 'a', 'lottery']
nonspamdata = ['thanks', 'for', 'signing', 'up', 'for', 'our', 'newsletter',
              'your', 'profile', 'was', 'recently', 'on', 'changed',
              'confirm', 'you', 'new', 'account', 'recommended', 'courses', 'for', 'you',
              'customer', 'invoice']
frequency = {}
counter = 0
s_counter = 0
for a in spamdata:
    for b in spamdata:
        if a == b:
            counter += 1
            frequency[a] = [counter, s_counter]
            if a in nonspamdata:
                s_counter += 1
                frequency[a] = [counter, s_counter]
    counter = 0
    s_counter = 0
for c in nonspamdata:
    for d in nonspamdata:
        if c == d:
            s_counter += 1
            if c in frequency:
                frequency[c][1] = s_counter
            elif c not in frequency:
                frequency[c] = [counter, s_counter]
    s_counter = 0

def posterior(prob_of_predictor, prior_probability, prob_of_class):
    try:
        posterior_prob = (prob_of_predictor * prior_probability)/prob_of_class
        return posterior_prob
    except ZeroDivisionError:
        return 0

#Total of both classes
spam_all = 0
for d in frequency:
    spam_all = spam_all + frequency[d][0]
nonspam_all = 0
for e in frequency:
    nonspam_all = nonspam_all + frequency[e][1]

subjectline = "new professional courses is recommneded for you"
t_data = subjectline.split()
t_data_likelihood = {}

#spam table
for f in t_data:
    if f in frequency:
        word_frequency = frequency[f][0]
    else:
        word_frequency = 0
    t_data_likelihood[f] = word_frequency

def theprobofclass(word):
    try:
        add_class = frequency[word][0] + frequency[word][1]
        return add_class
    except KeyError:
        return 0


prior_probability = spam_all/(spam_all+nonspam_all)

nn = 0
for g in t_data_likelihood:
    posterior_prob = posterior(t_data_likelihood[g], prior_probability, theprobofclass(g))
    nn += posterior_prob
print("The Posterior Probability of the mail being Spam is given as", nn)

#nonspam table
nt_data_likelihood = {}
for h in t_data:
    if h in frequency:
        n_word_frequency = frequency[h][1]
    else:
        n_word_frequency = 0
    nt_data_likelihood[h] = n_word_frequency
    
n_prior_probability = nonspam_all/(spam_all+nonspam_all)

mm = 0
for i in nt_data_likelihood:
    n_posterior_prob = posterior(nt_data_likelihood[i], n_prior_probability, theprobofclass(i))
    mm += n_posterior_prob
print("The Posterior Probability of the mail being non spam is given as ", mm)
