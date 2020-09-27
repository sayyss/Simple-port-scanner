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
    

labelText=StringVar()
labelText.set("IP ADDRESS")
labelDir=Label(root, textvariable=labelText, height=4, bg="#F1F1F1")
labelDir.grid(row=1,column=1, padx=10,pady=10)

ip = Entry(root,width=20)
ip.grid(row=1,column=2, padx=5,pady=10)


labelText=StringVar()
labelText.set("Port Range:")
labelDir=Label(root, textvariable=labelText, height=4,bg="#F1F1F1")
labelDir.grid(row=1,column=3, padx=5,pady=10)

portStart = Entry(root,width=8)
portStart.grid(row=1,column=4, padx=4,pady=10)

labelText=StringVar()
labelText.set(":")
labelDir=Label(root, textvariable=labelText, height=4,bg="#F1F1F1")
labelDir.grid(row=1,column=5, padx=0,pady=0)

portEnd = Entry(root,width=8)
portEnd.grid(row=1,column=6, padx=5,pady=10)


text = scrolledtext.ScrolledText(root)
text.grid(column=1,row=2,columnspan=12, padx=10,pady=10)

scanPort = partial(scan,ip,portStart,portEnd,text)

button = Button(root, text="SCAN", command = scanPort)
button.grid(row=1,column=7,padx=5,pady=10)

root.title("Port Scanner")
root.mainloop()