

myList =[]

for x in range(0, 120):
    myList.append(x)

    #'         \n'  #   0 -  9
    #'         \n'  #  10 - 19
    #' rnbqkbnr\n'  #  20 - 29
    #' pppppppp\n'  #  30 - 39
    #' ........\n'  #  40 - 49
    #' ........\n'  #  50 - 59
    #' ........\n'  #  60 - 69
    #' ........\n'  #  70 - 79
    #' PPPPPPPP\n'  #  80 - 89
    #' RNBQKBNR\n'  #  90 - 99
    #'         \n'  # 100 -109
    #'         \n'  # 110 -119
    # A1, H1, A8, H8 = 91, 98, 21, 28

N = -10
S = 10
W = -1
E = 1

bishopMoves = (N+E, N+W, S+E, S+W)