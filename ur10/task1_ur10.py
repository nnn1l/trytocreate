def oops():
    raise KeyError('Oh no... You need to think about it one more time!')
    #raise IndexError('Oops! It seems that it is too hard for you. Would you stop?')

def catch():
    try:
        oops()
    except IndexError:
        print('Haha! I caught you!')

catch()
