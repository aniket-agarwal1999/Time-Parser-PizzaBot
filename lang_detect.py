
#I don't think this file is of any use

import langid
#it cannot detect hinglish but our users will either use english or hinglish 
#so i am considering that if detect is not english then it is hinglish

#input
ip=input("write somethin ")

lang=langid.classify(ip)[0]

if lang=='en':
    print('language is english')
    
else:
    print('language is hinglish')
