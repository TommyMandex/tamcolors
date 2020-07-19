# built in libraries
import unittest
import unittest.mock

# tamcolors libraries
from tamcolors import tam
from tamcolors import tam_tools


"""
tests that checks tam_tools library
"""


class TAMPrintTest(unittest.TestCase):
    def test_tam_print(self):
        buffer = tam.tam_buffer.TAMBuffer(6, 5, "@", 1, 2)
        tam_tools.tam_print.tam_print(buffer, 0, 1, "Test", 3, 4)
        self.assertEqual(buffer.get_spot(0, 1), ("T", 3, 4))
        self.assertEqual(buffer.get_spot(1, 1), ("e", 3, 4))
        self.assertEqual(buffer.get_spot(2, 1), ("s", 3, 4))
        self.assertEqual(buffer.get_spot(3, 1), ("t", 3, 4))
        self.assertEqual(buffer.get_spot(4, 1), ("@", 1, 2))

    def test_tam_print_2(self):
        buffer = tam.tam_buffer.TAMBuffer(7, 5, "@", 1, 2)
        buffer.set_spot(3, 1, "E", 8, 9)
        tam_tools.tam_print.tam_print(buffer, 2, 1, "Test", 3, -1)
        self.assertEqual(buffer.get_spot(2, 1), ("T", 3, 2))
        self.assertEqual(buffer.get_spot(3, 1), ("e", 3, 9))
        self.assertEqual(buffer.get_spot(4, 1), ("s", 3, 2))
        self.assertEqual(buffer.get_spot(5, 1), ("t", 3, 2))
        self.assertEqual(buffer.get_spot(6, 1), ("@", 1, 2))

    def test_tam_print_3(self):
        buffer = tam.tam_buffer.TAMBuffer(7, 5, "@", 1, 2)
        buffer.set_spot(3, 1, "E", 8, 9)
        tam_tools.tam_print.tam_print(buffer, 2, 1, "Test\n\tcat", 3, -1)
        self.assertEqual(buffer.get_spot(2, 1), ("T", 3, 2))
        self.assertEqual(buffer.get_spot(3, 1), ("e", 3, 9))
        self.assertEqual(buffer.get_spot(4, 1), ("s", 3, 2))
        self.assertEqual(buffer.get_spot(5, 1), ("t", 3, 2))
        self.assertEqual(buffer.get_spot(6, 1), ("@", 1, 2))
        self.assertEqual(buffer.get_spot(2, 2), (" ", 3, 2))
        self.assertEqual(buffer.get_spot(3, 2), (" ", 3, 2))
        self.assertEqual(buffer.get_spot(4, 2), (" ", 3, 2))
        self.assertEqual(buffer.get_spot(5, 2), (" ", 3, 2))
        self.assertEqual(buffer.get_spot(6, 2), ("c", 3, 2))
        self.assertEqual(buffer.get_spot(7, 2), None)

    def test_tam_print_4(self):
        buffer = tam.tam_buffer.TAMBuffer(7, 5, "@", 1, 2)
        buffer.set_spot(3, 1, "E", 8, 9)
        tam_tools.tam_print.tam_print(buffer, 2, 1, "Test\n\r\tcat", 3, -1)
        self.assertEqual(buffer.get_spot(2, 1), ("T", 3, 2))
        self.assertEqual(buffer.get_spot(3, 1), ("e", 3, 9))
        self.assertEqual(buffer.get_spot(4, 1), ("s", 3, 2))
        self.assertEqual(buffer.get_spot(5, 1), ("t", 3, 2))
        self.assertEqual(buffer.get_spot(6, 1), ("@", 1, 2))
        self.assertEqual(buffer.get_spot(2, 2), (" ", 3, 2))
        self.assertEqual(buffer.get_spot(3, 2), (" ", 3, 2))
        self.assertEqual(buffer.get_spot(4, 2), (" ", 3, 2))
        self.assertEqual(buffer.get_spot(5, 2), (" ", 3, 2))
        self.assertEqual(buffer.get_spot(6, 2), ("c", 3, 2))
        self.assertEqual(buffer.get_spot(7, 2), None)

    def test_tam_print_5(self):
        buffer = tam.tam_buffer.TAMBuffer(7, 5, "@", 1, 2)
        buffer.set_spot(3, 1, "E", 8, 9)
        self.assertRaises(tam_tools.tam_str.TAMStrError,
                          tam_tools.tam_print.tam_print,
                          buffer,
                          2,
                          1,
                          "Test\n\r\tcat",
                          3,
                          -1,
                          error_bad_char=True)


