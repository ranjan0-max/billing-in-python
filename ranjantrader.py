from tkinter import *
from tkinter import ttk
import tkinter as tk
from csv import DictWriter
import os


win = tk.Tk()
win.title("Ranjan Trader")
win.geometry("950x400")

# Label
bill_label = ttk.Label(win, text='bill_no : ')
bill_label.grid(row=0, column=0, sticky=tk.W)

date_label = ttk.Label(win, text='Date : ')
date_label.grid(row=1, column=0, sticky=tk.W)

to_label = ttk.Label(win, text='To : ')
to_label.grid(row=2, column=0, sticky=tk.W)

name_label = ttk.Label(win, text='Product Name')
name_label.grid(row=3, column=0, padx=20)

quantity_label = ttk.Label(win, text='Quantity')
quantity_label.grid(row=3, column=1, padx=20)

bag_kg = ttk.Label(win, text='Bag / Kg')
bag_kg.grid(row=3, column=2, padx=20)

gst_label = ttk.Label(win, text='GST')
gst_label.grid(row=3, column=3, padx=20)

rate_label = ttk.Label(win, text='Rate')
rate_label.grid(row=3, column=4, padx=20)

net_amount_label = ttk.Label(win, text='Net amount')
net_amount_label.grid(row=3, column=5, padx=20)

adding_iteam_label = ttk.Label(win, text='Added To File')
adding_iteam_label.grid(row=6, column=0, padx=20)


# Entry box
bill_var = tk.IntVar()
bill_e_box = ttk.Entry(win, width=16, textvariable=bill_var)
bill_e_box.grid(row=0, columnspan=2, pady=5)


date_var = tk.StringVar()
date_e_box = ttk.Entry(win, width=16, textvariable=date_var)
date_e_box.grid(row=1, columnspan=2, pady=5)
date_e_box.focus()

to_name_var = tk.StringVar()
to_name_e_box = ttk.Entry(win, width=16, textvariable=to_name_var)
to_name_e_box.grid(row=2, columnspan=2, pady=5)

p_name_var = tk.StringVar()
name_e_box = ttk.Entry(win, width=16, textvariable=p_name_var)
name_e_box.grid(row=4, column=0, padx=10)

quantity_var = tk.IntVar()
quantity_e_box = ttk.Entry(win, width=16, textvariable=quantity_var)
quantity_e_box.grid(row=4, column=1, padx=10)

bag_kg_var = tk.StringVar()
bag_kg_e_box = ttk.Entry(win, width=16, textvariable=bag_kg_var)
bag_kg_e_box.grid(row=4, column=2, padx=10)

gst_var = tk.IntVar()
gst_e_box = ttk.Entry(win, width=16, textvariable=gst_var)
gst_e_box.grid(row=4, column=3, padx=10)

rate_var = tk.IntVar()
rate_e_box = ttk.Entry(win, width=16, textvariable=rate_var)
rate_e_box.grid(row=4, column=4, padx=10)

# variables declare

gst_amount_5 = 0
gst_amount_12 = 0
gst_amount_18 = 0
gst_amount_28 = 0

gst_5 = 0
gst_12 = 0
gst_18 = 0
gst_28 = 0

total = 0

counter = 6

bill_count = 0

name_count = 0

def bill_no(billno):
    global bill_count
    
    if bill_count == 0:
        new_bill_no = billno
        bill_count = bill_count + 1
        return new_bill_no
        
    else:
        new_bill_no = billno + bill_count
        bill_count = bill_count + 1
        return new_bill_no

def add():
    global counter
    global total
    global gst_amount_5
    global gst_amount_12
    global gst_amount_18
    global gst_amount_28
    global gst_5
    global gst_12
    global gst_18
    global gst_28

    counter = counter+1

    current_bill_no = bill_var.get()
    date = date_var.get()
    to_name = to_name_var.get()
    prod_name = p_name_var.get()
    quantity = quantity_var.get()           # Get the values from entry box
    gst = gst_var.get()
    original_cost = rate_var.get()
    bag_kg = bag_kg_var.get()

    if gst == 5:
        gst_amount_5 = original_cost - (original_cost * ( 100 / ( 100 + gst)))  
        gst_amount_5 = gst_amount_5*quantity
        gst_5 = gst_5 + round(gst_amount_5,2)

    elif gst == 12:
        gst_amount_12 = original_cost - (original_cost * ( 100 / ( 100 + gst)))  
        gst_amount_12 = gst_amount_12*quantity
        gst_12 = gst_12 + round(gst_amount_12,2)

    elif gst == 18:
        gst_amount_18 = original_cost - (original_cost * ( 100 / ( 100 + gst)))  
        gst_amount_18 = gst_amount_18 * quantity
        gst_18 = gst_18 + round(gst_amount_18,2)

    elif gst == 28:
        gst_amount_28 = original_cost - (original_cost * ( 100 / ( 100 + gst)))  
        gst_amount_28 = gst_amount_28 * quantity
        gst_28 = gst_28 + round(gst_amount_28,2)
    else:
        pass

    gst_amount = original_cost - (original_cost * ( 100 / ( 100 + gst)))  
    original_cost = original_cost - round(gst_amount,2)          # Logic of how to Calculate amount
    total_prize = quantity*round(original_cost,2)

    # os.mkdir("ranjan trader")
    
    with open('temp_file.csv', 'a', newline="") as fc:
        csv_writer = DictWriter(
            fc, fieldnames=['I.Name', 'Quantity', 'GST', 'Rate', 'Total Prize'])
        if os.stat('temp_file.csv').st_size == 0:
            with open('temp_file.csv', 'a',) as fc:
                fc.write(f'Bill NO : {bill_no(current_bill_no)}\nDate : {date}\nRanjan Trader\nGST no : 02BIAPC942K1ZK\nP.no : 8627814292 \nTo : {to_name}\n')
            csv_writer.writeheader()
        csv_writer.writerow({
            # What to write and how to write in files
            'I.Name': prod_name,
            'Quantity': str(quantity)+bag_kg.upper(),
            'GST': str(gst)+'%',
            'Rate': round(original_cost,2),
            'Total Prize': round(total_prize,2)
        })
    total = total+round(total_prize,2)
    total_label = ttk.Label(win, text=round(gst_5,2) + round(gst_12,2) + round(gst_18,2) + round(gst_28,2) + round(total,2))
    total_label.grid(row=4, column=5, padx=20)

    l1 = ttk.Label(win, text=prod_name)
    l1.grid(row=counter, column=0, sticky=W)

    l2 = ttk.Label(win, text=round(total_prize,2))
    l2.grid(row=counter, column=1)

    name_e_box.delete(0, tk.END)
    quantity_e_box.delete(0, tk.END)
    gst_e_box.delete(0, tk.END)
    rate_e_box.delete(0, tk.END)
    name_e_box.focus()

