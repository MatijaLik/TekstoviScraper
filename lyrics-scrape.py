from lxml import html
import requests
import time


start = time.time()
lyricsFile = open('lyrics.txt', 'w')
urlFile = open('songs.txt', 'r')
urls = urlFile.readlines()
songCount = 0
lineCount = 0
for url in urls:
    try:
        page = requests.get(url)
    except requests.exceptions.RequestException as e:
        continue;
    f = html.fromstring(page.content)#opens the page
    lyrics = f.xpath('//p[@class="lyric"]/text()')#get all the lyircs
    songCount += 1
    for line in lyrics:
        newLine = line.replace('\r', '')#removes non-essential line breaks
        lyricsFile.write(newLine)#write to file
        lineCount += 1
    lyricsFile.write("\n")
    lyricsFile.write("\n")
    if(songCount % 100 == 0):
        print("-------")
        print("Songs processed: " + str(songCount))
        tim = time.time()
        print("Current time: " + str(tim-start))
        
print("##################")
print("Songs processed: " + str(songCount))
print("Lines processed: " + str(lineCount))

end = time.time()
print("Execution time: " + str(end-start))

