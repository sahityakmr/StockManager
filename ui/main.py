from tkinter import *
from configs.config_reader import ConfigManager
from PIL import Image, ImageTk
from tkcalendar import DateEntry
config = ConfigManager()

root = Tk()
root.title(config.get_val("ui.main_ui.title"))
width = int(config.get_val("ui.main_ui.width"))
height = int(config.get_val("ui.main_ui.height"))

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

canvas_for_image = Canvas(root, bg='#6666ff', height=200, width=200, borderwidth=0, highlightthickness=0)
canvas_for_image.grid(row=4, column=2, sticky='nesw', padx=0, pady=0)

# create image from image location resize it to 200X200 and put in on canvas
image = Image.open('ui/logo.png')
canvas_for_image.image = ImageTk.PhotoImage(image.resize((200, 200), Image.ANTIALIAS))
canvas_for_image.create_image(0, 0, image=canvas_for_image.image, anchor='nw')

cal = DateEntry(root, selectmode='day')
cal.grid(row=7, column=1, padx=0, pady=0)

cal2 = DateEntry(root, selectmode='day')
cal2.grid(row=9, column=1, padx=0, pady=0)

dat = []
global uss
uss = StringVar()
global text
text = StringVar()


def my_upd():  # triggered on Button Click
    l1.config(text=cal.get_date())
    # print(cal.get_date())# read and display date
    dat.append(str(cal.get_date()))
    # print(dat)


def my_upd1():  # triggered on Button Click
    l2.config(text=cal2.get_date())
    dat.append(str(cal2.get_date()))
    # print(dat)


l1 = Label(root, text='data', bg='yellow')  # Label to display date
l1.grid(row=7, column=3)

l2 = Label(root, text='data', bg='green')  # Label to display date
l2.grid(row=9, column=3)

b1 = Button(root, text='Read', command=lambda: my_upd())
b1.grid(row=7, column=2)

b2 = Button(root, text='Read', command=lambda: my_upd1())
b2.grid(row=9, column=2)

l3 = Label(root, text='Select Financial Year', bg='red')  # Label to display date
l3.grid(row=5, column=3)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))
# root.resizable(0, 0)
root.config(bg="#6666ff")
global i
# ========================================VARIABLES========================================
global USERNAME
MANUAL = StringVar()
MANUAL1 = StringVar()
USERNAME = StringVar()
PASSWORD = StringVar()
PRODUCT_NAME = StringVar()
PRODUCT_PRICE = IntVar()
PRODUCT_QTY = IntVar()
SEARCH = StringVar()
PRODUCT_CODE = StringVar()
clicked = StringVar()
PRODUCT_DIMENSION = StringVar()
PART = StringVar()
SIZE = StringVar()
GODOWN_NUMBER = StringVar()
PRODUCT_SIZE = StringVar()
BILL = IntVar()
PARTY_NAME = StringVar()
CONTACT = IntVar()
WEIGHT = StringVar()
PRICE = StringVar()
i = StringVar()
PRODUCT_CODE = StringVar()
global axxx
axxx = StringVar()


def ShowLoginForm6():
    pass


def ShowLoginForm2():
    pass


def ShowLoginForm3():
    pass


def ShowLoginForm4():
    pass


def Exit():
    pass


def ShowLoginForm():
    pass

def Backu():
    pass


def Backup_1():
    pass

# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu2 = Menu(menubar, tearoff=0)
filemenu3 = Menu(menubar, tearoff=0)
filemenu.add_command(label="Admin", command=ShowLoginForm6)
filemenu.add_command(label="User", command=ShowLoginForm2)
filemenu.add_command(label="Register", command=ShowLoginForm3)
filemenu.add_command(label="Delete User", command=ShowLoginForm4)
filemenu.add_command(label="Exit", command=Exit)
filemenu2.add_command(label="TOTP for Admin", command=ShowLoginForm)
filemenu3.add_command(label="Backup To Server", command=Backu)
filemenu3.add_command(label="Backup to Local", command=Backup_1)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Security", menu=filemenu2)
menubar.add_cascade(label="Backup", menu=filemenu3)
root.config(menu=menubar)

# ========================================FRAME============================================
Title = Frame(root, relief=SOLID)
Title.grid(pady=10)

# ========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="MEENA STOCK ", font=('arial', 45))
lbl_display.pack()

root.mainloop()