def d_call():
    global name_count
    name_count = name_count + 1

def save_copy():

    global name_count
    global counter
    global gst_5
    global gst_12
    global gst_18
    global gst_28
    global total

    grand_total = round(gst_5,2) + round(gst_12,2) + round(gst_18,2) + round(gst_28,2) + round(total,2)

    date = date_var.get()

    if os.path.exists(r"temp_file.csv"):
        if os.path.exists("Ranjan trader"):
            if os.path.exists(f'Ranjan trader\Ranjan {date}({name_count}).csv'):
                d_call()
                with open('temp_file.csv', 'r') as fc:
                    with open(f'Ranjan trader\Ranjan {date}({name_count}).csv', 'w') as wf:
                        wf.write(fc.read())
                with open(f'Ranjan trader\Ranjan {date}({name_count}).csv', 'a') as wf:
                    wf.write(
                        f"\nGST 5% = {round(gst_5,2)}\nGST 12% = {round(gst_12,2)}\nGST 18% = {round(gst_18,2)}\nGST 28% = {round(gst_28,2)}\n                                                           Grand totale : {round(grand_total,2)}\n\n- - - - - - - - - - - - - - -- - - - - -\n\n\n")
            else:
                name_count = 0
                with open('temp_file.csv', 'r') as fc:
                    with open(f'Ranjan trader\Ranjan {date}({name_count}).csv', 'w') as wf:
                        wf.write(fc.read())
                with open(f'Ranjan trader\Ranjan {date}({name_count}).csv', 'a') as wf:
                    wf.write(
                        f"\nGST 5% = {round(gst_5,2)}\nGST 12% = {round(gst_12,2)}\nGST 18% = {round(gst_18,2)}\nGST 28% = {round(gst_28,2)}\n                                                           Grand totale : {round(grand_total,2)}\n\n- - - - - - - - - - - - - - -- - - - - -\n\n\n")         
        else:
            os.mkdir("Ranjan trader")
            with open('temp_file.csv', 'r') as fc:
                with open(f'Ranjan trader\Ranjan {date}({name_count}).csv', 'w') as wf:
                    wf.write(fc.read())
            with open(f'Ranjan trader\Ranjan {date}({name_count}).csv', 'a') as wf:
                wf.write(
                    f"\nGST 5% = {round(gst_5,2)}\nGST 12% = {round(gst_12,2)}\nGST 18% = {round(gst_18,2)}\nGST 28% = {round(gst_28,2)}\n                                                           Grand totale : {round(grand_total,2)}\n\n- - - - - - - - - - - - - - -- - - - - -\n\n\n")
    else:
        pass

    name_e_box.delete(0, tk.END)
    quantity_e_box.delete(0, tk.END)
    gst_e_box.delete(0, tk.END)
    rate_e_box.delete(0, tk.END)
    to_name_e_box.delete(0, tk.END)
    date_e_box.delete(0, tk.END)
    total = 0
    gst_5 = 0
    gst_12 = 0
    gst_18 = 0
    gst_28 = 0
    total = 0
    counter = 6
    os.remove("temp_file.csv")
    date_e_box.focus()


def delete():
    global bill_count
    global counter
    global gst_5
    global gst_12
    global gst_18
    global gst_28
    global total
    # This function erase the data in file
    name_e_box.delete(0, tk.END)
    quantity_e_box.delete(0, tk.END)
    gst_e_box.delete(0, tk.END)
    rate_e_box.delete(0, tk.END)
    to_name_e_box.delete(0, tk.END)
    date_e_box.delete(0, tk.END)
    total = 0
    bill_count = bill_count - 1
    counter = 6
    gst_5 = 0
    gst_12 = 0
    gst_18 = 0
    gst_28 = 0
    os.remove("temp_file.csv")
    date_e_box.focus()


add_button = ttk.Button(win, text='Add', command=add)
add_button.grid(row=4, column=6, padx=20)

save_copy_button = ttk.Button(win, text='Save', command=save_copy)
save_copy_button.grid(row=5, column=5, padx=20)

del_button = ttk.Button(win, text='Delete', command=delete)
del_button.grid(row=4, column=7, padx=20)


win.mainloop()
