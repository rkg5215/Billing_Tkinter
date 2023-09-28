import tkinter
from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("700x300")
style= ttk.Style()
style.theme_use('clam')


frame = tkinter.Frame(window)
frame.grid(padx=5, pady=5)

c = ('s.no.', 'desc', 'qty', 'price', 'total')
scrollbary = Scrollbar(window, orient=VERTICAL)

tree = ttk.Treeview(window, columns=c, show="headings")
tree.grid(row=5, column=0, columnspan=4, padx=10, pady=5)
# tree.place(relx=0.01, rely=0.128, width=646, height=200)
tree.configure(yscrollcommand=scrollbary.set)

tree.configure(selectmode="extended")

scrollbary.configure(command=tree.yview)
scrollbary.place(relx=0.934, rely=0.128, width=22, height=220)


# tree.heading('#0', text='Serial',anchor=W)
tree.heading('s.no.', text='S.No.')
tree.heading('desc', text='Description')
tree.heading('qty', text='Quantity')
tree.heading('price', text='Unit Price')
tree.heading('total', text='Total')

tree.column("desc", anchor=tkinter.CENTER)

#enter data

tree.insert(parent='',index='end',values=("1", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00002',values=("2", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00003',values=("3", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00004',values=("4", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00005',values=("5", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00006',values=("6", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00007',values=("7", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00008',values=("8", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00001',values=("1", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00002',values=("2", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00003',values=("3", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00004',values=("4", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00005',values=("5", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00006',values=("6", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00007',values=("7", "Ravi", "Parle" "2", "5", "10"))
tree.insert(parent='',index='end',text='00008',values=("8", "Ravi", "Parle" "2", "5", "10"))






window.mainloop()