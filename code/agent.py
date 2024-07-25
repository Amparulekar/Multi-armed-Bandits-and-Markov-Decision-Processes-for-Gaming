import os
import sys
import random 
import json
import math
import utils
import time
import config
import numpy as np
random.seed(9)

class Agent:
    def __init__(self, table_config) -> None:
        self.table_config = table_config
        self.prev_action = None
        self.curr_iter = 0
        self.state_dict = {}
        self.holes =[]
        self.ns = utils.NextState()


    def set_holes(self, holes_x, holes_y, radius):
        #print('locationnnn',holes_x)
        #print('locationnnnnn',holes_y)
        for x in holes_x:
            for y in holes_y:
                self.holes.append((x[0], y[0]))
        self.ball_radius = radius


    def action(self, ball_pos=None):
        ## Code you agent here ##
        ## You can access data from config.py for geometry of the table, configuration of the levels, etc.
        ## You are NOT allowed to change the variables of config.py (we will fetch variables from a different file during evaluation)
        ## Do not use any library other than those that are already imported.
        ## Try out different ideas and have fun!
        #print(ball_pos)
        #print(len(ball_pos))
        dists=[]
        balls=[]
        closeballs=[]
        closedists=[]
        for i in ball_pos:
        	#print (i)
        	if (i!="white" and i!=0):
        		dists=np.append(dists,math.dist(ball_pos["white"],ball_pos[i]))
        		balls=np.append(balls,i)
        #print(dists)
        #print(balls)
        for i in ball_pos:
        	if (i!="white" and i!=0):
        		if (ball_pos[i][0]<100 and ball_pos[i][1]<100):
        			if (ball_pos[i][0]<ball_pos[0][0] and ball_pos[i][1]<ball_pos[0][1]):
        				closedists=np.append(closedists,math.dist(ball_pos[i],(40,40)))
        				closeballs=np.append(closeballs,i)
        		if (ball_pos[i][0]>440 and ball_pos[i][0]<560 and ball_pos[i][1]<100):
        			if (ball_pos[i][1]<ball_pos[0][1]):
        				if(ball_pos[i][0]>ball_pos[0][0] and 500>ball_pos[0][0]):
        					closedists=np.append(closedists,math.dist(ball_pos[i],(500,40)))
        					closeballs=np.append(closeballs,i)
        				if(ball_pos[i][0]<ball_pos[0][0] and 500<ball_pos[0][0]):
        					closedists=np.append(closedists,math.dist(ball_pos[i],(500,40)))
        					closeballs=np.append(closeballs,i)
        		if (ball_pos[i][0]>900 and ball_pos[i][1]<100):
        			if (ball_pos[i][0]>ball_pos[0][0] and ball_pos[i][1]<ball_pos[0][1]):
        				closedists=np.append(closedists,math.dist(ball_pos[i],(960,40)))
        				closeballs=np.append(closeballs,i)
        		if (ball_pos[i][0]<100 and ball_pos[i][1]>400):
        			if (ball_pos[i][0]<ball_pos[0][0] and ball_pos[i][1]>ball_pos[0][1]):
        				closedists=np.append(closedists,math.dist(ball_pos[i],(40,460)))
        				closeballs=np.append(closeballs,i)
        		if (ball_pos[i][0]>440 and ball_pos[i][0]<560 and ball_pos[i][1]>400):
        			if (ball_pos[i][1]>ball_pos[0][1]):
        				if(ball_pos[i][0]>ball_pos[0][0] and 500>ball_pos[0][0]):
        					closedists=np.append(closedists,math.dist(ball_pos[i],(500,460)))
        					closeballs=np.append(closeballs,i)
        				if(ball_pos[i][0]<ball_pos[0][0] and 500<ball_pos[0][0]):
        					closedists=np.append(closedists,math.dist(ball_pos[i],(500,460)))
        					closeballs=np.append(closeballs,i)
        		if (ball_pos[i][0]>900 and ball_pos[i][1]>400):
        			if (ball_pos[i][0]>ball_pos[0][0] and ball_pos[i][1]>ball_pos[0][1]):
        				closedists=np.append(closedists,math.dist(ball_pos[i],(960,460)))
        				closeballs=np.append(closeballs,i)
        whitey=ball_pos[0][1]
        whitex=ball_pos[0][0]
        holeangs=[]
        ballangs=[]
        angballs=[]
        for i in ball_pos:
        	if (i!="white" and i!=0):
        		bally=ball_pos[i][1]
        		ballx=ball_pos[i][0]
        		if (bally>whitey):
        			if (ballx>whitex):
        				ballangs=np.append(ballangs,-(1-math.atan((ballx-whitex)/(bally-whitey))/3.14159265))
        				angballs=np.append(angballs,i)
        			if (ballx==whitex):
        				ballangs=np.append(ballangs,1)
        				angballs=np.append(angballs,i)
        			if (ballx<whitex):
        				ballangs=np.append(ballangs,1+math.atan((ballx-whitex)/(bally-whitey))/3.14159265)
        				angballs=np.append(angballs,i)
        		if (bally==whitey):
        			if (ballx>whitex):
        				ballangs=np.append(ballangs,-0.5)
        				angballs=np.append(angballs,i)
        			if (ballx==whitex):
        				ballangs=np.append(ballangs,0)
        				angballs=np.append(angballs,i)
        			if (ballx<whitex):
        				ballangs=np.append(ballangs,0.5)
        				angballs=np.append(angballs,i)
        		if (bally<whitey):
        			if (ballx>whitex):
        				ballangs=np.append(ballangs,math.atan((ballx-whitex)/(bally-whitey))/3.14159265)
        				angballs=np.append(angballs,i)
        			if (ballx==whitex):
        				ballangs=np.append(ballangs,0)
        				angballs=np.append(angballs,i)
        			if (ballx<whitex):
        				ballangs=np.append(ballangs,math.atan((ballx-whitex)/(bally-whitey))/3.14159265)
        				angballs=np.append(angballs,i)
        holeangs=np.append(holeangs,-(1-math.atan((960-whitex)/(360-whitey))/3.14159265))
        holeangs=np.append(holeangs,1+math.atan((40-whitex)/(360-whitey))/3.14159265)
        holeangs=np.append(holeangs,math.atan((40-whitex)/(40-whitey))/3.14159265)
        holeangs=np.append(holeangs,math.atan((960-whitex)/(40-whitey))/3.14159265)
        if (whitex>500):
        	holeangs=np.append(holeangs,1+math.atan((500-whitex)/(360-whitey))/3.14159265)
        	holeangs=np.append(holeangs,math.atan((500-whitex)/(40-whitey))/3.14159265)
        if (whitex<500):
        	holeangs=np.append(holeangs,-(1-math.atan((500-whitex)/(360-whitey))/3.14159265))
        	holeangs=np.append(holeangs,math.atan((500-whitex)/(40-whitey))/3.14159265)
        if (whitex==500):
        	holeangs=np.append(holeangs,1)
        	holeangs=np.append(holeangs,0)
        #print(holeangs)
        #print(ballangs)
        #print(angballs)
        minball=balls[np.argmin(dists)]
        #print(ball_pos[minball])
        #print(ball_pos[0])
        bally=ball_pos[minball][1]
        ballx=ball_pos[minball][0]
        f=0.9
        if (len(closeballs)>0):
        	minball=closeballs[np.argmin(closedists)]
        	bally=ball_pos[minball][1]
        	ballx=ball_pos[minball][0]
        	f=0.9
        collballs=[]
        ballcoll=[]
        for i in holeangs:
        	for j in range(len(ballangs)):
        		if (np.abs(i-ballangs[j])<0.006):
        			ballcoll=np.append(ballcoll,np.abs(i-ballangs[j]))
        			collballs=np.append(collballs,angballs[j])
        		
        #print(ballcoll)
        #print(collballs)
        if (len(collballs)>0):
        	minball=collballs[np.argmin(ballcoll)]	
        	bally=ball_pos[minball][1]
        	ballx=ball_pos[minball][0]
        	f=0.6
        #print (f)
        if (bally>whitey):
        	if (ballx>whitex):
        		a=-(1-math.atan((ballx-whitex)/(bally-whitey))/3.14159265)
        	if (ballx==whitex):
        		a= 1
        	if (ballx<whitex):
        		a=1+math.atan((ballx-whitex)/(bally-whitey))/3.14159265
        if (bally==whitey):
        	if (ballx>whitex):
        		a=-0.5
        	if (ballx==whitex):
        		a=0
        	if (ballx<whitex):
        		a=0.5
        if (bally<whitey):
        	if (ballx>whitex):
        		a=math.atan((ballx-whitex)/(bally-whitey))/3.14159265
        	if (ballx==whitex):
        		a=0
        	if (ballx<whitex):
        		a=math.atan((ballx-whitex)/(bally-whitey))/3.14159265
        #print(a)
        return (a, f)
