"""import nmap

scanner = nmap.PortScanner()

ip = '127.0.0.1'

for i  in range(75,80):
    
    res = scanner.scan(ip,i);
    res = res['scan'][ip]['tcp'][i]['state']

    print('port {} state: {}'.format(i,res))
"""
from tkinter import Tk,Frame,Entry,StringVar,Label,Listbox,Text,Button,END
from functools import partial

root = Tk()
root.geometry("812x512")

def scan(ip,start,end,textBox):

    ip = ip.get() 
    rangeStart = start.get()
    rangeEnd = end.get()
    

labelText=StringVar()
labelText.set("IP ADDRESS")
labelDir=Label(root, textvariable=labelText, height=4)
labelDir.grid(row=1,column=1, padx=10,pady=10)

ip = Entry(root,width=20)
ip.grid(row=1,column=2, padx=5,pady=10)


labelText=StringVar()
labelText.set("Port Range:")
labelDir=Label(root, textvariable=labelText, height=4)
labelDir.grid(row=1,column=3, padx=5,pady=10)

portStart = Entry(root,width=8)
portStart.grid(row=1,column=4, padx=4,pady=10)

labelText=StringVar()
labelText.set(":")
labelDir=Label(root, textvariable=labelText, height=4)
labelDir.grid(row=1,column=5, padx=0,pady=0)

portEnd = Entry(root,width=8)
portEnd.grid(row=1,column=6, padx=5,pady=10)


text = Text(root)
text.grid(column=1,row=2,columnspan=12, padx=10,pady=10)

scanPort = partial(scan,ip,portStart,portEnd,text)

button = Button(root, text="SCAN", command = scanPort)
button.grid(row=1,column=7,padx=5,pady=10)

root.title("Port Scanner")
root.mainloop()