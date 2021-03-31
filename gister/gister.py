import xml.etree.ElementTree as ET
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from pytube import YouTube

link_to_explore = "https://www.youtube.com/watch?v=Y2jyjfcp1as"

yt = YouTube(link_to_explore)
title = yt.title
length_in_seconds = yt.length
keywords = [x.replace('\\','') for x in yt.keywords]

try:
  xc = yt.captions['en'].xml_captions
except:
  try:
    xc = yt.captions['a.en'].xml_captions
  except:
    print("It seems there is no english caption....aborting!!")
    exit()

full_text = []
tree = ET.fromstring(xc)
for c in tree:
    full_text.append(c.text.replace("\n"," ").replace("&#39;","'").replace('Laughter',' ').replace("&quot;"," "))

ft = " ".join(full_text)

stopwords = set(STOPWORDS)
mask = np.array(Image.open("masker.jpg"))
wordcloud = WordCloud(stopwords=stopwords, 
                      background_color="white", 
                      contour_width=1, 
                      contour_color='firebrick',
                      mask=mask).generate(ft)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
