'''
    @Author: Rehan
    @Date: 2022-06-03 00:58:30
    @Last Modified by: Rehan
    @Last Modified time: 2022-06-03 00:47:30
    @Title : Program to simulate a Gambling condition for a bet
    '''

import random
if __name__ == '__main__':
    STAKE=100
    BET_AMOUNT=1
    GOAL=200
    bets=0
    won=0
    while 0<STAKE<GOAL:
        bets=bets+1
        chance=random.randint(0,1)
        if chance==1:
            won=won+1
            STAKE=STAKE+1
        else:
            STAKE=STAKE-1
    if STAKE>=GOAL:
        print("Player Won")
        print("Number of bets Won:",won)
        print("Bets Won:",(((won/bets)*100)),"%")
        print("Bets Lose:",(((bets-won)/bets)*100),"%")
    else:
        print("Player Lose")
        print("Number of bets Won:",won)
        print("Bets Won:",(((won/bets)*100)),"%")
        print("Bets Lose:",(((bets-won)/bets)*100),"%")