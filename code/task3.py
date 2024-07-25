"""
NOTE: You are only allowed to edit this file between the lines that say:
    # START EDITING HERE
    # END EDITING HERE

This file contains the FaultyBanditsAlgo class. Here are the method details:
    - __init__(self, num_arms, horizon, fault): This method is called when the class
        is instantiated. Here, you can add any other member variables that you
        need in your algorithm.
    
    - give_pull(self): This method is called when the algorithm needs to
        select an arm to pull. The method should return the index of the arm
        that it wants to pull (0-indexed).
    
    - get_reward(self, arm_index, reward): This method is called just after the 
        give_pull method. The method should update the algorithm's internal
        state based on the arm that was pulled and the reward that was received.
        (The value of arm_index is the same as the one returned by give_pull.)
"""

import numpy as np
import math

# START EDITING HERE
def decision(probability):
    return np.random.random() < probability
#https://stackoverflow.com/questions/5886987/true-or-false-output-based-on-a-probability
# END EDITING HERE

class FaultyBanditsAlgo:
    def __init__(self, num_arms, horizon, fault):
        self.num_arms = num_arms
        self.horizon = horizon
        self.fault = fault 
        # START EDITING HERE
        #Variables for bandits instance
        self.s=np.zeros(num_arms)
        self.f=np.zeros(num_arms)
        self.beta=np.zeros(num_arms)
        self.t=0
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        #First pull is random
        if self.t==0:
        	return np.random.randint(self.num_arms)
        #All remaining pulls maximise beta
        else:    
        	betalist=self.beta.tolist()
        	return betalist.index(max(betalist))
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        #With probabilty '1-fault', update the beta based on the reward
        if decision(1-self.fault):
        	self.t+=1
        	if reward==1:
        		self.s[arm_index] += 1
        	else:
        		self.f[arm_index] += 1
        	for i in range (self.num_arms):
        		self.beta[i]=np.random.beta(self.s[i]+1,self.f[i]+1)
        #With probability 'fault' do nothing, just increase time-step, completely ignoring reward
        else:
        	self.t+=1
        #END EDITING HERE

