import tkinter
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox
import re


def time():
    string = datetime.datetime.now().time().strftime('%I:%M:%S %p')
    l15.config(text=string)
    l15.after(1000, time)

#call back Function

def checkname(name):
    if name != '' and all(chr.isalpha() or chr.isspace() for chr in name):
        return True
    if name=="":
        return True
    else:
        messagebox.showwarning("Invalid Name", "Not allowed"" " +name[-1])
        return False

def checkaddress(address):

    if address != "" and all(chr.isalnum() or chr.isspace() for chr in address):
        return True
    if address=="":
        return True
    else:
        messagebox.showwarning("Invalid Address", "Not allowed" " " +address[-1])
        return False

def checkphone(phone):
    if phone.isdigit():
        return True
    if phone == "":
        return True

    else:
        messagebox.showwarning("Invalid Phone Number", "Enter Only Digit")
        return False

def checkgst(gst):
    if gst.isalnum():
        return True
    if gst=="":
        return True
    else:
        messagebox.showwarning("Invalid GST", "Not allowed" " " +gst[-1])
        return False

def checkdescription(description):
    if description != '' and all(chr.isalnum() or chr.isspace() for chr in description):
        return True
    if description=="":
        return True
    else:
        messagebox.showwarning("Invalid Item", "Not allowed" " " +description[-1])
        return False

def checkquantity(quantity):

    if quantity != '' and all(chr.isdigit() or chr=="." for chr in quantity):
        return True
    if quantity=="":
        return True
    else:
        messagebox.showwarning("Invalid Quantity", "Not allowed" " " +quantity[-1])
        return False

def checkprice(price):

    if price != '' and all(chr.isdigit() or chr=="." for chr in price):
        return True
    if price == "":
        return True
    else:
        messagebox.showwarning("Invalid Price", "Enter Only Digit")
        return False


def add_item():
    pattern = re.compile(r"^[0-9]\d*(\.\d+)?$")
    pattern2 = re.compile(r"^[.]\d*(\d+)?$")
    global t
    t = (re.sub(' +', ' ', e6.get()))  # Remove Extra Space in Description

    match1 = re.search(pattern, e7.get())
    match2 = re.search(pattern2, e7.get())
    match3 = re.search(pattern, e8.get())
    match4 = re.search(pattern2, e8.get())

##----This is For Entry Validation

    if e1.get() == "" or e1.get().isspace():
        messagebox.showinfo("Alert", "Enter Name")
    elif e2.get() == "" or e2.get().isspace():
        messagebox.showinfo("Alert", "Enter Address")
    elif e3.get() == "" or len(e3.get()) != 10:
        messagebox.showinfo("Alert", "Enter Valid Phone Number")
    elif e4.get() != "" and len(e4.get()) != 15:
        messagebox.showinfo("Alert", "GST Number Should be 15")
    elif t == "" or t == "0" or t.isspace():
        messagebox.showinfo("Alert", "Enter Item")
    elif e7.get() == "" :
        messagebox.showinfo("Alert", "Enter Quantity")
    elif match1 or match2:
        m = float(e7.get()) * 1
        if float('%.3f' % m) == 0.0:
            messagebox.showinfo("Alert", "Quantity Can't be Acceptable")
        elif e8.get() == "" :
            messagebox.showinfo("Alert", "Enter Unit Price")
        elif match3 or match4:
            s = float(e8.get()) * 1
            if float('%.2f' % s) == 0.0:
                messagebox.showinfo("Alert", "Unit Price Can't be Acceptable")
            else:
                add_item_row()  # Adding Items In Row
        else:
            messagebox.showinfo("Alert", "Unit Price Pattern is Wrong")
    else:
        messagebox.showinfo("Alert", "Quantity should Be digit")

def clear_item():
    e6.delete(0, tkinter.END)
    e7.delete(0, tkinter.END)
    e7.insert(0, "1")
    e8.delete(0, tkinter.END)

def clear_whole_item():
    e1.delete(0, tkinter.END)
    e2.delete(0, tkinter.END)
    e3.delete(0, tkinter.END)
    e4.delete(0, tkinter.END)
    # e5.delete(0, tkinter.END)
    # e5.insert(0, "1")
    clear_item()
    tree.delete(*tree.get_children())
    old_list.clear()
    calculation()
    treecount()

def treecount():
    global serial
    serial = (len(tree.get_children()))
    l13.config(text=serial+1)

old_list=[]
def add_item_row():
    # sno = int(e5.get())
    serial = (len(tree.get_children()))
    sno = serial + 1
    l13.config(text=sno+1)
    desc = t
    quan = float(e7.get())
    qty = float('%.3f' % quan)
    z = float(e8.get())
    price = float('%.2f' % z)
    total = float('%.2f' % (qty * price))  # Upto 2 decimal Places ('%.2f' %)
    invoice_item = [sno, desc, qty, price, total]
    tree.insert('', 100, values=invoice_item)
    old_list.append(invoice_item)
    # e5.delete(0, tkinter.END)
    # e5.insert(0, sno + 1)
    clear_item()
    calculation()
    print(old_list)


