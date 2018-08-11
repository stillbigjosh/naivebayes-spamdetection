# -*- coding: utf-8 -*-
"""
author: Skywalker(@alojoecee)
"""

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
    
print(frequency)