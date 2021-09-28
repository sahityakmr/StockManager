import math
import smtplib

import tk
from ui.enroll_user import Registration_form_support as registration_form

def create_otp(OTP_p):
    global OTPp
    OTPp = tk.IntVar()
    corpus = "0123456789"
    OTPp = ""
    size = 6
    length = len(corpus)
    for i in range(size):
        from random import random
        OTPp += corpus[math.floor(random() * length)]
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("775singhj@gmail.com", "27April@1993")
    message = OTPp
    s.sendmail("775singhj@gmail.com", "singhj775@outlook.com", message)
    s.quit()
    return registration_form.register(OTP_p)
