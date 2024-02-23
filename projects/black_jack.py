import random, sys

HEARTS = chr(9829) # Символ 9829 — '♥'
DIAMONDS = chr(9830) # Символ 9830 — '♦'.
SPADES = chr(9824) # Символ 9824 — '♠'.
CLUBS = chr(9827) # Символ 9827 — '♣'.

BACKSIDE = 'backside'

def main():
    print('''Правила:
        Попытайся дойти до 21 как можно ближе,
        дама король валет - 10 очков
        туз - 1 или 11
        обычные карты 2-10 по их значению
        (H)it что бы взятьк арту
        (S)tand чтобы закончить брать карты
        В начале ты можешь нажать (D)ouble down чтобы удвоить ставку
        В случае ничьи деньги возвращаются игроку''')
    
    money = 5000
    while True:
        if money <= 0:
            print('У тебя кончились деньги ты проиграл')
            sys.exit()
    
        print('Деньги: ', money)
        bet = getBet(money)
        
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print("Ставка:", bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()
            
            if getHandValue(playerHand) > 21:
                break
            move = getMove(playerHand, money - bet)
            
            if move == 'D':
                additionalBet = getBet(min(bet, (money -bet)))
                bet += additionalBet
                print("Ставка увеличена на {}.".format(bet))
                print("Ставка:", bet)

            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                print('Ты вытащил {} {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue
            
            if move in ('S', 'D'):
                break
            
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("Дилер берет...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                input("Нажмите enter чтобы продолжить..")
                print('\n\n')

        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if dealerValue > 21:
            print("Дилер проиграл!Ты выиграл ${}".format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("Ты проиграл!")
            money -= bet
        elif (playerValue > dealerValue):
            print("Ты выиграл {}$".format(bet))
            money += bet
        elif playerValue == dealerValue:
            print("Ничья, деньги возвращаются")

        input('Нажми Enter чтобы продолжить..')
        print('\n\n')

def getBet(maxBet):
    while True:
        print("Сколько ты хочешь поставить?(1-{}, или QUIT)".format(maxBet))
        bet = input('>').upper().strip()
        if bet == "QUIT":
            sys.exit()
        
        if not bet.isdecimal():
            continue

        bet = int(bet)

        if 1 <= bet <= maxBet:
            return bet
        
def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in  range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'K','Q','A'):
            deck.append((rank, suit))
        random.shuffle(deck)
        return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print("Дилер:", getHandValue(dealerHand))
        displayCards(dealerHand)
    else: 
        print("Диллер: ???")
        displayCards([BACKSIDE] + dealerHand[1:])

    print('Игрок: ', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K','Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value


def displayCards(cards):
    rows = ['','','','','']
    for i, card in enumerate(cards):
        rows[0] += '___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)


def getMove(playerHand, money):
    moves = ['(H)Еще', '(S)Хватит']

    if len(playerHand) == 2 and money > 0:
        moves.append('(D)Повысить')

    movePrompt = ', '.join(moves) + '> '
    move = input(movePrompt).upper()
    if move in ('H', 'S'):
        return move
    if move == 'D' and '(D)Повысить' in moves:
        return move
    
if __name__ == '__main__':
    main()