from os import path
import sys
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts

def main():

#open/read file
    direct = path.dirname(__file__)
    sentiment = open(path.join(direct, 'mentalhealth.txt')).read()
#use pytagcloud module to create tags based on name counts, create image. 
    healthtags = make_tags(get_tag_counts(mentalhealth), maxsize=150)
    create_tag_image(simondstags, 'mentalhealth.png', size=(1200, 1200))

if __name__ == "__main__":
    main()