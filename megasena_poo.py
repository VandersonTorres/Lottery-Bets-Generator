###################################     LOTTERY GAME GENERATOR     ###################################
##                                                                                                  ##
##                                           DESCRIPTION:                                           ##
##                                                                                                  ##
##                      Brazilian Lottery whose raffle 6 dozens of numbers from 0 to 60             ##
##                                                                                                  ##
######################################################################################################

from random import sample

sena_2021 = [12,15,23,32,33,46]

class Lottery:
    def __init__(self,amount): 
        self.amount = amount
    
    def raffle_dozens(self):                                                        # This Method, criate a list of 6 random numbers not repeated
        lista = list(range(1,61)) 
        game = sample(lista,6)
        game.sort()
        print (game)
        return (game)

    def play(self):                                                                 # This Method enables playing many times as user wants
        self.amount = int(input('How many bets do you want to place?\n'))           # Amount of bets beeing played
        counter = 0
        while counter < self.amount:
            play = self.raffle_dozens()
            counter += 1
            if play == sena_2021:
                print (f'CONGRATULATIONS! You Won on the {counter}ª bet!')          # If user hits 'sena_2021', a congratulation message is displayed
                break
        print (f'You placed {counter} times!')                                      # Total amount of bets
        self.verify()
        
    def verify(self):                                                               # This Method verify if the program is going to keep running after a raffle
        question = input("Do you wish to keep betting?\n")
        if question in ["YES","Y","Yes",'yes','y']:
            _continue = Lottery(self.amount)
            _continue.play()
        else: print ("You are out the application...")     

game1 = Lottery(0)
game1.play()