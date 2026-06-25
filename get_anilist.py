import urllib.request, json
query = '''
query {
  c1: Character(search: "Ichigo Kurosaki") { image { large } }
  c2: Character(search: "Kyojuro Rengoku") { image { large } }
  c3: Character(search: "Mai Sakurajima") { image { large } }
}
'''
req = urllib.request.Request('https://graphql.anilist.co', data=json.dumps({'query': query}).encode(), headers={'Content-Type': 'application/json'})
res = urllib.request.urlopen(req).read().decode()
with open('anilist_urls.txt', 'w') as f:
    f.write(res)
