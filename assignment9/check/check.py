import os 

read = [float(item.split(":")[1]) for item in open("eval6.txt","r")]

print(sum(read)/len(read))