# - * - coding: utf - 8 -*-
import codecs
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud ,STOPWORDS, ImageColorGenerator
import  matplotlib.pyplot as plt

mytext=codecs.open("D:/spider.txt","r",encoding='utf-8').read()
mytext=''.join( jieba.cut(mytext) )
#background_Image=plt.imread("qq.png")
background_Image = Image.open("ap.jpg") #打开图片
img_array = np.array(background_Image) #

wc = WordCloud( background_color="white",
               mask=img_array,
               max_words=2000,
               stopwords=STOPWORDS,
               font_path="Redocn.ttf",
               max_font_size=60,
               color_func=None,
               random_state=15).generate(mytext)
plt.imshow(wc)
image_colors=ImageColorGenerator(img_array)
wc.recolor(color_func=image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()