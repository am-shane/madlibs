## Algorithm: Program prompts user for in/out filenames through userInputs, are opened, and are then passed to wordReplace function,
##            which will scan through the first line, finding placeholders and appending any non-placeholders to a list.
##            Once a placeholder is found it will be passed back to UserInputs so the user may fill in the blank.
##            The placeholder has its brackets and dashes replaced with spaces when printed to the user.
##            The new word is then passed back to WordReplace and is saved to to the list in order with other words.
##            Once a full line has had all its placeholders replaced, the line is written to the new file specified by the user.
##            The program then moves on to the next line, repeating the same process until all lines in the original file have
##            been iterated through and had their placeholders replaced and written to the new file.
##            The user then has the option to view the completed madlib and start a new game or quit.

## Austin Shane
## January 30, 2020

## Sources Used: https://stackoverflow.com/questions/423710/how-to-return-more-than-one-value-from-a-function-in-python/423722
##               https://stackoverflow.com/questions/12538160/replacing-specific-words-in-a-string-python
##               https://stackoverflow.com/questions/1832528/is-close-necessary-when-using-iterator-on-a-python-file-object
##               https://www.geeksforgeeks.org/join-function-python/

######################## USER INPUTS FUNCTION ########################################

def userInputs(type, fileInputName, fileOutputName):
    '''Function contains prompts for user to input information needed to complete madlib'''
    if type == "FIN":
        fileInputName = input("What is the name of the madlibs file to be used? (include file extension): ") ##user inputs file name to open
        try: #exception handling for fileInputName
            file = open(fileInputName, "r") ##opens file inputed by user
            print("File has been found and opened!")
            return file, fileInputName
        except:
            print("File not found.") ##continuously reprompts until user inputs openable file
            userInputs("FIN")

    elif type == "FON":
        fileOutputName = input("what will the file name of the completed madlibs file be? (include file extension): ") ##user enters name of new file
        newFile = open(fileOutputName, "w") ##writes file and adds .txt file extention to inputed name
        ##readNewFile = open(fileOutputName, "r")
        return newFile, fileOutputName
    elif type == "DIS":
        openNewFile = open(fileOutputName, "r") #opens completed madlib in read mode
        print("You have completed filling in all blanks found.")
        toDisplay = input("Would you like to view the completed MadLib? Enter Y/N: ") #prompts user to view completed madlib
        if toDisplay == "Y" or toDisplay == "y": #accounts for  normal inputs
            #print(lineList)
            #for line in lineList: #did not work correctly
                #print(line + "\n")
            print("Completed Madlib for " + fileInputName + ": \n ______________________________________________________") #gives visual seperation to completed madlib
            for line in openNewFile:
                print(line)
            print(" ______________________________________________________") #ends visual seperation
        elif toDisplay == "N" or toDisplay == "n": #accounts for potential inputs
            print("viewing " + fileOutputName + " has been skipped.")
        elif toDisplay != "Y" or toDisplay != "y" or toDisplay != "N" or toDisplay != "n":
            #print(toDisplay)
            print("Invalid input! enter Y or N!") #reprompts user if Y/Nstyle input not found
            userInputs("DIS")
    elif type == "PA":
        again = input("would you like to complete another Madlib? Enter Y/N: ") #prompts usser to start another game
        if again == "Y" or again == "y":
            print("starting new game... \n \n")
            main() #goes back to beginning
        elif again == "N" or again == "n":
            print("Ending game...")
            exit("Madlib game is closed.") #exits program with message
        elif again != "Y" or again != "y" or again != "N" or again != "n":
            print("invalid input! enter Y or N!")
            userInputs("PA") #reprompts user if valid input not found

    else:
        word = str(type).replace("-", " ") #replaces dash in string with space
        toReplace = str(input("enter a "+ word[1:-1]+": ")) ##user inputs new word to replace placeholder, when placeholder is printed the "<" and ">" are clipped off the ends
        return toReplace

################################ Word Replacement Function ############################################################

def wordReplace(file, newFile, fileInputName, fileOutputName):
    '''function will iterate through a line of text, pass a word with </> to the userInputs function to enter a new word,
    words will then be appended to a list in the correct order, combined again, and the line will be written to the new document'''
    for line in file: #iterates through each line
        wordList = [] #creates new lists for words in the line
        #lineList = [] #not needed, used other method
        for word in line.split(): #iterates through words in the line
            if "<" and ">" in word:
                toReplace = userInputs(word, fileOutputName, fileOutputName) ##passes word to userInputs function so user can input new word
                wordList.append(str(toReplace))  ##appends new word to wordList
            else:
                wordList.append(word) ##if word does not have brackets append it without change
        lineToWrite = " ".join(wordList) ##joins all words in list into one line with spaces between each word
        #lineList.append(lineToWrite) #did not work correctly
        newFile.write(str(lineToWrite) + "\n") ##writes line to newFile and goes to next line to keep text in same formatting
        #print(lineToWrite)

######################## Main Function #################################################################################

def main():
    '''connects userInputs and wordReplace functions together'''
    file, fileInputName = userInputs("FIN",0,0) ##prompts for file name (FIN = File Input Name)
    newFile, fileOutputName = userInputs("FON",0,0) ## user inputs new file name (FON = File Output Name)
    wordReplace(file, newFile, fileInputName, fileOutputName)
    file.close()  # closes files used
    newFile.close()
    userInputs("DIS", fileInputName, fileOutputName) ##prompts user to view completed file (DIS = Display)
    userInputs("PA", fileInputName, fileOutputName) ##prompts to complete another madlib (PA = Play Again)
main() ##runs main