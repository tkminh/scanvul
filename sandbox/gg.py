from googlesearch import search
from googlesearch import get_random_user_agent

query = 'site:playhearthstone.com'
for res in search(query, lang='en', num=10, start=0, stop=10, pause=3.0, country='vn', user_agent=get_random_user_agent()):
    print(res)

print("Done")