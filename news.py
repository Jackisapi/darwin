import requests
import xmltodict
import playsound

def podFetch(url='https://feeds.npr.org/500005/podcast.xml', filename='podcast.xml'):
    r = requests.get(url)
    open(filename, 'wb').write(r.content)
    return filename


def xml2url(file):
    with open(file, 'r', encoding='utf8') as f:
        my_xml = f.read()
    xmlDict = xmltodict.parse(my_xml)
    data = xmlDict
    return data['rss']['channel']['item']['enclosure']['@url']


def play():
    print(podFetch())
    print(xml2url(podFetch()))
    news = requests.get(xml2url(podFetch()))
    open('file.mp3','wb').write(news.content)
    playsound.playsound('file.mp3',True)
