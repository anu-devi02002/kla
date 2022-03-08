
import _thread
import yaml 
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
    if ex=="Sequential":
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
    elif ex=='Concurrent':
        th=[]
        s_entry=[]
        s_exit=[]
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
                s_entry.append(s1)
                _thread.start_new_thread(flow, (i,i['Execution'],) )
                #th.append(threading.Thread(target=flow, args=(i,i['Execution'])))
                s1=str(datetime.datetime.now())
                s1+=";"
                for e in range(len(st)):
                    if e==len(st)-1:
                        s1+=st[e]
                    else:
                        s1+=st[e]
                        s1+="."
                s1+=" Exit"
                s_exit.append(s1)
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
                fi.write(s1+'\n')
                s_entry.append(s1)
                _thread.start_new_thread(TimeFunction, (i['Inputs']['FunctionInput'],int(i['Inputs']['ExecutionTime']),) )
                #th.append(threading.Thread(target=TimeFunction, args=(i['Inputs']['FunctionInput'],int(i['Inputs']['ExecutionTime']))))
                #TimeFunction(i['Inputs']['FunctionInput'],int(i['Inputs']['ExecutionTime']))
                s1=str(datetime.datetime.now())
                s1+=";"
                for e in range(len(st)):
                    if e==len(st)-1:
                        s1+=st[e]
                    else:
                        s1+=st[e]
                        s1+="."
                s1+=" Exit"
                s_exit.append(s1)
                st.remove(kk[n])
        for l in range(len(th)):
            th[l].start()
            fi.write(s_entry[l]+'\n')
        for l in range(len(th)):
            th[l].join()
            fi.write(s_exit[l]+'\n')
        


# Open the file and load the file
with open('Milestone1\Milestone1B.yaml') as f:
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
    