class TAMFilmTest(unittest.TestCase):
    def test_init_film(self):
        film = tam_tools.tam_film.TAMFilm([tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6),
                                           tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)],
                                          circular=True)

        self.assertTrue(film.get_circular())

    def test_setitem(self):
        film = tam_tools.tam_film.TAMFilm([tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6),
                                           tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)],
                                          circular=False)

        tam_buffer = tam.tam_buffer.TAMBuffer(5, 6, "T", 9, 1)
        film[1] = tam_buffer

        self.assertIs(film[1], tam_buffer)

    def test_setitem_2(self):
        film = tam_tools.tam_film.TAMFilm([tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6),
                                           tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)],
                                          circular=False)

        self.assertRaises(tam_tools.tam_film.TAMFilmError,
                          film.__setitem__,
                          "key",
                          tam.tam_buffer.TAMBuffer(8, 5, "B", 1, 9))

    def test_setitem_3(self):
        film = tam_tools.tam_film.TAMFilm([tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6),
                                           tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)],
                                          circular=False)

        self.assertRaises(tam_tools.tam_film.TAMFilmError,
                          film.__setitem__,
                          -1,
                          tam.tam_buffer.TAMBuffer(8, 5, "B", 1, 9))

    def test_getitem(self):
        tam_buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6)
        tam_buffer_2 = tam.tam_buffer.TAMBuffer(4, 5, "B", 4, 3)
        tam_buffer_3 = tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)
        film = tam_tools.tam_film.TAMFilm((tam_buffer, tam_buffer_2, tam_buffer_3), circular=False)

        self.assertIs(film[0], tam_buffer)
        self.assertIs(film[1], tam_buffer_2)
        self.assertIs(film[2], tam_buffer_3)

    def test_getitem_2(self):
        tam_buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6)
        tam_buffer_2 = tam.tam_buffer.TAMBuffer(4, 5, "B", 4, 3)
        film = tam_tools.tam_film.TAMFilm((tam_buffer, tam_buffer_2), circular=False)

        self.assertIs(film[0], tam_buffer)
        self.assertIs(film[1], tam_buffer_2)

        self.assertRaises(tam_tools.tam_film.TAMFilmError, film.__getitem__, "id")

    def test_getitem_3(self):
        tam_buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6)
        tam_buffer_2 = tam.tam_buffer.TAMBuffer(4, 5, "B", 4, 3)
        film = tam_tools.tam_film.TAMFilm((tam_buffer, tam_buffer_2), circular=False)

        self.assertIs(film[0], tam_buffer)
        self.assertIs(film[1], tam_buffer_2)

        self.assertRaises(tam_tools.tam_film.TAMFilmError, film.__getitem__, 2)

    def test_next(self):
        tam_buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6)
        tam_buffer_2 = tam.tam_buffer.TAMBuffer(4, 5, "B", 4, 3)
        tam_buffer_3 = tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)

        film = tam_tools.tam_film.TAMFilm((tam_buffer, tam_buffer_2, tam_buffer_3), circular=False)

        self.assertIs(tam_buffer, next(film))
        self.assertIs(tam_buffer_2, next(film))
        self.assertIs(tam_buffer_3, next(film))
        self.assertIs(tam_buffer_3, next(film))

    def test_next_2(self):
        tam_buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6)
        tam_buffer_2 = tam.tam_buffer.TAMBuffer(4, 5, "B", 4, 3)
        tam_buffer_3 = tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)

        film = tam_tools.tam_film.TAMFilm((tam_buffer, tam_buffer_2, tam_buffer_3), circular=True)

        self.assertIs(tam_buffer, next(film))
        self.assertIs(tam_buffer_2, next(film))
        self.assertIs(tam_buffer_3, next(film))
        self.assertIs(tam_buffer, next(film))

    def test_len(self):
        film = tam_tools.tam_film.TAMFilm([], circular=True)

        self.assertEqual(len(film), 0)

    def test_len_2(self):
        film = tam_tools.tam_film.TAMFilm([tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6),
                                           tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)],
                                          circular=False)

        self.assertEqual(len(film), 2)

    def test_set(self):
        film = tam_tools.tam_film.TAMFilm([tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6),
                                           tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)],
                                          circular=False)

        tam_buffer = tam.tam_buffer.TAMBuffer(5, 6, "T", 9, 1)
        film.set(1, tam_buffer)

        self.assertIs(film.get(1), tam_buffer)

    def test_set_2(self):
        film = tam_tools.tam_film.TAMFilm([tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6),
                                           tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)],
                                          circular=False)

        self.assertRaises(tam_tools.tam_film.TAMFilmError,
                          film.set,
                          "key",
                          tam.tam_buffer.TAMBuffer(8, 5, "B", 1, 9))

    def test_set_3(self):
        film = tam_tools.tam_film.TAMFilm([tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6),
                                           tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)],
                                          circular=False)

        self.assertRaises(tam_tools.tam_film.TAMFilmError,
                          film.set,
                          -1,
                          tam.tam_buffer.TAMBuffer(8, 5, "B", 1, 9))

    def test_get(self):
        tam_buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6)
        tam_buffer_2 = tam.tam_buffer.TAMBuffer(4, 5, "B", 4, 3)
        tam_buffer_3 = tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)
        film = tam_tools.tam_film.TAMFilm((tam_buffer, tam_buffer_2, tam_buffer_3), circular=False)

        self.assertIs(film.get(0), tam_buffer)
        self.assertIs(film.get(1), tam_buffer_2)
        self.assertIs(film.get(2), tam_buffer_3)

    def test_get_2(self):
        tam_buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6)
        tam_buffer_2 = tam.tam_buffer.TAMBuffer(4, 5, "B", 4, 3)
        film = tam_tools.tam_film.TAMFilm((tam_buffer, tam_buffer_2), circular=False)

        self.assertIs(film.get(0), tam_buffer)
        self.assertIs(film.get(1), tam_buffer_2)

        self.assertRaises(tam_tools.tam_film.TAMFilmError, film.get, "id")

    def test_get_3(self):
        tam_buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6)
        tam_buffer_2 = tam.tam_buffer.TAMBuffer(4, 5, "B", 4, 3)
        film = tam_tools.tam_film.TAMFilm((tam_buffer, tam_buffer_2), circular=False)

        self.assertIs(film.get(0), tam_buffer)
        self.assertIs(film.get(1), tam_buffer_2)

        self.assertRaises(tam_tools.tam_film.TAMFilmError, film.get, 2)

    def test_slide(self):
        tam_buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6)
        tam_buffer_2 = tam.tam_buffer.TAMBuffer(4, 5, "B", 4, 3)
        tam_buffer_3 = tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)

        film = tam_tools.tam_film.TAMFilm((tam_buffer, tam_buffer_2, tam_buffer_3), circular=False)

        self.assertIs(tam_buffer, film.slide())
        self.assertIs(tam_buffer_2, film.slide())
        self.assertIs(tam_buffer_3, film.slide())
        self.assertIs(tam_buffer_3, film.slide())

    def test_slide_2(self):
        tam_buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6)
        tam_buffer_2 = tam.tam_buffer.TAMBuffer(4, 5, "B", 4, 3)
        tam_buffer_3 = tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)

        film = tam_tools.tam_film.TAMFilm((tam_buffer, tam_buffer_2, tam_buffer_3), circular=True)

        self.assertIs(tam_buffer, film.slide())
        self.assertIs(tam_buffer_2, film.slide())
        self.assertIs(tam_buffer_3, film.slide())
        self.assertIs(tam_buffer, film.slide())

    def test_peak(self):
        tam_buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6)
        tam_buffer_2 = tam.tam_buffer.TAMBuffer(4, 5, "B", 4, 3)
        tam_buffer_3 = tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)

        film = tam_tools.tam_film.TAMFilm((tam_buffer, tam_buffer_2, tam_buffer_3), circular=False)

        self.assertIs(tam_buffer, film.peak())
        self.assertIs(tam_buffer, film.peak())
        self.assertIs(tam_buffer, film.slide())

        self.assertIs(tam_buffer_2, film.peak())
        self.assertIs(tam_buffer_2, film.peak())
        self.assertIs(tam_buffer_2, film.slide())

        self.assertIs(tam_buffer_3, film.peak())
        self.assertIs(tam_buffer_3, film.peak())
        self.assertIs(tam_buffer_3, film.slide())

        self.assertIs(tam_buffer_3, film.peak())
        self.assertIs(tam_buffer_3, film.peak())
        self.assertIs(tam_buffer_3, film.slide())

    def test_peak_2(self):
        tam_buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6)
        tam_buffer_2 = tam.tam_buffer.TAMBuffer(4, 5, "B", 4, 3)
        tam_buffer_3 = tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)

        film = tam_tools.tam_film.TAMFilm((tam_buffer, tam_buffer_2, tam_buffer_3), circular=True)

        self.assertIs(tam_buffer, film.peak())
        self.assertIs(tam_buffer, film.peak())
        self.assertIs(tam_buffer, film.slide())

        self.assertIs(tam_buffer_2, film.peak())
        self.assertIs(tam_buffer_2, film.peak())
        self.assertIs(tam_buffer_2, film.slide())

        self.assertIs(tam_buffer_3, film.peak())
        self.assertIs(tam_buffer_3, film.peak())
        self.assertIs(tam_buffer_3, film.slide())

        self.assertIs(tam_buffer, film.peak())
        self.assertIs(tam_buffer, film.peak())
        self.assertIs(tam_buffer, film.slide())

    def test_peak_3(self):
        film = tam_tools.tam_film.TAMFilm((), circular=True)
        self.assertIs(None, film.peak())

    def test_append(self):
        film = tam_tools.tam_film.TAMFilm([tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6),
                                           tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)],
                                          circular=False)

        self.assertEqual(len(film), 2)
        film.append(tam.tam_buffer.TAMBuffer(3, 2, "Q", 6, 7))
        self.assertEqual(len(film), 3)

        film.append(tam.tam_buffer.TAMBuffer(3, 2, "P", 6, 7))
        self.assertEqual(len(film), 4)

    def test_pop(self):
        tam_buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6)
        tam_buffer_2 = tam.tam_buffer.TAMBuffer(4, 5, "B", 4, 3)
        tam_buffer_3 = tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)

        film = tam_tools.tam_film.TAMFilm((tam_buffer, tam_buffer_2, tam_buffer_3), circular=True)

        self.assertIs(film.pop(), tam_buffer_3)
        self.assertIs(film.pop(), tam_buffer_2)
        self.assertIs(film.pop(), tam_buffer)
        self.assertIs(film.pop(), None)

    def test_get_circular(self):
        film = tam_tools.tam_film.TAMFilm([tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6),
                                           tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)],
                                          circular=False)

        self.assertFalse(film.get_circular())

    def test_get_circular_2(self):
        film = tam_tools.tam_film.TAMFilm([tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6),
                                           tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)],
                                          circular=True)

        self.assertTrue(film.get_circular())

    def test_set_circular(self):
        film = tam_tools.tam_film.TAMFilm([tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6),
                                           tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)],
                                          circular=True)

        film.set_circular(False)
        self.assertFalse(film.get_circular())

    def test_done(self):
        film = tam_tools.tam_film.TAMFilm([tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6),
                                           tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)],
                                          circular=False)

        self.assertFalse(film.done())

    def test_done_2(self):
        tam_buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 5, 6)
        tam_buffer_2 = tam.tam_buffer.TAMBuffer(4, 5, "B", 4, 3)
        tam_buffer_3 = tam.tam_buffer.TAMBuffer(4, 5, "C", 4, 3)

        film = tam_tools.tam_film.TAMFilm((tam_buffer, tam_buffer_2, tam_buffer_3), circular=False)

        self.assertFalse(film.done())
        self.assertIs(tam_buffer, next(film))
        self.assertFalse(film.done())
        self.assertIs(tam_buffer_2, next(film))
        self.assertFalse(film.done())
        self.assertIs(tam_buffer_3, next(film))
        self.assertTrue(film.done())
        self.assertIs(tam_buffer_3, next(film))

    def test_done_3(self):
        film = tam_tools.tam_film.TAMFilm((), circular=False)

        self.assertTrue(film.done())
        self.assertRaises(StopIteration, next, film)


