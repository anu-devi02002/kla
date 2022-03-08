import yaml 
import threading
import time
import datetime
from yaml.loader import SafeLoader
def TimeFunction(cont,t):
    print("current time:-",datetime.datetime.now())    
    time.sleep(t)
    print("current time:-",datetime.datetime.now())  

def flow(dic):
    print(dic['Activities'])
    kk=list(dic['Activities'].keys())

    for i in range(dic):
        print(i)
        if type=='flow':
            flow(i)
        else:
            TimeFunction(dic[inputs['Function']],dic[inputs['ExecutionTime']])
# Open the file and load the file
with open('Milestone1_Example.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    k=list(data.keys())
    print(k[0])
    print(data[k[0]])
    for i in data[k[0]]:
        print(i)
        if type=='flow':
            flow(i)
    
    
