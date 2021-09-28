import logging
import sys

from service.user_service import UserService
from service.config_service import ConfigService
from ui.enroll_user import registration_form as registration_form
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

from PIL import Image, ImageTk

logger = logging.getLogger("mainframe_support")

configService = ConfigService.getInstance()
userService = UserService.getInstance()


def set_Tk_var():
    global selectedButton
    selectedButton = tk.IntVar()


def initViews():
    # w.userEntry.configure(state='disabled')
    # w.passwordEntry.configure(state='disabled')
    logger.debug(configService.getConfig("resources.logo_res"))
    logo_image = Image.open(configService.getConfig("resources.logo_res"))
    resized_image = ImageTk.PhotoImage(logo_image.resize((100, 100), Image.ANTIALIAS))
    window.logoCanvas.image = resized_image
    window.logoCanvas.create_image(0, 0, image=resized_image, anchor='nw')
    window.orgTitleLabel.configure(text=configService.getConfig("ui.main_ui.title"))

def init(top: tk.Tk, gui, *args, **kwargs):
    global window, top_level, root
    window = gui
    top_level = top
    root = top
    initViews()


def delete():
    pass
def approve():
    pass


def modify_user():
        global viewform
        viewform = tk.Toplevel()
        viewform.title("MEENA STOCK /View Product")
        width = 700
        height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
        # viewform10.resizable(0, 0)
        ViewForm()

def ViewForm():
        global treee, SEARCH
        SEARCH=tk.StringVar()
        TopViewForm = tk.Frame(viewform10, width=600, bd=1, relief=tk.SOLID)
        TopViewForm.pack(side=tk.TOP, fill=tk.X)
        LeftViewForm = tk.Frame(viewform10, width=600)
        LeftViewForm.pack(side=tk.LEFT, fill=tk.Y)
        MidViewForm = tk.Frame(viewform10, width=600)
        MidViewForm.pack(side=tk.RIGHT)
        lbl_text = tk.Label(TopViewForm, text="View Products", font=('arial', 18), width=600)
        lbl_text.pack(fill=tk.X)
        lbl_txtsearch = tk.Label(LeftViewForm, text="Search", font=('arial', 15))
        lbl_txtsearch.pack(side=tk.TOP, anchor=tk.W)
        search = tk.Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
        search.pack(side=tk.TOP, padx=10, fill=tk.X)
        btn_search = tk.Button(LeftViewForm, text="Search", command=delete)
        btn_search.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)
        btn_delete = tk.Button(LeftViewForm, text="Delete", command=approve)
        btn_delete.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)
        scrollbarx = tk.Scrollbar(MidViewForm, orient=tk.HORIZONTAL)
        scrollbary = tk.Scrollbar(MidViewForm, orient=tk.VERTICAL)
        treee = ttk.Treeview(MidViewForm, columns=("fname", "lname", "userid"), selectmode="extended", height=100,
                             yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=treee.yview)
        scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbarx.config(command=treee.xview)
        scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
        treee.heading('fname', text="FIRST NAME", anchor=tk.W)
        treee.heading('userid', text="USER NAME", anchor=tk.W)
        treee.heading('fname', text="FIRST NAME", anchor=tk.W)
        treee.column('#0', stretch=tk.NO, minwidth=0, width=0)
        treee.column('#1', stretch=tk.NO, minwidth=0, width=0)
        treee.column('#2', stretch=tk.NO, minwidth=0, width=200)
        treee.column('#3', stretch=tk.NO, minwidth=0, width=120)
        treee.pack()
        #DisplayData()


# def DisplayData():
#     Database()
#     cursor.execute("SELECT * FROM `user`")
#     fetch = cursor.fetchall()
#     for data in fetch:
#         treee.insert('', 'end', values=(data))
#     cursor.close()
#     conn.close()



def enrollAdmin():
    print('mainframe_support.enrollAdmin')
    sys.stdout.flush()


def enrollUser():
    registration_form.vp_start_gui_registration()


def login(username, password):
    user = userService.getUser(username, password)
    logger.debug(str("Trying to login using username : %s and password : %s" % (username, password)))
    if user is not None:
        print("Login Success")
    else:
        print("Login Failed")


def takeBackup():
    print('mainframe_support.takeBackup')
    sys.stdout.flush()






def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import mainframe

    mainframe.vp_start_gui()
