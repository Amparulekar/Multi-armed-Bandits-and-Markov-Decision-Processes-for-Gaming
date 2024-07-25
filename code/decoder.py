import numpy as np
import matplotlib.pyplot as plt
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--value-policy", type=str, required=True)
    parser.add_argument("--opponent", type=str)
    args = parser.parse_args()
    
    file1 = open(args.opponent, 'r')
    lines=file1.readlines()
    file1.close()
    
    file2 = open(args.value-policy, 'r')
    lines2=file2.readlines()
    file2.close()
    
    for i in range (8192):
        print (lines[i+1][0], " ", lines2[i][2], " ", lines2[i][1])
    print(0, " ", lines2[8192][2]," ", lines2[8192][0])
    print(1, " ", lines2[8193][2]," ", lines2[8193][0])
    
