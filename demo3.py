from tkinter import *
import serial

SERIAL_PORT = 'COM7'
BAAUD_RATE =9600

ser = serial.Serial(SERIAL_PORT, BAAUD_RATE) 

def update_plot():
    data = ser.readline().decode('utf-8')
    print(data)
    if data == "Object is present":
        slot1_dis.configure(bg = "green")
    else :
        slot1_dis.configure(bg = "red")


# def readSerialData():
#     # ports = serial.tools.list_ports.comports()
#     serialInst = serial.Serial

#     # portsList = []

#     # for onePort in ports:
#     #     portsList.append(str(onePort))
#     #     print(str(onePort))

#     # val = input("Select Port: COM")

#     # for x in range(0,len(portsList)):
#     #     if portsList[x].startswith("COM" + str(val)):
#     #         portVar = "COM" + str(val)
#     #         print(portVar)

#     serialInst.baudrate = 9600
#     serialInst.port = "COM7"
#     serialInst.open()
#     packet = serialInst.readline()

#     while packet:
#         # if serialInst.in_waiting:
#         # print(packet.decode('utf').rstrip('\n'))
#             if packet.decode('utf') == "Object is present":
#                 slot1_dis.configure(bg = "green")
#             else :
#                 slot1_dis.configure(bg = "red")

def visual():
    global root, slot1_dis
    root = Tk()
    root.title("Serial communication")
    root.geometry("250x250")
    root.config(bg="white")

    slot1 = Label(root, text="Slot - 1 ", bg="white")
    slot1.grid(column=1, row=1, pady=20, padx=30)
    slot1_dis = Button(root, height=1, width=5, bg="red", state="disabled")
    slot1_dis.grid(column=2, row=1)
    # slot1_dis.configure(bg = "green")

    slot2 = Label(root, text="Slot - 2 ", bg="white")
    slot2.grid(column=1, row=2, pady=20, padx=50)
    slot2_dis = Button(root, height=1, width=5, bg="red", state="disabled")
    slot2_dis.grid(column=2, row=2)

    slot3 = Label(root, text="Slot - 3 ", bg="white")
    slot3.grid(column=1, row=3, pady=20, padx=50)
    slot3_dis = Button(root, height=1, width=5, bg="red", state="disabled")
    slot3_dis.grid(column=2, row=3)

    slot4 = Label(root, text="Slot - 4 ", bg="white")
    slot4.grid(column=1, row=4, pady=20, padx=50)
    slot4_dis = Button(root, height=1, width=5, bg="red", state="disabled")
    slot4_dis.grid(column=2, row=4)

    # while True:
    #     update_plot()


visual()
root.mainloop()