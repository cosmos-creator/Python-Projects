'''
RULES :

Both player and the dealer gets 2 cards in hand.
If the sum reaches 21 for either of them then it is a win for them.
Otherwise if the sum exceeds 21 for either of them, it's a win for the other.
If the dealer is at 17 he won't draw another card i.e he will stay/stand, then it depends upon the player whether they chooses to draw a card or not.
If the dealer has 17 or greater and you have less than him and you choos to stay then its a win for dealer.
Likewise if the dealer has 17 or greater and you draw greater than him then its your win.
    HAPPY WINING!
'''
from random import randint
import time
def black_jack():
    
    player_draw_1 = randint(1,11)
    player_draw_2 = randint(1,11)
    
    dealer_draw_1 = randint(1,11)
    dealer_draw_2 = randint(1,11)
    
    player_total = player_draw_1+player_draw_2
    dealer_total = dealer_draw_1+dealer_draw_2
    
    player_draws = 0
    dealer_draws = 0
    
    if player_draw_1+player_draw_2 <= 21 and dealer_draw_1+dealer_draw_2 <= 21:
        print("Player's first draw :",player_draw_1)
        time.sleep(2)
        print("Dealer's first draw :",dealer_draw_1)
        time.sleep(2)
        print("Player's second draw :",player_draw_2)
        time.sleep(2)
        print("Dealer's second draw :",dealer_draw_2)
        print()
        print("Dealer total : ",dealer_total)
        print("Player total : ",player_total)
        print()
        if (player_total==21) and (dealer_total==21):
            print("Its a draw")
            return None
        elif player_total ==21:
            print("Player wins")
            return None
        elif dealer_total ==21:
            print("Dealer wins!")
            return None
        decision = input("Will you draw another card or stay? [Draw : Y | Stay : N] :")
        while decision.lower() == 'y':
            player_draws+=1
            draw = randint(1,11)
            player_total+=draw
            print("Card drawn : ",draw)
            print("Total : ",player_total)
            decision = ''
            if player_total<21:
                decision = input("Will you draw a card again? [Draw : Y | Stay : N] : ")
                if decision.lower()=='y':
                    continue
                else :
                    break
            elif player_total == 21:
                time.sleep(3)
                print("You win!")
                return None
            else:
                print("Bust!")
                print('You lost!')
                return None
                
        if decision.lower()=='n':
            print("You chose to stay!")
            time.sleep(2)
            print("Passing on the turn to the dealer!")
            print("Dealers turn")
            print()
            while dealer_total < 17:
                dealer_draw = randint(1,11)
                dealer_draws+=1
                dealer_total+=dealer_draw
                if dealer_total == 21:
                    print("Dealer won!")
                    return None
                elif dealer_total >21:
                    print("You win!")
                    print("Dealer busted!")
                    return None
                
            print(f"Dealer hand is at {dealer_total}, he will stand \n")
            if player_total>dealer_total:
                time.sleep(3)
                print("You win!")
                return None
            elif player_total==dealer_total:
                time.sleep(2)                   
                print()
                print("Dealer total :",dealer_total)
                print("Player total :",player_total)
                print("Both has the same score!")
                print("It's a draw!")                    
                return None                    
            else:
                time.sleep(2)
                print("Dealer has more than you!")
                print("He won!")
                return None
                    
    elif player_draw_1+player_draw_2 > 21 and dealer_draw_1+dealer_draw_2 > 21:
        print("Player's first draw :",player_draw_1)
        time.sleep(2)
        print("Dealer's first draw :",dealer_draw_1)
        time.sleep(2)
        print("Player's second draw :",player_draw_2)
        time.sleep(2)
        print("Dealer's second draw :",dealer_draw_2)
        print()
        print("Dealer total : ",dealer_draw_1+dealer_draw_2)
        print("Player total : ",player_draw_1+player_draw_2)
        print()
        print("It's a draw!")
        return None
        
    
    elif dealer_draw_1+dealer_draw_2 > 21 :
        print("Player's first draw :",player_draw_1)
        time.sleep(2)
        print("Dealer's first draw :",dealer_draw_1)
        time.sleep(2)
        print("Player's second draw :",player_draw_2)
        time.sleep(2)
        print("Dealer's second draw :",dealer_draw_2)
        print()
        print("Dealer total : ",dealer_draw_1+dealer_draw_2)
        print("Player total : ",player_draw_1+player_draw_2)
        print()
        print("Dealer busted!\n You win!")
        return None
        
    elif player_draw_1+player_draw_2 >21:
        print("Player's first draw :",player_draw_1)
        time.sleep(2)
        print("Dealer's first draw :",dealer_draw_1)
        time.sleep(2)
        print("Player's second draw :",player_draw_2)
        time.sleep(2)
        print("Dealer's second draw :",dealer_draw_2)
        print()
        print("Dealer total : ",dealer_draw_1+dealer_draw_2)
        print("Player total : ",player_draw_1+player_draw_2)
        print()
        print("Busted!")
        print("You lost!")
        return None

black_jack()
