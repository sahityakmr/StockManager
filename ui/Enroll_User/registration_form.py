import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
from ui.Enroll_User import Registration_form_support as registration_form_support
#autosave.tcl##_support

def vp_start_gui_registration():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    #autosave.tcl##_support.set_Tk_var()
    top = Toplevel1 (root)
    #autosave.tcl##_support.init(root, user_enroll)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    #autosave.tcl##_support.set_Tk_var()
    top = Toplevel1 (w)
    #autosave.tcl##_support.init(w, user_enroll, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, user_enroll=None):
        '''This class configures and populates the toplevel window.
           user_enroll is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        user_enroll.geometry("600x450+340+116")
        user_enroll.minsize(120, 1)
        user_enroll.maxsize(1284, 781)
        user_enroll.resizable(1, 1)
        user_enroll.title("New Toplevel")
        user_enroll.configure(background="#d9d9d9")

        self.Label1 = tk.Label(user_enroll)
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=142)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(relief="groove")
        self.Label1.configure(text='''Registration Form''')

        self.Labelframe1 = tk.LabelFrame(user_enroll)
        self.Labelframe1.place(relx=0.033, rely=0.111, relheight=0.878
                , relwidth=0.933)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(font="-family {Times New Roman} -size 12 -weight bold")
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''ENROLL USER''')
        self.Labelframe1.configure(background="#d9d9d9")

        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(relx=0.054, rely=0.051, height=30, width=134
                , bordermode='ignore')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''First Name''')

        self.Label3 = tk.Label(self.Labelframe1)
        self.Label3.place(relx=0.054, rely=0.203, height=15, width=134
                , bordermode='ignore')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Last Name''')

        self.Label4 = tk.Label(self.Labelframe1)
        self.Label4.place(relx=0.107, rely=0.405, height=30, width=74
                , bordermode='ignore')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''User Name''')

        self.Label5 = tk.Label(self.Labelframe1)
        self.Label5.place(relx=0.125, rely=0.582, height=21, width=56
                , bordermode='ignore')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Password''')

        self.Entry1 = tk.Entry(self.Labelframe1)
        self.Entry1.place(relx=0.321, rely=0.051, height=30, relwidth=0.346
                , bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(self.Labelframe1)
        self.Entry2.place(relx=0.321, rely=0.177, height=30, relwidth=0.346
                , bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        genderVar=tk.StringVar(user_enroll)
        self.Radiobutton1 = tk.Radiobutton(self.Labelframe1)
        self.Radiobutton1.place(relx=0.375, rely=0.304, relheight=0.063
                , relwidth=0.139, bordermode='ignore')
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''Male''')
        self.Radiobutton1.configure(variable=genderVar)#autosave.tcl##_support.selectedButton)
        self.Radiobutton1.configure(value="male")
        self.Radiobutton1.configure(command=lambda: registration_form_support.radio_gender(genderVar.get()))

        self.Radiobutton2 = tk.Radiobutton(self.Labelframe1)
        self.Radiobutton2.place(relx=0.536, rely=0.304, relheight=0.063
                , relwidth=0.121, bordermode='ignore')
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''Female''')
        self.Radiobutton2.configure(variable=genderVar)#autosave.tcl##_support.selectedButton)
        self.Radiobutton2.configure(value="female")
        self.Radiobutton2.configure(command=lambda: registration_form_support.radio_gender(genderVar.get()))
        self.Entry3 = tk.Entry(self.Labelframe1)
        self.Entry3.place(relx=0.321, rely=0.405, height=30, relwidth=0.346
                , bordermode='ignore')
        self.Entry3.configure(background="white")
        self.Entry3.configure(cursor="fleur")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Entry4 = tk.Entry(self.Labelframe1)
        self.Entry4.place(relx=0.321, rely=0.557, height=30, relwidth=0.346
                , bordermode='ignore')
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Label6 = tk.Label(self.Labelframe1)
        self.Label6.place(relx=0.107, rely=0.684, height=51, width=54
                , bordermode='ignore')
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''OTP''')

        self.Entry5 = tk.Entry(self.Labelframe1)
        self.Entry5.place(relx=0.321, rely=0.709, height=30, relwidth=0.346
                , bordermode='ignore')
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")

        self.Button1 = tk.Button(self.Labelframe1)
        self.Button1.place(relx=0.571, rely=0.785, height=20, width=47
                , bordermode='ignore')
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="groove")
        self.Button1.configure(text='''get OTP''')
        self.Button1.configure(command=registration_form_support.otp)
        self.Button2 = tk.Button(self.Labelframe1)
        self.Button2.place(relx=0.143, rely=0.886, height=34, width=77
                , bordermode='ignore')
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Register''')
        self.Button2.configure(command=registration_form_support.register)

        self.Button3 = tk.Button(self.Labelframe1)
        self.Button3.place(relx=0.843, rely=0.486, height=34, width=77
                           , bordermode='ignore')
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Upload''')
        self.Button3.configure(command=registration_form_support.upload)

        self.Canvas1 = tk.Canvas(self.Labelframe1)
        self.Canvas1.place(relx=0.714, rely=0.101, relheight=0.337
                , relwidth=0.238, bordermode='ignore')
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="groove")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        self.Message1 = tk.Message(self.Labelframe1)
        self.Message1.place(relx=0.607, rely=0.911, relheight=0.058
                , relwidth=0.446, bordermode='ignore')
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Please Fill All the Details Carefully!!''')
        self.Message1.configure(width=250)

if __name__ == '__main__':
    vp_start_gui_registration()





