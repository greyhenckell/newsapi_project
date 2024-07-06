import requests


url = "https://newsapi.ai/api/v1/article/getArticles?"

params = {
    "dateStart":"2024-06-23"
    ,"dateEnd":"2024-06-30"
    ,"articlesSortBy":"socialScore"
    ,"lang":"eng"
    ,"resultType":"articles"
    ,"isDuplicateFilter":"skipDuplicates"
    ,"eventFilter":"skipArticlesWithoutEvent"
    ,"sourceLocationUri":"http://en.wikipedia.org/wiki/Finland"
    ,"apiKey":"1e1d8a79-fa57-4488-9a1b-04fc02663c39"
} 

headers = {
  'Content-Type': 'application/json'
}

res = requests.get(url, params=params, headers=headers)

if res.status_code == 200:
    content = res.json()
    for item in content['articles']['results']:
        print(f"---{item['title']}")
