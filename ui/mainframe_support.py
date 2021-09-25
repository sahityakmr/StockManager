import logging
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

import db.dbops as db
from configs.config_reader import ConfigManager
from PIL import Image, ImageTk

logger = logging.getLogger("mainframe_support")

config = ConfigManager()


def set_Tk_var():
    global selectedButton
    selectedButton = tk.IntVar()


def initViews():
    # w.userEntry.configure(state='disabled')
    # w.passwordEntry.configure(state='disabled')
    logger.debug(config.get_val("resources.logo_res"))
    logo_image = Image.open(config.get_val("resources.logo_res"))
    resized_image = ImageTk.PhotoImage(logo_image.resize((100, 100), Image.ANTIALIAS))
    window.logoCanvas.image = resized_image
    window.logoCanvas.create_image(0, 0, image=resized_image, anchor='nw')
    window.orgTitleLabel.configure(text=config.get_val("ui.main_ui.title"))


def init(top: tk.Tk, gui, *args, **kwargs):
    global window, top_level, root
    window = gui
    top_level = top
    root = top
    initViews()


def deleteUser():
    print('mainframe_support.deleteUser')
    sys.stdout.flush()


def enrollAdmin():
    print('mainframe_support.enrollAdmin')
    sys.stdout.flush()


def enrollUser():
    print('mainframe_support.enrollUser')
    sys.stdout.flush()


def login(username, password):
    user = dbOperations.getUser(username, password)
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