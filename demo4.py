from tkinter import *
import serial
from serial.tools import list_ports

def connect_menu_inti():
    global root, connect_btn, refresh_btn
    root = Tk()
    root.title("Serial communication")
    root.geometry("500x500")
    root.config(bg="white")

    port_label = Label(root, text="Available Port(s): ", bg="white")
    port_label.grid(column=1, row=2, pady=20, padx=10)
    port_bd = Label(root, text="Baude Rate ", bg="white")
    port_bd.grid(column=1, row=3, pady=20, padx=10)

    refresh_btn = Button(root, text="R", height=2, width=10, command = update_coms)
    refresh_btn.grid(column=3, row=2)
    connect_btn = Button(root, text="Connect", height=2, width=10, state="disabled", command = connexion)
    connect_btn.grid(column=3, row=4)
    baud_select()
    update_coms()

def connect_check(args):
    if "-" in clicked_com.get() or "-" in clicked_bd.get():
        connect_btn["state"] = "disable"
    else :
        connect_btn["state"] = "active"

 
def baud_select():
    global clicked_bd, drop_bd
    clicked_bd = StringVar()
    bds = ["-","600","1200","9600"]
    clicked_bd.set(bds[0])
    drop_bd = OptionMenu(root, clicked_bd, *bds, command=connect_check)
    drop_bd.config(width = 20)
    drop_bd.grid(column = 2, row = 3, padx = 50)

def update_coms():
    global clicked_com, drop_COM
    ports = serial.tools.list_ports.comports()
    coms = [com[0] for com in ports]
    coms.insert(0, "-")
    try:
        drop_COM.destroy()
    except:
        pass
    clicked_com = StringVar()
    clicked_com.set(coms[0])
    drop_COM = OptionMenu(root, clicked_com, *coms, command=connect_check)
    drop_COM.config(width = 20)
    drop_COM.grid(column = 2, row = 2, padx = 50)
    connect_check(0)

def readSerial():
    global serialData
    while serialData :
        data = ser.readline()
        print(data.decode('utf8'))
        # if len(data) > 0:
        #     try:
        #         sensor = int(data.decode('utf8'))
        #         print(sensor)
        #     except:
        #         pass

def connexion():
    global ser, serialData
    if connect_btn["text"] in "Disconnect":
        serialData = False
        connect_btn["text"] = "Connect"
        refresh_btn["state"] = "active"
        drop_bd["state"] = "active"
        drop_COM["state"] = "active"
    else :
        serialData = True
        connect_btn['text'] = "Disconnect"
        refresh_btn["state"] = "disable"
        drop_bd["state"] = "disable"
        drop_COM["state"] = "disable"
        port = clicked_com.get()
        baud = clicked_bd.get()
        try:
            ser = serial.Serial(port, baud, timeout=0)
        except:
            pass
        readSerial()


connect_menu_inti()
root.mainloop()