from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud


#open/read file
direct = path.dirname(__file__)
sentiment = open(path.join(direct, 'mentalhealth.txt')).read()
#use pytagcloud module to create tags based on name counts, create image. 
wordcloud = WordCloud.generate(sentiment)
# Open a plot of the generated image.
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
