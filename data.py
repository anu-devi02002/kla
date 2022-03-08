import yaml 
import threading
import time
import datetime
from yaml.loader import SafeLoader
st=[]
def TimeFunction(cont,t,tt):
    print(datetime.datetime.now(),tt)    
    time.sleep(t)
    print(datetime.datetime.now(),tt)  

def flow(dic,ex):
    d=dic["Activities"]
    kk=list(d.keys())
    n=-1
    for i in d.values():
        n+=1
        if i['Type']=='Flow':
            st.append(kk[0])
            print(datetime.datetime.now(),end=";")
            for i in st:
                print(i,end=".")
            print("entry")
            flow(i,i['Execution'])
            print(datetime.datetime.now(),kk[0],'exit') 
        else:
            print(datetime.datetime.now(),kk[n])  
            TimeFunction(i['Inputs']['FunctionInput'],int(i['Inputs']['ExecutionTime']),kk[n])

# Open the file and load the file
with open('Milestone1_Example.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    kk=list(data.keys())
    print(kk[0])
    for i in data.values():
        print(i['Type'])
        if i['Type']=='Flow':
            st.append(kk[0])
            print(datetime.datetime.now(),kk[0],'entry')  
            flow(i,i['Execution'])
            print(datetime.datetime.now(),kk[0],'exit') 
    
