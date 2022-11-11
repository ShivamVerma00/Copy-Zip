from tkinter import *
from tkinter.filedialog import askopenfilename,askdirectory
from tkinter import messagebox
from zipfile import *


ms=Tk()
ms.title("File Transfer")
ms.geometry("640x500")
ms.resizable(width=False,height=False)
ms['bg']='black'




#--------------------------------Functions-------------------------
#------------------DOC FILe----------
def doc():
    """ Document Transfering.."""
    #Frame.....
    f=Frame(ms,bg='black')
    f.place(x=0,y=0,width=640,height=500)

    #Label.....
    l=Label(f,text="Select the File to be copied:",bg='black',fg='white',
            font='bold')
    l.place(x=10,y=50)

    l1=Label(f,text="Choose the location where you want to copy the file:",
             bg='black',fg='white',font='bold')
    l1.place(x=10,y=180)

    l2=Label(f,text="Enter Name of the File:",bg='black',fg='white',font='bold')
    l2.place(x=10,y=270)

    l3=Label(f,text="Enter Type of the File:",bg='black',fg='white',font='bold')
    l3.place(x=10,y=320)


    #EntryBox...........
    evar=StringVar()#Stores the data in entry box..
    e=Entry(f,textvariable=evar,bd=2)
    e.place(x=260,y=272,width=220)

    e1var=StringVar()#Stores the data in entry box..
    e1=Entry(f,textvariable=e1var,bd=2)
    e1.place(x=260,y=322,width=220)


    #Functions...
    def askl1():
        """ Select Directory of File to be copied..."""
        global docof
        docof=askopenfilename()

        l=Label(f,text=docof,fg='red')
        l.place(x=240,y=110)

    def askl2():
        """ Select Directory of the File..."""
        global docd
        docd=askdirectory()

        l=Label(f,text=docd,fg='red')
        l.place(x=240,y=220)

    def start():
        """ Start Copying the File.."""
        f=open(docof,'r')
        
        name=str(evar)
        typ=str(e1var)

        f1=open(docd+"\\"+name+"."+typ,"w")
        f1.write(f.read())
        messagebox.showwarning('Message',"File Copied Successfully....")
        f1.close()
        f.close()
        



    #Buttons.....
    btn_l1=Button(f,text="Select File",bg='grey',width=15,bd=2,
                  font='Arial 12 bold',command=askl1)
    btn_l1.place(x=320,y=48)

    btn_l2=Button(f,text="Select Directory",bg='grey',bd=2,
                  font='Arial 12 bold',command=askl2)
    btn_l2.place(x=490,y=178)

    btn_start=Button(f,text="START",bg='grey',bd=2,width=20,
                  font='Arial 12 bold',command=start)
    btn_start.place(x=250,y=400)



    

#--------------------IMAGE FILE------------
def img():
    """ Image Transfering...."""
    #Frame.....
    f=Frame(ms,bg='black')
    f.place(x=0,y=0,width=640,height=500)

    #Label.....
    l=Label(f,text="Select the File to be copied:",bg='black',fg='white',
            font='bold')
    l.place(x=10,y=50)

    l1=Label(f,text="Choose the location where you want to copy the file:",
             bg='black',fg='white',font='bold')
    l1.place(x=10,y=180)

    l2=Label(f,text="Enter Name of the File:",bg='black',fg='white',font='bold')
    l2.place(x=10,y=270)

    l3=Label(f,text="Enter Type of the File:",bg='black',fg='white',font='bold')
    l3.place(x=10,y=320)


    #EntryBox...........
    evar=StringVar()#Stores the data in entry box..
    e=Entry(f,textvariable=evar,bd=2)
    e.place(x=260,y=272,width=220)

    e1var=StringVar()#Stores the data in entry box..
    e1=Entry(f,textvariable=e1var,bd=2)
    e1.place(x=260,y=322,width=220)


    #Functions...
    def askl1():
        """ Select Directory of File to be copied..."""
        global imgof
        imgof=askopenfilename()

        l=Label(f,text=imgof,fg='red')
        l.place(x=240,y=110)

    def askl2():
        """ Select Directory of the File..."""
        global imgd
        imgd=askdirectory()

        l=Label(f,text=imgd,fg='red')
        l.place(x=240,y=220)

    def start():
        """ Start Copying the File.."""
        f=open(imgof,'rb')
        
        name=str(evar)
        typ=str(e1var)

        f1=open(imgd+"\\"+name+"."+typ,"wb")
        f1.write(f.read())
        messagebox.showwarning('Message',"File Copied Successfully....")
        f1.close()
        f.close()

    #Buttons.....
    btn_l1=Button(f,text="Select File",bg='grey',width=15,bd=2,
                  font='Arial 12 bold',command=askl1)
    btn_l1.place(x=320,y=48)

    btn_l2=Button(f,text="Select Directory",bg='grey',bd=2,
                  font='Arial 12 bold',command=askl2)
    btn_l2.place(x=490,y=178)

    btn_start=Button(f,text="START",bg='grey',bd=2,width=20,
                  font='Arial 12 bold',command=start)
    btn_start.place(x=250,y=400)
    


