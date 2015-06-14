import codecs

def main():

    words = open('mentalhealth.txt', 'rU').readlines()
    wordsfile = open('mentalhealthcount.txt', 'w')
    worddict = {}
    wordlist = []
    countlist = []
    for word in words:
        word = word.replace("\n", "")
        n = word.split('\t')
        print n
        if n[0] in worddict:
            worddict[n[0]] += 1
        else:
            worddict[n[0]] = 1
    
    for key, value in worddict.items():
        wordlist.append(key)
        countlist.append(value)
    
    zips =  zip(wordlist, countlist)
    for items in zips:
        items = str(items)
        items = items.split(',')
        items[0] = items[0].replace("('", '').replace("'", '')
        items[1] = items[1].replace(")", '')
        items = ';'.join(items)
        print type(items)
        wordsfile.writelines(items + '\n')
    #     for item in items:
#             print type(item)
            #names.write(item)
#         print items[0]
#         print items[1]
#         print character
#         names.writes(item[0] + ';')
#         names.writes(items[1] + '\n')
        
    print worddict
if __name__ == '__main__':
  main()