class Flashcard:
    def __init__(self, word, meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):

        #we will return a string
        return self.word+'('+self.meaning+')'
    

flash =[]
print("Welcome to the flashcard application")

#the following loop will be repeated until
#user stops to add the flashcards

while(True):
    word=input("enter the name you want to add to flashcard : ")
    meaning = input("enter the meaning of the word : ")

    flash.append(Flashcard(word, meaning))
    option=int(input("enter 0, if you want to add another flaschard otherwise enter 1 : "))

    if (option): #getting out of while loop; 0=true, 1=false in computer language
        break

#printing all the flashcards
print('\nYour flashcards')
for i in flash:
    print(">", i)