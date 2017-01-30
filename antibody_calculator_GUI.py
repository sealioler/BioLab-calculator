import Tkinter as tk
import tkMessageBox


def calculate_click(): #calculate button, calc & show results
    final=float(final_volumes.get())
    start=float(start_folds.get())
    if final >=0 and start>1:
        concentration=final/start
        dilute_solution=final-concentration
        antibody_lable.config(text=str("%.3f" % concentration)+' ul Antibody')
        dilute_lable.config(text=str("%.3f" % dilute_solution)+' ul Dilution')
    else:
        result=tkMessageBox.showerror("Calculate error", "Please enter right value.")
                                     
                     
def reset_click(): #reset button, clear all values and results
    start_folds.set('0')
    final_volumes.set('0')
    antibody_lable.config(text='? ul Antibody')
    dilute_lable.config(text='? ul Dilution')


def exit_click(): # exit button, leave program
    result=tkMessageBox.askokcancel("Exit?", "Ending calculator?")
    if result==True:
        win.destroy()


win=tk.Tk()
win.title("Antiboy Calculator")
win.geometry()
win.resizable(0,0)
#create a window with title, window size depend on content, user can't adjust


welcome_message=tk.LabelFrame(win, text="Please enter values:")
welcome_message.grid(row=0)
start_folds=tk.DoubleVar()
conc_lable=tk.Label(welcome_message, text="Concentration Fold:")
conc_lable.grid(row=2, column=1)
conc_entry=tk.Entry(welcome_message, textvariable=start_folds)
conc_entry.grid(row=2, column=2)
start_folds.set('250')

final_volumes=tk.DoubleVar()
fold_lable=tk.Label(welcome_message, text="Final Volume (ul) :")
fold_lable.grid(row=3, column=1)
fold_entry=tk.Entry(welcome_message, textvariable=final_volumes)
fold_entry.grid(row=3, column=2)
final_volumes.set('1000')
#values input area

  
calculate_button=tk.Button(win, text="Calculate", command=calculate_click)
calculate_button.grid(row=1)
#calculate button


result_message=tk.LabelFrame(win, text="Your result is:")
result_message.grid(row=2)
adding_row=tk.Label(result_message, text="Adding")
adding_row.grid(row=1)

antibody_lable=tk.Label(result_message, text="? ul Antibody")
antibody_lable.grid(row=2)

in_row=tk.Label(result_message, text="in")
in_row.grid(row=3)

dilute_lable=tk.Label(result_message, text="? ul Dilution")
dilute_lable.grid(row=4)
# results showing area


reset_button=tk.Button(win, text="Reset", command=reset_click)
reset_button.grid(row=3)
#reset button


exit_button=tk.Button(win, text="Exit", command=exit_click)
exit_button.grid(row=6, column=0)
#exit button

win.mainloop()
