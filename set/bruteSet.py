
class card:
    def __init__(self, number, shape, color, fill):
        self.number = number
        self.shape = shape
        self.color = color
        self.fill = fill

    def isSet(self, c1, c2):
        vn = (self.number + c1.number + c2.number) % 3 == 0
        vs = (self.shape + c1.shape + c2.shape)% 3 == 0
        vc = (self.color + c1.color + c2.color)% 3 == 0
        vf = (self.fill + c1.fill + c2.fill)% 3 == 0

        return vn and vs and vc and vf

    def pretty_print(self):
        print self.number, self.shape, self.color, self.fill

if __name__ == "__main__":
    deck = []
    for color in range(3):
        for number in range(3):
            for fill in range(3):
                for shape in range(3):
                    print number, shape, color, fill
                    c = card(number, shape, color, fill)
                    deck.append(c)
    print "in", len(deck), "cards..."

    numSets = {}
    for card in deck:
        num = 0
        deck.remove(card)
        for c1 in deck:
            deck.remove(c1)
            for c2 in deck:
                if card.isSet(c1, c2):
                    card.pretty_print()
                    c1.pretty_print()
                    c2.pretty_print()
                    print ''
                    num += 1
            deck.append(c1)
        deck.append(card)
        numSets[card] = num
    