#-----------------AUDIO FILE------------------
def aud():
    """ Audio File  Transfering...."""
    #Frame.....
    f=Frame(ms,bg='black')
    f.place(x=0,y=0,width=640,height=500)

    #Label.....
    l=Label(f,text="Select the File to be copied:",bg='black',fg='white',
            font='bold')
    l.place(x=10,y=50)

    l1=Label(f,text="Choose the location where you want to copy the file:",
             bg='black',fg='white',font='bold')
    l1.place(x=10,y=180)

    l2=Label(f,text="Enter Name of the File:",bg='black',fg='white',font='bold')
    l2.place(x=10,y=270)

    l3=Label(f,text="Enter Type of the File:",bg='black',fg='white',font='bold')
    l3.place(x=10,y=320)


    #EntryBox...........
    evar=StringVar()#Stores the data in entry box..
    e=Entry(f,textvariable=evar,bd=2)
    e.place(x=260,y=272,width=220)

    e1var=StringVar()#Stores the data in entry box..
    e1=Entry(f,textvariable=e1var,bd=2)
    e1.place(x=260,y=322,width=220)


    #Functions...
    def askl1():
        """ Select Directory of File to be copied..."""
        global audof
        audof=askopenfilename()

        l=Label(f,text=audof,fg='red')
        l.place(x=240,y=110)

    def askl2():
        """ Select Directory of the File..."""
        global audd
        audd=askdirectory()

        l=Label(f,text=audd,fg='red')
        l.place(x=240,y=220)

    def start():
        """ Start Copying the File.."""
        f=open(audof,'rb')
        
        name=str(evar)
        typ=str(e1var)

        f1=open(audd+"\\"+name+"."+typ,"wb")
        f1.write(f.read())
        messagebox.showwarning('Message',"File Copied Successfully....")
        f1.close()
        f.close()

    #Buttons.....
    btn_l1=Button(f,text="Select File",bg='grey',width=15,bd=2,
                  font='Arial 12 bold',command=askl1)
    btn_l1.place(x=320,y=48)

    btn_l2=Button(f,text="Select Directory",bg='grey',bd=2,
                  font='Arial 12 bold',command=askl2)
    btn_l2.place(x=490,y=178)

    btn_start=Button(f,text="START",bg='grey',bd=2,width=20,
                  font='Arial 12 bold',command=start)
    btn_start.place(x=250,y=400)


#------------------VIDEO FILE-------------
def vid():
    """ Video Transfering...."""
    #Frame.....
    f=Frame(ms,bg='black')
    f.place(x=0,y=0,width=640,height=500)

    #Label.....
    l=Label(f,text="Select the File to be copied:",bg='black',fg='white',
            font='bold')
    l.place(x=10,y=50)

    l1=Label(f,text="Choose the location where you want to copy the file:",
             bg='black',fg='white',font='bold')
    l1.place(x=10,y=180)

    l2=Label(f,text="Enter Name of the File:",bg='black',fg='white',font='bold')
    l2.place(x=10,y=270)

    l3=Label(f,text="Enter Type of the File:",bg='black',fg='white',font='bold')
    l3.place(x=10,y=320)


    #EntryBox...........
    evar=StringVar()#Stores the data in entry box..
    e=Entry(f,textvariable=evar,bd=2)
    e.place(x=260,y=272,width=220)

    e1var=StringVar()#Stores the data in entry box..
    e1=Entry(f,textvariable=e1var,bd=2)
    e1.place(x=260,y=322,width=220)


    #Functions...
    def askl1():
        """ Select Directory of File to be copied..."""
        global vidof
        vidof=askopenfilename()

        l=Label(f,text=vidof,fg='red')
        l.place(x=240,y=110)

    def askl2():
        """ Select Directory of the File..."""
        global vidd
        vidd=askdirectory()

        l=Label(f,text=vidd,fg='red')
        l.place(x=240,y=220)

    def start():
        """ Start Copying the File.."""
        f=open(vidof,'rb')
        
        name=str(evar)
        typ=str(e1var)

        f1=open(vidd+"\\"+name+"."+typ,"wb")
        f1.write(f.read())
        messagebox.showwarning('Message',"File Copied Successfully....")
        f1.close()
        f.close()

    #Buttons.....
    btn_l1=Button(f,text="Select File",bg='grey',width=15,bd=2,
                  font='Arial 12 bold',command=askl1)
    btn_l1.place(x=320,y=48)

    btn_l2=Button(f,text="Select Directory",bg='grey',bd=2,
                  font='Arial 12 bold',command=askl2)
    btn_l2.place(x=490,y=178)

    btn_start=Button(f,text="START",bg='grey',bd=2,width=20,
                  font='Arial 12 bold',command=start)
    btn_start.place(x=250,y=400)
    


