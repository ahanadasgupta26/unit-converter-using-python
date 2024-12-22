from tkinter import *
from tkinter import ttk
from unitconvert import digitalunits,lengthunits,timeunits,volumeunits,massunits,temperatureunits

root=Tk()
root.geometry("650x350")
root.title("Unit Converter")
root.resizable(False,False)
root.configure(bg='lightblue')

userin=IntVar()
resin=IntVar()
u1=StringVar()
u2=StringVar()

def convert():
    try:
        a=digitalunits.DigitalUnit(userin.get(),f'{u1.get()}',f'{u2.get()}').doconvert()
        resin.set(a)
    except:
        try:
            b=lengthunits.LengthUnit(userin.get(),f'{u1.get()}',f'{u2.get()}').doconvert()
            resin.set(b)
        except:
            try:
                c=timeunits.TimeUnit(userin.get(),f'{u1.get()}',f'{u2.get()}').doconvert()
                resin.set(c)
            except:
                try:
                    d=volumeunits.VolumeUnit(userin.get(),f'{u1.get()}',f'{u2.get()}').doconvert()
                    resin.set(d)
                except:
                    try:
                        e=massunits.MassUnit(userin.get(),f'{u1.get()}',f'{u2.get()}').doconvert()
                        resin.set(e)
                    except:
                        try:
                            f=temperatureunits.TemperatureUnit(userin.get(),f'{u1.get()}',f'{u2.get()}').doconvert()
                            resin.set(f)
                        except:
                            resin.set("Invalid unit or value")

head=Label(root,text="Unit Converter",font=("Arial",25),bg='pink')
head.grid(row=0,column=0,columnspan=2,padx=210,pady=20)

userinp=Entry(root,textvariable=userin,font="Arial",width=10)
userinp.grid(row=1,column=0,pady=10,padx=5)

unit1=ttk.Combobox(root,textvariable=u1,font=("Arial",20),width=5)
unit1.grid(row=1,column=1,pady=10,padx=10,columnspan=1)
unit1['value']=('B','kB','MB','GB','TB','PB','EB','ZB','YB','KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB','mm','cm','in','ft','yd','m','km','mi','ms','sec','min','hr','day','wk','mo','yr','ml','l','tsp','tbsp','floz','cup','pt','qt','gal','lcup','in3','ft3','mg','g','oz','lb','kg','F','C','K')

unit2=ttk.Combobox(root,textvariable=u2,font=("Arial",20),width=5)
unit2.grid(row=2,column=1,padx=10,pady=10,columnspan=1)
unit2['value']=('B','kB','MB','GB','TB','PB','EB','ZB','YB','KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB','mm','cm','in','ft','yd','m','km','mi','ms','sec','min','hr','day','wk','mo','yr','ml','l','tsp','tbsp','floz','cup','pt','qt','gal','lcup','in3','ft3','mg','g','oz','lb','kg','F','C','K')

res=Label(root,textvariable=resin,font=("Arial",20),width=20)
res.grid(row=2,column=0,padx=10,pady=10,columnspan=1)

submit=Button(root,text="SUBMIT",font=("Arial",15),command=convert,bg='gray')
submit.grid(row=3,columnspan=1,padx=10,pady=30,column=0)

reset=Button(root,text="RESET",font=("Arial",15),command=lambda:[userin.set(0),resin.set(""),u1.set(""),u2.set("")],bg='gray')
reset.grid(row=3,columnspan=2,padx=10,pady=30,column=1)

root.mainloop()