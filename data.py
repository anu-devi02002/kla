import yaml 
import threading
import time
import datetime
from yaml.loader import SafeLoader
fi=open("log_file.txt","w+")
st=[]
def TimeFunction(cont,t):
    s1=str(datetime.datetime.now())
    s1+=";"
    for e in range(len(st)):
        if e==len(st)-1:
            s1+=st[e]
        else:
            s1+=st[e]
            s1+="."
    s1+=" Executing TimeFunction ("
    s1=s1+cont+", "+str(t)+")"
    fi.writelines(s1+'\n') 
    time.sleep(t)
 

def flow(dic,ex):
    d=dic["Activities"]
    kk=list(d.keys())
    n=-1
    for i in d.values():
        n+=1
        if i['Type']=='Flow':
            st.append(kk[n])
            s1=str(datetime.datetime.now())
            s1+=";"
            for e in range(len(st)):
                if e==len(st)-1:
                    s1+=st[e]
                else:
                    s1+=st[e]
                    s1+="."
            s1+=" Entry"
            fi.writelines(s1+'\n')
            flow(i,i['Execution'])
            s1=str(datetime.datetime.now())
            s1+=";"
            for e in range(len(st)):
                if e==len(st)-1:
                    s1+=st[e]
                else:
                    s1+=st[e]
                    s1+="."
            s1+=" Exit"
            fi.write(s1+'\n')
            st.remove(kk[n])
        else: 
            st.append(kk[n])
            s1=str(datetime.datetime.now())
            s1+=";"
            for e in range(len(st)):
                if e==len(st)-1:
                    s1+=st[e]
                else:
                    s1+=st[e]
                    s1+="."
            s1+=" Entry"
            fi.writelines(s1+'\n')
            TimeFunction(i['Inputs']['FunctionInput'],int(i['Inputs']['ExecutionTime']))
            s1=str(datetime.datetime.now())
            s1+=";"
            for e in range(len(st)):
                if e==len(st)-1:
                    s1+=st[e]
                else:
                    s1+=st[e]
                    s1+="."
            s1+=" Exit"
            fi.write(s1+'\n')
            st.remove(kk[n])

# Open the file and load the file
with open('Milestone1_Example.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    kk=list(data.keys())
    for i in data.values():
        if i['Type']=='Flow':
            st.append(kk[0])
            s1=str(datetime.datetime.now())
            s1+=";"
            for e in range(len(st)):
                if e==len(st)-1:
                    s1+=st[e]
                else:
                    s1+=st[e]
                    s1+="."
            s1+=" Entry"
            fi.writelines(s1+'\n')
            flow(i,i['Execution'])
            s1=str(datetime.datetime.now())
            s1+=";"
            for e in range(len(st)):
                if e==len(st)-1:
                    s1+=st[e]
                else:
                    s1+=st[e]
                    s1+="."
            s1+=" Exit"
            fi.write(s1)
            st.remove(kk[0])
    