#--------------------ZIPFILE----------
def zipfile():
    """ For Making Zip File ..........."""
    #Frame.....
    f=Frame(ms,bg='black')
    f.place(x=0,y=0,width=640,height=500)

    #Label.....
    l1=Label(f,text="Select the File to be Zipped:",bg='black',fg='white',
            font='bold')
    l1.place(x=10,y=50)

    l2=Label(f,text="Select the File to be Zipped:",bg='black',fg='white',
            font='bold')
    l2.place(x=10,y=120)

    l3=Label(f,text="Select the File to be Zipped:",bg='black',fg='white',
            font='bold')
    l3.place(x=10,y=190)

    l4=Label(f,text="Select the File to be Zipped:",bg='black',fg='white',
            font='bold')
    l4.place(x=10,y=260)

    lop=Label(f,text="Choose the location where you want to Zip the file:",
             bg='black',fg='white',font='bold')
    lop.place(x=10,y=330)

    lfn=Label(f,text="Enter Name of the File:",bg='black',fg='white',font='bold')
    lfn.place(x=10,y=400)


    #EntryBox...........
    evar=StringVar()#Stores the data in entry box..
    e=Entry(f,textvariable=evar,bd=2)
    e.place(x=260,y=400,width=220)



    #Functions...
    def askl1():
        """ Select Directory of File to be copied..."""
        global of1
        of1=askopenfilename()

        l=Label(f,text=of1,fg='red')
        l.place(x=240,y=90)

    
    def askl2():
        """ Select Directory of File to be copied..."""
        global of2
        of2=askopenfilename()

        l=Label(f,text=of2,fg='red')
        l.place(x=240,y=150)

     
    def askl3():
        """ Select Directory of File to be copied..."""
        global of3
        of3=askopenfilename()

        l=Label(f,text=of3,fg='red')
        l.place(x=240,y=210)

    
    def askl4():
        """ Select Directory of File to be copied..."""
        global of4
        of4=askopenfilename()

        l=Label(f,text=of4,fg='red')
        l.place(x=240,y=290)

    def op():
        """ Selecting Directory For Zip File..."""
        global d
        d=askdirectory()
        
        l=Label(f,text=d,fg='red')
        l.place(x=240,y=360)





    def start():
        """ Start Zipping the File.."""
        name=d+"\\"+str(evar)
        
        f=ZipFile(name+".zip","w",ZIP_DEFLATED)
        f.write(of1)
        f.write(of2)
        f.write(of3)
        f.write(of4)

        f.close()

        messagebox.showwarning('Message',"File Zipped Successfully....")

    #Buttons.....
    
    btn_l1=Button(f,text="Select File",bg='grey',width=15,bd=2,
                  font='Arial 12 bold',command=askl1)
    btn_l1.place(x=320,y=48)  

    btn_l2=Button(f,text="Select File",bg='grey',width=15,bd=2,
                  font='Arial 12 bold',command=askl2)
    btn_l2.place(x=320,y=118)

    
    btn_l3=Button(f,text="Select File",bg='grey',width=15,bd=2,
                  font='Arial 12 bold',command=askl3)
    btn_l3.place(x=320,y=188)
    
    btn_l4=Button(f,text="Select File",bg='grey',width=15,bd=2,
                  font='Arial 12 bold',command=askl4)
    btn_l4.place(x=320,y=258)

    btn_open=Button(f,text="Select Directory",bg='grey',bd=2,
                  font='Arial 12 bold',command=op)
    btn_open.place(x=490,y=328)

    btn_start=Button(f,text="START",bg='grey',bd=2,width=20,
                  font='Arial 12 bold',command=start)
    btn_start.place(x=220,y=460)
    





#----------Label & Buttons on MS........
l=Label(ms,text="Choose the type of File",fg='red',font=("Arial 25 bold"))
l.place(x=120,y=20)

btn_doc=Button(ms,text="Document",width=15,bd=5,font='bold',command=doc)
btn_doc.place(x=220,y=150)

btn_img=Button(ms,text="Image",width=15,bd=5,font='bold',command=img)
btn_img.place(x=220,y=200)


btn_aud=Button(ms,text="Audio",width=15,bd=5,font='bold',command=aud)
btn_aud.place(x=220,y=250)

btn_vid=Button(ms,text="Video",width=15,bd=5,font='bold',command=vid)
btn_vid.place(x=220,y=300)

btn_zip=Button(ms,text="Zip",width=15,bd=5,font='bold',command=zipfile)
btn_zip.place(x=220,y=350)



ms.mainloop()
