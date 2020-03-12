class CardGroupType:
    Tonghuashun=9
    Tiezhi=8
    Hulu=7
    Tonghua=6
    Shunzi=5
    Santiao=4
    Liangdui=3
    Duizi=2
    Sanpai=1

class Card:
    Number = 2
    Face = "D"

class CardGroup:
     type = 0
     cards = []
     cmpNumber = 0
     cmpNumber2 = 0
     cmpNumber3 = 0
     cmpNumber4 = 0
     cmpNumber5 = 0

class CompareCard:
    def compare(self,A,B):
        mp = {"T":10,'J':11,'Q':12,"K":13,"A":14}
        for i in range(2,10):
            mp[str(i)]=i
        arr = A.split(" ")
        cardsA =[]
        for ss in arr:
            card = Card()
            card.Face = ss[1]
            card.Number = mp[ss[0]]
            cardsA.append(card)
        arr = B.split(" ")
        cardsB = []
        for ss in arr:
            card = Card()
            card.Face = ss[1]
            card.Number = mp[ss[0]]
            cardsB.append(card)
        cardsA = sorted(cardsA,key=lambda x:x.Number)
        cardsB = sorted(cardsB,key=lambda x:x.Number)
        cardGroupA = self.__parseCardGroup(cardsA)
        cardGroupB = self.__parseCardGroup(cardsB)
        # print(cardGroupA.type,cardGroupA.cmpNumber,cardGroupA.cmpNumber2,cardGroupA.cmpNumber3,cardGroupA.cmpNumber4,cardGroupA.cmpNumber5)
        # print(cardGroupB.type,cardGroupB.cmpNumber,cardGroupB.cmpNumber2,cardGroupB.cmpNumber3,cardGroupB.cmpNumber4,cardGroupB.cmpNumber5)
        arr = [cardGroupA,cardGroupB]
        arr = sorted(arr,key=lambda x:[x.type,x.cmpNumber,x.cmpNumber2,x.cmpNumber3])
        if cardGroupA.type==cardGroupB.type and cardGroupA.cmpNumber==cardGroupB.cmpNumber \
                and cardGroupA.cmpNumber2==cardGroupB.cmpNumber2 and cardGroupA.cmpNumber3==cardGroupB.cmpNumber3:
            return 'Tie game'
        if arr[1]==cardGroupA:
            return "Black wins"
        if arr[1]==cardGroupB:
            return "White wins"
        if cardGroupA.type==cardGroupB.type and cardGroupA.cmpNumber==cardGroupB.cmpNumber \
            and cardGroupA.cmpNumber2==cardGroupB.cmpNumber2 and cardGroupA.cmpNumber3==cardGroupB.cmpNumber3:
            return 'Tie game'


        pass

    def __parseCardGroup(self,cards):
        cardGroup = CardGroup()
        if cards[0].Face == cards[1].Face ==cards[2].Face==cards[3].Face==cards[4].Face and\
            cards[0].Number+4==cards[1].Number+3==cards[2].Number+2==cards[3].Number+1==cards[4].Number:
            cardGroup.type = CardGroupType.Tonghuashun
            return cardGroup

        if cards[0].Number == cards[1].Number==cards[2].Number==cards[3].Number or\
            cards[4].Number == cards[1].Number==cards[2].Number==cards[3].Number:
            cardGroup.type = CardGroupType.Tiezhi
            cardGroup.cmpNumber = cards[2].Number
            return cardGroup

        if cards[0].Number == cards[1].Number and cards[2].Number == cards[3].Number== cards[4].Number\
                or cards[0].Number == cards[1].Number == cards[2].Number and cards[3].Number== cards[4].Number:
            cardGroup.type = CardGroupType.Hulu
            cardGroup.cmpNumber = cards[2].Number
            return cardGroup

        if  cards[0].Face == cards[1].Face ==cards[2].Face==cards[3].Face==cards[4].Face:
            cardGroup.type = CardGroupType.Tonghua
            cardGroup.cmpNumber = cards[4].Number
            return cardGroup
        if cards[0].Number+4==cards[1].Number+3==cards[2].Number+2==cards[3].Number+1==cards[4].Number:
            cardGroup.type = CardGroupType.Shunzi
            cardGroup.cmpNumber = cards[4].Number
            return cardGroup
        if cards[0].Number == cards[1].Number == cards[2].Number  or \
            cards[1].Number == cards[2].Number == cards[3].Number  or \
            cards[2].Number == cards[3].Number == cards[4].Number:
            cardGroup.type = CardGroupType.Santiao
            cardGroup.cmpNumber = cards[2].Number
            return cardGroup
        if cards[0].Number==cards[1].Number and cards[2].Number==cards[3].Number or \
                cards[0].Number==cards[1].Number and cards[3].Number==cards[4].Number or \
                cards[1].Number==cards[2].Number and cards[3].Number==cards[4].Number:
                cardGroup.type = CardGroupType.Liangdui
                cardGroup.cmpNumber = cards[3].Number
                cardGroup.cmpNumber2 = cards[1].Number
                if cards[0].Number==cards[1].Number and cards[2].Number==cards[3].Number:
                    cardGroup.cmpNumber3=cards[3].Number
                if cards[0].Number==cards[1].Number and cards[3].Number==cards[4].Number:
                    cardGroup.cmpNumber3=cards[2].Number
                if cards[1].Number==cards[2].Number and cards[3].Number==cards[4].Number:
                    cardGroup.cmpNumber3=cards[0].Number
                return cardGroup
        for i in range(4):
            if cards[i].Number == cards[i+1].Number:
                cardGroup.type = CardGroupType.Duizi
                cardGroup.cmpNumber = cards[2].Number
                return cardGroup
        cardGroup.type = CardGroupType.Sanpai
        cardGroup.cmpNumber = cards[4].Number
        cardGroup.cmpNumber2 = cards[3].Number
        cardGroup.cmpNumber3 = cards[2].Number
        cardGroup.cmpNumber4 = cards[1].Number
        cardGroup.cmpNumber5 = cards[0].Number
        return cardGroup

if __name__ == "__main__":
    cmp = CompareCard()
    #'2H 3D 5S 9C KD', '2C 3H 4S 8C AH'
    #'2H 4S 4C 2D 4H', '2S 8S AS QS 3S'
    #'2H 3D 5S 9C KD', '2C 3H 4S 8C KH'
    print(cmp.compare('2H 3D 5S 9C KD', '2C 3H 4S 8C KH'))