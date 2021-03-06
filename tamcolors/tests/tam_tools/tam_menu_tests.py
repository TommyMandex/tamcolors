# built in libraries
import unittest
import unittest.mock

# tamcolors libraries
from tamcolors import tam_io
from tamcolors import tam_tools


class TAMMenuTests(unittest.TestCase):
    def test_tam_menu(self):
        self.assertIsInstance(tam_tools.tam_menu.TAMMenu([], "a", {}), tam_tools.tam_menu.TAMMenu)

    def test_tam_menu_2(self):
        buttons = (tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("12345678", 3, 8, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2))

        goto_map = {0: {"UP": 3, "DOWN": 1},
                    1: {"UP": 0, "DOWN": 2},
                    2: {"UP": 1, "DOWN": 3},
                    3: {"UP": 2, "DOWN": 0}}

        self.assertIsInstance(tam_tools.tam_menu.TAMMenu(buttons, "a", goto_map), tam_tools.tam_menu.TAMMenu)

    def test_update(self):
        hit_button = tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2)
        buttons = (hit_button,
                   tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("12345678", 3, 8, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2))

        goto_map = {0: {"UP": 3, "DOWN": 1},
                    1: {"UP": 0, "DOWN": 2},
                    2: {"UP": 1, "DOWN": 3},
                    3: {"UP": 2, "DOWN": 0}}

        menu = tam_tools.tam_menu.TAMMenu(buttons, "a", goto_map)

        with unittest.mock.patch.object(tam_tools.tam_menu.TAMTextButton, "__call__", return_value=None) as call:
            menu.update((("a", "NORMAL"),))
            call.assert_called_once_with()
            self.assertIs(menu.get_on()[1], hit_button)

    def test_update_2(self):
        hit_button = tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2)
        buttons = (hit_button,
                   tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("12345678", 3, 8, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2))

        goto_map = {0: {"UP": 3, "DOWN": 1},
                    1: {"UP": 0, "DOWN": 2},
                    2: {"UP": 1, "DOWN": 3},
                    3: {"UP": 2, "DOWN": 0}}

        menu = tam_tools.tam_menu.TAMMenu(buttons, "a", goto_map)

        with unittest.mock.patch.object(tam_tools.tam_menu.TAMTextButton, "__call__", return_value=None) as call:
            menu.update((("a", "NORMAL"),))
            call.assert_called_once_with()
            self.assertIs(menu.get_on()[1], hit_button)
            menu.update((("a", "NORMAL"),))
            self.assertEqual(call.call_count, 2)
            self.assertIs(menu.get_on()[1], hit_button)

    def test_update_3(self):
        hit_button = tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2)
        hit_button_2 = tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2)
        hit_button_3 = tam_tools.tam_menu.TAMTextButton("12345678", 3, 8, 6, 2, lambda: None, 5, 2)
        hit_button_4 = tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2)

        buttons = (hit_button,
                   hit_button_2,
                   hit_button_3,
                   hit_button_4)

        goto_map = {0: {"UP": 3, "DOWN": 1},
                    1: {"UP": 0, "DOWN": 2},
                    2: {"UP": 1, "DOWN": 3},
                    3: {"UP": 2, "DOWN": 0}}

        menu = tam_tools.tam_menu.TAMMenu(buttons, "a", goto_map)

        with unittest.mock.patch.object(tam_tools.tam_menu.TAMTextButton, "__call__", return_value=None) as call:
            menu.update((("a", "NORMAL"),))
            call.assert_called_once_with()
            self.assertIs(menu.get_on()[1], hit_button)

            menu.update((("a", "NORMAL"),))
            self.assertEqual(call.call_count, 2)
            self.assertIs(menu.get_on()[1], hit_button)

            menu.update((("DOWN", "SPECIAL"), ("a", "NORMAL")))
            self.assertEqual(call.call_count, 3)
            self.assertIs(menu.get_on()[1], hit_button_2)

            menu.update((("DOWN", "SPECIAL"), ("a", "NORMAL")))
            self.assertEqual(call.call_count, 4)
            self.assertIs(menu.get_on()[1], hit_button_3)

            menu.update((("DOWN", "SPECIAL"), ("a", "NORMAL")))
            self.assertEqual(call.call_count, 4)
            self.assertIs(menu.get_on()[1], hit_button_4)

            menu.update((("UP", "SPECIAL"), ("a", "NORMAL")))
            self.assertEqual(call.call_count, 5)
            self.assertIs(menu.get_on()[1], hit_button_3)

    def test_draw(self):
        buttons = (tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("12345678", 3, 8, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2))

        goto_map = {0: {"UP": 3, "DOWN": 1},
                    1: {"UP": 0, "DOWN": 2},
                    2: {"UP": 1, "DOWN": 3},
                    3: {"UP": 2, "DOWN": 0}}

        menu = tam_tools.tam_menu.TAMMenu(buttons, "a", goto_map)
        with unittest.mock.patch.object(tam_tools.tam_menu.TAMTextButton, "draw", return_value=None) as text_draw:
            with unittest.mock.patch.object(tam_tools.tam_menu.TAMTextBoxButton, "draw", return_value=None) as box_draw:
                buffer = tam_io.tam_buffer.TAMBuffer(0, 0, " ", 1, 2)
                menu.draw(buffer)
                self.assertEqual(text_draw.call_count, 3)
                box_draw.assert_called_once_with(buffer)

    def test_get_call_key(self):
        buttons = (tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("12345678", 3, 8, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2))

        goto_map = {0: {"UP": 3, "DOWN": 1},
                    1: {"UP": 0, "DOWN": 2},
                    2: {"UP": 1, "DOWN": 3},
                    3: {"UP": 2, "DOWN": 0}}

        menu = tam_tools.tam_menu.TAMMenu(buttons, "a", goto_map)

        self.assertEqual(menu.get_call_key(), "a")

    def test_get_call_key_2(self):
        buttons = (tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("12345678", 3, 8, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2))

        goto_map = {0: {"UP": 3, "DOWN": 1},
                    1: {"UP": 0, "DOWN": 2},
                    2: {"UP": 1, "DOWN": 3},
                    3: {"UP": 2, "DOWN": 0}}

        menu = tam_tools.tam_menu.TAMMenu(buttons, "UP", goto_map)

        self.assertEqual(menu.get_call_key(), "UP")

    def test_get_on(self):
        hit_button = tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2)
        buttons = (hit_button,
                   tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("12345678", 3, 8, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2))

        goto_map = {0: {"UP": 3, "DOWN": 1},
                    1: {"UP": 0, "DOWN": 2},
                    2: {"UP": 1, "DOWN": 3},
                    3: {"UP": 2, "DOWN": 0}}

        menu = tam_tools.tam_menu.TAMMenu(buttons, "a", goto_map)

        self.assertEqual(menu.get_on(), (0, hit_button))

    def test_get_on_2(self):
        hit_button = tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2)
        buttons = (tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2),
                   hit_button,
                   tam_tools.tam_menu.TAMTextButton("12345678", 3, 8, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2))

        goto_map = {0: {"UP": 3, "DOWN": 1},
                    1: {"UP": 0, "DOWN": 2},
                    2: {"UP": 1, "DOWN": 3},
                    3: {"UP": 2, "DOWN": 0}}

        menu = tam_tools.tam_menu.TAMMenu(buttons, "a", goto_map)
        menu.update((("DOWN", "SPECIAL"),))
        self.assertEqual(menu.get_on(), (1, hit_button))

    def test_get_goto_map(self):
        hit_button = tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2)
        buttons = (tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2),
                   hit_button,
                   tam_tools.tam_menu.TAMTextButton("12345678", 3, 8, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2))

        goto_map = {0: {"UP": 3, "DOWN": 1},
                    1: {"UP": 0, "DOWN": 2},
                    2: {"UP": 1, "DOWN": 3},
                    3: {"UP": 2, "DOWN": 0}}

        menu = tam_tools.tam_menu.TAMMenu(buttons, "a", goto_map)

        self.assertEqual(menu.get_goto_map(), goto_map)

    def test_get_buttons(self):
        buttons = [tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("12345678", 3, 8, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2)]

        goto_map = {0: {"UP": 3, "DOWN": 1},
                    1: {"UP": 0, "DOWN": 2},
                    2: {"UP": 1, "DOWN": 3},
                    3: {"UP": 2, "DOWN": 0}}

        menu = tam_tools.tam_menu.TAMMenu(buttons, "a", goto_map)

        self.assertEqual(menu.get_buttons(), buttons)

    def test_get_buttons_2(self):
        buttons = [tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("12345678", 3, 8, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2)]

        goto_map = {0: {"UP": 2, "DOWN": 1},
                    1: {"UP": 0, "DOWN": 2},
                    2: {"UP": 1, "DOWN": 0}}

        menu = tam_tools.tam_menu.TAMMenu(buttons, "a", goto_map)

        self.assertEqual(menu.get_buttons(), buttons)

    def test_get_buttons_3(self):
        buttons = []

        goto_map = {}

        menu = tam_tools.tam_menu.TAMMenu(buttons, "a", goto_map)

        self.assertEqual(menu.get_buttons(), buttons)

    def test_simple_menu_builder(self):
        buttons = [tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("12345678", 3, 8, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2)]

        menu = tam_tools.tam_menu.TAMMenu.simple_menu_builder(buttons, "a")

        self.assertEqual(menu.get_goto_map(), {0: {"UP": 3, "DOWN": 1},
                                               1: {"UP": 0, "DOWN": 2},
                                               2: {"UP": 1, "DOWN": 3},
                                               3: {"UP": 2, "DOWN": 0}})

    def test_simple_menu_builder_2(self):
        buttons = [tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2)]

        menu = tam_tools.tam_menu.TAMMenu.simple_menu_builder(buttons, "a", up_keys=("U", "C"))
        self.assertEqual(menu.get_goto_map(), {0: {"C": 2, "U": 2, "DOWN": 1},
                                               1: {"C": 0, "U": 0, "DOWN": 2},
                                               2: {"C": 1, "U": 1, "DOWN": 0}})

    def test_simple_menu_builder_3(self):
        buttons = [tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextButton("By", 3, 6, 6, 2, lambda: None, 5, 2),
                   tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2)]

        menu = tam_tools.tam_menu.TAMMenu.simple_menu_builder(buttons, "a", up_keys=("A", "C"), down_keys=("D",), on=1)
        self.assertEqual(menu.get_goto_map(), {0: {"A": 2, "C": 2, "D": 1},
                                               1: {"A": 0, "C": 0, "D": 2},
                                               2: {"A": 1, "C": 1, "D": 0}})

        self.assertEqual(menu.get_on()[0], 1)

    def test_simple_menu_builder_4(self):
        buttons = [tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2)]

        menu = tam_tools.tam_menu.TAMMenu.simple_menu_builder(buttons, "a")

        self.assertEqual(menu.get_goto_map(), {0: {"UP": 0, "DOWN": 0}})

    def test_simple_menu_builder_5(self):
        menu = tam_tools.tam_menu.TAMMenu.simple_menu_builder([], "a")

        self.assertEqual(menu.get_goto_map(), {})

        self.assertEqual(menu.get_on()[0], 0)