class TAMColorPaletteTest(unittest.TestCase):
    def test_init_color_palette(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        self.assertIsInstance(color_palette, tam_tools.tam_color_palette.TAMColorPalette)

    def test_init_color_palette_2(self):
        rules = {6: tam_tools.tam_color_palette.TAMDefaultColor(5),
                 7: tam_tools.tam_color_palette.TAMCycleColor((1, 2), 5)}
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 5), rules)
        self.assertIsInstance(color_palette, tam_tools.tam_color_palette.TAMColorPalette)

    def test_str(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        self.assertEqual(str(color_palette), str({key: key for key in range(1, 25)}))

    def test_str_2(self):
        rules = {6: tam_tools.tam_color_palette.TAMDefaultColor(6),
                 7: tam_tools.tam_color_palette.TAMCycleColor((7, 2), 5)}
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 6), rules)
        color_palette.update()
        self.assertEqual(str(color_palette), str({key: key for key in range(1, 8)}))

    def test_getitem(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        self.assertEqual(color_palette[15], 15)

    def test_getitem_2(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        self.assertEqual(color_palette[20], 20)

    def test_getitem_3(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        self.assertRaises(tam_tools.tam_color_palette.TAMColorPaletteError, color_palette.__getitem__, -1)

    def test_setitem(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        color_palette[11] = 3
        self.assertEqual(color_palette[11], 3)

    def test_setitem_2(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        color_palette[12] = 4
        self.assertEqual(color_palette[12], 4)

    def test_setitem_3(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        self.assertRaises(tam_tools.tam_color_palette.TAMColorPaletteError, color_palette.__setitem__, {}, 45)

    def test_get_color(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        self.assertEqual(color_palette.get_color(15), 15)

    def test_get_color_2(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        self.assertEqual(color_palette.get_color(20), 20)

    def test_get_color_3(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        self.assertRaises(tam_tools.tam_color_palette.TAMColorPaletteError, color_palette.get_color, -1)

    def test_set_color(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        color_palette.set_color(11, 3)
        self.assertEqual(color_palette.get_color(11), 3)

    def test_set_color_2(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        color_palette.set_color(12, 4)
        self.assertEqual(color_palette.get_color(12), 4)

    def test_set_color_3(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        self.assertRaises(tam_tools.tam_color_palette.TAMColorPaletteError, color_palette.set_color, {}, 45)

    def test_key_present(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        self.assertTrue(color_palette.key_present(4))

    def test_key_present_2(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 25))
        self.assertFalse(color_palette.key_present(-123))

    def test_update(self):
        rules = {6: tam_tools.tam_color_palette.TAMDefaultColor(5),
                 7: tam_tools.tam_color_palette.TAMCycleColor((1, 2), 1)}
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(range(1, 10), rules)
        for key in range(1, 10):
            self.assertEqual(color_palette[key], key)
        color_palette.update()
        self.assertEqual(color_palette[6], 5)
        self.assertEqual(color_palette[7], 1)

    def test_set_rule(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette()
        rule = tam_tools.tam_color_palette.TAMDefaultColor(66)
        color_palette.set_rule(5, rule)
        color_palette.update()
        self.assertEqual(color_palette[5], 66)

    def test_set_rule_2(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette()
        rule = tam_tools.tam_color_palette.TAMDefaultColor(66)
        self.assertRaises(tam_tools.tam_color_palette.TAMColorPaletteError, color_palette.set_rule, {}, rule)

    def test_get_rule(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette()
        rule = tam_tools.tam_color_palette.TAMDefaultColor(66)
        color_palette.set_rule(5, rule)
        self.assertIs(color_palette.get_rule(5), rule)

    def test_get_rule_2(self):
        color_palette = tam_tools.tam_color_palette.TAMColorPalette()
        self.assertIs(color_palette.get_rule(5), None)


class TAMDefaultColorTest(unittest.TestCase):
    def test_init_default_color(self):
        default_color = tam_tools.tam_color_palette.TAMDefaultColor(45)
        self.assertIsInstance(default_color, tam_tools.tam_color_palette.TAMColorPaletteRule)
        self.assertIsInstance(default_color, tam_tools.tam_color_palette.TAMDefaultColor)

    def test_get_color(self):
        default_color = tam_tools.tam_color_palette.TAMDefaultColor(45)
        self.assertEqual(default_color.get_color(), 45)

    def test_set_color(self):
        default_color = tam_tools.tam_color_palette.TAMDefaultColor(45)
        default_color.set_color(23)
        self.assertEqual(default_color.get_color(), 23)

    def test_update(self):
        default_color = tam_tools.tam_color_palette.TAMDefaultColor(45)
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(color_rules={12: default_color})
        color_palette.update()
        self.assertEqual(color_palette[12], 45)


class TAMCycleColor(unittest.TestCase):
    def test_init_cycle_color(self):
        cycle_color = tam_tools.tam_color_palette.TAMCycleColor((1, 2, 3, 4), clock=1)
        self.assertIsInstance(cycle_color, tam_tools.tam_color_palette.TAMColorPaletteRule)
        self.assertIsInstance(cycle_color, tam_tools.tam_color_palette.TAMCycleColor)

    def test_set_colors(self):
        cycle_color = tam_tools.tam_color_palette.TAMCycleColor((4, 3, 2, 1), clock=1)
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(color_rules={4: cycle_color})
        color_palette.update()
        self.assertEqual(color_palette[4], 4)
        cycle_color.set_colors((1, 2, 3, 4))
        color_palette.update()
        self.assertEqual(color_palette[1], 1)

    def test_get_clock(self):
        cycle_color = tam_tools.tam_color_palette.TAMCycleColor((1, 4), clock=2)
        self.assertEqual(cycle_color.get_clock(), 2)

    def test_set_clock(self):
        cycle_color = tam_tools.tam_color_palette.TAMCycleColor((1, 4), clock=2)
        cycle_color.set_clock(45)
        self.assertEqual(cycle_color.get_clock(), 45)

    def test_update(self):
        cycle_color = tam_tools.tam_color_palette.TAMCycleColor((1, 2, 3, 4), clock=1)
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(color_rules={4: cycle_color})
        for color in (1, 2, 3, 4, 1, 2, 3, 4):
            color_palette.update()
            self.assertEqual(color_palette[4], color)

    def test_update_2(self):
        cycle_color = tam_tools.tam_color_palette.TAMCycleColor((1, 4), clock=2)
        color_palette = tam_tools.tam_color_palette.TAMColorPalette(color_rules={4: cycle_color})
        for color in (1, 1, 4, 4, 1, 1, 4):
            color_palette.update()
            self.assertEqual(color_palette[4], color)


class TAMKeyManagerTest(unittest.TestCase):
    def test_init_key_manger(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()
        self.assertIsInstance(key_manger, tam_tools.tam_key_manager.TAMKeyManager)

    def test_iter(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()
        key_manger.update((("a", "NORMAL"), ("B", "NORMAL")))
        count = None
        for count, key in enumerate(key_manger):
            self.assertIsInstance(key, tuple)
        self.assertEqual(count, 1)

    def test_update(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()
        key_manger.update((("a", "NORMAL"), ("B", "NORMAL")))

        self.assertEqual(key_manger.get_raw_user_input(), (("a", "NORMAL"), ("B", "NORMAL")))

    def test_update_2(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()
        key_manger.update((("!", "NORMAL"),))

        self.assertEqual(key_manger.get_raw_user_input(), (("!", "NORMAL"),))

    def test_get_key_state(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()
        self.assertFalse(key_manger.get_key_state("A"))

    def test_get_key_state_2(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()
        key_manger.update((("a", "NORMAL"), ("B", "NORMAL")))

        self.assertFalse(key_manger.get_key_state("A"))
        self.assertTrue(key_manger.get_key_state("a"))
        self.assertTrue(key_manger.get_key_state("B"))

    def test_silent_key_state(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()

        self.assertFalse(key_manger.silent_key_state("A"))
        self.assertFalse(key_manger.silent_key_state("A"))

    def test_silent_key_state_2(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()
        key_manger.update((("a", "NORMAL"), ("B", "NORMAL")))

        self.assertTrue(key_manger.silent_key_state("B"))
        self.assertFalse(key_manger.silent_key_state("B"))

    def test_silent_key_state_3(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()
        key_manger.update((("A", "NORMAL"), ("C", "NORMAL")))

        self.assertTrue(key_manger.silent_key_state("C"))
        self.assertFalse(key_manger.silent_key_state("C"))
        self.assertTrue(key_manger.silent_key_state("A"))
        self.assertFalse(key_manger.silent_key_state("A"))
        self.assertFalse(key_manger.silent_key_state("B"))
        self.assertFalse(key_manger.silent_key_state("B"))

        key_manger.update((("a", "NORMAL"), ("B", "NORMAL")))

        self.assertTrue(key_manger.silent_key_state("B"))
        self.assertFalse(key_manger.silent_key_state("B"))

    def test_get_user_input(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()

        self.assertIs(key_manger.get_user_input(), None)
        self.assertIs(key_manger.get_user_input(), None)

    def test_get_user_input_2(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()
        key_manger.update((("A", "NORMAL"), ("C", "NORMAL")))

        self.assertEqual(key_manger.get_user_input(), ("A", "NORMAL"))
        self.assertEqual(key_manger.get_user_input(), ("C", "NORMAL"))
        self.assertIs(key_manger.get_user_input(), None)

    def test_get_user_input_3(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()
        key_manger.update((("X", "NORMAL"),))

        self.assertEqual(key_manger.get_user_input(), ("X", "NORMAL"))
        self.assertIs(key_manger.get_user_input(), None)

        key_manger.update((("A", "NORMAL"), ("C", "NORMAL")))

        self.assertEqual(key_manger.get_user_input(), ("A", "NORMAL"))
        self.assertEqual(key_manger.get_user_input(), ("C", "NORMAL"))
        self.assertIs(key_manger.get_user_input(), None)

    def test_get_raw_user_input(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()

        self.assertEqual(list(key_manger.get_raw_user_input()), [])

    def get_raw_user_input_2(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()
        key_manger.update((("A", "NORMAL"), ("C", "NORMAL")))

        self.assertEqual(list(key_manger.get_raw_user_input()), [("A", "NORMAL"), ("C", "NORMAL")])

    def get_raw_user_input_3(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()
        key_manger.update((("A", "NORMAL"), ("C", "NORMAL")))

        self.assertEqual(list(key_manger.get_raw_user_input()), [("A", "NORMAL"), ("C", "NORMAL")])

        key_manger.update((("4", "NORMAL"), ("1", "NORMAL")))
        self.assertEqual(list(key_manger.get_raw_user_input()), [("4", "NORMAL"), ("1", "NORMAL")])

    def test_get_user_input_generator(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()

        key_generator = key_manger.get_user_input_generator()
        self.assertRaises(StopIteration, next, key_generator)

    def test_get_user_input_generator_2(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()

        key_generator = key_manger.get_user_input_generator()
        self.assertRaises(StopIteration, next, key_generator)

        key_manger.update((("A", "NORMAL"), ("C", "NORMAL")))

        key_generator = key_manger.get_user_input_generator()
        self.assertEqual(next(key_generator), ("A", "NORMAL"))
        self.assertEqual(next(key_generator), ("C", "NORMAL"))
        self.assertRaises(StopIteration, next, key_generator)

    def test_get_user_input_generator_3(self):
        key_manger = tam_tools.tam_key_manager.TAMKeyManager()

        key_generator = key_manger.get_user_input_generator()
        self.assertRaises(StopIteration, next, key_generator)

        key_manger.update((("B", "NORMAL"), ("C", "NORMAL")))

        key_generator = key_manger.get_user_input_generator()
        self.assertEqual(next(key_generator), ("B", "NORMAL"))
        self.assertEqual(next(key_generator), ("C", "NORMAL"))
        self.assertRaises(StopIteration, next, key_generator)

        key_manger.update((("B", "NORMAL"), ("C", "NORMAL"), ("5", "NORMAL")))

        key_generator = key_manger.get_user_input_generator()
        self.assertEqual(next(key_generator), ("B", "NORMAL"))
        self.assertEqual(next(key_generator), ("C", "NORMAL"))
        self.assertEqual(next(key_generator), ("5", "NORMAL"))
        self.assertRaises(StopIteration, next, key_generator)


class MakeTAMStrTest(unittest.TestCase):
    def test_make_tam_str(self):
        tam_str = tam_tools.tam_str.make_tam_str("test\t123")
        self.assertEqual(tam_str, "test    123")

    def test_make_tam_str_2(self):
        tam_str = tam_tools.tam_str.make_tam_str("test\t12\n3")
        self.assertEqual(tam_str, "test    12\n3")

    def test_make_tam_str_3(self):
        self.assertRaises(tam_tools.tam_str.TAMStrError, tam_tools.tam_str.make_tam_str, "123\r123")

    def test_make_tam_str_4(self):
        tam_str = tam_tools.tam_str.make_tam_str("test\r12\n3", bad_char="%^&")
        self.assertEqual(tam_str, "test%^&12\n3")

    def test_make_tam_str_5(self):
        tam_str = tam_tools.tam_str.make_tam_str("\r\\\n\ng\n", end_line="45", bad_char="@")
        self.assertEqual(tam_str, "@\\4545g45")


class TAMTextBoxTest(unittest.TestCase):
    def test_tam_text_box_init(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertIsInstance(text_box, tam_tools.tam_text_box.TAMTextBox)

    def test_tam_text_box_str(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertEqual(str(text_box), "hello world!")

    def test_tam_text_box_str_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("cat world!\n123", 20, 34, "#", 3, 5)
        self.assertEqual(str(text_box), "cat world!\n123")

    def test_update(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("", 20, 15, "#", 3, 5)

        buffer = tam.tam_buffer.TAMBuffer(20, 15, " ", 3, 5)
        buffer2 = tam.tam_buffer.TAMBuffer(20, 15, "@", 1, 2)
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)

        for i in range(20):
            buffer.set_spot(i, 0, "#", 3, 5)
            buffer.set_spot(i, 14, "#", 3, 5)

        for i in range(1, 15):
            buffer.set_spot(0, i, "#", 3, 5)
            buffer.set_spot(19, i, "#", 3, 5)

        text_box.update()
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)

    def test_draw(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 15, "#", 3, 5)
        buffer = tam.tam_buffer.TAMBuffer(20, 15, " ", 3, 5)
        buffer2 = tam.tam_buffer.TAMBuffer(20, 15, "@", 1, 2)
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)

        for i in range(20):
            buffer.set_spot(i, 0, "#", 3, 5)
            buffer.set_spot(i, 14, "#", 3, 5)

        for i in range(1, 15):
            buffer.set_spot(0, i, "#", 3, 5)
            buffer.set_spot(19, i, "#", 3, 5)

        for spot, char in enumerate("hello world!"):
            buffer.set_spot(2 + spot, 7, char, 3, 5)

        text_box.update()
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)

    def test_draw_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 15, "#", 3, 5, clock=1)
        buffer = tam.tam_buffer.TAMBuffer(20, 15, " ", 3, 5)
        buffer2 = tam.tam_buffer.TAMBuffer(20, 15, "@", 1, 2)
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)

        for i in range(20):
            buffer.set_spot(i, 0, "#", 3, 5)
            buffer.set_spot(i, 14, "#", 3, 5)

        for i in range(1, 15):
            buffer.set_spot(0, i, "#", 3, 5)
            buffer.set_spot(19, i, "#", 3, 5)

        text_box.update()
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)
        for spot, char in enumerate("hello world!"):
            buffer.set_spot(2 + spot, 7, char, 3, 5)
            text_box.update()
            text_box.draw(buffer2)
            self.assertEqual(buffer, buffer2)

        text_box.update()
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)

    def test_draw_3(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!\ncats\n1\n\nhi",
                                                     19,
                                                     16,
                                                     "#",
                                                     1,
                                                     2,
                                                     center_vertical=False,
                                                     center_horizontal=True,
                                                     vertical_space=2,
                                                     vertical_start=3,
                                                     char_background="%")

        buffer = tam.tam_buffer.TAMBuffer(19, 16, "%", 1, 2)
        buffer2 = tam.tam_buffer.TAMBuffer(19, 16, "@", 3, 4)

        for i in range(19):
            buffer.set_spot(i, 0, "#", 1, 2)
            buffer.set_spot(i, 15, "#", 1, 2)

        for i in range(1, 16):
            buffer.set_spot(0, i, "#", 1, 2)
            buffer.set_spot(18, i, "#", 1, 2)

        for spot, char in enumerate("hello world!"):
            buffer.set_spot(3 + spot, 3, char, 1, 2)

        for spot, char in enumerate("cats"):
            buffer.set_spot(7 + spot, 5, char, 1, 2)

        buffer.set_spot(9, 7, "1", 1, 2)

        for spot, char in enumerate("hi"):
            buffer.set_spot(8 + spot, 11, char, 1, 2)

        text_box.update()
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)

    def test_done(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertFalse(text_box.done())
        text_box.update()
        self.assertTrue(text_box.done())

    def test_done_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5, clock=1)
        for _ in range(14):
            self.assertFalse(text_box.done())
            text_box.update()
        self.assertTrue(text_box.done())

    def test_set_colors(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertFalse(text_box.done())
        text_box.update()
        self.assertTrue(text_box.done())
        text_box.set_colors(4, 6)
        self.assertTrue(text_box.done())

    def test_set_colors_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5, clock=1)
        for _ in range(14):
            self.assertFalse(text_box.done())
            text_box.update()

        self.assertTrue(text_box.done())
        text_box.set_colors(4, 6)
        self.assertTrue(text_box.done())

    def test_set_colors_3(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5, clock=1)
        for _ in range(13):
            self.assertFalse(text_box.done())
            text_box.update()

        self.assertFalse(text_box.done())
        text_box.set_colors(4, 6)
        self.assertFalse(text_box.done())

    def test_get_colors(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertEqual(text_box.get_colors(), (3, 5))

    def test_get_colors_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 6, 1)
        self.assertEqual(text_box.get_colors(), (6, 1))

    def test_set_char(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "^", 3, 5)
        text_box.set_char("#")
        self.assertEqual(text_box.get_char(), "#")

    def test_set_char_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "@", 6, 1)
        text_box.set_char("$")
        self.assertEqual(text_box.get_char(), "$")

    def test_get_char(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertEqual(text_box.get_char(), "#")

    def test_get_char_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "!", 6, 1)
        self.assertEqual(text_box.get_char(), "!")

    def test_get_text(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertEqual(text_box.get_text(), "hello world!")

    def test_get_text_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("cat world!\n123", 20, 34, "#", 3, 5)
        self.assertEqual(text_box.get_text(), "cat world!\n123")

    def test_get_dimensions(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertEqual(text_box.get_dimensions(), (20, 34))

    def test_get_dimensions_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 4, 3, "#", 3, 5)
        self.assertEqual(text_box.get_dimensions(), (4, 3))


class TAMPlacingTest(unittest.TestCase):
    def test__get_center(self):
        self.assertEqual(tam_tools.tam_placing._get_center(9, 3), 8)

    def test__get_center_2(self):
        self.assertEqual(tam_tools.tam_placing._get_center(90, 33), 74)

    def test__get_other_side(self):
        self.assertEqual(tam_tools.tam_placing._get_other_side(9, 3), 7)

    def test__get_other_side_2(self):
        self.assertEqual(tam_tools.tam_placing._get_other_side(90, 33), 58)

    def test__get_dimensions_wrapper(self):
        @tam_tools.tam_placing._get_dimensions
        def func(x, y, w, h):
            return x, y, w, h
        self.assertEqual(func(1, 2, 3, 4), (1, 2, 3, 4))

    def test__get_dimensions_wrapper_2(self):
        @tam_tools.tam_placing._get_dimensions
        def func(x, y, w, h):
            return x, y, w, h
        self.assertEqual(func(1, 2, None, None, tam.tam_buffer.TAMBuffer(3, 4, "c", 8, 9)), (1, 2, 3, 4))

    def test__get_dimensions_wrapper_3(self):
        @tam_tools.tam_placing._get_dimensions
        def func(x, y, w, h):
            return x, y, w, h
        self.assertEqual(func(1, 2, 12, 15, tam.tam_buffer.TAMBuffer(30, 40, "c", 8, 9)), (1, 2, 30, 40))

    def test_top_left(self):
        self.assertEqual(tam_tools.tam_placing.top_left(1, 2, 3, 4), (1, 2))

    def test_top_left_2(self):
        self.assertEqual(tam_tools.tam_placing.top_left(11, 23, 13, 24), (11, 23))

    def test_top_right(self):
        self.assertEqual(tam_tools.tam_placing.top_right(1, 2, 3, 4), (-1, 2))

    def test_top_right_2(self):
        self.assertEqual(tam_tools.tam_placing.top_right(11, 23, 15, 24), (-3, 23))

    def test_bottom_left(self):
        self.assertEqual(tam_tools.tam_placing.bottom_left(1, 2, 3, 4), (1, -1))

    def test_bottom_left_2(self):
        self.assertEqual(tam_tools.tam_placing.bottom_left(11, 23, 15, 24), (11, 0))

    def test_bottom_right(self):
        self.assertEqual(tam_tools.tam_placing.bottom_right(1, 2, 3, 4), (-1, -1))

    def test_bottom_right_2(self):
        self.assertEqual(tam_tools.tam_placing.bottom_right(11, 23, 15, 24), (-3, 0))

    def test_center(self):
        self.assertEqual(tam_tools.tam_placing.center(1, 2, 3, 4), (0, 0))

    def test_center_2(self):
        self.assertEqual(tam_tools.tam_placing.center(11, 23, 15, 24), (4, 11))


class TAMFilmFadeInTest(unittest.TestCase):
    def test_tam_fade_in(self):
        buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 1, 2)
        buffer2 = tam.tam_buffer.TAMBuffer(4, 5, "&", 3, 7)
        film = tam_tools.tam_fade.tam_fade_in(buffer, "&", 3, 7)

        self.assertEqual(len(film), 24)
        self.assertEqual(buffer2, film[0])
        self.assertEqual(buffer, film[23])

    def test_tam_fade_in_2(self):
        buffer = tam.tam_buffer.TAMBuffer(4, 5, "A", 1, 2)
        buffer2 = tam.tam_buffer.TAMBuffer(4, 5, "&", 3, 7)
        film = tam_tools.tam_fade.tam_fade_in(buffer, "&", 3, 7, reverse=True)

        self.assertEqual(len(film), 24)
        self.assertEqual(buffer, film[0])
        self.assertEqual(buffer2, film[23])

    def test_tam_fade_in_3(self):
        buffer = tam.tam_buffer.TAMBuffer(2, 3, "A", 1, 2)
        buffer.set_spot(1, 1, "B", 6, 9)
        buffer2 = tam.tam_buffer.TAMBuffer(2, 3, "&", 3, 7)
        film = tam_tools.tam_fade.tam_fade_in(buffer, "&", 3, 7)

        self.assertEqual(len(film), 10)
        self.assertEqual(buffer2, film[0])
        self.assertEqual(buffer, film[9])

    def test_tam_fade_in_4(self):
        buffer = tam.tam_buffer.TAMBuffer(2, 3, "A", 1, 2)
        buffer.set_spot(1, 1, "B", 6, 9)
        buffer2 = tam.tam_buffer.TAMBuffer(2, 3, "&", 3, 7)
        film = tam_tools.tam_fade.tam_fade_in(buffer, "&", 3, 7, rand=[True])

        self.assertEqual(len(film), 9)
        self.assertEqual(buffer2, film[0])
        self.assertEqual(buffer, film[8])


class TAMMenuTest(unittest.TestCase):
    def test_tammenu(self):
        self.assertIsInstance(tam_tools.tam_menu.TAMMenu([], "a", {}), tam_tools.tam_menu.TAMMenu)

    def test_tammenu_2(self):
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
                buffer = tam.tam_buffer.TAMBuffer(0, 0, " ", 1, 2)
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
                   tam_tools.tam_menu.TMATextBoxButton("test", 3, 10, 12, 5, "#", 6, 2, lambda: None, 5, 2))

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


class TMATextButtonTest(unittest.TestCase):
    def test_init_TextButton(self):
        button = tam_tools.tam_menu.TMATextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2)

        self.assertIsInstance(button, tam_tools.tam_menu.TMATextButton)

    def test_init_TextButton_2(self):
        button = tam_tools.tam_menu.TMATextButton("Hello\nCats\t123",
                                                  3,
                                                  4,
                                                  6,
                                                  2,
                                                  lambda: None,
                                                  5,
                                                  2,
                                                  on_chars="!@#$%^&*")

        self.assertIsInstance(button, tam_tools.tam_menu.TMATextButton)

    @staticmethod
    def test_call_TextButton():
        button = tam_tools.tam_menu.TMATextButton("Hello\nCats\t123",
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
        button = tam_tools.tam_menu.TMATextButton("Hello", 3, 4, 6, 2, lambda: None, 5, 2)

        self.assertEqual(str(button), "Hello")

    def test_str_TextButton_2(self):
        button = tam_tools.tam_menu.TMATextButton("Hello\nCats\t123",
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
        button = tam_tools.tam_menu.TMATextButton("Hello\nCats\t123",
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
        button = tam_tools.tam_menu.TMATextButton("Hello", 0, 0, 6, 2, lambda: None, 5, 2)

        buffer = tam.tam_buffer.TAMBuffer(6, 6, " ", 0, 0)

        button.draw(buffer)

        for spot, char in enumerate("Hello"):
            self.assertEqual(buffer.get_spot(spot, 0), (char, 6, 2))

    def test_draw_2(self):
        button = tam_tools.tam_menu.TMATextButton("Hello\ncats", 0, 0, 6, 2, lambda: None, 5, 2)

        buffer = tam.tam_buffer.TAMBuffer(6, 6, " ", 0, 0)

        button.draw(buffer)

        for spot, char in enumerate("Hello"):
            self.assertEqual(buffer.get_spot(spot, 0), (char, 6, 2))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot, 1), (char, 6, 2))

    def test_on(self):
        button = tam_tools.tam_menu.TMATextButton("Hello 123\ncats", 2, 0, 6, 2, lambda: None, 5, 8)

        buffer = tam.tam_buffer.TAMBuffer(15, 6, " ", 0, 0)

        button.off()
        button.on()
        button.draw(buffer)

        for spot, char in enumerate("* Hello 123"):
            self.assertEqual(buffer.get_spot(spot, 0), (char, 5, 8))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot + 2, 1), (char, 5, 8))

    def test_on_2(self):
        button = tam_tools.tam_menu.TMATextButton("Hello\ncats\nlol",
                                                  8,
                                                  0,
                                                  6,
                                                  2,
                                                  lambda: None,
                                                  5,
                                                  3,
                                                  on_chars="!@#$%^&*")

        buffer = tam.tam_buffer.TAMBuffer(15, 6, " ", 0, 0)

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
        button = tam_tools.tam_menu.TMATextButton("Hello\ncats", 0, 0, 6, 2, lambda: None, 5, 2)

        buffer = tam.tam_buffer.TAMBuffer(6, 6, " ", 0, 0)

        button.on()
        button.off()
        button.draw(buffer)

        for spot, char in enumerate("Hello"):
            self.assertEqual(buffer.get_spot(spot, 0), (char, 6, 2))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot, 1), (char, 6, 2))

    def test_off_2(self):
        button = tam_tools.tam_menu.TMATextButton("Hello 123\nc\tats", 3, 1, 6, 2, lambda: None, 5, 2)

        buffer = tam.tam_buffer.TAMBuffer(19, 19, " ", 0, 0)

        button.on()
        button.off()
        button.draw(buffer)

        for spot, char in enumerate("Hello 123"):
            self.assertEqual(buffer.get_spot(spot + 3, 1), (char, 6, 2))

        for spot, char in enumerate("c    ats"):
            self.assertEqual(buffer.get_spot(spot + 3, 2), (char, 6, 2))

    @staticmethod
    def test_run_action():
        button = tam_tools.tam_menu.TMATextButton("Hello\nCats\t123",
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

        button = tam_tools.tam_menu.TMATextButton("Hello\nCats\t123",
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

        button = tam_tools.tam_menu.TMATextButton("Hello\nCats\t123",
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
        button = tam_tools.tam_menu.TMATextButton("Hello\ncats", 0, 0, 6, 2, lambda: None, 5, 2)

        self.assertEqual(button.get_position(), (0, 0))

    def test_get_position_2(self):
        button = tam_tools.tam_menu.TMATextButton("Hello 123\nc\tats", 3, 1, 6, 2, lambda: None, 5, 2)

        self.assertEqual(button.get_position(), (3, 1))

    def test_set_position(self):
        button = tam_tools.tam_menu.TMATextButton("Hello 123\nc\tats", 3, 1, 6, 2, lambda: None, 5, 2)

        buffer = tam.tam_buffer.TAMBuffer(19, 19, " ", 0, 0)

        button.on()
        button.off()
        button.set_position(0, 0)
        button.draw(buffer)

        for spot, char in enumerate("Hello 123"):
            self.assertEqual(buffer.get_spot(spot, 0), (char, 6, 2))

        for spot, char in enumerate("c    ats"):
            self.assertEqual(buffer.get_spot(spot, 1), (char, 6, 2))

    def test_set_position_2(self):
        button = tam_tools.tam_menu.TMATextButton("Hello\ncats\nlol",
                                                  8,
                                                  0,
                                                  6,
                                                  2,
                                                  lambda: None,
                                                  5,
                                                  3,
                                                  on_chars="!@#$%^&*")

        buffer = tam.tam_buffer.TAMBuffer(15, 6, " ", 0, 0)

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


class TMATextBoxButtonTest(unittest.TestCase):
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

        buffer = tam.tam_buffer.TAMBuffer(12, 6, " ", 0, 0)

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

        buffer = tam.tam_buffer.TAMBuffer(12, 12, " ", 0, 0)

        button.draw(buffer)

        self.assertEqual(buffer.get_spot(0, 0), (">", 7, 3))
        for spot, char in enumerate("test_2"):
            self.assertEqual(buffer.get_spot(spot + 2, 2), (char, 7, 3))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot + 2, 3), (char, 7, 3))

    def test_on(self):
        button = tam_tools.tam_menu.TAMTextBoxButton("test", 0, 0, 10, 5, "#", 6, 2, lambda: None, 5, 1)

        buffer = tam.tam_buffer.TAMBuffer(12, 6, " ", 0, 0)

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

        buffer = tam.tam_buffer.TAMBuffer(15, 15, " ", 0, 0)

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

        buffer = tam.tam_buffer.TAMBuffer(12, 6, " ", 0, 0)

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

        buffer = tam.tam_buffer.TAMBuffer(15, 15, " ", 0, 0)

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

        buffer = tam.tam_buffer.TAMBuffer(15, 15, " ", 0, 0)

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

        buffer = tam.tam_buffer.TAMBuffer(15, 15, " ", 0, 0)

        button.off()
        button.on()
        button.set_position(4, 6)
        button.draw(buffer)

        self.assertEqual(buffer.get_spot(4, 6), ("$", 4, 5))
        for spot, char in enumerate("test_2"):
            self.assertEqual(buffer.get_spot(spot + 6, 8), (char, 4, 5))

        for spot, char in enumerate("cats"):
            self.assertEqual(buffer.get_spot(spot + 6, 9), (char, 4, 5))


class TMAListBufferTest(unittest.TestCase):
    def test_tma_list_buffer(self):
        buffer = [["1", "2", "3"],
                  ["4", "5", "6"]]

        tma_buffer = tam.tam_buffer.TAMBuffer(3, 2, " ", 1, 2)
        for i in range(3):
            tma_buffer.set_spot(i, 0, str(i + 1), 1, 2)
            tma_buffer.set_spot(i, 1, str(i + 4), 1, 2)

        ret_tma_buffer = tam_tools.tam_list_buffer.tam_list_buffer(buffer, 1, 2)

        self.assertEqual(ret_tma_buffer, tma_buffer)

    def test_tma_list_buffer_2(self):
        buffer = [["1", "2", "3"],
                  ["4", "5", "6"],
                  ["1", "2", "3"]]

        tma_buffer = tam.tam_buffer.TAMBuffer(3, 3, " ", 1, 2)
        for i in range(3):
            tma_buffer.set_spot(i, 0, str(i + 1), 1, 2)
            tma_buffer.set_spot(i, 1, str(i + 4), 1, 2)
            tma_buffer.set_spot(i, 2, str(i + 1), 1, 2)

        ret_tma_buffer = tam_tools.tam_list_buffer.tam_list_buffer(buffer, 1, 2)

        self.assertEqual(ret_tma_buffer, tma_buffer)

    def test_tma_list_buffer_3(self):
        buffer = [["1", "2", "3"],
                  ["4", "5", "6"]]

        foreground_colors = [[1, 2, 3],
                             [4, 5, 6]]

        tma_buffer = tam.tam_buffer.TAMBuffer(3, 2, " ", 1, 2)
        for i in range(3):
            tma_buffer.set_spot(i, 0, str(i + 1), i + 1, 2)
            tma_buffer.set_spot(i, 1, str(i + 4), i + 4, 2)

        ret_tma_buffer = tam_tools.tam_list_buffer.tam_list_buffer(buffer, foreground_colors, 2)

        self.assertEqual(ret_tma_buffer, tma_buffer)

    def test_tma_list_buffer_4(self):
        buffer = [["1", "2", "3"],
                  ["4", "5", "6"]]

        background_colors = [[1, 2, 3],
                             [4, 5, 6]]

        tma_buffer = tam.tam_buffer.TAMBuffer(3, 2, " ", 1, 2)
        for i in range(3):
            tma_buffer.set_spot(i, 0, str(i + 1), 1, i + 1)
            tma_buffer.set_spot(i, 1, str(i + 4), 1, i + 4)

        ret_tma_buffer = tam_tools.tam_list_buffer.tam_list_buffer(buffer, 1, background_colors)

        self.assertEqual(ret_tma_buffer, tma_buffer)

    def test_tma_list_buffer_5(self):
        buffer = [["1", "2", "3"],
                  ["4", "5", "6"]]

        foreground_colors = [[2, 4, 6],
                             [8, 10, 12]]

        background_colors = [[1, 2, 3],
                             [4, 5, 6]]

        tma_buffer = tam.tam_buffer.TAMBuffer(3, 2, " ", 1, 2)
        for i in range(3):
            tma_buffer.set_spot(i, 0, str(i + 1), (i + 1) * 2, i + 1)
            tma_buffer.set_spot(i, 1, str(i + 4), (i + 4) * 2, i + 4)

        ret_tma_buffer = tam_tools.tam_list_buffer.tam_list_buffer(buffer, foreground_colors, background_colors)

        self.assertEqual(ret_tma_buffer, tma_buffer)
