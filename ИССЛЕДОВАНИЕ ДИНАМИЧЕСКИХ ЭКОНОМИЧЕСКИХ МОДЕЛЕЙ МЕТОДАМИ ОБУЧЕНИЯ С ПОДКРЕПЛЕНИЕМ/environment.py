import random
import numpy as np
import collections

TIME_LIMIT = 3
DISCOUNT_FACTOR = 0.9
GROWTH_RATE = 1.05
START_MONEY = 1000.0




class Economical_env:
    '''
    time_limit-горизон планирования
    discout_factor - коэфицент дисконтирования
    growth_rate - коэффицент прироста денежных средств
    start_money - денежные активы
    '''
    def __init__(self, randomSeed = 0,
                 time_limit = TIME_LIMIT,
                 discount_factor = DISCOUNT_FACTOR,
                 growth_rate = GROWTH_RATE,
                 start_money = START_MONEY):
        
        self.time_limit = time_limit
        self.discount_factor = discount_factor
        self.growth_rate = growth_rate
#         self.start_money = start_money
#         self.start_time = 0
#         self.start_state = np.array([self.start_money, self.start_time])
        
        
    def reset(self, seed = 0, time = TIME_LIMIT, discount = DISCOUNT_FACTOR, g_rate = GROWTH_RATE, s_money = START_MONEY):
            self.__init__(randomSeed = seed, time_limit = time, discount_factor = discount,\
                          growth_rate = g_rate, start_money = s_money)
            self.start_money = s_money
            self.start_time = 0
            self.start_state = np.array([self.start_money, self.start_time, self.time_limit - self.start_time])
            
            return self.start_state
    
    
    def step(self, action):
        if action > self.growth_rate * self.start_money:
            done = True
            reward = np.log(self.start_money) * self.discount_factor ** self.start_time
            self.start_money = 0
        else:
            done = False
            reward = np.log(action) * self.discount_factor ** self.start_time
            self.start_money = self.start_money * self.growth_rate - action
        self.start_time += 1
        if self.start_time == self.time_limit:
            done = True
        
        return (np.array([self.start_money, self.start_time, self.time_limit - self.start_time]), np.array([reward]), done)
    
    def observation_space_dimension(self):
        '''размерность простравнства состояний''' 
        return 3

    def action_space_dimension(self):
        '''размерность простравнства действий''' 
        return 1
        