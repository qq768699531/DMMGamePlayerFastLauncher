from customtkinter import CTkBaseClass, CTkFont, CTkFrame, CTkImage, CTkLabel
from customtkinter import ThemeManager as CTkm
from lib.toast import ToastController, error_toast
from PIL import Image

import i18n


class HomeTab(CTkFrame):
    toast: ToastController

    def __init__(self, master: CTkBaseClass):
        super().__init__(master, fg_color=CTkm.theme["CTkToplevel"]["fg_color"])
        self.toast = ToastController(self)

    @error_toast
    def create(self):
        frame = CTkFrame(self, fg_color=CTkm.theme["CTkToplevel"]["fg_color"])
        frame.pack(anchor="center", expand=1)

        image = CTkImage(light_image=Image.open("assets/img/DMMGamePlayerFastLauncher.png"), size=(240, 240))
        CTkLabel(frame, image=image, text="").pack()
        CTkLabel(frame, text=i18n.t("app.title"), font=CTkFont(size=28)).pack(pady=20)

        CTkLabel(frame, text=i18n.t("app.version"), font=CTkFont(size=18)).pack()
        return self
