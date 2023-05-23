import random
def prepare_card():
    symbol_list=['C','D','S','H']
    number_list=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    card_list=[]
    number_list4=number_list*4
    for symbol in symbol_list:
        for number in number_list:
            if number == 1:
                card=symbol+'A'
            elif number==11:
                card=symbol+'J'
            elif number==12:
                card=symbol+'Q'
            elif number==13:
                card=symbol+'K'
            else:
                card=symbol+str(number)
            card_list.append(card)
        card_dict = dict(zip(card_list,number_list4))
    return card_dict,card_list
def card_draw(card_list,n):
    card_draw=card_list[n]
    return card_draw
def check_card():
    print("まだひきますか y/n=0/1")
    number=int(input())
    return number
def goukei(card_draw,card_dict):
    int_card_draw=[]
    for i in card_draw:
        int_card_draw.append(card_dict[i])
    sume=sum(int_card_draw)
    print("sum=",sume)
    return sume
def oute(sume):
    if sume >21:
        print("バーストです")
        return 0
    return 1
def katimake(out1,out2,sume1,sume2):
    if out1<out2:
        print("2 win")
    elif out1>out2:
        print("1 win")
    else:
        if sume1<sume2:
            print("2 win")
        elif sume1>sume2:
            print("1 win")
        else:
            print("drow")
def syori(card_list,card_dict):
    n=0
    number1=0
    number2=0
    card_draw1=[]
    card_draw2=[]
    while True:
        if number1==0:
            card_draw1.append(card_draw(card_list,n))
            print("1",card_draw1)
            sume1=goukei(card_draw1,card_dict)
            out1=oute(sume1)
            if out1==0:
                number1=1
                breakev
            n=n+1
            number1=check_card()
        if number2==0:
            card_draw2.append(card_draw(card_list,n))
            print("2",card_draw2)
            sume2=goukei(card_draw2,card_dict)
            out2=oute(sume2)
            if out2==0:
                number2=1
                break
            n=n+1
            number2=check_card()
        elif number1==1 and number2==1:
            break
    return out1,out2,sume1,sume2
card_dict,card_list=prepare_card()
random.shuffle(card_list)
out1,out2,sume1,sume2=syori(card_list,card_dict)
katimake(out1,out2,sume1,sume2)