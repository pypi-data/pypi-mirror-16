"""
Code heavily adapted from http://pastebin.com/wzYZGZrs
"""
import atexit

from .keyboard_event import KeyboardEvent, KEY_DOWN, KEY_UP, normalize_name
from .generic import GenericScanCodeTable

import ctypes
from ctypes import c_short, c_char, c_uint8, c_int32, c_int, c_uint, c_uint32, c_long, Structure, CFUNCTYPE, POINTER
from ctypes.wintypes import DWORD, BOOL, HHOOK, MSG, LPWSTR, WCHAR, WPARAM, LPARAM
LPMSG = POINTER(MSG)

user32 = ctypes.windll.user32

class KBDLLHOOKSTRUCT(Structure):
    _fields_ = [("vk_code", DWORD),
                ("scan_code", DWORD),
                ("flags", DWORD),
                ("time", c_int),]

LowLevelKeyboardProc = CFUNCTYPE(c_int, WPARAM, LPARAM, POINTER(KBDLLHOOKSTRUCT))

SetWindowsHookEx = user32.SetWindowsHookExA
#SetWindowsHookEx.argtypes = [c_int, LowLevelKeyboardProc, c_int, c_int]
SetWindowsHookEx.restype = HHOOK

CallNextHookEx = user32.CallNextHookEx
#CallNextHookEx.argtypes = [c_int , c_int, c_int, POINTER(KBDLLHOOKSTRUCT)]
CallNextHookEx.restype = c_int

UnhookWindowsHookEx = user32.UnhookWindowsHookEx
UnhookWindowsHookEx.argtypes = [HHOOK]
UnhookWindowsHookEx.restype = BOOL

GetMessage = user32.GetMessageW
GetMessage.argtypes = [LPMSG, c_int, c_int, c_int]
GetMessage.restype = BOOL

TranslateMessage = user32.TranslateMessage
TranslateMessage.argtypes = [LPMSG]
TranslateMessage.restype = BOOL

DispatchMessage = user32.DispatchMessageA
DispatchMessage.argtypes = [LPMSG]


keyboard_state_type = c_uint8 * 256

GetKeyboardState = user32.GetKeyboardState
GetKeyboardState.argtypes = [keyboard_state_type]
GetKeyboardState.restype = BOOL

GetKeyNameText = user32.GetKeyNameTextW
GetKeyNameText.argtypes = [c_long, LPWSTR, c_int]
GetKeyNameText.restype = c_int

MapVirtualKey = user32.MapVirtualKeyW
MapVirtualKey.argtypes = [c_uint, c_uint]
MapVirtualKey.restype = c_uint

MAPVK_VSC_TO_VK = 1

class ScanCodeTable(GenericScanCodeTable):
    def __init__(self):
        GenericScanCodeTable.__init__(self)
        self.keycode_by_scan_code = {}

    def populate(self):
        self.table[541] = [('alt gr', False)]
        for scan_code in range(2**(23-16)):
            entries = []
            for entry in self.get_descriptions(scan_code):
                if entry not in entries:
                    entries.append(entry)
            
            if entries:
                self.table[scan_code] = entries

            ret = MapVirtualKey(scan_code, MAPVK_VSC_TO_VK)
            if ret:
                self.keycode_by_scan_code[scan_code] = ret

    def get_descriptions(self, scan_code):
        for enhanced in 0, 1:
            ret = GetKeyNameText(scan_code << 16 | enhanced << 24, name_buffer, 1024)
            name = normalize_name(name_buffer.value)
            if ret:
                if name.startswith('num ') and name != 'num lock':
                    is_keypad = True
                    name = name[len('num '):]
                else:
                    is_keypad = False

                if name.startswith('left ') or name.startswith('right '):
                    side, name = name.split(' ', 1)
                    name = normalize_name(name)
                    yield (name, is_keypad)
                    yield (side + ' '+ name, is_keypad)
                else:
                    yield (name, is_keypad)

    def map_char(self, char):
        self.ensure_populated()
        ret = VkKeyScan(WCHAR(char))
        if ret == -1:
            raise ValueError('Cannot type character ' + char)
        keycode = ret & 0x00FF
        shift = ret & 0xFF00
        scan_code = next(k for k, v in self.keycode_by_scan_code.items() if v == keycode)
        return scan_code, shift

scan_code_table = ScanCodeTable()

name_buffer = ctypes.create_unicode_buffer(32)

VkKeyScan = user32.VkKeyScanW
VkKeyScan.argtypes = [WCHAR]
VkKeyScan.restype = c_short

NULL = c_int(0)

WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_SYSKEYDOWN = 0x104 # Used for ALT key
WM_SYSKEYUP = 0x105

keyboard_event_types = {
    WM_KEYDOWN: KEY_DOWN,
    WM_KEYUP: KEY_UP,
    WM_SYSKEYDOWN: KEY_DOWN,
    WM_SYSKEYUP: KEY_UP,
}

def listen(handler):
    def low_level_keyboard_handler(nCode, wParam, lParam):
        # You may be tempted to use ToUnicode to extract the character from
        # this event. Do not. ToUnicode breaks dead keys.

        scan_code = lParam.contents.scan_code
        entries = list(scan_code_table.get_descriptions(scan_code))
        names = [name for name, is_keypad in entries]
        is_keypad = len(entries) and entries[0][1]

        event = KeyboardEvent(keyboard_event_types[wParam], scan_code, is_keypad, names)
        
        if handler(event):
            return 1
        else:
            return CallNextHookEx(NULL, nCode, wParam, lParam)

    WH_KEYBOARD_LL = c_int(13)
    keyboard_callback = LowLevelKeyboardProc(low_level_keyboard_handler)
    keyboard_hook = SetWindowsHookEx(WH_KEYBOARD_LL, keyboard_callback, NULL, NULL)

    # Register to remove the hook when the interpreter exits. Unfortunately a
    # try/finally block doesn't seem to work here.
    atexit.register(UnhookWindowsHookEx, keyboard_callback)

    msg = LPMSG()
    while not GetMessage(msg, NULL, NULL, NULL):
        TranslateMessage(msg)
        DispatchMessage(msg)

map_char = scan_code_table.map_char

def press(scan_code):
    scan_code_table.ensure_populated()
    user32.keybd_event(scan_code_table.keycode_by_scan_code[scan_code], 0, 0, 0)

def release(scan_code):
    scan_code_table.ensure_populated()
    user32.keybd_event(scan_code_table.keycode_by_scan_code[scan_code], 0, 2, 0)

if __name__ == '__main__':
    def p(e):
        print(e)
    listen(p)
