# Austin Whitley 08/27/2021
# Assignment 2

#  Imports to use the Random Library
import random

# Main module to run code
def main():
    userChoice()

# Default list of vocab

# Take the user input to ask if they would like to choose default words or use their own
def userChoice():
    # Converts to lower to help make the if/else unbreakable
    userInput = input("Would you like to use your own words (yes or no): ").lower()
    # If user selects yes it runs the functions that collect the words
    if userInput == "yes":
        print("user input selected")
        # Each function returns a list of words
        nouns = chooseNouns()
        verbs = chooseVerbs()
        adjectives = chooseAdjectives()
        articles = chooseArticles()
        # Function call sending the lists of words
        createSentence(nouns,verbs,adjectives,articles)
    # If user selects to use default a hard coded list of words is created
    elif userInput == "no":
        print("default selected")
        defaultNouns = ["dog","desk","energy drink", "key"]
        defaultVerbs = ["jumps", "sits", "drives", "rides"]
        defaultAdjectives = ["purple", "hot", "big", "small"]
        defaultArticles = ["A", "The", "Those", "That"]
        # Hard coded lists are sent with function call
        createSentence(defaultNouns,defaultVerbs,defaultAdjectives,defaultArticles)
    # If a choice other than yes or no is entered the user is made aware and the function is called again
    else:
        print("Unusble input entered. Try Agian")
        userChoice()

# Function used to collect nouns returns a list
def chooseNouns():
    print("\nNouns:\n")
    nouns = []
    count = 1
    # While loop used to collect only 3 nouns and add to the list 
    while count <= 3:
        userNoun = input("Please Enter a noun: ").lower()
        nouns.append(userNoun)
        count = count + 1
    return nouns

# Funtion used to collect verbs return a list
def chooseVerbs():
    print("\nVerbs:\n")
    verbs = []
    count = 1
    # While loop used to collect only 3 verbs and add to the list
    while count <= 3:
        userVerb = input("Please Enter a verb: ").lower()
        verbs.append(userVerb)
        count = count + 1
    return verbs

# Function used to collect adjectives returns a list
def chooseAdjectives():
    print("\nAdjectives:\n")
    adjectives = []
    count = 1
    # While loop used to collect only 3 adjectives and add to the list
    while count <= 3:
        userAdjective = input("Please Enter an adjective: ").lower()
        adjectives.append(userAdjective)
        count = count + 1
    return adjectives

# Function used to collect articles reutns a list
def chooseArticles():
    print("\nArticles:\n")
    articles = []
    count = 1
    # While loop used to collect only 2 articles and add to the list
    while count <= 2:
        userArticles = input("Please Enter an article: ").lower()
        articles.append(userArticles)
        count = count + 1
    return articles

# Function that takes in lists, ceates a random sentece and prints the sentence
def createSentence(nouns, verbs, adjectives, articles):
    print("\nRandom Sentences:\n")
    count = 1
    # While loop used to create only 3 sentences
    while count <= 3:
        # random.choice is used to select a random index from the list \
        randomArticle = random.choice(articles)
        randomAdjective = random.choice(adjectives)
        randomNoun = random.choice(nouns)
        randomVerb = random.choice(verbs)
        # Creates the sentence to print
        sentence = f"{randomArticle.title()} {randomAdjective.lower()} {randomNoun.lower()} {randomVerb.lower()}"
        print(sentence)
        count = count + 1

# Runs program
main()