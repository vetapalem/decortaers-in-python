import time as iii
from functools import wraps
def infofile(gh):
    def caller(hj):
        # @wraps(hj)
        def player(*uk,**u):
            a=iii.time()
            
            print(f'{gh} before execution time is  {a/60:3.2f} and function is {hj.__name__}')
            # hi=hj(*uk,**u)
            print(f'{gh} the player details is {uk} and final time is {(iii.time()- a)/60:3.2f}')
        return player
    return caller
while True:
    @infofile('primer:')
    def gamer(nam,ag):
        print(f'the player name is {nam} and {ag} years old'.capitalize())
    vbi=gamer('ravi sankar',15)
    print(gamer.__name__)

    break
