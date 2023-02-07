from tkinter import*
from tkinter import messagebox 
root = Tk()


root.title("Heart_Diagnose_Report")
root.geometry("600x600")
root.configure(bg="limegreen")

Question1_r1=StringVar(value="0")
question1 = Label(root, text="Do you experience shortness of breath during routine activities?")
question1.pack()
radiobutton1 = Radiobutton(root, text="Yes", variable = Question1_r1, value = "Yes")
radiobutton1.pack()
radiobutton2 = Radiobutton(root, text="No", variable = Question1_r1, value = "No")
radiobutton2.pack()
Question2_r2=StringVar(value="0")
question2 = Label(root, text="Do you have swelling in the feet/ ankles/ legs (shoes feel tighter) or abdomen?")
question2.pack()
radiobutton1 = Radiobutton(root, text="Yes", variable = Question2_r2, value = "Yes")
radiobutton1.pack()
radiobutton2 = Radiobutton(root, text="No", variable = Question2_r2, value = "No")
radiobutton2.pack()
Question3_r3=StringVar(value="0")
question3 = Label(root, text="Do you feel any of these symptoms - confusion, disorientation, or loss of memory?")
question3.pack()
radiobutton1 = Radiobutton(root, text="Yes", variable = Question3_r3, value = "Yes")
radiobutton1.pack()
radiobutton2 = Radiobutton(root, text="No", variable = Question3_r3, value = "No")
radiobutton2.pack()
Question4_r4=StringVar(value="0")
question4 = Label(root, text="Do you experience shortness of breath while at rest / lying down?")
question4.pack()
radiobutton1 = Radiobutton(root, text="Yes", variable = Question4_r4, value = "Yes")
radiobutton1.pack()
radiobutton2 = Radiobutton(root, text="No", variable = Question4_r4, value = "No")
radiobutton2.pack()
Question5_r5=StringVar(value="0")
question5 = Label(root, text="Do you experience persistent coughing / wheezing that produces white or pink blood tinged mucus?")
question5.pack()
radiobutton1 = Radiobutton(root, text="Yes", variable = Question5_r5, value = "Yes")
radiobutton1.pack()
radiobutton2 = Radiobutton(root, text="No", variable = Question5_r5, value = "No")
radiobutton2.pack()

def report():
    score=0
    if question1.get()=="yes":
        score= score+10
        print(score)
    if question2.get()=="yes":
        score = score+10
        print(score)
    if question3.get()=="yes":
        score=score+10
        print(score)
    if question4.get()=="yes":
            score = score+10
            print(score)
    if question5.get()=="yes":
                score = score+10
                print(score)
                
    
         
    if score <= 10:
        messagebox.showinfo("Report", "You do not need to go to the Doctor")
    elif score > 10 and score <= 30: 
        messagebox.showinfo("Report", "You May Need To Go To The Doctor")
    else:
        messagebox.showinfo("Report", "You NEED To Go To The Doctor!")
        
        
        
btn = Button(root, text="Click Me", command=report,padx = 10, pady = 1, bg="skyblue", fg="white")
btn.pack()
root.mainloop()