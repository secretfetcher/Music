from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ShrutiMusic import app

# =========================
# HELP PAGES
# =========================

def help_pannel_page1(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Admin", callback_data="help_callback hb1"),
                InlineKeyboardButton(text="Auth", callback_data="help_callback hb2"),
            ],
            [
                InlineKeyboardButton(text="Play", callback_data="help_callback hb3"),
                InlineKeyboardButton(text="Settings", callback_data="help_callback hb4"),
            ],
            [
                InlineKeyboardButton(text="Tools", callback_data="help_callback hb5"),
                InlineKeyboardButton(text="Voice", callback_data="help_callback hb6"),
                InlineKeyboardButton(text="Extra", callback_data="help_callback hb7"),
            ],
            [
                InlineKeyboardButton(text="⏮", callback_data="help_page_4"),
                InlineKeyboardButton(
                    text="BACK" if START else "CLOSE",
                    callback_data="settingsback_helper" if START else "close",
                ),
                InlineKeyboardButton(text="⏭", callback_data="help_page_2"),
            ],
        ]
    )


def help_pannel_page2(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Queue", callback_data="help_callback hb11"),
                InlineKeyboardButton(text="Skip", callback_data="help_callback hb12"),
            ],
            [
                InlineKeyboardButton(text="Pause", callback_data="help_callback hb13"),
                InlineKeyboardButton(text="Resume", callback_data="help_callback hb14"),
            ],
            [
                InlineKeyboardButton(text="⏮", callback_data="help_page_1"),
                InlineKeyboardButton(
                    text="BACK" if START else "CLOSE",
                    callback_data="settingsback_helper" if START else "close",
                ),
                InlineKeyboardButton(text="⏭", callback_data="help_page_3"),
            ],
        ]
    )


def help_pannel_page3(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Speed", callback_data="help_callback hb21"),
                InlineKeyboardButton(text="Loop", callback_data="help_callback hb22"),
            ],
            [
                InlineKeyboardButton(text="⏮", callback_data="help_page_2"),
                InlineKeyboardButton(
                    text="BACK" if START else "CLOSE",
                    callback_data="settingsback_helper" if START else "close",
                ),
                InlineKeyboardButton(text="⏭", callback_data="help_page_4"),
            ],
        ]
    )


def help_pannel_page4(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Stats", callback_data="help_callback hb31"),
                InlineKeyboardButton(text="Ping", callback_data="help_callback hb32"),
            ],
            [
                InlineKeyboardButton(text="⏮", callback_data="help_page_3"),
                InlineKeyboardButton(
                    text="BACK" if START else "CLOSE",
                    callback_data="settingsback_helper" if START else "close",
                ),
                InlineKeyboardButton(text="⏭", callback_data="help_page_1"),
            ],
        ]
    )


# =========================
# BACK BUTTON
# =========================

def help_back_markup(_, page: int = 1):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🔙 BACK",
                    callback_data=f"help_page_{page}",
                )
            ]
        ]
    )


# =========================
# PRIVATE HELP BUTTON (FIXED)
# =========================

def private_help_panel(_):
    return [
        [
            InlineKeyboardButton(
                text="📚 HELP",
                url=f"https://t.me/{app.username}?start=help",  # ✅ YOUR BOT ONLY
            ),
        ]
]
