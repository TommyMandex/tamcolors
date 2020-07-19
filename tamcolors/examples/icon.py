from tamcolors import tam, tam_tools


def get_icon():
    c = "c"
    n = "4"
    s = " "

    icon_chars = ((c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, s, s, s, s, s, s, s, s, n, n, n, n, n, n, n, n, s, s, s, s, s, s, s, s, s, s, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, s, s, s, s, s, s, s, n, n, n, n, n, n, n, n, s, s, s, s, s, s, s, s, s, s, s, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, s, s, s, s, s, s, n, n, n, n, n, n, n, n, s, s, s, s, s, s, s, s, s, s, s, s, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, s, s, s, s, s, n, n, n, n, n, n, n, n, s, s, s, s, s, s, s, s, s, s, s, s, s, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, s, s, s, s, n, n, n, n, n, n, n, n, s, s, s, s, s, s, s, s, s, s, s, s, s, s, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, s, s, s, n, n, n, n, n, n, n, n, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, s, s, n, n, n, n, n, n, n, n, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, s, n, n, n, n, n, n, n, n, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, n, n, n, n, n, n, n, n, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, s, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, n, n, n, n, n, n, n),
                  (c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, n, n, n, n, n, n, n))

    char_to_color = {c: 3, n: 4, s: 6}
    icon_background = []
    for row in icon_chars:
        new_row = []
        for item in row:
            new_row.append(char_to_color[item])

        icon_background.append(new_row)

    return tam_tools.tma_list_buffer.tma_list_buffer(icon_chars, 0, icon_background)


class BootLogo:
    def __init__(self):
        """
        info: Makes a BootLogo Object. Will display the logo and author's name
        """
        self.icon = tam_tools.tma_fade.tma_fade_in(get_icon(),
                                                   " ",
                                                   0,
                                                   0)
        self.wait = 10

    def update(self, tma_loop, keys, loop_data):

        if not self.icon.done():
            self.icon.slide()
        else:
            self.wait -= 1

        if self.wait == 0:
            tma_loop.done()

    def draw(self, tma_buffer, loop_data):
        tma_buffer.clear()

        tma_buffer.draw_onto(self.icon.peak(),
                             *tam_tools.tma_placing.center(35, 15, buffer=self.icon.peak()))

        tam_tools.tma_print.tma_print(tma_buffer, *tam_tools.tma_placing.center(35, 28, len("tamcolors"), 1),
                                      "tamcolors",
                                      15,
                                      0)

    def done(self, tma_loop, loop_data):
        pass

    @staticmethod
    def get_frame():
        return tam.tma_loop.TMAFrame(BootLogo(),
                                     10,
                                     " ",
                                     2,
                                     0,
                                     70, 70, 40, 40)


def run():
    loop = tam.tma_loop.TMALoop(BootLogo.get_frame())
    loop.run()
