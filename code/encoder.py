import numpy as np
import matplotlib.pyplot as plt
import argparse

def encode(first,second,opp,pos):
    statte=(pos-1)*1+(opp-1)*2+(second-1)*32+(first-1)*512
    return statte
    
    
    
    
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--opponent", type=str, required=True)
    parser.add_argument("--p", type=float)
    parser.add_argument("--q", type=float)
    args = parser.parse_args()
    
    p=args.p
    q=args.q
    file1 = open(args.opponent, 'r')
    lines=file1.readlines()
    file1.close()
     
    print("numStates 8194")
    print("numActions 10")
    print("end 8192 8193")
    k=0
    for line in lines:
        k=k+1
        if (k==1):
            continue
        linearr=line.split()
        state=linearr[0]
        statep=k-2
        substring=state[:2]
        if (substring[0]=='0'):
            locP1=int(substring[1:2])
        else:
            locP1=int(float(substring[:2]))
        substring=state[2:4]
        if (substring[0]=='0'):
            locP2=int(substring[1:2])
        else:
            locP2=int(float(substring[:2]))         
        substring=state[4:6]
        if (substring[0]=='0'):
            locOp=int(substring[1:2])
        else:
            locOp=int(float(substring[:2]))
        poss=int(state[6:7])
        Opleft=float(linearr[1])
        Opright=float(linearr[2])
        Opup=float(linearr[3])
        Opdown=float(linearr[4])
            
        for act in range(10):
                if (act==0): #p1 moves left
                    P1F=locP1-1
                    if (locP1 == 2 or locP1 == 3 or locP1 == 4 or locP1 == 6 or locP1 == 7 or locP1 == 8 or locP1 == 10 or locP1 == 11 or locP1 == 12 or locP1 == 14 or locP1 == 15 or locP1 == 16): #survival cases
                        OpF1=-1
                        OpF2=-1
                        OpF3=-1
                        OpF4=-1
                        if (Opleft!=0): #opponent moves left
                            OpF1=locOp-1
                            if (poss==1): #Ball with P1
                                if (P1F==OpF1): #tackle
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF1): #tackle
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-p))#no tackle
                        if (Opright!=0): #opponent moves right
                            OpF2=locOp+1
                            if (poss==1): #Ball with P1
                                if (P1F==OpF2 or (locP1==OpF2 and P1F==locOp)): #tackle
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF2): #tackle
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opup!=0): #opponent moves up
                            OpF3=locOp-4
                            if (poss==1): #Ball with P1
                                if (P1F==OpF3 ): #tackle
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF3 ): #tackle
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opdown!=0): #opponent moves up
                            OpF4=locOp+4
                            if (poss==1): #Ball with P1
                                if (P1F==OpF4 ): #tackle
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF4 ): #tackle
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 0 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-p))#no tackle
                        #tackle won cases
                        if (poss==1):
                            if (locP1==OpF4 or locP1==OpF3 or locP1==OpF2 or locP1==OpF1 or (locP1==OpF2 and P1F==locOp)):
                                print ("transition",statep," 0 8192 0 ",1-((1-2*p)*0.5))
                        elif (poss==2):
                            if (locP2==OpF4 or locP2==OpF3 or locP2==OpF2 or locP2==OpF1):
                                print ("transition",statep," 0 8192 0 ",1-((1-p)*0.5))
                    else:
                        print ("transition",statep," 0 8192 0 1")
                        
                elif (act==1): #p1 moves right
                    P1F=locP1+1
                    if (locP1 == 2 or locP1 == 3 or locP1 == 1 or locP1 == 6 or locP1 == 7 or locP1 == 5 or locP1 == 10 or locP1 == 11 or locP1 == 9 or locP1 == 14 or locP1 == 15 or locP1 == 13): #survival cases
                        OpF1=-1
                        OpF2=-1
                        OpF3=-1
                        OpF4=-1
                        if (Opleft!=0): #opponent moves left
                            OpF1=locOp-1
                            if (poss==1): #Ball with P1
                                if (P1F==OpF1 or (locP1==OpF1 and P1F==locOp)): #tackle
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF1): #tackle
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-p))#no tackle
                        if (Opright!=0): #opponent moves right
                            OpF2=locOp+1
                            if (poss==1): #Ball with P1
                                if (P1F==OpF2 ): #tackle
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF2): #tackle
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opup!=0): #opponent moves up
                            OpF3=locOp-4
                            if (poss==1): #Ball with P1
                                if (P1F==OpF3 ): #tackle
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF3 ): #tackle
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opdown!=0): #opponent moves up
                            OpF4=locOp+4
                            if (poss==1): #Ball with P1
                                if (P1F==OpF4 ): #tackle
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF4 ): #tackle
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 1 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-p))#no tackle
                        #tackle won cases
                        if (poss==1):
                            if (locP1==OpF4 or locP1==OpF3 or locP1==OpF2 or locP1==OpF1 or (locP1==OpF1 and P1F==locOp)):
                                print ("transition",statep," 1 8192 -100 ",1-((1-2*p)*0.5))
                        elif (poss==2):
                            if (locP2==OpF4 or locP2==OpF3 or locP2==OpF2 or locP2==OpF1):
                                print ("transition",statep," 1 8192 0 ",1-((1-p)*0.5))
                    else:
                        print ("transition",statep," 1 8192 0 1")
                        
                elif (act==2): #p1 moves up
                    P1F=locP1-4
                    if (locP1 == 5 or locP1 == 6 or locP1 == 7 or locP1 == 8 or locP1 == 9 or locP1 == 10 or locP1 == 11 or locP1 == 12 or locP1 == 13 or locP1 == 14 or locP1 == 15 or locP1 == 16): #survival cases
                        OpF1=-1
                        OpF2=-1
                        OpF3=-1
                        OpF4=-1
                        if (Opleft!=0): #opponent moves left
                            OpF1=locOp-1
                            if (poss==1): #Ball with P1
                                if (P1F==OpF1 ): #tackle
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF1): #tackle
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-p))#no tackle
                        if (Opright!=0): #opponent moves right
                            OpF2=locOp+1
                            if (poss==1): #Ball with P1
                                if (P1F==OpF2 ): #tackle
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF2): #tackle
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opup!=0): #opponent moves up
                            OpF3=locOp-4
                            if (poss==1): #Ball with P1
                                if (P1F==OpF3 ): #tackle
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF3 ): #tackle
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opdown!=0): #opponent moves up
                            OpF4=locOp+4
                            if (poss==1): #Ball with P1
                                if (P1F==OpF4 or (locP1==OpF4 and P1F==locOp)): #tackle
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF4 ): #tackle
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 2 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-p))#no tackle
                        #tackle won cases
                        if (poss==1):
                            if (locP1==OpF4 or locP1==OpF3 or locP1==OpF2 or locP1==OpF1 or (locP1==OpF1 and P1F==locOp)):
                                print ("transition",statep," 2 8192 0 ",1-((1-2*p)*0.5))
                        elif (poss==2):
                            if (locP2==OpF4 or locP2==OpF3 or locP2==OpF2 or locP2==OpF1):
                                print ("transition",statep," 2 8192 0 ",1-((1-p)*0.5))
                    else:
                        print ("transition",statep," 2 8192 0 1")
                        
                elif (act==3): #p1 moves down
                    P1F=locP1+1
                    if (locP1 == 1 or locP1 == 2 or locP1 == 3 or locP1 == 4 or locP1 == 5 or locP1 == 6 or locP1 == 7 or locP1 == 8 or locP1 == 9 or locP1 == 10 or locP1 == 11 or locP1 == 12): #survival cases
                        OpF1=-1
                        OpF2=-1
                        OpF3=-1
                        OpF4=-1
                        if (Opleft!=0): #opponent moves left
                            OpF1=locOp-1
                            if (poss==1): #Ball with P1
                                if (P1F==OpF1 ): #tackle
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF1): #tackle
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF1,poss)," 0 ",Opleft*(1-p))#no tackle
                        if (Opright!=0): #opponent moves right
                            OpF2=locOp+1
                            if (poss==1): #Ball with P1
                                if (P1F==OpF2 ): #tackle
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF2): #tackle
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF2,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opup!=0): #opponent moves up
                            OpF3=locOp-4
                            if (poss==1): #Ball with P1
                                if (P1F==OpF3 or (locP1==OpF3 and P1F==locOp)): #tackle
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF3 ): #tackle
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF3,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opdown!=0): #opponent moves up
                            OpF4=locOp+4
                            if (poss==1): #Ball with P1
                                if (P1F==OpF4 ): #tackle
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF4 ): #tackle
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 3 ", encode(P1F,locP2,OpF4,poss)," 0 ",Opright*(1-p))#no tackle
                        #tackle won cases
                        if (poss==1):
                            if (locP1==OpF4 or locP1==OpF3 or locP1==OpF2 or locP1==OpF1 or (locP1==OpF1 and P1F==locOp)):
                                print ("transition",statep," 3 8192 0 ",1-((1-2*p)*0.5))
                        elif (poss==2):
                            if (locP2==OpF4 or locP2==OpF3 or locP2==OpF2 or locP2==OpF1):
                                print ("transition",statep," 3 8192 0 ",1-((1-p)*0.5))
                    else:
                        print ("transition",statep," 3 8192 0 1")
                        
                elif (act==4): #p1 moves left
                    P2F=locP2-1
                    if (locP2 == 2 or locP2 == 3 or locP2 == 4 or locP2 == 6 or locP2 == 7 or locP2 == 8 or locP2 == 10 or locP2 == 11 or locP2 == 12 or locP2 == 14 or locP2 == 15 or locP2 == 16): #survival cases
                        OpF1=-1
                        OpF2=-1
                        OpF3=-1
                        OpF4=-1
                        if (Opleft!=0): #opponent moves left
                            OpF1=locOp-1
                            if (poss==2): #Ball with P1
                                if (P2F==OpF1): #tackle
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP1==OpF1): #tackle
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-p))#no tackle
                        if (Opright!=0): #opponent moves right
                            OpF2=locOp+1
                            if (poss==2): #Ball with P1
                                if (P2F==OpF2 or (locP2==OpF2 and P2F==locOp)): #tackle
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP1==OpF2): #tackle
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opup!=0): #opponent moves up
                            OpF3=locOp-4
                            if (poss==2): #Ball with P1
                                if (P2F==OpF3 ): #tackle
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF3,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF3,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP1==OpF3 ): #tackle
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF3,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF3,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opdown!=0): #opponent moves up
                            OpF4=locOp+4
                            if (poss==2): #Ball with P1
                                if (P2F==OpF4 ): #tackle
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP1==OpF4 ): #tackle
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 4 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-p))#no tackle
                        #tackle won cases
                        if (poss==2):
                            if (locP2==OpF4 or locP2==OpF3 or locP2==OpF2 or locP2==OpF1 or (locP2==OpF2 and P2F==locOp)):
                                print ("transition",statep," 4 8192 0 ",1-((1-2*p)*0.5))
                        elif (poss==1):
                            if (locP1==OpF4 or locP1==OpF3 or locP1==OpF2 or locP1==OpF1):
                                print ("transition",statep," 4 8192 0 ",1-((1-p)*0.5))
                    else:
                        print ("transition",statep," 4 8192 0 1")
                        
                elif (act==5): #p1 moves right
                    P2F=locP2+1
                    if (locP2 == 2 or locP2 == 3 or locP2 == 1 or locP2 == 6 or locP2 == 7 or locP2 == 5 or locP2 == 10 or locP2 == 11 or locP2 == 9 or locP2 == 14 or locP2 == 15 or locP2 == 13): #survival cases
                        OpF1=-1
                        OpF2=-1
                        OpF3=-1
                        OpF4=-1
                        if (Opleft!=0): #opponent moves left
                            OpF1=locOp-1
                            if (poss==2): #Ball with P1
                                if (P2F==OpF1 or (locP2==OpF1 and P2F==locOp)): #tackle
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-2*p))#no tackle
                            if (poss==2): #Ball with P2
                                if (locP2==OpF1): #tackle
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-p))#no tackle
                        if (Opright!=0): #opponent moves right
                            OpF2=locOp+1
                            if (poss==2): #Ball with P1
                                if (P2F==OpF2 ): #tackle
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP1==OpF2): #tackle
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opup!=0): #opponent moves up
                            OpF3=locOp-4
                            if (poss==2): #Ball with P1
                                if (P2F==OpF3 ): #tackle
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF3,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF3,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP1==OpF3 ): #tackle
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF3,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF3,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opdown!=0): #opponent moves up
                            OpF4=locOp+4
                            if (poss==2): #Ball with P1
                                if (P2F==OpF4 ): #tackle
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP1==OpF4 ): #tackle
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 5 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-p))#no tackle
                        #tackle won cases
                        if (poss==2):
                            if (locP2==OpF4 or locP2==OpF3 or locP2==OpF2 or locP2==OpF1 or (locP2==OpF1 and P2F==locOp)):
                                print ("transition",statep," 5 8192 0 ",1-((1-2*p)*0.5))
                        elif (poss==1):
                            if (locP1==OpF4 or locP1==OpF3 or locP1==OpF2 or locP1==OpF1):
                                print ("transition",statep," 5 8192 0 ",1-((1-p)*0.5))
                    else:
                        print ("transition",statep," 5 8192 0 1")
                        
                elif (act==6): #p1 moves up
                    P2F=locP2-4
                    if (locP2 == 5 or locP2 == 6 or locP2 == 7 or locP2 == 8 or locP2 == 9 or locP2 == 10 or locP2 == 11 or locP2 == 12 or locP2 == 13 or locP2 == 14 or locP2 == 15 or locP2 == 16): #survival cases
                        OpF1=-1
                        OpF2=-1
                        OpF3=-1
                        OpF4=-1
                        if (Opleft!=0): #opponent moves left
                            OpF1=locOp-1
                            if (poss==2): #Ball with P1
                                if (P2F==OpF1 ): #tackle
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP1==OpF1): #tackle
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-p))#no tackle
                        if (Opright!=0): #opponent moves right
                            OpF2=locOp+1
                            if (poss==2): #Ball with P1
                                if (P2F==OpF2 ): #tackle
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 6 ",encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP2==OpF2): #tackle
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opup!=0): #opponent moves up
                            OpF3=locOp-4
                            if (poss==2): #Ball with P1
                                if (P2F==OpF3 ): #tackle
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF3,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF3,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP1==OpF3 ): #tackle
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF3,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF3,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opdown!=0): #opponent moves up
                            OpF4=locOp+4
                            if (poss==2): #Ball with P1
                                if (P2F==OpF4 or (locP2==OpF4 and P2F==locOp)): #tackle
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP1==OpF4 ): #tackle
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 6 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-p))#no tackle
                        #tackle won cases
                        if (poss==2):
                            if (locP2==OpF4 or locP2==OpF3 or locP2==OpF2 or locP2==OpF1 or (locP2==OpF1 and P2F==locOp)):
                                print ("transition",statep," 6 8192 0 ",1-((1-2*p)*0.5))
                        elif (poss==1):
                            if (locP1==OpF4 or locP1==OpF3 or locP1==OpF2 or locP1==OpF1):
                                print ("transition",statep," 6 8192 0 ",1-((1-p)*0.5))
                    else:
                        print ("transition",statep," 6 8192 0 1")
                        
                elif (act==7): #p1 moves down
                    P2F=locP2+1
                    if (locP2 == 1 or locP2 == 2 or locP2 == 3 or locP2 == 4 or locP2 == 5 or locP2 == 6 or locP2 == 7 or locP2 == 8 or locP2 == 9 or locP2 == 10 or locP2 == 11 or locP2 == 12): #survival cases
                        OpF1=-1
                        OpF2=-1
                        OpF3=-1
                        OpF4=-1
                        if (Opleft!=0): #opponent moves left
                            OpF1=locOp-1
                            if (poss==2): #Ball with P1
                                if (P2F==OpF1 ): #tackle
                                    print ("transition ", statep," 7 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 7 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP1==OpF1): #tackle
                                    print ("transition ", statep," 7 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 7 ", encode(locP1,P2F,OpF1,poss)," 0 ",Opleft*(1-p))#no tackle
                        if (Opright!=0): #opponent moves right
                            OpF2=locOp+1
                            if (poss==2): #Ball with P1
                                if (P2F==OpF2 ): #tackle
                                    print ("transition ", statep," 7 ",encode( locP1,P2F,OpF2,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 7 ", encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP1==OpF2): #tackle
                                    print ("transition ", statep," 7 ", encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 3 ", encode(locP1,P2F,OpF2,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opup!=0): #opponent moves up
                            OpF3=locOp-4
                            if (poss==2): #Ball with P1
                                if (P2F==OpF3 or (locP2==OpF3 and P2F==locOp)): #tackle
                                    print ("transition ", statep," 7 ",encode( locP1,P2F,OpF3,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 7 ",encode( locP1,P2F,OpF3,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP1==OpF3 ): #tackle
                                    print ("transition ", statep," 7 ", encode(locP1,P2F,OpF3,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 7 ", encode(locP1,P2F,OpF3,poss)," 0 ",Opright*(1-p))#no tackle
                        if (Opdown!=0): #opponent moves up
                            OpF4=locOp+4
                            if (poss==2): #Ball with P1
                                if (P2F==OpF4 ): #tackle
                                    print ("transition ", statep," 7 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-2*p)*0.5)#tackle lost
                                else:
                                    print ("transition ", statep," 7 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-2*p))#no tackle
                            if (poss==1): #Ball with P2
                                if (locP1==OpF4 ): #tackle
                                    print ("transition ", statep," 7 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-p)*0.5)#tackle lost    
                                else:
                                    print ("transition ", statep," 7 ", encode(locP1,P2F,OpF4,poss)," 0 ",Opright*(1-p))#no tackle
                        #tackle won cases
                        if (poss==2):
                            if (locP2==OpF4 or locP2==OpF3 or locP2==OpF2 or locP2==OpF1 or (locP2==OpF1 and P2F==locOp)):
                                print ("transition",statep," 7 8192 0 ",1-((1-2*p)*0.5))
                        elif (poss==1):
                            if (locP1==OpF4 or locP1==OpF3 or locP1==OpF2 or locP1==OpF1):
                                print ("transition",statep," 7 8192 0 ",1-((1-p)*0.5))
                    else:
                        print ("transition",statep," 7 8192 0 1")
                
                elif (act==8): #p1 moves down
                    xP1= (locP1-1)%4
                    yP1= (locP1-1)//4
                    xP2= (locP2-1)%4
                    yP2= (locP2-1)//4
                    xcheck=0
                    ycheck=0
                    diag=0
                    if (xP1==xP2):
                        xcheck=1
                    elif (yP1==yP2):
                        ycheck=1
                    elif (yP2-yP1==xP2-xP1 or yP2-yP1==xP1-xP2):
                        diag=1
                    Opfac1=1
                    Opfac2=1
                    Opfac3=1
                    Opfac4=1
                    if (poss==1):
                        passs=2
                    if (poss==2):
                        passs=1
                    prob=q - 0.1*max(np.abs(xP1-xP2), np.abs(yP1-yP2))
                    if (Opleft!=0):
                        OpF1=locOp-1 
                        if (OpF1==locP1 or OpF1==locP2):
                            Opfac1=0.5
                        elif (xcheck==1):
                            if ((OpF1-1)%4==xP1):
                                Opfac1=0.5
                        elif (ycheck==1):
                            if ((OpF1-1)//4==yP1):
                                Opfac1=0.5
                        elif (diag==1):
                            if ((xP1-(OpF1-1)%4==yP1-(OpF1-1)//4 and xP2-(OpF1-1)%4==yP2-(OpF1-1)//4) or (xP1-(OpF1-1)%4==-1*(yP1-(OpF1-1)//4) and xP2-(OpF1-1)%4==-1*(yP2-(OpF1-1)//4))):
                                Opfac1=0.5
                        print ("transition ", statep," 8 ", encode(locP1,locP2,OpF1,passs)," 0 ",Opleft*Opfac1*prob)
                    if (Opright!=0):
                        OpF2=locOp+1 
                        if (OpF2==locP1 or OpF2==locP2):
                            Opfac2=0.5
                        elif (xcheck==1):
                            if ((OpF2-1)%4==xP1):
                                Opfac2=0.5
                        elif (ycheck==1):
                            if ((OpF2-1)//4==yP1):
                                Opfac2=0.5
                        elif (diag==1):
                            if ((xP1-(OpF2-1)%4==yP1-(OpF2-1)//4 and xP2-(OpF2-1)%4==yP2-(OpF2-1)//4) or (xP1-(OpF2-1)%4==-1*(yP1-(OpF2-1)//4) and xP2-(OpF2-1)%4==-1*(yP2-(OpF2-1)//4))):
                                Opfac=0.5
                        print ("transition ", statep," 8 ", encode(locP1,locP2,OpF2,passs)," 0 ",Opright*Opfac2*prob)
                    if (Opup!=0):
                        OpF3=locOp-4 
                        if (OpF3==locP1 or OpF3==locP2):
                            Opfac3=0.5
                        elif (xcheck==1):
                            if ((OpF3-1)%4==xP1):
                                Opfac3=0.5
                        elif (ycheck==1):
                            if ((OpF3-1)//4==yP1):
                                Opfac3=0.5
                        elif (diag==1):
                            if ((xP1-(OpF3-1)%4==yP1-(OpF3-1)//4 and xP2-(OpF3-1)%4==yP2-(OpF3-1)//4) or (xP1-(OpF3-1)%4==-1*(yP1-(OpF3-1)//4) and xP2-(OpF3-1)%4==-1*(yP2-(OpF3-1)//4))):
                                Opfac3=0.5
                        print ("transition ", statep," 8 ", encode(locP1,locP2,OpF3,passs)," 0 ",Opup*Opfac3*prob)
                    if (Opdown!=0):
                        OpF4=locOp+4
                        if (OpF4==locP1 or OpF4==locP2):
                            Opfac4=0.5
                        elif (xcheck==1):
                            if ((OpF4-1)%4==xP1):
                                Opfac4=0.5
                        elif (ycheck==1):
                            if ((OpF4-1)//4==yP1):
                                Opfac4=0.5
                        elif (diag==1):
                            if ((xP1-(OpF4-1)%4==yP1-(OpF4-1)//4 and xP2-(OpF4-1)%4==yP2-(OpF4-1)//4) or (xP1-(OpF4-1)%4==-1*(yP1-(OpF4-1)//4) and xP2-(OpF4-1)%4==-1*(yP2-(OpF4-1)//4))):
                                Opfac4=0.5
                        print ("transition ", statep," 8 ", encode(locP1,locP2,OpF4,passs)," 0 ",Opdown*Opfac4*prob)
                    print ("transition ", statep," 8 8192 0 ",1-(Opfac1*Opleft*prob+ Opfac2*Opright*prob+ Opfac3*Opup*prob+Opfac4*Opdown*prob))
                    
                elif (act==9):
                    xP1= (locP1-1)%4
                    yP1= (locP1-1)//4
                    xP2= (locP2-1)%4
                    yP2= (locP2-1)//4
                    Opfac1=1
                    Opfac2=1
                    Opfac3=1
                    Opfac4=1
                    if (poss==1):
                        prob=q-0.2*(3-xP1)
                    if (poss==2):
                        prob=q-0.2*(3-xP2)
                    if (Opleft!=0):
                        OpF1=locOp-1 
                        if (OpF1==8 or OpF1==12):
                            Opfac1=0.5
                    if (Opright!=0):
                        OpF2=locOp+1 
                        if (OpF2==8 or OpF2==12):
                            Opfac2=0.5
                    if (Opup!=0):
                        OpF3=locOp-4 
                        if (OpF3==8 or OpF3==12):
                            Opfac3=0.5
                    if (Opdown!=0):
                        OpF4=locOp+4
                        if (OpF4==8 or OpF4==12):
                            Opfac4=0.5
                    print("transition",statep," 9 8193 1 ",Opfac1*Opleft*prob+ Opfac2*Opright*prob+ Opfac3*Opup*prob+Opfac4*Opdown*prob)
                    print("transition",statep," 9 8192 0 ",1-(Opfac1*Opleft*prob+ Opfac2*Opright*prob+ Opfac3*Opup*prob+Opfac4*Opdown*prob))
                    
    print ("mdptype episodic")
    print ("gamma 0.9")
    
