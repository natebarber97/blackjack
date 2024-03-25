


#TODO: implement inheritence for players and npc dealer
#      add betting functionality




import random
from player import Player

def initializeDeck():
    deck = []
    initializeDeckHelper(deck, "ace")
    initializeDeckHelper(deck, "jack")
    initializeDeckHelper(deck, "queen")
    initializeDeckHelper(deck, "king")

    for i in range(2, 11):
        initializeDeckHelper(deck, i)

    return deck

def initializeDeckHelper(deck, val):
    temp = val
    if val == "ace":
        val = 11
    elif val in ["jack", "queen", "king"]:
        val = 10
    temp = str(temp)
    deck.append([val, temp + " of spades"])
    deck.append([val, temp + " of diamonds"])
    deck.append([val, temp + " of clubs"])
    deck.append([val, temp + " of hearts"])

def distributeCard(deck, p):
    p.hand.append()

def printRules():
    print("All players begin with 50 chips. Players have to bet at least 1 chip each round.")
    print("The goal is to have a higher hand than the dealer without exceeding a value of 21.")
    print("Players will draw cards in order, then the dealer will draw.")
    print("A player immediately wins a round if they have a blackjack and the dealer does not also have a blackjack.")
    print("If a player busts or has a lower hand than the dealer, they lose their bet.")
    print("If a player has a higher hand than the dealer, they win their bet.")
    print("If a player has an equal hand to a dealer, no bets are won or lost.")
    print("A blackjack is considered a higher hand than other hands equaling 21.\n")



while True:
    numPlayers = int(input("Select from between 1 and 6 players: "))
    if 1 <= numPlayers <= 6:
        break
    print("invalid input")

players = []
dealer = Player(name = "dealer")

for i in range(numPlayers):
    pName = input("Please enter player " + str(i + 1) + "\'s name: ")
    p = Player(pName)
    players.append(p)
    print("hello, " + p.name + "! " + "You will start with one visible card and one hole card.\n")
    pHelp = input("press the \'h\' key if you need to go over the rules. Otherwise press \'enter\'. ")
    print()
    if pHelp == 'h':
        printRules()


cont = 'y'
while cont != 'n':
    deck = initializeDeck()
    random.shuffle(deck)

    for i in range(2):
        for player in players:
            player.addToHand(deck.pop())
        dealer.addToHand(deck.pop())

    for player in players:
        print(player.name + "\'s turn:")
        player.showHand()
        if player.val == 21:
            print("blackjack!")
            player.blackjack = True
        else:
            dec = 0
            while dec != '2':
                dec = input("select \'1\' to hit or \'2\' to hold: ")
                print()
                if dec == '1':
                    player.addToHand(deck.pop())
                    player.showHand()
                    if player.val > 21:
                        print("Bust!\n")
                        player.bust = True
                        break


    if dealer.val == 21:
        dealer.showHand()
        print("blackjack!")
        dealer.blackjack = True
    else:
        while dealer.val <= 17:
            dealer.addToHand(deck.pop())
        dealer.showHand()
        if dealer.val > 21:
            print("bust!")
            dealer.bust = True


    for player in players:
        if player.bust or (dealer.blackjack and not player.blackjack) or ((player.val < dealer.val) and not dealer.bust):
            print(player.name + " loses")
        elif (player.val == dealer.val) or (player.blackjack and dealer.blackjack):
            print(player.name + " stalemates")
        else:
            print(player.name + " wins!")
        player.resetHand()
    dealer.resetHand()

    cont = input("select \'n\' to exit the game, otherwise press \'enter\' ")
    print()


                    


                

