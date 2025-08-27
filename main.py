import tkinter as tk
import ui

# create app name it app or root
app = tk.Tk()
# set a title of the app
app.title("Task Manager")
# give it a size
app.geometry("720x480")

# fetch all the tasks with the function
ui.show_all_tasks_frame(app)

# show/run the app
app.mainloop()