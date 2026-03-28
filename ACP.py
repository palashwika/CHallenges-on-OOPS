
class Numeral:
    def __init__(self):
        self.number={1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 1000:"M", }
    

    def convert(self):
        while (True):
            #number,numeral=list(self.number.items()); not needed, we do not need to convert as a list
            user=int(input("Enter a number you wanna convert to numerals"))
            result=""

            for value in sorted(self.number.keys(), reverse=True): #go through each digit in dictionary; REVERSE=TRUE makes from BIGGEST to SMALLEST; value refers to keys
                 while user >= value:  #is hte num >= keys
                    result = result+self.number[value] #brackets are for dictionary indexing for accessing value from for loop
                    user = user - value #user keeps getting overrided by subtracting added numeral value

        #1994
        #1994>=1000
        #0=0+M
        #1994-1000 

            print("Roman number: ",result)
    
    # LINE 13 Inside the loop, when value == 900: 
#print(value)               # → 900   (the key)
#print(self.number[value])  # → "CM"  (the dictionary value)

            
            #if(user)==number:
                #print(numeral)
            #else:
                #print("We can only convert some numbers")

            option=int(input("enter 0, if you want to play again otherwise enter 1: "))
            if (option):
                break


num=Numeral()
num.convert()


