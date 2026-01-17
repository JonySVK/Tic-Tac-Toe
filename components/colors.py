class Colors:
    def __init__(self):
        self.colors = [
            ("Red",    (255, 0, 0)),
            ("Green",  (0, 255, 0)),
            ("Blue",   (0, 0, 255)),
            ("Yellow", (200, 180, 0)),
            ("Purple", (110, 0, 140)),
            ("Orange", (220, 120, 0)),
            ("Pink",   (200, 120, 150)),
            ("Brown",  (120, 60, 30)),
            ("Gray",   (90, 90, 90)),
            ("Black",  (0, 0, 0)),
            ("White",  (255, 255, 255))
        ]

        self.hover_colors = self.hover_colors = [
            ("Red",    (255, 100, 100)),
            ("Green",  (100, 255, 100)),
            ("Blue",   (100, 100, 255)),
            ("Yellow", (255, 220, 50)),
            ("Purple", (170, 50, 200)),
            ("Orange", (255, 180, 50)),
            ("Pink",   (255, 170, 200)),
            ("Brown",  (180, 120, 80)),
            ("Gray",   (140, 140, 140)),
        ]


    def get_color_code(self, name):
        for color in self.colors:
            if color[0] == name:
                return color[1]
    
    def get_color_list(self, without=[], default=None):
        colors_list = []
        for color in self.colors:
            if color[0] not in without:
                colors_list.append(color)
        if default is not None:
            for i, color in enumerate(colors_list):
                if color[0] == default:
                    colors_list.insert(0, colors_list.pop(i))
                    break
        return colors_list

    def get_hover_color_code(self, name=None, code=None):
        if name is not None:
            for color in self.hover_colors:
                if color[0] == name:
                    return color[1]
        elif code is not None:
            for color in self.colors:
                if color[1] == code:
                    name = color[0]
            for color in self.hover_colors:
                if color[0] == name:
                    return color[1]
