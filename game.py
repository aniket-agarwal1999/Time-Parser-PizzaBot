data={'pool':'game','snooker':'game','tt':'game','table':'game','tennis':'game','fooseball':'game','carrom':'game','carromboard':'game','chess':'game','chessboard':'game','khelna':'game', 'board':'game'}

def game_decider():
    print("Welcome to the gaming portal")
    print("So what do you want to play from the following: ")
    print("Snooker pool")
    print("Table tennis")
    print("Fooseball")
    print("Carrom")
    print("Chess")

    response = input()
    response = response.lower()
    res = response.split('and')   #As the user can ask for more than one games

    if len(res) == 1:
        res_firstGame = res[0].spilt()
        i=0
        while i<len(res_firstGame):
            if res_firstGame[i] in data:
                if res_firstGame=='pool'



def poolGame():
    print("***********So you are in the Snooker pool game portal!!***********")
    print("At what time do you wish to book the snooker table.")
    time = input()
    time = time.lower()
    time_list = time.spilt()

