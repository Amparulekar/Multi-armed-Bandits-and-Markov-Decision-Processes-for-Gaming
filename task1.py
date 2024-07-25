"""
NOTE: You are only allowed to edit this file between the lines that say:
    # START EDITING HERE
    # END EDITING HERE

This file contains the base Algorithm class that all algorithms should inherit
from. Here are the method details:
    - __init__(self, num_arms, horizon): This method is called when the class
        is instantiated. Here, you can add any other member variables that you
        need in your algorithm.
    
    - give_pull(self): This method is called when the algorithm needs to
        select an arm to pull. The method should return the index of the arm
        that it wants to pull (0-indexed).
    
    - get_reward(self, arm_index, reward): This method is called just after the 
        give_pull method. The method should update the algorithm's internal
        state based on the arm that was pulled and the reward that was received.
        (The value of arm_index is the same as the one returned by give_pull.)

We have implemented the epsilon-greedy algorithm for you. You can use it as a
reference for implementing your own algorithms.
"""

import numpy as np
import math

class Algorithm:
    def __init__(self, num_arms, horizon):
        self.num_arms = num_arms
        self.horizon = horizon
    
    def give_pull(self):
        raise NotImplementedError
    
    def get_reward(self, arm_index, reward):
        raise NotImplementedError

# Example implementation of Epsilon Greedy algorithm
class Eps_Greedy(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        self.eps = 0.1
        self.counts = np.zeros(num_arms)
        self.values = np.zeros(num_arms)
    
    def give_pull(self):
        if np.random.random() < self.eps:
            return np.random.randint(self.num_arms)
        else:
            return np.argmax(self.values)
    
    def get_reward(self, arm_index, reward):
        self.counts[arm_index] += 1
        n = self.counts[arm_index]
        value = self.values[arm_index]
        new_value = ((n - 1) / n) * value + (1 / n) * reward
        self.values[arm_index] = new_value

# START EDITING HERE
    
def binary_search(self,low, high,i):
    #Binary search for KL UCB, to solve the equation in q, given q belongs to range p to 1
    if high - low > 0.000001:
        mid = low + (high - low)/2.0
        #KLUCB equation: RHS of equation is zero, so calculate value using a q and if less than zero, search for q ahead while if more than zero search for q behind
        midval=self.ua[i]*(self.pa[i]*math.log(self.pa[i]/mid)+(1-self.pa[i])*math.log((1-self.pa[i])/(1-mid)))- math.log(self.t)
        # If found at mid, then return it
        if midval<0:
            return binary_search(self, mid, high, i)
        # Search the left half
        elif midval > 0:
            return binary_search(self, low, mid, i)
        # Search the right half
        else:
            return mid
        # Stop is high and low values are very close, then you have found your q
    else:
            return low
     #https://www.studytonight.com/python-programs/binary-search-in-python
# END EDITING HERE

class UCB(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # START EDITING HERE
        #Adding variables needed for the algorithm
        self.ua=np.zeros(num_arms)
        self.pa=np.zeros(num_arms)
        self.ucba=np.zeros(num_arms)
        self.t=0
        self.num_arms=num_arms
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        #First every arm is pulled
        if self.t<self.num_arms:
        	return self.t
        #For remaining pulls, arm with max UCB chosen
        else:    
        	ucbalist=self.ucba.tolist()
        	return ucbalist.index(max(ucbalist))
        # END EDITING HERE  
        
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        #Updating time
        self.t+=1
        #Updating no of pulls on the arm
        self.ua[arm_index] += 1
        n = self.ua[arm_index]
        #Updating empirical mean of the arm 
        p = self.pa[arm_index]
        new_p = ((n - 1) / n) * p + (1 / n) * reward
        self.pa[arm_index] = new_p
        #If it is still pulling each arm for the first time, only update ucb of that arm
        if self.t-1 == arm_index:
        	self.ucba[arm_index]=self.pa[arm_index]+math.sqrt(2*math.log(self.t)/self.ua[arm_index])
        #Updating UCB for all arms
        else:
        	for i in range (self.num_arms):
        		self.ucba[i]=self.pa[i]+math.sqrt(2*math.log(self.t)/self.ua[i])
        
        # END EDITING HERE


class KL_UCB(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # START EDITING HERE
        #Adding variables needed for the algorithm
        self.ua=np.ones(num_arms)
       	self.pa=np.array([0.0001 for i in range(num_arms)])
       	self.ucba=np.zeros(num_arms)
       	self.t=0
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        #First arm chosen randomly
        #First every arm is pulled
        if self.t<self.num_arms:
        	return self.t
        #For remaining pulls, arm with max UCB chosen
        else:    
        	ucbalist=self.ucba.tolist()
        	return ucbalist.index(max(ucbalist))
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        #Updating no of pulls on the arm
        self.ua[arm_index] += 1
        n = self.ua[arm_index]
        #Updating empirical mean of the arm 
        p = self.pa[arm_index]
        new_p = ((n - 1) / n) * p + (1 / n) * reward
        self.pa[arm_index] = new_p
        #Updating time
        self.t+=1
        #If it is still pulling each arm for the first time, only update ucb of that arm
        if self.t-1 == arm_index:
                if self.pa[arm_index]==1:
                            self.ucba[arm_index]=1
                else:
                            self.ucba[arm_index] = binary_search(self,self.pa[arm_index],1,arm_index)
        #Updating UCB for all arms
        else:
        	for i in range (self.num_arms):
        		#Checking edge case where p is 1 so q will be 1
        		if self.pa[i]==1:
        			self.ucba[i]=1
        		#Updating KL ucb for all arms by solving the equation and searching for q
        		else:
        			self.ucba[i] = binary_search(self,self.pa[i],1,i)
        # END EDITING HERE

class Thompson_Sampling(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # START EDITING HERE
        #Adding variables needed for the algorithm
        self.s=np.zeros(num_arms)
        self.f=np.zeros(num_arms)
        self.beta=np.zeros(num_arms)
        self.t=0
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        #First arm chosen randomly
        if self.t==0:
        	return np.random.randint(self.num_arms)
        #For remaining pulls, arm with max beta chosen
        else:    
        	betalist=self.beta.tolist()
        	return betalist.index(max(betalist))
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        #Updating success and failure of arm
        if reward==1:
        	self.s[arm_index] += 1
        else:
        	self.f[arm_index] += 1
        #Updating beta for all arms
        for i in range (self.num_arms):
        	self.beta[i]=np.random.beta(self.s[i]+1,self.f[i]+1)
        #Updating time
        self.t+=1
        # END EDITING HERE
