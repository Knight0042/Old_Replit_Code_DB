import tkinter as tk

window = tk.Tk()
window.title('Tkinter Experimenting')
window.configure(bg='black')

# menu = tk.Menu(window)
# item = tk.Menu(menu)
# item.add_command(label='New')
# menu.add_cascade(label='File', menu=item)
# window.config(menu=menu)

greeting = tk.Label(
  text='Hello, Welcome to the Calculator!',
  fg="yellow",
  bg='black',
  width=30,
  height=2
  )
greeting2 = tk.Label(
  text='Student Total 1: ',
  fg="yellow",
  bg='black',
  width=30,
  height=2
  )

entry = tk.Entry(
  fg='yellow',
  bg='gray',
  width=30,
  # height=2
)
def clicked():
  name = entry.get()
  user_name = tk.Label(
    text=f'Your name is {name}',
    fg="yellow",
    bg='black',
    width=30,
    height=2
  )
  user_name.grid(column = 1, row = 3)
button = tk.Button(
  text='Finished',
  fg="yellow",
  bg='black',
  width=15,
  height=2,
  activebackground = 'gray',
  activeforeground = 'yellow',
  command=clicked
  )
text_box = tk.Text(
  fg='yellow',
  bg='gray')


# all_things =[]
# all_things.append(greeting)
# all_things.append(entry)
# for i in all_things:
#   i.pack()
greeting.grid(column = 1, row = 0)
greeting2.grid(column = 1, row = 1)
# button.pack()
entry.grid(column = 1, row = 2)
button.grid(column = 2, row = 2)
# text_box.grid(column = 0, row = 0)
# name = entry.get()
# name

# entry.insert(0, name)
# name
# entry.delete(0, 4)

window.mainloop()

