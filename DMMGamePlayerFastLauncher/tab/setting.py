import json
import os
from tkinter import StringVar

import customtkinter as ctk
import i18n
from component.component import CheckBoxComponent, ConfirmWindow, DirectoryPathComponent, EntryComponent, OptionMenuComponent, OptionMenuTupleComponent, PaddingComponent
from component.slider import CTkFloatSlider
from component.tab_menu import TabMenuComponent
from customtkinter import CTkBaseClass, CTkButton, CTkFrame, CTkLabel, CTkScrollableFrame
from lib.toast import ToastController, error_toast
from models.setting_data import SettingData
from static.config import AppConfig, AssetsPathConfig, DataPathConfig


class SettingTab(CTkFrame):
    tab: TabMenuComponent

    def __init__(self, master: CTkBaseClass):
        super().__init__(master, fg_color="transparent")
        self.tab = TabMenuComponent(self)

    def create(self):
        self.tab.create()
        self.tab.add(text=i18n.t("app.tab.edit"), callback=self.edit_callback)
        self.tab.add(text=i18n.t("app.tab.other"), callback=self.other_callback)
        return self

    def edit_callback(self, master: CTkBaseClass):
        SettingEditTab(master).create().pack(expand=True, fill=ctk.BOTH)

    def other_callback(self, master: CTkBaseClass):
        SettingOtherTab(master).create().pack(expand=True, fill=ctk.BOTH)


class SettingEditTab(CTkScrollableFrame):
    # 提示弹窗
    toast: ToastController
    # 设置数据
    data: SettingData
    # 当前可选语言
    lang: dict[str, str]
    theme: list[str]

    def __init__(self, master: CTkBaseClass):
        super().__init__(master, fg_color="transparent")
        self.toast = ToastController(self)
        self.data = AppConfig.DATA

        self.lang = {}

        # 初始化, 从语音文件夹中获取所有语言
        for x in AssetsPathConfig.I18N.iterdir():
            y = x.suffixes[0].removeprefix(".")
            self.lang.update({y: i18n.t("app.language." + y)})

        self.theme = [x.stem for x in AssetsPathConfig.THEMES.iterdir()]

    def create(self):
        DirectoryPathComponent(self, text=i18n.t("app.setting.dmm_game_player_program_folder"), variable=self.data.dmm_game_player_program_folder, required=True).create()
        DirectoryPathComponent(self, text=i18n.t("app.setting.dmm_game_player_data_folder"), variable=self.data.dmm_game_player_data_folder, required=True).create()
        # 创建语言下拉菜单
        OptionMenuTupleComponent(self, text=i18n.t("app.setting.lang"), values=self.lang, variable=self.data.lang).create()
        OptionMenuComponent(self, text=i18n.t("app.setting.theme"), values=self.theme, variable=self.data.theme).create()
        OptionMenuComponent(self, text=i18n.t("app.setting.appearance"), values=["light", "dark", "system"], variable=self.data.appearance_mode).create()

        EntryComponent(self, text=i18n.t("app.setting.proxy_http"), variable=self.data.proxy_http).create()
        EntryComponent(self, text=i18n.t("app.setting.proxy_https"), variable=self.data.proxy_https).create()

        PaddingComponent(self, height=5).create()
        CTkLabel(self, text=i18n.t("app.setting.window_scaling")).pack(anchor=ctk.W)
        CTkFloatSlider(self, from_=0.75, to=1.25, variable=self.data.window_scaling).pack(fill=ctk.X)

        PaddingComponent(self, height=5).create()
        CheckBoxComponent(self, text=i18n.t("app.setting.debug_window"), variable=self.data.debug_window).create()

        PaddingComponent(self, height=5).create()
        CTkButton(self, text=i18n.t("app.setting.save"), command=self.save_callback).pack(fill=ctk.X, pady=10)

        command = lambda: ConfirmWindow(self, command=self.delete_callback, text=i18n.t("app.setting.confirm_reset")).create()
        CTkButton(self, text=i18n.t("app.setting.reset_all_settings"), command=command).pack(fill=ctk.X, pady=10)

        return self

    @error_toast
    def save_callback(self):
        with open(DataPathConfig.APP_CONFIG, "w+", encoding="utf-8") as f:
            json.dump(self.data.to_dict(), f)
        self.reload_callback()

    @error_toast
    def reload_callback(self):
        from app import App

        app = self.winfo_toplevel()
        assert isinstance(app, App)
        app.loder(app)
        app.create()
        self.toast.info(i18n.t("app.setting.save_success"))

    @error_toast
    def delete_callback(self):
        DataPathConfig.APP_CONFIG.unlink()
        self.reload_callback()


class SettingOtherTab(CTkScrollableFrame):
    toast: ToastController

    def __init__(self, master: CTkBaseClass):
        super().__init__(master, fg_color="transparent")
        self.toast = ToastController(self)

    def create(self):
        CTkLabel(self, text=i18n.t("app.setting.other_detail"), justify=ctk.LEFT).pack(anchor=ctk.W)
        CTkButton(self, text=i18n.t("app.setting.open_save_folder"), command=self.open_folder_callback).pack(fill=ctk.X, pady=10)
        return self

    @error_toast
    def open_folder_callback(self):
        os.startfile(DataPathConfig.DATA)
