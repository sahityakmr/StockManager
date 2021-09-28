import logging
from idlelib.idle_test.test_browser import mb
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd, messagebox
from service.config_service import ConfigService
from ui.enroll_user import otp_generator as otp
from PIL import ImageTk
from PIL.Image import Image

logger = logging.getLogger("Registration_form_support")

configService = ConfigService.getInstance()

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


def set_Tk_var():
    global selectedButton
    selectedButton = tk.IntVar()


def otp():
    otp.create_otp()


def register(OTP_p,FNAME):
    if OTP_p.get() == "":
        mb.showinfo('Information', "Please Enter otp")
        return
    if FNAME.get() == "": #or LNAME.get() == "" or USERID.get() == "" or PASS.get() == "":
        #lbl_result.config(text="Please Fill all the Details", fg="red")
        print("7")
        return
    else:
        print("yes")
    #     Database()
    #     cursor.execute("INSERT INTO `user` (fname, lname, userid, password) VALUES(%s, %s, %s, %s)",
    #                    (str(NAME.get()), str(LNAME.get()), str(USERID.get()), str(PASS.get())))
    #     conn.commit()
    #     conn.close()
    #     tkMessageBox.showinfo("DATA SAVED", "Your Data is Saved Succesfully")
    #     root.withdraw()
    #     Home()
    #     loginform.destroy()


def initViews():
    logger.debug(configService.getConfig("resources.logo_res"))
    logo_image = Image.open(configService.getConfig("resources.logo_res"))
    resized_image = ImageTk.PhotoImage(logo_image.resize((100, 100), Image.ANTIALIAS))
    w.Canvas1.image = resized_image
    w.Canvas1.create_image(0, 0, image=resized_image, anchor='ne')


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    initViews()


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def radio_gender(genderVar):
    if genderVar == "male":
        selection = "You selected the option " + str(genderVar)

        return
    if genderVar == "female":
        selection = "You selected the option " + str(genderVar)

        return
    else:
        print("error")


def upload():
    filetypes = (('image files', '*.jpg'), ('All files', '*.*'))

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=[filename]
    )

    try:

        # if filename:
        #     image_file_name = os.path.basename(filename)
        #     file_to_copy = filename
        #     image_selected = True
        #         cursor = conn.cursor(buffered=True)
        #         cursor.execute("create database if not exists meena")
        #         cursor.execute("use meena")
        #         cursor.execute(
        #             '''CREATE TABLE IF NOT EXISTS `test` (image LONGBLOB null,bill_number varchar(100) primary key NOT NULL )''')
        #         with open(file_to_copy, 'rb') as ff:
        #             bd = ff.read()
        #         cursor.execute('''insert into test(image,bill_number) values(%s,%s)''', (bd, billl))
        #         conn.commit()
        #
        mb.showinfo("File uploaded succesfully")
    except IOError as err:
        image_selected = False
        mb.showinfo("File Error", err)


if __name__ == '__main__':
    import registraion_form

    registraion_form.vp_start_gui_registration()
