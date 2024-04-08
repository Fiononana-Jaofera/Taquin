from algo import *

width = 800
height = 600

racine.geometry(f"{width}x{height}+{(racine.winfo_screenwidth()-width)//2}+{(racine.winfo_screenheight()-height)//2}")

container = tk.Frame(racine, width=width, height=height)
container.grid_rowconfigure(1, pad=width//8)
container.grid_propagate(False)
container.grid_anchor('center')
container.grid()

table = tk.Frame(container)
table.grid(row=0)

buttons = tk.Frame(container)
buttons.grid(row=1)

# Label
b1 = tk.Label(table, text='1', width=width//60, height=height//100, bg='purple', foreground='white', anchor='center', cursor='hand2', relief='sunken', name='l1')
b2 = tk.Label(table, text='2', width=width//60, height=height//100, bg='purple', foreground='white', anchor='center', cursor='hand2', relief='sunken', name='l2')
b3 = tk.Label(table, text='3', width=width//60, height=height//100, bg='purple', foreground='white', anchor='center', cursor='hand2', relief='sunken', name='l3')
b4 = tk.Label(table, text='4', width=width//60, height=height//100, bg='purple', foreground='white', anchor='center', cursor='hand2', relief='sunken', name='l4')
b5 = tk.Label(table, text='5', width=width//60, height=height//100, bg='purple', foreground='white', anchor='center', cursor='hand2', relief='sunken', name='l5')
b6 = tk.Label(table, text='6', width=width//60, height=height//100, bg='purple', foreground='white', anchor='center', cursor='hand2', relief='sunken', name='l6')
b7 = tk.Label(table, text='7', width=width//60, height=height//100, bg='purple', foreground='white', anchor='center', cursor='hand2', relief='sunken', name='l7')
b8 = tk.Label(table, text='8', width=width//60, height=height//100, bg='purple', foreground='white', anchor='center', cursor='hand2', relief='sunken', name='l8')
b9 = tk.Label(table, text='', width=width//60, height=height//100, bg='white', foreground='white', anchor='center', name='l0')

# Handle event
b1.bind("<Button-1>", on_label_click)
b2.bind("<Button-1>", on_label_click)
b3.bind("<Button-1>", on_label_click)
b4.bind("<Button-1>", on_label_click)
b5.bind("<Button-1>", on_label_click)
b6.bind("<Button-1>", on_label_click)
b7.bind("<Button-1>", on_label_click)
b8.bind("<Button-1>", on_label_click)
b9.bind("<Button-1>", on_label_click)

# Position
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

shuffle = tk.Button(buttons, text='Shuffle', cursor='hand2',bg='yellow', padx=width//16, name='shuffle')
resolve = tk.Button(buttons, text='Resolve', cursor='hand2',bg='green', padx=width//16, name="resolve")

shuffle.bind("<Button-1>", on_button_click)
resolve.bind("<Button-1>", on_button_click)

shuffle.grid(row=0, column=0)
resolve.grid(row=0, column=1)

racine.mainloop()