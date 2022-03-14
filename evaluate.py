import numpy as np
from base import GridWorld, RandomPolicy

gw = GridWorld()
print(gw)

board = np.zeros(np.array([7, 7]))
print(board)
terminal=np.array([1, 3])
board[tuple(terminal)] = -1
print(board)

gw.step('down')
print(gw)


rp = RandomPolicy(gw)
eval(gw, rp)

size = np.array([7,7])
board = np.zeros(size)
V = np.zeros_like(board)
V_ = np.empty_like(board)

delta = 0
theta = 0.001
S = np.indices(board.shape).reshape(board.shape[0]*board.shape[1],2)
for s in S:
    print(s)

    v = V[tuple(s)]
    #V[tuple(s)] =
    r = 0
    for a in actions:
        for d in dynamics:
            r += 1
    print(' ', v)


type(S[0])

board[tuple(S[0])]

board[1, 5]

def eval(env, agent):
    # create V, V'
    # so what we have in env
    # S must be ndarray of [,] or tuples
    # and we will be able to do V[s] directly it is elegant

    print(env)
    S = np.indices(board.shape).reshape(board.shape[0] * board.shape[1], 2)
    print(S)

    for s in S:
        # print(V[s])
    pass
