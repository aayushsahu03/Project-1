from wordcloud import STOPWORDS, WordCloud
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


print("hello venv")

s = pd.Series(['cat', 'dog', np.nan, 'rabbit'])
print(s.map(lambda x: x+' yo' if pd.notna(x) else 'yo'))


lt =[1,2,3,"yo","great","yo","better"]
lt = list(map(str,lt))
my_string = " ".join(lt)
print(my_string)

stopwords = set(STOPWORDS)

wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(my_string)
 
# plot the WordCloud image                      
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()