import abc, random
import numpy as np


class Environment(abc.ABC):
    @abc.abstractmethod
    def __init__(self, init_state=None):
        self.state = init_state
        raise NotImplementedError

    @abc.abstractmethod
    def step(self, a, s=None):
        # return s', r
        raise NotImplementedError

    @abc.abstractmethod
    def dynamics(self, a, s=None):  # or call it step or..
        # return a tab of probs of pairs of 
        # new states and rewards (s',r)
        raise NotImplementedError

    def test(self):
        print('step: ', self.step(1))
        print('dynamics: ', self.dynamics(1, 1))


class Agent(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abc.abstractmethod
    def step(self, s):
        # ... 
        # use policy here
        # return action
        raise NotImplementedError

    @abc.abstractmethod
    def pi(self, s):
        # can be probabilistic (obtain and return list of probs of actions, not
        # allowed actions have 0 prob) or deterministic (return action)
        # return []#list of probabilities of allowed actions
        raise NotImplementedError

    def test(self):
        print('step: ', self.step(1))
        print('pi: ', self.pi(1, 1))


# TODO:
#   - make states.n, actions.n like in gym ai api
#   - add tests

class Easy21(Environment):
    def __init__(self, logging=False):
        # hit = 1, stick = 0
        self.logging = logging
        self.reset()

    def draw_a_card(self, black_only=False):
        if black_only:
            r = random.randint(1, 10)
        else:
            r = random.randint(1, 10) * (-1 if random.random() < 1 / 3 else 1)
        if self.logging: print('C:', r)
        return r

    def state(self):
        return [self.dealer_sum, self.player_sum]

    def set_state(self, state):
        self.dealer_sum, self.player_sum = state[0], state[1]

    def draw(self):
        return self.player_sum == 21

    def goes_bust(self, summ):
        if summ > 21 or summ < 1:
            return True

    def dealer_hit(self):
        if self.dealer_sum < 17:
            return True
        return False

    def step(self, action):

        state = self.state()
        if self.started == False:
            self.reset()
            self.start()

            return state, action, 0
        else:
            if action == 1:
                if self.logging: print('hit')
                self.player_sum += self.draw_a_card()

                if self.draw():
                    if self.logging: print('R: draw')
                    self.started = False
                    return state, action, 0

                if self.goes_bust(self.player_sum):
                    if self.logging: print('R: dealer win')
                    self.started = False
                    return state, action, -1

                return state, action, 0
            else:
                if self.logging: print('stick')
                while self.dealer_hit():
                    self.dealer_sum += self.draw_a_card()

                if self.goes_bust(self.dealer_sum) or self.dealer_sum < self.player_sum:
                    if self.logging: print('R: player win')
                    self.started = False
                    return state, action, 1

                if self.dealer_sum > self.player_sum:
                    if self.logging: print('R: dealer win')
                    self.started = False
                    return state, action, -1

                if self.dealer_sum == self.player_sum:
                    if self.logging: print('R: draw')
                    self.started = False
                    return state, action, 0

                return state, action, 0

    def start(self):
        if self.logging: print('start a new game..')
        self.player_sum = self.draw_a_card(True)
        self.dealer_sum = self.draw_a_card(True)
        self.started = True

    def reset(self):
        if self.logging: print('reset')
        self.dealer_sum = 0
        self.player_sum = 0
        self.started = False
        return 0


# TODO:
#   - reimplement grid world like GridWorld(Environment)
#   - implement random policy agent for GW
#   - implement policy evaluation algorithm


# from IPython.display import clear_output

class GridWorld(Environment):

    def __init__(self,
                 start=np.array([2, 0]),
                 actions=['up', 'down', 'left', 'right'],
                 size=np.array([7, 7]),
                 terminal=np.array([1, 3]),
                 deterministic=True,
                 step_reward=-1):

        self.start_state = start
        self._state = start
        self.size = size
        self.terminal = terminal
        self.step_reward = step_reward
        self.actions = actions
        self.board = np.zeros(size)
        self.board[terminal] = -1
        self.setstate(start)
        self.R = 0
        self.steps = 0
        self.last_action = None

    def isterminal(self):
        #         print('_state ', self._state)
        #         print('TERMINAL ', TERMINAL)
        if (self._state == self.terminal).all():
            return True
        else:
            return False

    def dynamics(self, a, s=None):
        #         # for general case return list of (s_, r, prob)
        # for deterministic case return [(s_, r, p)]

        if s is not None:
            self.setstate(s)

        if a == 'up':
            state = np.array([self._state[0] - 1, self._state[1]])
        elif a == 'down':
            state = np.array([self._state[0] + 1, self._state[1]])
        elif a == 'left':
            state = np.array([self._state[0], self._state[1] - 1])
        elif a == 'right':
            state = np.array([self._state[0], self._state[1] + 1])
        else:
            print('ERROR: UNKNOWN ACTION')

        if (state[0] >= 0 and state[0] < self.board.shape[0] and
                state[1] >= 0 and state[1] < self.board.shape[1]):
            self.setstate(state)

        if self.isterminal():
            R = 0
        else:
            R = self.step_reward

        return [(self._state, R, 1)]

        # TODO: impl test dynamics
        # some regular & edge cases

    def step(self, a='up', s=None):
        #         print('#1')
        actions = self.dynamics(a, s)
        #         print('#2')
        #         print('actions: ', actions)
        #         print(self._state)
        # here choose action in general case
        # with probability to be chosen proportionally to prob of a

        # 1. get array of probs
        probs = [i[2] for i in actions]
        probs /= np.array([i[2] for i in actions]).sum()
        #         print('#3')
        # 2. need a function for choose proportionally to prob
        picked = np.random.choice(np.array(actions, dtype=np.dtype('2int, int, float')), 1, p=probs)
        _s, r, p = picked[0]
        self.last_action = a
        self.setstate(_s)
        if self.isterminal():
            print('is terminal')
            return self._state, 0
        else:
            self.R += self.step_reward
            return self._state, self.step_reward

    def setstate(self, state):
        #         if type(state) is not np.ndarray:
        #             print('in setstate')
        #             print('type(state) ', type(state))
        # update board
        self.board[self._state[0]][self._state[1]] = 0
        self.board[state[0]][state[1]] = 1
        # set state
        self._state = state

    def print(self):
        info = []
        info.append('  total_reward: ' + str(self.R))
        info.append('  steps: ' + str(self.steps))
        info.append('  last action: ' + str(self.last_action))

        for i in range(self.size[0]):
            out = '|'
            for j in range(self.size[1]):
                if self.board[i, j] == 0:
                    out += ' ' + '|'
                elif self.board[i, j] == 1:
                    out += '*' + '|'
                elif self.board[i, j] == -1:
                    out += 'T' + '|'

            if i < len(info):
                out += info[i]
            print(out)

    def __str__(self):
        info = ['  total_reward: ' + str(self.R), '  steps: ' + str(self.steps),
                '  last action: ' + str(self.last_action)]

        result = ''
        for i in range(self.size[0]):
            out = '\n|'
            for j in range(self.size[1]):
                if self.board[i, j] == 0:
                    out += ' ' + '|'
                elif self.board[i, j] == 1:
                    out += '*' + '|'
                elif self.board[i, j] == -1:
                    out += 'T' + '|'

            if i < len(info):
                out += info[i]
            result += out
        return result

    def restart(self):
        self.__init__(self.start_state, self.actions)
        return -1


class RandomPolicy(Agent):

    def __init__(self, env=None):
        self.env = env

    def step(self):
        return np.random.choice(self.env.actions)

    def pi(self, s):
        # should agent choose between eligible actions
        # look at gridworld description in Sutton's book
        # Sutton p. 76, agent is able to choose any of 4 actions __equiprobably__
        # so return list [(0.25, "up"), (0.25, "down"), (0.25, "left"), (0.25, "right")]
        return dict([("up", 0.25), ("down", 0.25), ("left", 0.25), ("right", 0.25)])
