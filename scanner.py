"""import nmap

scanner = nmap.PortScanner()

ip = '127.0.0.1'

for i  in range(75,80):
    
    res = scanner.scan(ip,i);
    res = res['scan'][ip]['tcp'][i]['state']

    print('port {} state: {}'.format(i,res))
"""
from tkinter import Tk,Frame,Entry

root = Tk()
root.geometry("512x512")
frame = Frame(root)
frame.pack()

ip = Entry(frame,width=20)
ip.insert(0,'IP')
ip.pack(padx=5,pady=5)
root.title("Port Scanner")
root.mainloop()