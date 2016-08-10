import random


class Deck(object):
    def __init__(self):
        self.cards = []

    def generateDeck(self, suits = ['hearts', 'clubs', 'diamonds', 'spades'], values = range(1, 14)):
        suits = suits
        values = values

        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

        self.shuffle()

    def shuffle(self):
        numCards = len(self.cards)

        for i in range(numCards-1, 0, -1):
            randomNum = random.randrange(0, i)
            (self.cards[i], self.cards[randomNum]) = (self.cards[randomNum], self.cards[i])

    def deal(self, playerList, numCards = 7):
        for i in range(numCards):
            for player in playerList:
                if len(self.cards) > 0:
                    player.hand.append(self.cards[0])
                    self.cards.pop(0)
                else:
                    return "Empty deck"
        return "Dealt cards"

    def show(self):
        for each in self.cards:
            each.show()


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print "card is", self.suit, self.value


class Player(object):
    def __init__(self, name="player"):
        self.name = name
        self.hand = []

    def draw(self, deck, numCards=1):
        if len(deck.cards) > 0:
            deck.deal([self], numCards)
        else:
            print "No cards to draw"
        return self

    def discard(self, cardIndex, location=[]):
        if 0 <= cardIndex < len(self.hand):
            location.append(self.hand.pop(cardIndex))
        else:
            print "that's not a card index"
        return self

    def show(self):
        print self.name
        for card in self.hand:
            print card.suit, card.value

deck = Deck()
deck.generateDeck()
deck.show()

playerList = [Player("player {}".format(i+1)) for i in range(4)]
print deck.deal(playerList)

for player in playerList:
    player.show()
