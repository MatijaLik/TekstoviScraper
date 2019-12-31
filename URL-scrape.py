from lxml import html
import time
import requests
txtFile = open('scrapedAuthors.txt', 'w')
rootPage = 'https://tekstovi.net/2,'

start = time.time()
#get all the authors
#having a separate txt file for authours is unnecessary, but I will leave it for debugging purposes.
print('Scraping authours...')
cnt = 0
for i in range(27):
    c = chr(64+i) #64 je @
    url = rootPage + c + ',0.html'
    page = requests.get(url)
    f = html.fromstring(page.content)
    for author in f.xpath('//p[@class="artLyrList"]//a'):
        href = author.get('href')
        txtFile.write('https://tekstovi.net/'+href+'\n')
        cnt += 1
txtFile.close()
print('Auhtors porcessed: ' + str(cnt))
print('Done')

print('Scraping songs...')
#for each author, get all their songs
authorFile = open('scrapedAuthors.txt', 'r')
songFile = open('songs.txt', 'w')
urls = authorFile.readlines()
count = 0
for url in urls:
    page = requests.get(url)
    f = html.fromstring(page.content)
    for song in f.xpath('//p[@class="artLyrList"]//a'):
        href = song.get('href')
        songFile.write('https://tekstovi.net/'+href+'\n')
        count += 1
        if(count % 1000 == 0):
            print("Songs processed: " + str(count))
songFile.close()
authorFile.close()
print("Songs processed: " + str(count))
print('Done')
end = time.time()
print("Execution time: " + str(end-start))
