import random                                                                       

ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

suits = ("of hearts", "of diamonds", "of clubs", "of spades")
deck = [(rank, suit) for suit in suits for rank in ranks]
random.shuffle(deck)

p1_deck = deck[:26]
p2_deck = deck[26:]
table = []

def play_round(p1_deck, p2_deck, table):                         
    while len(p1_deck) != 0 or len(p2_deck) != 0:    
        print(f"Player 1 has {len(p1_deck)} cards")
        print(f"Player 2 has {len(p2_deck)} cards")
        if len(p2_deck) == 0:
            print("PLAYER 1 WINS!")
            break
        if len(p1_deck) == 0:
            print("PLAYER 2 WINS!")
            break
        if len(p1_deck) != 0 and len(p2_deck) != 0:       
            x,y = p1_deck.pop(0), p2_deck.pop(0)          
            card_comparison(x, y, p1_deck, p2_deck, table)
            print("")
            input("Press enter to continue")

def card_comparison(p1_card, p2_card, p1_deck, p2_deck, table):
    print(f"Player 1 played {p1_card}")
    print(f"Player 2 played {p2_card}")
    print("")
    if ranks.index(p1_card[0]) > ranks.index(p2_card[0]): 
        print("Player 1 has won the battle")
        p1_deck.append(p1_card) 
        p1_deck.append(p2_card)
    elif ranks.index(p1_card[0]) < ranks.index(p2_card[0]): 
        print("Player 2 has won the battle")
        p2_deck.append(p1_card) 
        p2_deck.append(p2_card)
    else:
        table.append(p1_card)
        table.append(p2_card)        
        print("WAR HAS BEGUN!")
        war(p1_deck, p2_deck, table)

def war(p1_deck, p2_deck, table):
    if len(p1_deck) < 4 or len(p2_deck) < 4:
        if len(p1_deck) == 0 or len(p2_deck) == 0:
            return
        else:
            table.append(p1_deck[0])
            table.append(p2_deck[0])
            p1_deck.remove(p1_deck[0])
            p2_deck.remove(p2_deck[0])
            print(f"Player 1 has {table[-2]} as its attacker!")
            print(f"Player 2 has {table[-1]} as its attacker!")
            if ranks.index(table[-2][0]) > ranks.index(table[-1][0]):
                p1_deck.extend(table)
                table.clear()
                print("Player 1 has won the war!")
            elif ranks.index(table[-2][0]) < ranks.index(table[-1][0]):
                p2_deck.extend(table)
                table.clear()
                print("Player 2 has won the war!")
            else:
                print("Draw! The war continues!")
                war(p1_deck, p2_deck, table)                             
    if len(p1_deck) > 4 and len(p2_deck) > 4:
        for _ in range(4):                                 
           x, y = p1_deck[0], p2_deck[0]
           table.append(x)
           table.append(y)
           p1_deck.remove(x)
           p2_deck.remove(y)
        print(f"Player 1 has {table[-2]} as its attacker!")
        print(f"Player 2 has {table[-1]} as its attacker!")
        if ranks.index(table[-2][0]) > ranks.index(table[-1][0]):   
            p1_deck.extend(table)
            table.clear()
            print("Player 1 has won the war!")
        elif ranks.index(table[-2][0]) < ranks.index(table[-1][0]):
            p2_deck.extend(table)
            table.clear()
            print("Player 2 has won the war!")
        else:
            print("Draw! The war continues!")
            war(p1_deck, p2_deck, table)

play_round(p1_deck, p2_deck, table)