def calculation():
    if e4.get() == "":
        subtotal = sum(item[4] for item in old_list)
        l9.config(text="Subtotal = %.2f" % subtotal)
        l10.config(text="Total Tax = 0")
        l11.config(text="Bill Amount = %.2f" % subtotal)

    else:
        sub = sum(item[4] for item in old_list)
        cgst = float('%.2f' % (sub * 0.09))
        sgst = float('%.2f' % (sub * 0.09))
        igst = 0
        totaltax = float('%.2f' % (cgst + sgst + igst))
        finaltotal = float('%.2f' % (sub + cgst + sgst + igst))

        l9.config(text="Subtotal = %.2f" % sub)
        l10.config(text="Total Tax = %.2f" % totaltax)
        l11.config(text="Bill Amount = %.2f" % finaltotal)


def delete_item():

    x = tree.selection()
    if x==():
        messagebox.showwarning("Warning", "Please Select an Item")
    else:
        q=messagebox.askquestion("Delete Item", "Are You Sure want to delete?")
        if (q=="yes"):
            for result in x:

                t = tree.index(result)
                l12.config(text=t)
                old_list.pop(t)
                tree.delete(result)
    treecount()
    print(len(tree.get_children()))
    print(old_list)
    calculation()


def new_invoice():
    e = messagebox.askquestion("New Invoice", "Are You Sure want to Create New Invoice?")
    if (e == "yes"):
        clear_whole_item()

def generate_invoice():
    if old_list == []:
        messagebox.showwarning("Alert", "Item List Is Empty")
    elif e1.get() == "" or e1.get().isspace():
        messagebox.showinfo("Alert", "Enter Name")
    elif e2.get() == "" or e2.get().isspace():
        messagebox.showinfo("Alert", "Enter Address")
    elif e3.get() == "" or len(e3.get()) != 10:
        messagebox.showinfo("Alert", "Enter Valid Phone Number")
    elif e4.get() != "" and len(e4.get()) != 15:
        messagebox.showinfo("Alert", "GST Number Should be 15")

    else:
        w = messagebox.askquestion("Generate Invoice", "Are You Sure want to Create Invoice?")
        if (w == "yes"):
            doc = DocxTemplate('Invoice Template/invoice.docx')
            s = datetime.datetime.now()
            y = s.date().strftime('%d/%m/%y')
            p = s.date().strftime('_%d_%m_%y_')
            t = s.time().strftime('%I_%M_%S_%p')

            name = re.sub(' +', ' ', e1.get())  # Remove Extra Space in Name
            address = re.sub(' +', ' ', e2.get())
            phone = e3.get()
            gst = e4.get()
            sub = sum(item[4] for item in old_list)
            if e4.get() == "":
                total = float('%.2f' % (sub))
                doc.render({"name": name,
                            "address": address,
                            "phone": phone,
                            "gst": gst,
                            "date": y,
                            "invoice_list": old_list,
                            "subtotal": sub,
                            "cgst": 0,
                            "sgst": 0,
                            "igst": 0,
                            "shipping": 0,
                            "total": total, })
                doc.save(name + p + t + ".docx")
                messagebox.showinfo("Success", "Invoice Created Successfully")
                print("GST NHI HAI")
                print(old_list)
                clear_whole_item()

            else:
                cgst = float('%.2f' % (sub * 0.09))
                sgst = float('%.2f' % (sub * 0.09))
                igst = 0
                total = float('%.2f' % (sub + cgst + sgst + igst))
                doc.render({"name": name,
                            "address": address,
                            "phone": phone,
                            "gst": gst,
                            "date": y,
                            "invoice_list": old_list,
                            "subtotal": sub,
                            "cgst": cgst,
                            "sgst": sgst,
                            "igst": igst,
                            "shipping": 0,
                            "total": total, })

                doc.save(name + p + t + ".docx")

                print("GST HAI")
                clear_whole_item()
                messagebox.showinfo("Success", "Invoice Created Successfully")

        else:
            pass


window = tkinter.Tk()

#--- Styling-----
back_color="skyblue"
font_size= ('Arial', 11, 'bold' )



window.title("Billing Management")
frame = tkinter.Frame(window,bg= back_color)
frame.pack(padx=5, pady=5)


##

l1 = tkinter.Label(frame, text="Name",bg=back_color, font=font_size)
l1.grid(row=0, column=0)

e1 = tkinter.Entry(frame)
e1.grid(row=1, column=0)

# Validate Command Entry

validate_name= frame.register(checkname)   #callback
e1.config(validate="key", validatecommand=(validate_name, "%P"))  #bind

