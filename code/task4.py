"""
NOTE: You are only allowed to edit this file between the lines that say:
    # START EDITING HERE
    # END EDITING HERE

This file contains the MultiBanditsAlgo class. Here are the method details:
    - __init__(self, num_arms, horizon): This method is called when the class
        is instantiated. Here, you can add any other member variables that you
        need in your algorithm.
    
    - give_pull(self): This method is called when the algorithm needs to
        select an arm to pull. The method should return the index of the arm
        that it wants to pull (0-indexed).
    
    - get_reward(self, arm_index, set_pulled, reward): This method is called 
        just after the give_pull method. The method should update the 
        algorithm's internal state based on the arm that was pulled and the 
        reward that was received.
        (The value of arm_index is the same as the one returned by give_pull 
        but set_pulled is the set that is randomly chosen when the pull is 
        requested from the bandit instance.)
"""

import numpy as np


class MultiBanditsAlgo:
    def __init__(self, num_arms, horizon):
        self.num_arms = num_arms
        self.horizon = horizon
        # START EDITING HERE
        #Variables for first bandit instance
        self.s1=np.zeros(num_arms)
        self.f1=np.zeros(num_arms)
        self.beta1=np.zeros(num_arms)
        #Variables for second bandit instance
        self.s2=np.zeros(num_arms)
        self.f2=np.zeros(num_arms)
        self.beta2=np.zeros(num_arms)
        #Variables for overall set of bandit instances
        self.betanet=np.zeros(num_arms)
        self.t=0
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        #First pull is random
        if self.t==0:
        	return np.random.randint(self.num_arms)
        #All remaining pulls maximise net beta
        else:    
        	betalist=self.betanet.tolist()
        	return betalist.index(max(betalist))
        # END EDITING HERE
    
    def get_reward(self, arm_index, set_pulled, reward):
        # START EDITING HERE
        #If first instance used, update variables for that instance
        if set_pulled==0:
        	if reward==1:
        		self.s1[arm_index] += 1
        	else:
        		self.f1[arm_index] += 1
        	for i in range (self.num_arms):
        		self.beta1[i]=np.random.beta(self.s1[i]+1,self.f1[i]+1)
        #If second instance used, update variables for that instance
        if set_pulled==1:
        	if reward==1:
        		self.s2[arm_index] += 1
        	else:
        		self.f2[arm_index] += 1
        	for i in range (self.num_arms):
        		self.beta2[i]=np.random.beta(self.s2[i]+1,self.f2[i]+1)
        #Update overall variables, time and net beta which is the sum of the individual betas
        self.t += 1
        for i in range (self.num_arms):
        	self.betanet[i]=self.beta1[i]+self.beta2[i]
        # END EDITING HERE

