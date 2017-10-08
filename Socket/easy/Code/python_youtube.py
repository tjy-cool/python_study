#!/usr/bin/env python
# Funtion:      
# Filename:

base_url = 'https://www.youtube.com/watch?v=Z78zbnLlPUA&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq'
with open('url', 'w') as f:
    for i in range(21):
        i = i+1
        if i==1:
            url = base_url
        else:
            url = base_url + "&index=" + str(i)
        f.write(url)
        f.write('\n')
