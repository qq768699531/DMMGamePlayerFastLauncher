from dataclasses import dataclass, field
from tkinter import BooleanVar, DoubleVar, StringVar

from component.var import PathVar
from component.variable_base import VariableBase
from static.env import Env


@dataclass
class SettingData(VariableBase):
    # DMMGamePlayer 程序路径
    dmm_game_player_program_folder: PathVar = field(default_factory=lambda: PathVar(value=Env.DEFAULT_DMM_GAME_PLAYER_PROGURAM_FOLDER))
    # DMMGamePlayer 数据路径
    dmm_game_player_data_folder: PathVar = field(default_factory=lambda: PathVar(value=Env.DEFAULT_DMM_GAME_PLAYER_DATA_FOLDER))
    # HTTP 代理地址
    proxy_http: StringVar = field(default_factory=lambda: StringVar(value=""))
    # HTTPS 代理地址
    proxy_https: StringVar = field(default_factory=lambda: StringVar(value=""))
    # 当前选择的语言, 默认为日语
    lang: StringVar = field(default_factory=lambda: StringVar(value="jp"))
    # 当前主题
    theme: StringVar = field(default_factory=lambda: StringVar(value="blue"))
    # 当前配色
    appearance_mode: StringVar = field(default_factory=lambda: StringVar(value="dark"))
    # 当前缩放比例
    window_scaling: DoubleVar = field(default_factory=lambda: DoubleVar(value=1.0))
    # 是否打开调试窗口
    debug_window: BooleanVar = field(default_factory=lambda: BooleanVar(value=False))
