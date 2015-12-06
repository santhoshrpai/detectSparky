__author__ = 'kannan'

import Image


# REFERENCE: http://effbot.org/imagingbook/image.htm
# Dataset: Lichman, M. (2013). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.
background = Image.open("original.png")
# background.convert('RGBA').save('temp.png')
foreground = Image.open("sparky.gif")
# temp = Image.open('temp.png')
#Value Transparency mask error solved by - https://github.com/matthewwithanm/django-imagekit/issues/270
new_foreground = foreground.convert('RGBA')
x,y = foreground.size
background.paste(new_foreground, (20, 20 ,128 ,168), new_foreground)
background.save("superimposed_temp1.jpg")