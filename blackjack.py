
import random

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter






def load_images(card_images):
    suits=["heart","diamond","club","spade"]
    face_cards=["king","queen","jack"]
    for suit in suits:
        for x in range(1,11):
            name=("cards\{}_{}.{}".format((x),suit,"ppm"))
            image=tkinter.PhotoImage(file=name)
            card_images.append((x,image,))
    
        for face in face_cards:
            name="cards\{}_{}.{}".format(face,suit,"ppm")
            image=tkinter.PhotoImage(file=name)
            card_images.append((10,image,))

def deal_card(frame):
    next_card=deck.pop(0)
    deck.append(next_card)
    tkinter.Label(frame,image=next_card[1],relief="raised").pack(side="left")
    return next_card

def score_hand(hand):
    score=0
    ace=False
    for next_card in hand:
        card_value=next_card[0]
        if card_value==1 and not ace:
            ace=True
            card_value=11
        score+=card_value
        if score>21 and ace:
            score-=10
            ace=False
    return score    

def deal_dealer():
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score=score_hand(dealer_hand)
    
    while 0<dealer_score<17:    
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score=score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    player_score=score_hand(player_hand)
    if dealer_score>21:
        result_text.set("player wins")
    elif player_score>dealer_score:
        result_text.set("player wins")
    elif player_score<dealer_score:
        result_text.set("dealer wins")
    else:
        result_text.set("draw!")
def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score=score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score>21:
        result_text.set("dealer wins")



    #global player_score
    #global player_ace
    #card_value=deal_card(player_card_frame)[0]
    #if card_value==1 and not player_ace:
    #    card_value=11
    #    player_ace=True
    #player_score+=card_value
    #if player_score>21 and player_ace:
    #    player_score-=10
    #    player_ace=False
    #player_score_label.set(player_score)    
    #if player_score>21:
    #    result_text.set("dealer wins!")

def new_game():
    global dealer_card_frame
    global player_card_frame
    global player_hand
    global dealer_hand
    
    dealer_card_frame.destroy()
    dealer_card_frame=tkinter.Frame(card_frame,background="green")
    dealer_card_frame.grid(row=0,column=1,sticky="ew",rowspan=2)
    player_card_frame.destroy()
    player_card_frame=tkinter.Frame(card_frame,background="green")
    player_card_frame.grid(row=2,column=1,sticky='ew',rowspan=2)
    player_hand.clear()
    dealer_hand.clear()
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()
    result_text.set("")

def play():
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()
    mainwindow.mainloop()

def shuffle():
    randon.shuffle(deck)
    
    

    




mainwindow=tkinter.Tk()
mainwindow.title("Black Jack")
mainwindow.geometry("640x480")
mainwindow.configure(background="green")

result_text=tkinter.StringVar()
result=tkinter.Label(mainwindow,textvariable=result_text)
result.grid(row=0,column=0,columnspan=3)

card_frame=tkinter.Frame(mainwindow,relief="sunken",borderwidth=1,background="green")
card_frame.grid(row=1,column=0,sticky='ew',columnspan=3,rowspan=2)
#DEALER_SCORE_LABEL
dealer_score_label = tkinter.IntVar() 

tkinter.Label(card_frame,text="dealer",background="green",fg="white").grid(row=0,column=0)
tkinter.Label(card_frame,textvariable=dealer_score_label ,background="green",fg="white").grid(row=1,column=0)    

#PLAYER_SCORE_LABEL
player_score_label=tkinter.IntVar()

tkinter.Label(card_frame,text="Player",background="green",fg="white").grid(row=2,column=0)
tkinter.Label(card_frame,textvariable=player_score_label,background="green", fg="white").grid(row=3,column=0)

#embedded frame to hold the card images
dealer_card_frame=tkinter.Frame(card_frame,background="green")
dealer_card_frame.grid(row=0,column=1,sticky="ew",rowspan=2)

#embedded frame to hold card images
player_card_frame=tkinter.Frame(card_frame,background="green")
player_card_frame.grid(row=2,column=1,sticky='ew',rowspan=2)

#button frame
button_frame=tkinter.Frame(mainwindow)
button_frame.grid(row=3,column=0,columnspan=3,sticky='w')

dealer_button=tkinter.Button(button_frame,text='dealer',command=deal_dealer)
dealer_button.grid(row=0,column=0)

player_button=tkinter.Button(button_frame,text='player',command=deal_player)
player_button.grid(row=0,column=1)
new_game_button=tkinter.Button(button_frame,text="new_game",command=new_game)
new_game_button.grid(row=0,column=2)

cards=[]
load_images(cards)
#print(cards)
#deck of cards are been shuffled
deck=list(cards)
random.shuffle(deck)
#create list to store dealer's and player's hands
dealer_hand=[]
player_hand=[]

'''deal_player()
dealer_hand.append(deal_card(dealer_card_frame))
dealer_score_label.set(score_hand(dealer_hand))
deal_player()'''


if __name__=="__main__":
    play()











