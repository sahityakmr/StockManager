import logging
import sys

from service.user_service import UserService
from service.config_service import ConfigService

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

userLoginMode = None


def set_Tk_var():
    global selectedButton
    selectedButton = tk.IntVar()


def initViews():
    window.userEntry.configure(state='disabled')
    window.passwordEntry.configure(state='disabled')
    window.loginBtn.configure(state='disabled')
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


def deleteUser():
    print('mainframe_support.deleteUser')
    sys.stdout.flush()


def enrollAdmin():
    print('mainframe_support.enrollAdmin')
    sys.stdout.flush()


def enrollUser():
    print('mainframe_support.enrollUser')
    sys.stdout.flush()


def login():
    username = window.userEntry.get()
    password = window.passwordEntry.get()
    user_type = userLoginMode
    start_date = str(window.calendarStart.get_date())
    end_date = str(window.calendarEnd.get_date())
    user = userService.getUser(username, password)
    logger.debug(
        str("Trying to login using username : %s, password : %s, user_type : %s, start_date : %s, end_date : %s" %
            (username, password, user_type, start_date, end_date)))
    if user is not None:
        print("Login Success")
    else:
        print("Login Failed")


def triggerUIChanges():
    global window
    window.userEntry.configure(state='normal')
    window.passwordEntry.configure(state='normal')
    window.loginBtn.configure(state='normal')


def chooseUserType(user_type):
    global userLoginMode
    if user_type == "user_type_admin":
        userLoginMode = "ADMIN"
    elif user_type == "user_type_user":
        userLoginMode = "USER"
    if userLoginMode is not None:
        triggerUIChanges()


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
