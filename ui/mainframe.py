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

import ui.mainframe_support as mainframe_support
from tkcalendar import DateEntry
from ui.custom import custom_elements as ctk

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, window, root
    root = tk.Tk()
    mainframe_support.set_Tk_var()
    top = mainframe(root)
    mainframe_support.init(root, top)
    root.mainloop()


window = None


def create_mainframe(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_mainframe(root, *args, **kwargs)' .'''
    global window, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    mainframe_support.set_Tk_var()
    top = mainframe(w)
    mainframe_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_mainframe():
    global window
    w.destroy()
    w = None


class mainframe:
    def __init__(self, mainUI=None):
        '''This class configures and populates the toplevel window.
           user_enroll is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        mainUI.geometry("800x400+567+214")
        mainUI.minsize(148, 1)
        mainUI.maxsize(5764, 2335)
        mainUI.resizable(1, 1)
        mainUI.title("Mainframe")
        mainUI.configure(relief="ridge")
        mainUI.configure(background="#d9d9d9")

        self.menubar = tk.Menu(mainUI, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        mainUI.configure(menu=self.menubar)

        self.verticalSeparator = ttk.Separator(mainUI)
        self.verticalSeparator.place(relx=0.5, rely=0.375, relheight=0.5)
        self.verticalSeparator.configure(orient="vertical")

        self.logoCanvas = tk.Canvas(mainUI)
        self.logoCanvas.place(relx=0.15, rely=0.025, relheight=0.25
                              , relwidth=0.125)
        self.logoCanvas.configure(background="#d9d9d9")
        self.logoCanvas.configure(borderwidth="2")
        self.logoCanvas.configure(insertbackground="black")
        self.logoCanvas.configure(relief="ridge")
        self.logoCanvas.configure(selectbackground="blue")
        self.logoCanvas.configure(selectforeground="white")

        self.orgTitleLabel = tk.Label(mainUI)
        self.orgTitleLabel.place(relx=0.313, rely=0.05, height=80, width=400)
        self.orgTitleLabel.configure(background="#d9d9d9")
        self.orgTitleLabel.configure(disabledforeground="#a3a3a3")
        self.orgTitleLabel.configure(font="-family {Dubai} -size 24 -weight bold")
        self.orgTitleLabel.configure(foreground="#000000")
        self.orgTitleLabel.configure(text='''Company Name''')

        self.enrollAdminBtn = tk.Button(mainUI)
        self.enrollAdminBtn.place(relx=0.15, rely=0.4, height=33, width=200)
        self.enrollAdminBtn.configure(activebackground="#ececec")
        self.enrollAdminBtn.configure(activeforeground="#000000")
        self.enrollAdminBtn.configure(background="#d9d9d9")
        self.enrollAdminBtn.configure(command=mainframe_support.enrollAdmin)
        self.enrollAdminBtn.configure(disabledforeground="#a3a3a3")
        self.enrollAdminBtn.configure(foreground="#000000")
        self.enrollAdminBtn.configure(highlightbackground="#d9d9d9")
        self.enrollAdminBtn.configure(highlightcolor="black")
        self.enrollAdminBtn.configure(pady="0")
        self.enrollAdminBtn.configure(text='''Enroll Admin''')

        self.enrollUserBtn = tk.Button(mainUI)
        self.enrollUserBtn.place(relx=0.15, rely=0.525, height=33, width=200)
        self.enrollUserBtn.configure(activebackground="#ececec")
        self.enrollUserBtn.configure(activeforeground="#000000")
        self.enrollUserBtn.configure(background="#d9d9d9")
        self.enrollUserBtn.configure(command=mainframe_support.enrollUser)
        self.enrollUserBtn.configure(disabledforeground="#a3a3a3")
        self.enrollUserBtn.configure(foreground="#000000")
        self.enrollUserBtn.configure(highlightbackground="#d9d9d9")
        self.enrollUserBtn.configure(highlightcolor="black")
        self.enrollUserBtn.configure(pady="0")
        self.enrollUserBtn.configure(text='''Enroll User''')

        self.deleteUserBtn = tk.Button(mainUI)
        self.deleteUserBtn.place(relx=0.15, rely=0.65, height=33, width=200)
        self.deleteUserBtn.configure(activebackground="#ececec")
        self.deleteUserBtn.configure(activeforeground="#000000")
        self.deleteUserBtn.configure(background="#d9d9d9")
        self.deleteUserBtn.configure(command=mainframe_support.modify_user)
        self.deleteUserBtn.configure(cursor="fleur")
        self.deleteUserBtn.configure(disabledforeground="#a3a3a3")
        self.deleteUserBtn.configure(foreground="#000000")
        self.deleteUserBtn.configure(highlightbackground="#d9d9d9")
        self.deleteUserBtn.configure(highlightcolor="black")
        self.deleteUserBtn.configure(pady="0")
        self.deleteUserBtn.configure(text='''Modify User''')
        self.takeBackupBtn = tk.Button(mainUI)
        self.takeBackupBtn.place(relx=0.15, rely=0.775, height=33, width=200)
        self.takeBackupBtn.configure(activebackground="#ececec")
        self.takeBackupBtn.configure(activeforeground="#000000")
        self.takeBackupBtn.configure(background="#d9d9d9")
        self.takeBackupBtn.configure(command=mainframe_support.takeBackup)
        self.takeBackupBtn.configure(cursor="fleur")
        self.takeBackupBtn.configure(disabledforeground="#a3a3a3")
        self.takeBackupBtn.configure(foreground="#000000")
        self.takeBackupBtn.configure(highlightbackground="#d9d9d9")
        self.takeBackupBtn.configure(highlightcolor="black")
        self.takeBackupBtn.configure(pady="0")
        self.takeBackupBtn.configure(text='''Take Backup''')

        userVar = tk.StringVar(mainUI, "User")
        adminVar = tk.StringVar(mainUI, "Admin")
        self.style.map('TRadiobutton', background=[('selected', _bgcolor), ('active', _ana2color)])
        self.radioAdmin = ttk.Radiobutton(mainUI)
        self.radioAdmin.place(relx=0.65, rely=0.375, relwidth=0.091
                              , relheight=0.0, height=26)
        self.radioAdmin.configure(text='''Admin''')
        self.radioAdmin.configure(value=1)
        self.radioAdmin.configure(variable=adminVar)

        self.radioUser = ttk.Radiobutton(mainUI)
        self.radioUser.place(relx=0.775, rely=0.375, relwidth=0.091
                             , relheight=0.0, height=26)
        self.radioUser.configure(text='''User''')
        self.radioUser.configure(variable=userVar)
        self.radioUser.configure(value=2)

        self.userEntry = ctk.EntryCustom(mainUI, "UserName")
        self.userEntry.place(relx=0.65, rely=0.45, relheight=0.065
                             , relwidth=0.221)
        self.userEntry.configure(takefocus="")
        self.userEntry.configure(cursor="ibeam")

        self.passwordEntry = ctk.EntryCustom(mainUI, "Password")
        self.passwordEntry.place(relx=0.65, rely=0.525, relheight=0.065
                                 , relwidth=0.221)
        self.passwordEntry.configure(takefocus="")
        self.passwordEntry.configure(show='*')
        self.passwordEntry.configure(cursor="ibeam")

        self.calendarStart = DateEntry(mainUI)
        self.calendarStart.place(relx=0.65, rely=0.6, relheight=0.065
                                 , relwidth=0.221)
        self.calendarStart.configure(takefocus="")
        self.calendarStart.configure(cursor="ibeam")

        self.calendarEnd = DateEntry(mainUI)
        self.calendarEnd.place(relx=0.65, rely=0.675, relheight=0.065
                               , relwidth=0.221)
        self.calendarEnd.configure(takefocus="")
        self.calendarEnd.configure(cursor="ibeam")

        self.loginBtn = tk.Button(mainUI)
        self.loginBtn.place(relx=0.65, rely=0.775, height=33, width=176)
        self.loginBtn.configure(activebackground="#ececec")
        self.loginBtn.configure(activeforeground="#000000")
        self.loginBtn.configure(background="#d9d9d9")
        self.loginBtn.configure(command=lambda: mainframe_support.login(self.userEntry.get(), self.passwordEntry.get()))
        self.loginBtn.configure(cursor="fleur")
        self.loginBtn.configure(disabledforeground="#a3a3a3")
        self.loginBtn.configure(foreground="#000000")
        self.loginBtn.configure(highlightbackground="#d9d9d9")
        self.loginBtn.configure(highlightcolor="black")
        self.loginBtn.configure(pady="0")
        self.loginBtn.configure(text='''Login''')


if __name__ == '__main__':
    vp_start_gui()