class TAMTextButtonTests(unittest.TestCase):
    def test_init_TextButton(self):
        button = tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2)

        self.assertIsInstance(button, tam_tools.tam_menu.TAMTextButton)

    def test_init_TextButton_2(self):
        button = tam_tools.tam_menu.TAMTextButton("Hello\nCats\t123",
                                                  3,
                                                  4,
                                                  6,
                                                  2,
                                                  lambda: None,
                                                  5,
                                                  2,
                                                  on_chars="!@#$%^&*")

        self.assertIsInstance(button, tam_tools.tam_menu.TAMTextButton)

    @staticmethod
    def test_call_TextButton():
        button = tam_tools.tam_menu.TAMTextButton("Hello\nCats\t123",
                                                  3,
                                                  4,
                                                  6,
                                                  2,
                                                  lambda: None,
                                                  5,
                                                  2,
                                                  on_chars="( ")

        button()

    def test_str_TextButton(self):
        button = tam_tools.tam_menu.TAMTextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2)

        self.assertEqual(str(button), "Hello")

    def test_str_TextButton_2(self):
        button = tam_tools.tam_menu.TAMTextButton("Hello\nCats\t123",
                                                  3,
                                                  4,
                                                  6,
                                                  2,
                                                  lambda: None,
                                                  5,
                                                  2,
                                                  on_chars="( ")

        self.assertEqual(str(button), "Hello\nCats\t123")

    @staticmethod
    def test_update():
        button = tam_tools.tam_menu.TAMTextButton("Hello\nCats\t123",
                                                  3,
                                                  4,
                                                  6,
                                                  2,
                                                  lambda: None,
                                                  5,
                                                  2,
                                                  on_chars="!@#$%^&*")

        button.update()

    def test_draw(self):
        button = tam_tools.tam_menu.TAMTextButton("Hello", 0, 0, 6, 2, lambda: None, 5, 2)

        buffer = tam_io.tam_buffer.TAMBuffer(6, 6, " ", 0, 0)

        button.draw(buffer)

        for spot, char in enumerate("Hello"):
            self.assertEqual(buffer.get_spot(spot, 0), (char, 6, 2))

    def test_draw_2(self):
        button = tam_tools.tam_menu.TAMTextButton("Hello\ncats", 0, 0, 6, 2, lambda: None, 5, 2)

        buffer = tam_io.tam_buffer.TAMBuffer(6, 6, " ", 0, 0)

        button.draw(buffer)

        for spot, char in enumerate("Hello"):
            self.assertEqual(buffer.get_spot(spot, 0), (char, 6, 2))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot, 1), (char, 6, 2))

    def test_on(self):
        button = tam_tools.tam_menu.TAMTextButton("Hello 123\ncats", 2, 0, 6, 2, lambda: None, 5, 8)

        buffer = tam_io.tam_buffer.TAMBuffer(15, 6, " ", 0, 0)

        button.off()
        button.on()
        button.draw(buffer)

        for spot, char in enumerate("* Hello 123"):
            self.assertEqual(buffer.get_spot(spot, 0), (char, 5, 8))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot + 2, 1), (char, 5, 8))

    def test_on_2(self):
        button = tam_tools.tam_menu.TAMTextButton("Hello\ncats\nlol",
                                                  8,
                                                  0,
                                                  6,
                                                  2,
                                                  lambda: None,
                                                  5,
                                                  3,
                                                  on_chars="!@#$%^&*")

        buffer = tam_io.tam_buffer.TAMBuffer(15, 6, " ", 0, 0)

        button.off()
        button.on()
        button.draw(buffer)

        for spot, char in enumerate("!@#$%^&*Hello"):
            self.assertEqual(buffer.get_spot(spot, 0), (char, 5, 3))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot + 8, 1), (char, 5, 3))

        for spot, char in enumerate("lol"):
            self.assertEqual(buffer.get_spot(spot + 8, 2), (char, 5, 3))

    def test_off(self):
        button = tam_tools.tam_menu.TAMTextButton("Hello\ncats", 0, 0, 6, 2, lambda: None, 5, 2)

        buffer = tam_io.tam_buffer.TAMBuffer(6, 6, " ", 0, 0)

        button.on()
        button.off()
        button.draw(buffer)

        for spot, char in enumerate("Hello"):
            self.assertEqual(buffer.get_spot(spot, 0), (char, 6, 2))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot, 1), (char, 6, 2))

    def test_off_2(self):
        button = tam_tools.tam_menu.TAMTextButton("Hello 123\nc\tats", 3, 1, 6, 2, lambda: None, 5, 2)

        buffer = tam_io.tam_buffer.TAMBuffer(19, 19, " ", 0, 0)

        button.on()
        button.off()
        button.draw(buffer)

        for spot, char in enumerate("Hello 123"):
            self.assertEqual(buffer.get_spot(spot + 3, 1), (char, 6, 2))

        for spot, char in enumerate("c    ats"):
            self.assertEqual(buffer.get_spot(spot + 3, 2), (char, 6, 2))

    @staticmethod
    def test_run_action():
        button = tam_tools.tam_menu.TAMTextButton("Hello\nCats\t123",
                                                  3,
                                                  4,
                                                  6,
                                                  2,
                                                  lambda: None,
                                                  5,
                                                  2,
                                                  on_chars="( ")

        button.run_action()

    def test_set_action(self):
        def func():
            pass

        button = tam_tools.tam_menu.TAMTextButton("Hello\nCats\t123",
                                                  3,
                                                  4,
                                                  6,
                                                  2,
                                                  lambda: 1 + 90,
                                                  5,
                                                  2,
                                                  on_chars="( ")

        button.set_action(func)
        self.assertIs(button.get_action(), func)

    def test_get_action(self):
        def func():
            pass

        button = tam_tools.tam_menu.TAMTextButton("Hello\nCats\t123",
                                                  4,
                                                  4,
                                                  2,
                                                  3,
                                                  func,
                                                  9,
                                                  0,
                                                  on_chars="&*")

        self.assertIs(button.get_action(), func)

    def test_get_position(self):
        button = tam_tools.tam_menu.TAMTextButton("Hello\ncats", 0, 0, 6, 2, lambda: None, 5, 2)

        self.assertEqual(button.get_position(), (0, 0))

    def test_get_position_2(self):
        button = tam_tools.tam_menu.TAMTextButton("Hello 123\nc\tats", 3, 1, 6, 2, lambda: None, 5, 2)

        self.assertEqual(button.get_position(), (3, 1))

    def test_set_position(self):
        button = tam_tools.tam_menu.TAMTextButton("Hello 123\nc\tats", 3, 1, 6, 2, lambda: None, 5, 2)

        buffer = tam_io.tam_buffer.TAMBuffer(19, 19, " ", 0, 0)

        button.on()
        button.off()
        button.set_position(0, 0)
        button.draw(buffer)

        for spot, char in enumerate("Hello 123"):
            self.assertEqual(buffer.get_spot(spot, 0), (char, 6, 2))

        for spot, char in enumerate("c    ats"):
            self.assertEqual(buffer.get_spot(spot, 1), (char, 6, 2))

    def test_set_position_2(self):
        button = tam_tools.tam_menu.TAMTextButton("Hello\ncats\nlol",
                                                  8,
                                                  0,
                                                  6,
                                                  2,
                                                  lambda: None,
                                                  5,
                                                  3,
                                                  on_chars="!@#$%^&*")

        buffer = tam_io.tam_buffer.TAMBuffer(15, 6, " ", 0, 0)

        button.off()
        button.on()
        button.set_position(9, 1)
        button.draw(buffer)

        for spot, char in enumerate("!@#$%^&*Hello"):
            self.assertEqual(buffer.get_spot(spot + 1, 1), (char, 5, 3))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot + 9, 2), (char, 5, 3))

        for spot, char in enumerate("lol"):
            self.assertEqual(buffer.get_spot(spot + 9, 3), (char, 5, 3))


