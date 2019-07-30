'''

Used to extract the url of info on players with highest batting average from cricinfo site.
It also extracts the url of each players image from the respective info url above.
This information is needed for one of my educational dashboard project.

'''

from bs4 import BeautifulSoup
import requests
import csv

# Highest batting average link from espncricinfo
url = 'http://stats.espncricinfo.com/ci/content/records/282911.html'
doc = requests.get(url)
html_doc = doc.text

soup = BeautifulSoup(html_doc,'html.parser')

player = []

# Find the link for each player's info 
# and search for the image link from the info page
for data in soup.find_all('td', class_='left'):
    if(data.has_attr('title')):
        for i in data.find_all('a', class_='data-link'):
            name = data.get_text()
            ply_src = 'http://stats.espncricinfo.com'+i.get('href')
            soup_img = BeautifulSoup(requests.get(ply_src).text,'html.parser')
            ply_img = soup_img.find('link', rel='image_src').get('href')
            player.append([name,ply_src,ply_img])

# Save it in csv file            
with open('players.csv','w') as csvfile:
    filewriter = csv.writer(csvfile,delimiter=',', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['PlayerName','PlayerSource','PlayerImage'])
    filewriter.writerows(player)
