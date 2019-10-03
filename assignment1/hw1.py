#All functions are based on knowledge from regex documentation
import regex

def findSHStartLengthFour():
    ans = {'Question 1':'Find a word start with sh and at least length 4'}
    regex1 = regex.compile(r'\b(sh)(\w{2,})\b')

    # test for standard case
    ans['sherry'] = regex1.search('sherry') != None  
    # test for another standard case
    ans['sherryqelrwj'] = regex1.search('sherryqelrwj') != None  
    # test for length lower than 4
    ans['she'] = regex1.search('she') != None
    # test for starting without sh
    ans['herr'] = regex1.search('herr') != None  

    for key,value in ans.items():
        print(key + ": " + str(value))

def findDuplicate():
    ans = {'Question 2': 'Find duplicates'}
    regex2 = regex.compile(r'\b(\w+)\s\1\b')

    # test for standard case
    ans['hello hello'] = regex2.search('hello hello') != None 
    # test for another standard case
    ans['the the'] = regex2.search('the the') != None
    # test for only 1 word
    ans['she'] = regex2.search('she') != None
    # test for two words having different cases
    ans['herr Herr'] = regex2.search('herr') != None  

    for key, value in ans.items():
        print(key + ": " + str(value))

def findBAB():
    ans = {'Question 3': 'Find b-a-b'}
    regex3 = regex.compile(r'\b(b)(b*)a?(b+)\b')

    # test for standard case
    ans['bab'] = regex3.search('bab') != None
    # test for another standard case
    ans['babab'] = regex3.search('babab') != None
    # test for another standard case
    ans['bbbbbbbbbbabbbbbb'] = regex3.search('bbbbbbbbbbabbbbbb') != None
    # test for no b before a
    ans['abababab'] = regex3.search('abababab') != None
    # test for no b after a
    ans['ba'] = regex3.search('ba') != None
    # test for two 'a's next to each other
    ans['bbbbb'] = regex3.search('bbbbb') != None

    for key, value in ans.items():
        print(key + ": " + str(value))

def findNumAndWords():
    ans = {'Question 4': 'Find number + words'}
    regex4 = regex.compile(r'(?<=^\d).+(?=\w$)')

    # test for standard case
    ans['45 carol way'] = regex4.search('45 carol way') != None
    # test for another standard case
    ans['673 Happy Place'] = regex4.search('673 Happy Place') != None
    # test for numbers at the end
    ans['Henry 45'] = regex4.search('Henry 45') != None
    # test for only numbers
    ans['98'] = regex4.search('98') != None

    for key, value in ans.items():
        print(key + ": " + str(value))

def findPhoneNum():
    ans = {'Question 5': 'Find phone number'}
    regex5 = regex.compile(
        r'\b\d{10}\b|\b(\+1)?(\d{3})[\-\.\s\)]?(\d{3})[\-\.\s]?(\d{4})\b|\b\d{3}[\-\.\s]?[^\(]\d{4}\b')#Got some help from Paulina of this part [^\(]

    # test for standard case
    ans['234-879-8543'] = regex5.search('234-879-8543') != None
    # test for another standard case
    ans['678-5678'] = regex5.search('678-5678') != None
    # test for another standard case
    ans['846.087.0582'] = regex5.search('846.087.0582') != None
    # test for another standard case
    ans['+1 706 459 3223'] = regex5.search('+1 706 459 3223') != None
    # test for another standard case
    ans['1(657)897-9669'] = regex5.search('1(657)897-9669') != None
    # test for another standard case
    ans['6679875432'] = regex5.search('6679875432') != None
    # test for not correct number divisions
    ans['35-36-3676-36'] = regex5.search('35-36-3676-36') != None
    # test for two different parentheses
    ans['(325)(2353255)'] = regex5.search('(325)(2353255)') != None
    # test for over length
    ans['765432123456'] = regex5.search('765432123456') != None
    # test for insufficient length and incorrect number divisions
    ans['5678.98'] = regex5.search('5678.98') != None

    for key, value in ans.items():
        print(key + ": " + str(value))

#findSHStartLengthFour()
#findDuplicate()
#findBAB()
#findNumAndWords()        
#findPhoneNum()
    
