import json
from itertools import groupby


def getDate(day):
    from datetime import datetime, timedelta, date
    d = datetime.today() - timedelta(days=day)

    return d


# Opening JSON file
f = open('out.json')

# returns JSON object as
# a dictionary
data = json.load(f)
# print('Total Dictionaries ',len(data))
# Iterating through the json


#
text = data[0]['description'][0]


output = ''
blacklist = [
    '[document]',

   'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script',
    # there may be more elements you don't want, such as "style", etc.
]

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)




print(output)


# done
# getting post date
# date_posted = data[0]['dateposted']
# post_date=getDate(int(date_posted[1].split()[0][0]))



#done
#getting like comments and reposts
# comments_data=data[0]['comments']
# no_of_likes= comments_data[0]
# no_of_comments =  [''.join(g) for _, g in groupby(comments_data[1], str.isalpha)][0].strip()
# no_of_reposts =  [''.join(g) for _, g in groupby(comments_data[2], str.isalpha)][0].strip()
# print('Likes: ',no_of_likes,'Comments: ',no_of_comments,'Reposts: ',no_of_reposts)


# done
# simple words
# searchby = data[0]['searchby']
# searchedkeyword = data[0]['searchedkeyword']
# searcheduser = data[0]['searcheduser']




# Closing file
f.close()
