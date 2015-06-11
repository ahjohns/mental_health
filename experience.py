import urllib2, json

def main():


#open and read txt file
    experience = open('experience.txt', 'rU').read()
#open file to write out
    sentiment = open('mentalhealth.txt', 'w')

#words list
    experiencelist = []
    
    words = experience.split()
    if words == 'a':
        words == null
    if words == 'the':
        words == null
    if words == 'and':
        words == null
    
    print words
    #for ex in experience:
        #ex = ex.split('\n')
        #print ex

#for each json dictionary key value pair, grab first index of name, append to first name list
#    for key, value in response_string.items():
 #       if key == 'data':
  #          for member in value:
   #             for k, v in member.items():
    #                if k == 'name':
     #                   v = v.split()
      #                  firstnamelist.append(v[0])
#iterate through first name, convert to string, write to file
    #for item in firstnamelist:
     #   item = unicode(item)
      #  item = str(item)
       # firstnames.write(item + '\n')


if __name__ == "__main__":
    main()