import os

#get current location folder
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

badsentencelist = []

#Generate list of badwords
with open (os.path.join(__location__, 'wrong_devs.txt')) as misFile:
    for line in misFile:

        #extract sentence out of wrong devs
        sentence_start = line.find(",")
        sentence_end = line.rfind(",")
        sentence = line[sentence_start+2:sentence_end]

        #we generate a list of bad sentences
        badsentencelist.append(sentence[:len(sentence)-1])

    
#Remove badsentences from dev.tsv
with open('dev.tsv') as devfile, open('output.tsv', 'w') as outputfile:
    for line in devfile:
        for badsentence in badsentencelist:
            if line.find(badsentence) != -1:
                print(line)
