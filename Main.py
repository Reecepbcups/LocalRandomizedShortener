import random, string

# {FORMAT} #
# xztlm3=www.test.com
# msdjlv=www.test2.com
# This program rotates comparing index 0 and 1 to the provided string
# It checks the users shortened, or if the link is already in the file
# if so it will just return the opposite (kaldhY returns www.t.com)




def textFileLines(fileName='shortener.txt'):
    _tmp = open('shortener.txt', 'a');_tmp.close()#makeSureFileIsThere
    allLines =  open(fileName, 'r')
    return allLines

def func(link):
    foundLink = False
    alphabet = string.ascii_letters + string.digits
    

    # check if the user link in the txt file, saves random space (fbhuah always = faceook.com)
    links = textFileLines()
    
    for line in links:
        if line.split('=')[1].replace('\n','') == link:
            print(f"Your shortened link: {line.split('=')[0]}") # the random link gen for same link
            foundLink = True
        elif line.split('=')[0].replace('\n','') == link:
            print(f"Your Link: {line.split('=')[1]}") # the random link gen for same link
            foundLink = True

    # if link is not found in text file
    if foundLink == False:
        for line in links:
            if line.split('=')[0] == link:
                print(f"")
                
        shortend = ''.join([random.choice(alphabet) for i in range(6)])
        # checks to make sure the same gen is not already made
        for line in links:
            if line.split('=')[0] == shortend:
                shortend = ''.join([random.choice(alphabet) for i in range(6)])
        
        f = open('shortener.txt', 'a')
        f.write(shortend+'='+link+'\n')
        print(f'Your shortened link: {shortend}')
        f.close()

while True:            
    link = input('Link to shorten/decode > ')
    func(link)
