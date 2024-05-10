import tkinter as tk
import serial

ser = serial.Serial('COM7', 9600)

def read_serial_data():
    data = ser.readline().decode('utf')
    # print(data)
    update(data)
    
    root.after(500, read_serial_data)

def update(data): 
    status = [int(x) for x in data.split(":")]
    # print(status) 

    if status[0] == 1:
        slot1_dis.configure(bg = "green")
    else :
        slot1_dis.configure(bg = "red")

    if status[1] == 1:
        slot2_dis.configure(bg = "green")
    else :
        slot2_dis.configure(bg = "red")

    if status[2] == 1:
        slot3_dis.configure(bg = "green")
    else :
        slot3_dis.configure(bg = "red")

    if status[3] == 1:
        slot4_dis.configure(bg = "green")
    else :
        slot4_dis.configure(bg = "red")
   

root = tk.Tk()
root.title("car parking GUI")
root.geometry("250x255")
root.configure(background='black')

slot1 = tk.Label(root, text="Slot - 1 ", bg="black", fg="white", font="fontObj")
slot1.grid(column=1, row=1, pady=20, padx=30)
slot1_dis = tk.Button(root, height=1, width=5, bg="black", state="disabled")
slot1_dis.grid(column=2, row=1)

slot2 = tk.Label(root, text="Slot - 2 ", bg="black", fg="white", font="fontObj")
slot2.grid(column=1, row=2, pady=20, padx=50)
slot2_dis = tk.Button(root, height=1, width=5, bg="black", state="disabled")
slot2_dis.grid(column=2, row=2)

slot3 = tk.Label(root, text="Slot - 3 ", bg="black", fg="white", font="fontObj")
slot3.grid(column=1, row=3, pady=20, padx=50)
slot3_dis = tk.Button(root, height=1, width=5, bg="black", state="disabled")
slot3_dis.grid(column=2, row=3)

slot4 = tk.Label(root, text="Slot - 4 ", bg="black", fg="white", font="fontObj")
slot4.grid(column=1, row=4, pady=20, padx=50)
slot4_dis = tk.Button(root, height=1, width=5, bg="black", state="disabled")
slot4_dis.grid(column=2, row=4)

# Start reading serial data
read_serial_data()

root.mainloop()
