# built in libraries
import platform
import string
import sys
import os

# tamcolors libraries
from .tam_buffer import TAMBuffer
from . import io_tam
from tamcolors.tam_c import _uni_tam as io


"""
UniIO
draws out to Unix terminal
gets ASCII key input from linux terminal
color mode 2
color mode 16
"""


class UniIOError(Exception):
    pass


class UniIO(io_tam.SingletonIO):
    def __init__(self):
        """
        info: makes UniIO object
        """
        super().__init__()
        self.__buffer = TAMBuffer(0, 0, " ", 1, 1)
        self.__unix_keys = self.get_key_dict()

        self.__foreground_color_map = {-2: "39",
                                       -1: "39",
                                       0: "38;5;232",
                                       1: "38;5;20",
                                       2: "38;5;34",
                                       3: "38;5;75",
                                       4: "38;5;1",
                                       5: "38;5;90",
                                       6: "38;5;3",
                                       7: "38;5;252",
                                       8: "38;5;243",
                                       9: "38;5;33",
                                       10: "38;5;76",
                                       11: "38;5;117",
                                       12: "38;5;161",
                                       13: "38;5;126",
                                       14: "38;5;229",
                                       15: "38;5;15"}

        self.__background_color_map = {-2: "49",
                                       -1: "49",
                                       0: "48;5;232",
                                       1: "48;5;20",
                                       2: "48;5;34",
                                       3: "48;5;75",
                                       4: "48;5;1",
                                       5: "48;5;90",
                                       6: "48;5;3",
                                       7: "48;5;252",
                                       8: "48;5;243",
                                       9: "48;5;33",
                                       10: "48;5;76",
                                       11: "48;5;117",
                                       12: "48;5;161",
                                       13: "48;5;126",
                                       14: "48;5;229",
                                       15: "48;5;15"}

    @classmethod
    def able_to_execute(cls):
        """
        info: will see if environment supported by UniIO
        :return: bool
        """
        if platform.system() in ("Darwin", "Linux"):
            if os.system("test -t 0 -a -t 1 -a -t 2") == 0:
                return io is not None
        return False

    def draw(self, tam_buffer):
        """
        info: will draw tam buffer to terminal
        :param tam_buffer: TAMBuffer
        :return:
        """

        dimension = io._get_dimension()
        if self.__buffer.get_dimensions() != dimension:
            self.clear()
            self._show_console_cursor(False)
            io._enable_get_key()
            self.__buffer.set_dimensions_and_clear(*dimension)

        super().draw(tam_buffer)

    def _draw_2(self, tam_buffer):
        """
        info: will draw tam buffer to terminal in mode 2
        :param tam_buffer: TAMBuffer
        :return:
        """

        # checks if buffer needs to be updated
        if " " != self.__buffer.get_defaults()[0] or self.__buffer.get_defaults()[1:] != tam_buffer.get_defaults()[1:]:
            # buffer defaults changed
            self.__buffer.set_defaults_and_clear(" ", *tam_buffer.get_defaults()[1:])

        # draw onto LinIO buffer
        self._draw_onto(self.__buffer, tam_buffer)

        color = self._get_lin_tam_color(*self.__buffer.get_defaults()[1:])
        output = "".join(self.__buffer.get_raw_buffers()[0])
        sys.stdout.write("\u001b[1;1H\u001b[{0};{1}m{2}\u001b[0".format(*color, output))
        sys.stdout.flush()

    def _draw_16(self, tam_buffer):
        """
        info: will draw tam buffer to terminal in mode 16
        :param tam_buffer: TAMBuffer
        :return:
        """
        # checks if buffer needs to be updated
        if " " != self.__buffer.get_defaults()[0] or self.__buffer.get_defaults()[1:] != tam_buffer.get_defaults()[1:]:
            # buffer defaults changed
            self.__buffer.set_defaults_and_clear(" ", *tam_buffer.get_defaults()[1:])

        # draw onto LinIO buffer
        self._draw_onto(self.__buffer, tam_buffer)

        # make output string
        output = ["\u001b[1;1H"]
        foreground, background = None, None
        char_buffer, foreground_buffer, background_buffer = self.__buffer.get_raw_buffers()
        for spot in range(len(char_buffer)):
            if foreground is None:
                foreground = foreground_buffer[spot]
                background = background_buffer[spot]
                output.append("\u001b[{0};{1}m".format(*self._get_lin_tam_color(foreground, background)))
                output.append(char_buffer[spot])
            elif foreground == foreground_buffer[spot] and background == background_buffer[spot]:
                output.append(char_buffer[spot])
            else:
                foreground = foreground_buffer[spot]
                background = background_buffer[spot]
                output.append("\u001b[{0};{1}m".format(*self._get_lin_tam_color(foreground, background)))
                output.append(char_buffer[spot])

        sys.stdout.write("".join(output) + "\u001b[0")
        sys.stdout.flush()

    def start(self):
        """
        info: will setup terminal to be used
        :return:
        """
        self.clear()
        self._show_console_cursor(False)
        io._enable_get_key()

    def done(self):
        """
        info: will reset terminal
        :return:
        """
        self.clear()
        self._show_console_cursor(True)
        io._disable_get_key()
        os.system("clear")

    def get_key(self):
        """
        info: will get single key input or return False
        :return: str or False
        """
        key_bytes = []
        key_byte = io._get_key()
        while key_byte != -1:
            key_bytes.append(key_byte)
            key_byte = io._get_key()

        if len(key_bytes) != 0:
            return self.__unix_keys.get(";".join([str(key_byte) for key_byte in key_bytes]), False)

        return False

    def get_dimensions(self):
        """
        info: will get teh terminal dimensions
        :return: (int, int)
        """
        return io._get_dimension()

    @staticmethod
    def get_key_dict():
        """
        info: makes a dict mapping key codes to key
        :return: dict
        """
        normal_key = string.digits + string.ascii_letters + "`-=[]\\;',./~!@#$%^&*()_+{}|:\"<>?"
        linux_keys = {str(ord(key)): (key, "NORMAL") for key in normal_key}

        code_27_91 = [[65, "UP"], [66, "DOWN"], [68, "LEFT"], [67, "RIGHT"]]

        for code, key in code_27_91:
            linux_keys["27;91;{0}".format(code)] = (key, "SPECIAL")

        for f_key in range(0, 4):
            linux_keys["27;79;{0}".format(f_key + 80)] = ("F{0}".format(f_key + 1), "SPECIAL")
            linux_keys["27;91;49;59;50;{0}".format(f_key + 80)] = ("F{0}_SHIFT".format(f_key + 1), "SPECIAL")

        linux_keys["27;91;49;53;126"] = ("F5", "SPECIAL")
        linux_keys["27;91;49;53;59;50;126"] = ("F5_SHIFT", "SPECIAL")

        linux_keys["27;91;49;55;126"] = ("F6", "SPECIAL")
        linux_keys["27;91;49;55;59;50;126"] = ("F6_SHIFT", "SPECIAL")

        linux_keys["27;91;49;56;126"] = ("F7", "SPECIAL")
        linux_keys["27;91;49;56;59;50;126"] = ("F7_SHIFT", "SPECIAL")

        linux_keys["27;91;49;57;126"] = ("F8", "SPECIAL")
        linux_keys["27;91;49;57;59;50;126"] = ("F8_SHIFT", "SPECIAL")

        linux_keys["27;91;50;48;126"] = ("F9", "SPECIAL")
        linux_keys["27;91;50;48;59;50;126"] = ("F9_SHIFT", "SPECIAL")

        linux_keys["27;91;50;52;126"] = ("F12", "SPECIAL")
        linux_keys["27;91;50;52;59;50;126"] = ("F12_SHIFT", "SPECIAL")

        linux_keys["27;91;51;126"] = ("DELETE", "SPECIAL")

        linux_keys["9"] = ("\t", "WHITESPACE")
        linux_keys["10"] = ("\n", "WHITESPACE")
        linux_keys["32"] = (" ", "WHITESPACE")

        linux_keys["127"] = ("BACKSPACE", "SPECIAL")
        linux_keys["27"] = ("ESCAPE", "SPECIAL")

        return linux_keys

    @staticmethod
    def _show_console_cursor(show_flag):
        """
        info: will show or hide the cursor
        :param show_flag: bool:
        :return:
        """
        if platform.system() != "Darwin":
            if show_flag:
                os.system("setterm -cursor on")
            else:
                os.system("setterm -cursor off")

    def _get_lin_tam_color(self, foreground_color, background_color):
        """
        info: will get the ANI color code
        :param foreground_color: int
        :param background_color: int
        :return: (str, sr)
        """
        return self.__foreground_color_map.get(foreground_color),\
               self.__background_color_map.get(background_color)

    def printc(self, output, color, flush, stderr):
        """
        info: will print out user output with color
        :param output: str
        :param color: tuple: (int, int)
        :param flush: boolean
        :param stderr: boolean
        :return: None
        """
        output_str = "\u001b[{0};{1}m{2}\u001b[0m".format(*self._get_lin_tam_color(*color), output)
        self._write_to_output_stream(output_str, flush, stderr)

    def inputc(self, output, color):
        """
        info: will get user input with color
        :param output: str
        :param color: tuple: (int, int)
        :return: str
        """
        output_str = "\u001b[{0};{1}m{2}".format(*self._get_lin_tam_color(*color), output)
        ret = input(output_str)
        sys.stdout.write("\u001b[0m")
        sys.stdout.flush()
        return ret

    def clear(self):
        """
        info: will clear the screen. Note that it will also reset the terminal
        :return:
        """
        os.system("tput reset")
