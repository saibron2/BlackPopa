import random

def create_cards():
    cards = []
    for i in range(2,11):
        for j in('C','P','B','K'):
            cards.append(str(i)+j)
    for i in('J','Q','K','T'):
        for j in('C','P','B','K'):
            cards.append(i+j)
    return cards


def start_cards(cards):
    hand = []
    for i in range(2):
        hand.append(random.choice(cards))
        cards.remove(hand[-1])
    return hand, cards

def start_bot_cards():
    bot_cards = []
    for i in range(2,11):
        for j in('C','P','B','K'):
            bot_cards.append(str(i)+j)
    for i in('J','Q','K','T'):
        for j in('C','P','B','K'):
            bot_cards.append(i+j)
    return bot_cards
    
def start_bot_hand(bot_cards):
    bot_hand = []
    for i in range(2):
        bot_hand.append(random.choice(bot_cards))
        bot_cards.remove(bot_hand[-1])
    return bot_hand, bot_cards

def bot_newcard(bot_cards, bot_hand):
    botyn = ['y','n']
    bot_hand = start_bot_hand(bot_cards)
    print('Will you take one more card?(y,n)')
    res = random.choice(botyn)
    print(res)
    if res == 'y':
        bot_cards = start_bot_cards()
        bot_hand.append(random.choice(bot_cards))
        print(f'Bot have {bot_hand}')
    elif res == 'n':
        bot_hand = bot_hand
        print(f'Bot have {hand}')
    return bot_cards, bot_hand
        
def start_game():
    cards = create_cards()
    hand = []
    hand, cards = start_cards(cards)
    print(f'You have {hand}')
    res = input('Will you take one more card?(y,n)')
    if res == 'y':
        cards = create_cards()
        hand.append(random.choice(cards))
        print(f'You have {hand}')
    elif res == 'n':
        hand = hand
        print(f'You have {hand}')
    else:
        print('Sorry, i don`t understand you, write again')
bot_newcard(bot_cards, bot_hand)
    
start_game()
    
