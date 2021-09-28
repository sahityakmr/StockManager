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
from ui.enroll_user import registration_form_support as registration_form_support

def vp_start_gui_registration():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel(root)
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

        self.Label_user_enroll = tk.Label(user_enroll)
        self.Label_user_enroll.place(relx=0.367, rely=0.022, height=31, width=142)
        self.Label_user_enroll.configure(background="#d9d9d9")
        self.Label_user_enroll.configure(disabledforeground="#a3a3a3")
        self.Label_user_enroll.configure(foreground="#000000")
        self.Label_user_enroll.configure(relief="groove")
        self.Label_user_enroll.configure(text='''Registration Form''')

        self.Labelframe_user_enroll = tk.LabelFrame(user_enroll)
        self.Labelframe_user_enroll.place(relx=0.033, rely=0.111, relheight=0.878
                , relwidth=0.933)
        self.Labelframe_user_enroll.configure(relief='groove')
        self.Labelframe_user_enroll.configure(font="-family {Times New Roman} -size 12 -weight bold")
        self.Labelframe_user_enroll.configure(foreground="black")
        self.Labelframe_user_enroll.configure(text='''ENROLL USER''')
        self.Labelframe_user_enroll.configure(background="#d9d9d9")

        self.Label_first_name = tk.Label(self.Labelframe_user_enroll)
        self.Label_first_name.place(relx=0.054, rely=0.051, height=30, width=134
                , bordermode='ignore')
        self.Label_first_name.configure(background="#d9d9d9")
        self.Label_first_name.configure(disabledforeground="#a3a3a3")
        self.Label_first_name.configure(foreground="#000000")
        self.Label_first_name.configure(text='''First Name''')

        self.Label_last_name = tk.Label(self.Labelframe_user_enroll)
        self.Label_last_name.place(relx=0.054, rely=0.203, height=15, width=134
                , bordermode='ignore')
        self.Label_last_name.configure(background="#d9d9d9")
        self.Label_last_name.configure(disabledforeground="#a3a3a3")
        self.Label_last_name.configure(foreground="#000000")
        self.Label_last_name.configure(text='''Last Name''')

        self.Label_user_name = tk.Label(self.Labelframe_user_enroll)
        self.Label_user_name.place(relx=0.107, rely=0.405, height=30, width=74
                , bordermode='ignore')
        self.Label_user_name.configure(background="#d9d9d9")
        self.Label_user_name.configure(disabledforeground="#a3a3a3")
        self.Label_user_name.configure(foreground="#000000")
        self.Label_user_name.configure(text='''User Name''')

        self.Label_password = tk.Label(self.Labelframe_user_enroll)
        self.Label_password.place(relx=0.125, rely=0.582, height=21, width=56
                , bordermode='ignore')
        self.Label_password.configure(background="#d9d9d9")
        self.Label_password.configure(disabledforeground="#a3a3a3")
        self.Label_password.configure(foreground="#000000")
        self.Label_password.configure(text='''Passord''')
        self.FNAME= tk.StringVar(self.Labelframe_user_enroll)
        self.Entry_first_name = tk.Entry(self.Labelframe_user_enroll)
        self.Entry_first_name.place(relx=0.321, rely=0.051, height=30, relwidth=0.346
                , bordermode='ignore')
        self.Entry_first_name.configure(background="white")
        self.Entry_first_name.configure(disabledforeground="#a3a3a3")
        self.Entry_first_name.configure(font="TkFixedFont")
        self.Entry_first_name.configure(foreground="#000000")
        self.Entry_first_name.configure(insertbackground="black")
        self.Entry_first_name.configure(textvariable=self.FNAME)

        self.Entry_last_name = tk.Entry(self.Labelframe_user_enroll)
        self.Entry_last_name.place(relx=0.321, rely=0.177, height=30, relwidth=0.346
                , bordermode='ignore')
        self.Entry_last_name.configure(background="white")
        self.Entry_last_name.configure(disabledforeground="#a3a3a3")
        self.Entry_last_name.configure(font="TkFixedFont")
        self.Entry_last_name.configure(foreground="#000000")
        self.Entry_last_name.configure(insertbackground="black")
        genderVar=tk.StringVar(user_enroll)
        self.Radiobutton_male = tk.Radiobutton(self.Labelframe_user_enroll)
        self.Radiobutton_male.place(relx=0.375, rely=0.304, relheight=0.063
                , relwidth=0.139, bordermode='ignore')
        self.Radiobutton_male.configure(activebackground="#ececec")
        self.Radiobutton_male.configure(activeforeground="#000000")
        self.Radiobutton_male.configure(background="#d9d9d9")
        self.Radiobutton_male.configure(disabledforeground="#a3a3a3")
        self.Radiobutton_male.configure(foreground="#000000")
        self.Radiobutton_male.configure(highlightbackground="#d9d9d9")
        self.Radiobutton_male.configure(highlightcolor="black")
        self.Radiobutton_male.configure(justify='left')
        self.Radiobutton_male.configure(text='''Male''')
        self.Radiobutton_male.configure(variable=genderVar)#autosave.tcl##_support.selectedButton)
        self.Radiobutton_male.configure(value="male")
        self.Radiobutton_male.configure(command=lambda: registration_form_support.radio_gender(genderVar.get()))

        self.Radiobutton_female = tk.Radiobutton(self.Labelframe_user_enroll)
        self.Radiobutton_female.place(relx=0.536, rely=0.304, relheight=0.063
                , relwidth=0.121, bordermode='ignore')
        self.Radiobutton_female.configure(activebackground="#ececec")
        self.Radiobutton_female.configure(activeforeground="#000000")
        self.Radiobutton_female.configure(background="#d9d9d9")
        self.Radiobutton_female.configure(disabledforeground="#a3a3a3")
        self.Radiobutton_female.configure(foreground="#000000")
        self.Radiobutton_female.configure(highlightbackground="#d9d9d9")
        self.Radiobutton_female.configure(highlightcolor="black")
        self.Radiobutton_female.configure(justify='left')
        self.Radiobutton_female.configure(text='''Female''')
        self.Radiobutton_female.configure(variable=genderVar)#autosave.tcl##_support.selectedButton)
        self.Radiobutton_female.configure(value="female")
        self.Radiobutton_female.configure(command=lambda: registration_form_support.radio_gender(genderVar.get()))
        self.Entry_username = tk.Entry(self.Labelframe_user_enroll)
        self.Entry_username.place(relx=0.321, rely=0.405, height=30, relwidth=0.346
                , bordermode='ignore')
        self.Entry_username.configure(background="white")
        self.Entry_username.configure(cursor="fleur")
        self.Entry_username.configure(disabledforeground="#a3a3a3")
        self.Entry_username.configure(font="TkFixedFont")
        self.Entry_username.configure(foreground="#000000")
        self.Entry_username.configure(insertbackground="black")

        self.Entry_password = tk.Entry(self.Labelframe_user_enroll)
        self.Entry_password.place(relx=0.321, rely=0.557, height=30, relwidth=0.346
                , bordermode='ignore')
        self.Entry_password.configure(background="white")
        self.Entry_password.configure(disabledforeground="#a3a3a3")
        self.Entry_password.configure(font="TkFixedFont")
        self.Entry_password.configure(foreground="#000000")
        self.Entry_password.configure(insertbackground="black")

        self.Label_otp = tk.Label(self.Labelframe_user_enroll)
        self.Label_otp.place(relx=0.107, rely=0.684, height=51, width=54
                , bordermode='ignore')
        self.Label_otp.configure(background="#d9d9d9")
        self.Label_otp.configure(disabledforeground="#a3a3a3")
        self.Label_otp.configure(foreground="#000000")
        self.Label_otp.configure(text='''OTP''')

        self.Entry_otp = tk.Entry(self.Labelframe_user_enroll)
        self.Entry_otp.place(relx=0.321, rely=0.709, height=30, relwidth=0.346
                , bordermode='ignore')
        self.Entry_otp.configure(background="white")
        self.Entry_otp.configure(disabledforeground="#a3a3a3")
        self.Entry_otp.configure(font="TkFixedFont")
        self.Entry_otp.configure(foreground="#000000")
        self.Entry_otp.configure(insertbackground="black")

        self.Button_otp = tk.Button(self.Labelframe_user_enroll)
        self.Button_otp.place(relx=0.571, rely=0.785, height=20, width=47
                , bordermode='ignore')
        self.Button_otp.configure(activebackground="#ececec")
        self.Button_otp.configure(activeforeground="#000000")
        self.Button_otp.configure(background="#d9d9d9")
        self.Button_otp.configure(disabledforeground="#a3a3a3")
        self.Button_otp.configure(foreground="#000000")
        self.Button_otp.configure(highlightbackground="#d9d9d9")
        self.Button_otp.configure(highlightcolor="black")
        self.Button_otp.configure(pady="0")
        self.Button_otp.configure(relief="groove")
        self.Button_otp.configure(text='''get OTP''')
        self.Button_otp.configure(command=registration_form_support.otp)
        self.Button_register = tk.Button(self.Labelframe_user_enroll)
        self.Button_register.place(relx=0.143, rely=0.886, height=34, width=77
                , bordermode='ignore')
        self.Button_register.configure(activebackground="#ececec")
        self.Button_register.configure(activeforeground="#000000")
        self.Button_register.configure(background="#d9d9d9")
        self.Button_register.configure(disabledforeground="#a3a3a3")
        self.Button_register.configure(foreground="#000000")
        self.Button_register.configure(highlightbackground="#d9d9d9")
        self.Button_register.configure(highlightcolor="black")
        self.Button_register.configure(pady="0")
        self.Button_register.configure(text='''Register''')
        self.Button_register.configure(command=lambda:registration_form_support.register(self.FNAME.get()))

        self.Button_upload_image = tk.Button(self.Labelframe_user_enroll)
        self.Button_upload_image.place(relx=0.843, rely=0.486, height=34, width=77
                           , bordermode='ignore')
        self.Button_upload_image.configure(activebackground="#ececec")
        self.Button_upload_image.configure(activeforeground="#000000")
        self.Button_upload_image.configure(background="#d9d9d9")
        self.Button_upload_image.configure(disabledforeground="#a3a3a3")
        self.Button_upload_image.configure(foreground="#000000")
        self.Button_upload_image.configure(highlightbackground="#d9d9d9")
        self.Button_upload_image.configure(highlightcolor="black")
        self.Button_upload_image.configure(pady="0")
        self.Button_upload_image.configure(text='''Upload''')
        self.Button_upload_image.configure(command=registration_form_support.upload)

        self.Canvas_image = tk.Canvas(self.Labelframe_user_enroll)
        self.Canvas_image.place(relx=0.714, rely=0.101, relheight=0.337
                , relwidth=0.238, bordermode='ignore')
        self.Canvas_image.configure(background="#d9d9d9")
        self.Canvas_image.configure(borderwidth="2")
        self.Canvas_image.configure(insertbackground="black")
        self.Canvas_image.configure(relief="groove")
        self.Canvas_image.configure(selectbackground="blue")
        self.Canvas_image.configure(selectforeground="white")

        self.Message = tk.Message(self.Labelframe_user_enroll)
        self.Message.place(relx=0.607, rely=0.911, relheight=0.058
                , relwidth=0.446, bordermode='ignore')
        self.Message.configure(background="#d9d9d9")
        self.Message.configure(foreground="#000000")
        self.Message.configure(highlightbackground="#d9d9d9")
        self.Message.configure(highlightcolor="black")
        self.Message.configure(text='''Please Fill All the Details Carefully!!''')
        self.Message.configure(width=250)

if __name__ == '__main__':
    vp_start_gui_registration()





