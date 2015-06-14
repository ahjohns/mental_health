import urllib2, json, re, string 

def main():


#open and read txt file
    experience = open('experience.txt', 'rU').read()
#open file to write out
    sentiment = open('mentalhealth.txt', 'w')

#words list
    experiencelist = []
#take into account words having little emphasis in context
    articles = ['a', 'the', 'and', 'an', 'that', 'then', 'than', 'is', 'was', 'to', 'in', 'or', 'of', 'as', 'on', 'but', 'for', "it's",'any']
    
    words = experience.split()
    for a in words:
        a = a.lower()
        a = a.replace(",", "").replace(".", "").replace("(", "").replace(")", "")
        if a not in articles:
            experiencelist.append(a)
    
    print experiencelist
    for item in experiencelist:
        #item = unicode(item)
        item = str(item)
        sentiment.write(item + '\n')

if __name__ == "__main__":
    main()