class TAMTextBoxButtonTests(unittest.TestCase):
    def test_init_TextBoxButton(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 20, 5, "#", 6, 2, lambda: None, 5, 2)
        self.assertIsInstance(button, tam_tools.tam_menu.TAMTextBoxButton)

    def test_init_TextBoxButton_2(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test_2\ncats",
                                                     4,
                                                     11,
                                                     22,
                                                     7,
                                                     ">",
                                                     7,
                                                     3,
                                                     lambda: None,
                                                     4,
                                                     3,
                                                     on_char="$")
        self.assertIsInstance(button, tam_tools.tam_menu.TAMTextBoxButton)

    @staticmethod
    def test_call_TextBoxButton():
        button = tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 20, 5, "#", 6, 2, lambda: None, 5, 2)

        button()

    def test_str_TextBoxButton(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test", 3, 10, 20, 5, "#", 6, 2, lambda: None, 5, 2)

        self.assertEqual(str(button), "test")

    def test_str_TextBoxButton_2(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test_2\ncats",
                                                     4,
                                                     11,
                                                     22,
                                                     7,
                                                     ">",
                                                     7,
                                                     3,
                                                     lambda: None,
                                                     4,
                                                     3,
                                                     on_char="$")

        self.assertEqual(str(button), "test_2\ncats")

    @staticmethod
    def test_update():
        button = tam_tools.tam_menu.TAMTextBoxButton("test_2\ncats",
                                                     4,
                                                     11,
                                                     22,
                                                     7,
                                                     ">",
                                                     7,
                                                     3,
                                                     lambda: None,
                                                     4,
                                                     3,
                                                     on_char="$")

        button.update()

    def test_draw(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test", 0, 0, 10, 5, "#", 6, 2, lambda: None, 5, 2)

        buffer = tam_io.tam_buffer.TAMBuffer(12, 6, " ", 0, 0)

        button.draw(buffer)

        self.assertEqual(buffer.get_spot(0, 0), ("#", 6, 2))
        for spot, char in enumerate("test"):
            self.assertEqual(buffer.get_spot(spot + 2, 2), (char, 6, 2))

    def test_draw_2(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test_2\ncats",
                                                     0,
                                                     0,
                                                     9,
                                                     7,
                                                     ">",
                                                     7,
                                                     3,
                                                     lambda: None,
                                                     4,
                                                     3,
                                                     on_char="$")

        buffer = tam_io.tam_buffer.TAMBuffer(12, 12, " ", 0, 0)

        button.draw(buffer)

        self.assertEqual(buffer.get_spot(0, 0), (">", 7, 3))
        for spot, char in enumerate("test_2"):
            self.assertEqual(buffer.get_spot(spot + 2, 2), (char, 7, 3))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot + 2, 3), (char, 7, 3))

    def test_on(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test", 0, 0, 10, 5, "#", 6, 2, lambda: None, 5, 1)

        buffer = tam_io.tam_buffer.TAMBuffer(12, 6, " ", 0, 0)

        button.off()
        button.on()
        button.draw(buffer)

        self.assertEqual(buffer.get_spot(0, 0), ("/", 5, 1))
        for spot, char in enumerate("test"):
            self.assertEqual(buffer.get_spot(spot + 2, 2), (char, 5, 1))

    def test_on_2(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test_2\ncats",
                                                     0,
                                                     0,
                                                     9,
                                                     7,
                                                     ">",
                                                     7,
                                                     3,
                                                     lambda: None,
                                                     4,
                                                     5,
                                                     on_char="$")

        buffer = tam_io.tam_buffer.TAMBuffer(15, 15, " ", 0, 0)

        button.off()
        button.on()
        button.draw(buffer)

        self.assertEqual(buffer.get_spot(0, 0), ("$", 4, 5))
        for spot, char in enumerate("test_2"):
            self.assertEqual(buffer.get_spot(spot + 2, 2), (char, 4, 5))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot + 2, 3), (char, 4, 5))

    def test_off(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test", 0, 0, 10, 5, "#", 6, 2, lambda: None, 5, 1)

        buffer = tam_io.tam_buffer.TAMBuffer(12, 6, " ", 0, 0)

        button.on()
        button.off()
        button.draw(buffer)

        self.assertEqual(buffer.get_spot(0, 0), ("#", 6, 2))
        for spot, char in enumerate("test"):
            self.assertEqual(buffer.get_spot(spot + 2, 2), (char, 6, 2))

    def test_off_2(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test_2\ncats",
                                                     0,
                                                     0,
                                                     9,
                                                     7,
                                                     ">",
                                                     7,
                                                     3,
                                                     lambda: None,
                                                     4,
                                                     5,
                                                     on_char="$")

        buffer = tam_io.tam_buffer.TAMBuffer(15, 15, " ", 0, 0)

        button.on()
        button.off()
        button.draw(buffer)

        self.assertEqual(buffer.get_spot(0, 0), (">", 7, 3))
        for spot, char in enumerate("test_2"):
            self.assertEqual(buffer.get_spot(spot + 2, 2), (char, 7, 3))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot + 2, 3), (char, 7, 3))

    @staticmethod
    def test_run_action():
        button = tam_tools.tam_menu.TAMTextBoxButton("test_2\ncats",
                                                     0,
                                                     0,
                                                     9,
                                                     7,
                                                     ">",
                                                     7,
                                                     3,
                                                     lambda: None,
                                                     4,
                                                     5,
                                                     on_char="$")

        button.run_action()

    def test_set_action(self):
        def func():
            pass

        button = tam_tools.tam_menu.TAMTextBoxButton("test_2\ncats",
                                                     0,
                                                     0,
                                                     9,
                                                     7,
                                                     ">",
                                                     7,
                                                     3,
                                                     lambda: None,
                                                     4,
                                                     5,
                                                     on_char="$")

        button.set_action(func)
        self.assertIs(button.get_action(), func)

    def test_get_action(self):
        def func():
            pass

        button = tam_tools.tam_menu.TAMTextBoxButton("test_2\ncats",
                                                     0,
                                                     0,
                                                     9,
                                                     7,
                                                     ">",
                                                     7,
                                                     3,
                                                     func,
                                                     4,
                                                     5,
                                                     on_char="$")

        self.assertIs(button.get_action(), func)

    def test_get_position(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test_2\ncats",
                                                     0,
                                                     0,
                                                     9,
                                                     7,
                                                     ">",
                                                     7,
                                                     3,
                                                     lambda: None,
                                                     4,
                                                     5,
                                                     on_char="$")

        self.assertEqual(button.get_position(), (0, 0))

    def test_get_position_2(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test_2\ncats",
                                                     3,
                                                     1,
                                                     9,
                                                     7,
                                                     ">",
                                                     7,
                                                     3,
                                                     lambda: None,
                                                     4,
                                                     5,
                                                     on_char="$")

        self.assertEqual(button.get_position(), (3, 1))

    def test_set_position(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test_2\ncats",
                                                     0,
                                                     0,
                                                     9,
                                                     7,
                                                     ">",
                                                     7,
                                                     3,
                                                     lambda: None,
                                                     4,
                                                     5,
                                                     on_char="$")

        buffer = tam_io.tam_buffer.TAMBuffer(15, 15, " ", 0, 0)

        button.on()
        button.off()
        button.set_position(2, 3)
        button.draw(buffer)

        self.assertEqual(buffer.get_spot(2, 3), (">", 7, 3))
        for spot, char in enumerate("test_2"):
            self.assertEqual(buffer.get_spot(spot + 4, 5), (char, 7, 3))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot + 4, 6), (char, 7, 3))

    def test_set_position_2(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test_2\ncats",
                                                     0,
                                                     0,
                                                     9,
                                                     7,
                                                     ">",
                                                     7,
                                                     3,
                                                     lambda: None,
                                                     4,
                                                     5,
                                                     on_char="$")

        buffer = tam_io.tam_buffer.TAMBuffer(15, 15, " ", 0, 0)

        button.off()
        button.on()
        button.set_position(4, 6)
        button.draw(buffer)

        self.assertEqual(buffer.get_spot(4, 6), ("$", 4, 5))
        for spot, char in enumerate("test_2"):
            self.assertEqual(buffer.get_spot(spot + 6, 8), (char, 4, 5))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot + 6, 9), (char, 4, 5))
