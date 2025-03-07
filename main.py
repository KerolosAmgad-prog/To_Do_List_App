import tkinter as tk
from tkinter import  messagebox



#  Initialize The main window
App_window=tk.Tk()
App_window.title("a Todo list Application") # the title of the window

Tasks=[]    # the list of tasks , is empty to add the tasks on it

def add_task():
    task=add_task_entry.get()
    if task :
        Tasks.append(task) # add task in Tasks List
        list_box.insert(tk.END,task) # insert in List Box
        add_task_entry.delete(0,tk.END) # delete what write in Entry box after press on button
    else:
        messagebox.showwarning("Warning","Please Enter Your Task !")

def delete_task():
    try:
        select_task=list_box.curselection()[0] # select the task that you want to delete it
        list_box.delete(select_task) # remove from List Box
        Tasks.pop(select_task) # remove from Tasks List
    except IndexError:
        messagebox.showwarning("Warning","Please Select the Task to delete it")

def list_tasks():
    if not Tasks :
        messagebox.showinfo("Info","The list of tasks is empty ")
    else :
        formatted_list=[]
        for index, task in enumerate(Tasks):
            formatted_list.append(f"# {index} : {task} ")
        ListTask="\n".join(formatted_list)
        messagebox.showinfo( "Tasks",ListTask) # to show as index : # 0 : Task
def welcome_message():
    messagebox.showinfo("Welcome",
                        "Welcome to the To-Do List Application!"
                        "\n\nAdd, delete, and manage your tasks easily.") # welcome message when opn the App

# the code of creation of main window
#-------------------------------------

# Add Tasks (Button) & (Entry Box)
add_task_button=tk.Button(App_window,text="Add Task",command=add_task)
add_task_button.grid(row=0,column=1 ,padx=10 , pady=10)
add_task_entry=tk.Entry(App_window,width=40)
add_task_entry.grid(row=0 ,column=0 ,padx=10 , pady=10)
#-----------------------------------------------------------------------------

#Delete Tasks (Button) & (List Box)
delete_task_button=tk.Button(App_window, text="Delete Task",command=delete_task)
delete_task_button.grid(row=1,column=1 ,padx=10 , pady=10)
list_box=tk.Listbox(App_window,width=50 , height=10)
list_box.grid(row=1 ,column=0 ,padx=10 , pady=10)
#--------------------------------------------------------------------------------

# List tasks (Button)
list_button=tk.Button(App_window, text="List Tasks",command= list_tasks)
list_button.grid(row=2 , column=1 ,padx=10 , pady=10)

App_window.after(100,welcome_message) # after 100 ms , the message will remove or disappear
App_window.mainloop() # operating the window


