import numpy as np
import argparse
import matplotlib.pyplot as plt
from pulp import *

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--mdp", type=str, required=True)
    parser.add_argument("--algorithm", choices = ['vi', 'hpi', 'lp', 'default'], default="default")
    parser.add_argument("--policy", type=str, default="none")
    args = parser.parse_args()
    
    file1 = open(args.mdp, 'r')
    lines=file1.readlines()
    file1.close()
    
    numStates=0
    numActions=0
    endStates=[]
    
    for line in lines:
        linearr=line.split()
        if (linearr[0]=="numStates"):
            numStates=int(linearr[1])
        elif (linearr[0]=="numActions"):
            numActions=int(linearr[1])
            transitionFn=np.zeros((numStates,numActions,numStates))
            rewardFn=np.zeros((numStates,numActions,numStates))
        elif (linearr[0]=="end"):
            for i in range (len(linearr)-1):
                endStates.append(int(linearr[i+1]))
        elif (linearr[0]=="transition"):
            s1 = int(linearr[1])
            ac = int(linearr[2])
            s2 = int(linearr[3])
            r = float(linearr[4])
            p = float(linearr[5])
            transitionFn[s1][ac][s2]=p
            rewardFn[s1][ac][s2]=r
        elif (linearr[0]=="mdptype"):
            mdptype=linearr[1]
        else:
            gamma=float(linearr[1])
            
    if (args.algorithm=='vi'):
        V=np.zeros(numStates)
        bestAction=np.zeros(numStates)
        newV=np.zeros(numStates)
        while(True):
            actionValueFn=np.zeros((numStates,numActions))
            for i in range (numStates):
                for j in range (numActions):
                    for k in range (numStates):
                        actionValueFn[i][j]+=transitionFn[i][j][k]*(rewardFn[i][j][k]+ gamma*V[k])
            newV= np.max(actionValueFn,axis=-1)
            if (np.linalg.norm(newV-V)<0.000000001):
                Vfinal=newV
                break
            else:
                V=newV
        actionValueFn=np.zeros((numStates,numActions))
        for i in range (numStates):
                for j in range (numActions):
                    for k in range (numStates):
                        actionValueFn[i][j]+=transitionFn[i][j][k]*(rewardFn[i][j][k]+ gamma*Vfinal[k])
                bestAction[i]=np.argmax(actionValueFn[i])
        for i in range(numStates):
            print(round(Vfinal[i],6)," ",bestAction[i],"\n")
                 
#https://machinelearninggeek.com/solving-linear-programming-using-python-pulp/
    elif (args.algorithm=='lp'):
        V=LpVariable.dicts('ValueFn', range(numStates))
        model = LpProblem("ValueFn", LpMaximize)
        suma=0
        for i in range(numStates):
            suma = suma+ (-1*V[i])
        model+=suma
        for i in range(numStates):
            for j in range(numActions):
                sumb=0
                for k in range(numStates):
                     sumb=sumb+transitionFn[i][j][k]*(rewardFn[i][j][k]+ gamma*V[k])
                model+=V[i]>=sumb
        solver = PULP_CBC_CMD(msg=0)
        model.solve(solver)
        Vfinal=np.zeros(numStates)
        bestAction=np.zeros(numStates)
        for i in range(numStates):
            Vfinal[i]=V[i].varValue
        actionValueFn=np.zeros((numStates,numActions))
        for i in range (numStates):
                for j in range (numActions):
                    for k in range (numStates):
                        actionValueFn[i][j]+=transitionFn[i][j][k]*(rewardFn[i][j][k]+ gamma*Vfinal[k])
                    bestAction[i]=np.argmax(actionValueFn[i],axis=-1)
        for l in range(numStates):
            print(round(Vfinal[l],6)," ",bestAction[l],"\n")
         
    elif (args.algorithm=='hpi'):
        policy=np.zeros(numStates)
        Vinit=np.zeros(numStates)
        Vfinal=np.zeros(numStates)
        Vnew=np.zeros(numStates)
        for i in range (numStates):
            policy[i] = np.random.randint(0,numActions-1)
        for i in range (numStates):
            for k in range (numStates):
                Vnew[i] +=transitionFn[i][int(policy[i])][k]*(rewardFn[i][int(policy[i])][k]+ gamma*Vinit[k])
        while True:
            actionValueFn=np.zeros((numStates,numActions))
            for i in range (numStates):
                for j in range (numActions):
                    for k in range (numStates):
                        actionValueFn[i][j]+=transitionFn[i][j][k]*(rewardFn[i][j][k]+ gamma*Vnew[k])
            Qmax= np.max(actionValueFn,axis=-1)
            if (np.linalg.norm(Qmax-Vnew)<0.000000000001):
                Vfinal=Vnew
                policy=np.argmax(actionValueFn,axis=-1)
                break
            Vinit=Vnew
            Vnew=np.zeros(numStates)
            for i in range(numStates):
                policy=np.argmax(actionValueFn,axis=-1)
            for i in range (numStates):
                for k in range (numStates):
                    Vnew[i] +=transitionFn[i][int(policy[i])][k]*(rewardFn[i][int(policy[i])][k]+ gamma*Vinit[k])
        for l in range(numStates):
            print(round(Vfinal[l],6)," ",policy[l],"\n")
                   
    elif (args.policy!="none"):
        file2 = open(args.policy, 'r')
        lines2=file2.readlines()
        file2.close()
        policy=np.zeros(numStates)
        Vinit=np.zeros(numStates)
        Vfinal=np.zeros(numStates)
        Vnew=np.zeros(numStates)
        n=0
        for line2 in lines2:
            linearr2=line2.split()
            policy[n]=int(linearr2[0])
            n=n+1
        while(True):
            Vnew = np.zeros(numStates)
            for i in range (numStates):
                for k in range (numStates):
                    Vnew[i] +=transitionFn[i][int(policy[i])][k]*(rewardFn[i][int(policy[i])][k]+ gamma*Vinit[k])
            if (np.linalg.norm(Vnew-Vinit)<0.000000000001):
                Vfinal=Vnew
                break
            else:
                Vinit=Vnew
        for i in range(numStates):
            print(round(Vfinal[i],6)," ",policy[i],"\n")
    
    else:
        V=np.zeros(numStates)
        bestAction=np.zeros(numStates)
        newV=np.zeros(numStates)
        while(True):
            actionValueFn=np.zeros((numStates,numActions))
            for i in range (numStates):
                for j in range (numActions):
                    for k in range (numStates):
                        actionValueFn[i][j]+=transitionFn[i][j][k]*(rewardFn[i][j][k]+ gamma*V[k])
            newV= np.max(actionValueFn,axis=-1)
            if (np.linalg.norm(newV-V)<0.000000001):
                Vfinal=newV
                break
            else:
                V=newV
        actionValueFn=np.zeros((numStates,numActions))
        for i in range (numStates):
                for j in range (numActions):
                    for k in range (numStates):
                        actionValueFn[i][j]+=transitionFn[i][j][k]*(rewardFn[i][j][k]+ gamma*Vfinal[k])
                bestAction[i]=np.argmax(actionValueFn[i])
        for i in range(numStates):
            print(round(Vfinal[i],6)," ",bestAction[i],"\n")
        
        