l2 = tkinter.Label(frame, text="Address", bg=back_color, font=font_size)
l2.grid(row=0, column=1)

e2 = tkinter.Entry(frame)
e2.grid(row=1, column=1)

validate_address= frame.register(checkaddress)   #callback
e2.config(validate="key", validatecommand=(validate_address, "%P"))  #bind

l3 = tkinter.Label(frame, text="Phone", bg=back_color, font=font_size)
l3.grid(row=0, column=2)

e3 = tkinter.Entry(frame)
e3.grid(row=1, column=2)

validate_phone= frame.register(checkphone)   #callback
e3.config(validate="key",validatecommand=(validate_phone, "%P"))  #bind

l4 = tkinter.Label(frame, text="GST", bg=back_color, font=font_size)
l4.grid(row=0, column=3)

e4 = tkinter.Entry(frame)
e4.grid(row=1, column=3)

validate_gst= frame.register(checkgst)   #callback
e4.config(validate="key", validatecommand=(validate_gst, "%P"))  #bind

l5 = tkinter.Label(frame, text="S.No.", bg=back_color, font=font_size)
l5.grid(row=2, column=0)

# e5 = tkinter.Spinbox(frame, from_=1, to=100)
# e5.grid(row=3, column=0)

l6 = tkinter.Label(frame, text="Description", bg=back_color, font=font_size)
l6.grid(row=2, column=1)

e6 = tkinter.Entry(frame)
e6.grid(row=3, column=1)


validate_description= frame.register(checkdescription)   #callback
e6.config(validate="key", validatecommand=(validate_description, "%P"))  #bind


l7 = tkinter.Label(frame, text="Quantity", bg=back_color, font=font_size)
l7.grid(row=2, column=2)

e7 = tkinter.Spinbox(frame, from_=1, to=10000)
e7.grid(row=3, column=2)

validate_quantity= frame.register(checkquantity)   #callback
e7.config(validate="key", validatecommand=(validate_quantity, "%P"))  #bind

l8 = tkinter.Label(frame, text="Unit Price", bg=back_color, font=font_size)
l8.grid(row=2, column=3)

e8 = tkinter.Entry(frame)
e8.grid(row=3, column=3)

validate_price= frame.register(checkprice)   #callback
e8.config(validate="key", validatecommand=(validate_price, "%P"))  #bind

l9 = tkinter.Label(frame, text="Subtotal", bg=back_color, font=font_size)
l9.grid(row=4, column=0)

l10 = tkinter.Label(frame, text="Total Tax", bg=back_color, font=font_size)
l10.grid(row=4, column=1)

l11 = tkinter.Label(frame, text="Bill Amount", bg=back_color, font=font_size)
l11.grid(row=4, column=2)

l12 = tkinter.Label(frame, text="Index", bg=back_color, font=font_size)
l12.grid(row=8, column=0)

l13 = tkinter.Label(frame, text="1", bg="white", font=font_size)
l13.grid(row=3, column=0)

#------Date and Time Lebel

l14 = tkinter.Label(frame, text=datetime.datetime.now().date().strftime('%d/%m/%Y'), bg=back_color, font=font_size)
l14.grid(row=8, column=2)

l15 = tkinter.Label(frame,bg=back_color, font=font_size)
l15.grid(row=8, column=3)
time()

# ----Add Product Button & Style
button_font_color="black"
button_font_size= ('Arial', 14)

b1 = tkinter.Button(frame, text="Add Item", bg="#FFD814", fg=button_font_color, font=('Arial', 12 ), command=add_item )
b1.grid(row=4, column=3, pady=20)



c = ('s.no.', 'desc', 'qty', 'price', 'total')

tree = ttk.Treeview(frame, columns=c, show="headings")
tree.grid(row=5, column=0, columnspan=4, padx=10, pady=5)
tree.heading('s.no.', text='S.No.')
tree.heading('desc', text='Description')
tree.heading('qty', text='Quantity')
tree.heading('price', text='Unit Price')
tree.heading('total', text='Total')
# ttk.Treeview.config(font=font_size)

# ----Delete Item Button
b4 = tkinter.Button(frame, text="Delete Item",bg="#ED2024",fg=button_font_color, font=button_font_size, command=delete_item)
b4.grid(row=6, column=0, columnspan=2, sticky="news", padx=10, pady=5)

# ----Save Invoice Button
b2 = tkinter.Button(frame, text="Generate Invoice", bg="#14A44D",fg=button_font_color, font=button_font_size, command=generate_invoice)
b2.grid(row=6, column=2, columnspan=2, sticky="news", padx=10, pady=5)

# ----New Invoice Button
b3 = tkinter.Button(frame, text="Create New Invoice", bg="#FF6700",fg=button_font_color, font=button_font_size, command=new_invoice)
b3.grid(row=7, column=0, columnspan=4, sticky="news", padx=10, pady=5)


window.mainloop()