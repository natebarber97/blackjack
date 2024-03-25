class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chips = 50
        self.val = 0
        self.blackjack = False
        self.bust = False
    
    def showHand(self):
        print(self.name + ", your current hand is:")
        for card in self.hand:
            print(card[1])
        print("your current value is", self.val, "\n")

    def wager(self):
        num = input(self.name + ", please select how many chips you would like to wager: ")
        if num < 1:
            print("You cannot wager a negative amount. Placing your wager as the minimum amount (1 chip)")
            num = 1
        return num
    
    def addToHand(self, card):
        self.hand.append(card)
        if (self.val + card[0] > 21) and (card[0] == 11):
            card[0] = 1
        self.val = self.val + card[0]
    
    def resetHand(self):
        self.hand = []
        self.val = 0
        self.blackjack = False
        self.bust = False
