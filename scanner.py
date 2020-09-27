from tkinter import Tk,Frame,Entry,StringVar,Label,Listbox,Text,Button,END,scrolledtext
from functools import partial
import nmap


root = Tk()
root.geometry("612x512")
root.configure(bg='#F1F1F1')

def scan(ip,start,end,textBox):

    ip = ip.get()
    rangeStart = int(start.get())
    rangeEnd = int(end.get())
    textBox.delete('1.0',END)

    scanner = nmap.PortScanner()

    for i  in range(rangeStart,rangeEnd+1):
        
        res = scanner.scan(ip,str(i))
        res = res['scan'][ip]['tcp'][i]

        output = "---------------------\n"
        output += "Port: {} \n".format(i)
        output += "Name: {} \n".format(res['name'])
        output += "State: {} \n".format(res['state'])
        textBox.insert(END,output)

def createLabel(root,row,column,text,padx,pady):

    labelText=StringVar()
    labelText.set(text)
    labelDir=Label(root, textvariable=labelText, height=4, bg="#F1F1F1")
    labelDir.grid(row=row,column=column, padx=padx,pady=pady)

    return labelDir

def createEntry(root,row,column,width,padx,pady):

    ip = Entry(root,width=width)
    ip.grid(row=row,column=column, padx=padx,pady=pady)
    return ip

ipLabel = createLabel(root,1,1,"IP",10,10)

ip = createEntry(root,1,2,20,5,10)

portLabel = createLabel(root,1,3,"Port Range",5,10)

portStart = createEntry(root,1,4,8,5,10)

colonLabel = createLabel(root,1,5,":",0,0)

portEnd = createEntry(root,1,6,8,5,10)

text = scrolledtext.ScrolledText(root)
text.grid(column=1,row=2,columnspan=12, padx=10,pady=10)

scanPort = partial(scan,ip,portStart,portEnd,text)

button = Button(root, text="SCAN", command = scanPort)
button.grid(row=1,column=7,padx=5,pady=10)

root.title("Port Scanner")
root.resizable(width=False, height=False)
root.mainloop()