from bs4 import BeautifulSoup as bs
import requests

def get_weather_data(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")

    return soup

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"

url = 'https://www.google.com/search?client=firefox-b-1-d&q=harrisonburg+weather'

soup = get_weather_data(url)

# store all results on this dictionary
result = {}
# extract region
result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
# extract temperature now
result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
# get the day and hour now
result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
# get the actual weather
result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
# get the precipitation
result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
# get the % of humidity
result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
# extract the wind
result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text

# create output file
f = open('HBurgWeather', 'w')

f.write("Temperature:\t{}\n".format(result['temp_now']))
f.write("Time:\t{}\n".format(result['dayhour']))
f.write("Weather:\t{}\n".format(result['weather_now']))
f.write("Precipitation:\t{}\n".format(result['precipitation']))
f.write("Humidity:\t{}\n".format(result['humidity']))
f.write("Wind:\t{}\n".format(result['wind']))

