#########################################################
# Tool Name: BMI Calculator                             #
# Author   : Vimalraj Krishnan                          #
# Contact  : vimalraj.ece.kiot15@gmail.com              #
#########################################################

from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np


class simpleform_ap(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.topFrame = Frame(self)
        self.topFrame.pack(padx=5,pady=5)
        self.middleFrame = Frame(self)
        self.middleFrame.pack(padx=5,pady=5)
        self.bottomFrame = Frame(self)
        self.bottomFrame.pack(padx=5,pady=5,fill=X)

        heightList = ["cm","inch"]
        weightList = ["kg","lbs"]

        self.heightVar = StringVar()
        self.weightVar = StringVar()

        self.height = StringVar()
        self.weight = StringVar()

        self.heightVar.set("cm")
        self.weightVar.set("kg")

        self.label1 = Label(self.topFrame,text="Height",width=6)
        self.label1.pack(side="left", padx=2)
        self.label2 = Label(self.middleFrame,text="Weight",width=6)
        self.label2.pack(side="left", padx=2)

        self.heightEntry = Entry(self.topFrame,textvariable = self.height, width=20)
        self.heightEntry.pack(side="left", padx=2)
        self.weightEntry = Entry(self.middleFrame,textvariable = self.weight,width=20)
        self.weightEntry.pack(side="left", padx=2)

        self.heightMenu = OptionMenu(self.topFrame, self.heightVar, *heightList)
        self.heightMenu.pack()
        self.weightMenu = OptionMenu(self.middleFrame, self.weightVar, *weightList)
        self.weightMenu.pack()

        self.button1 = Button(self.bottomFrame,text="Calculate",command=self.calculate)
        self.button1.pack(side=RIGHT)

        self.label3 = Label(self.bottomFrame,text="")
        self.label3.pack(padx=2)

    def calculate(self):
        try:
            height = int(self.height.get())
            weight = int(self.weight.get())
            if self.heightVar.get() == 'inch':
                height = 2.54 * height
            if self.weightVar.get() == 'lbs':
                weight = 0.453592 * weight
            if height<142 or height>213 or weight<37 or weight > 123:
                messagebox.showerror("Input Error", "Kindly input value between the range\nHeight from 142cm to 213cm\nWeight from 37kg to 123kg")
                return
        except ValueError:
            messagebox.showerror("Input Error", "Kindly input value valid value")
            return

        print("height:%s\nweight:%s"%(height,weight))
        self.display(height,weight)
        main(height,weight)

    def display(self,height, weight):
        bmi = weight*10000/(height**2)
        if bmi<18.5:
            self.label3.config(text="Your BMI is %.1f"%(bmi),fg='orange')
            messagebox.showinfo("Result", "You are Lean")
        elif bmi <25:
            self.label3.config(text="Your BMI is %.1f"%(bmi),fg='green')
            messagebox.showinfo("Result", "You are Healthy")

        else:
            self.label3.config(text="Your BMI is %.1f"%(bmi),fg='red')
            messagebox.showinfo("Result", "Consider to reduce your weight")

def main(height,weight):
    x = np.arange(142,213)
    h = 15*x*x/10000
    a = 18.5*x*x/10000
    b = 22*x*x/10000
    c = 25*x*x/10000
    e = [i for i in 30*x*x/10000 if i<123]
    f = [i for i in 35*x*x/10000 if i<123]
    g = [i for i in 40*x*x/10000 if i<123]
    mid = x.size//2

    print(len(h),len(a))
    
    fig,ax=plt.subplots()
    fig.canvas.set_window_title('BMI Graph')
    ax.plot(x,a,x,b,x,c,x[:len(e)],e,x[:len(f)],f,x[:len(g)],g,x[16:],h[16:],linestyle='dotted',color='grey')
    ax.fill_between(x,37,a, facecolor='orange')
    ax.fill_between(x,a,c, facecolor='green')
    ax.fill_between(x,c,123, facecolor='red')

    plt.text(x[a.size//2],a[mid-16],"BMI=15")
    plt.text(x[a.size//2],a[mid],"BMI=18.5")
    plt.text(x[b.size//2-1],b[mid],"BMI=22")
    plt.text(x[c.size//2-3],c[mid],"BMI=25")
    plt.text(x[len(e)//2-2],e[len(e)//2],"BMI=30")
    plt.text(x[len(f)//2-2],f[len(f)//2],"BMI=35")
    plt.text(x[len(g)//2-2],g[len(g)//2],"BMI=40")
    plt.grid()
    plt.title("BMI Calculator")
    plt.xlabel("Height(cm)")
    plt.ylabel("Weight(kg)")
    ax.scatter(height,weight,100)
    plt.show()

def create_form():
    form = simpleform_ap()
    form.title('BMI Calculator')
    form.mainloop()

if __name__ == "__main__":
  create_form()
