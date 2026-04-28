import threading
import time
import window

BORDERS = {
    "SINGLELIGHT": "─│┌┐└┘├┤┬┴┼",
    "SINGLEHEAVY": "━┃┏┓┗┛┣┫┳┻╋",
    "DOUBLE": "═║╔╗╚╝╠╣╦╩╬",
    "DOUBLEH": "═│╒╕╘╛╞╡╤╧╪",
    "DOUBLEV": "─║╓╖╙╜╟╢╥╨╫",
    "ROUNDED": "─│╭╮╰╯├┤┬┴┼",
    "TRIPLEDASHLIGHT": "┄┆┌┐└┘├┤┬┴┼",
}

class AdvancedWindow:
    def __init__(self, titles:list, sizesx:list[int], sizesy:list[int], borderstyle: str):
        """
            Border styles: \n
            SINGLELIGHT: ─│┌┐└┘├┤┬┴┼\n
            SINGLEHEAVY: ━┃┏┓┗┛┣┫┳┻╋\n
            DOUBLE: ═║╔╗╚╝╠╣╦╩╬\n
            DOUBLEH: ═│╒╕╘╛╞╡╤╧╪\n
            DOUBLEV: ─║╓╖╙╜╟╢╥╨╫\n
            ROUNDED: ─│╭╮╰╯├┤┬┴┼\n
            TRIPLEDASHLIGHT: ┄┆┌┐└┘├┤┬┴┼\n
        """
        self.titles = titles
        self.sizesx = sizesx
        self.sizesy = sizesy
        self.boxesx = len(sizesx)
        self.boxesy = len(sizesy)
        self.borderstyle = borderstyle

    def draw(self):
        for y in range(self.boxesy):
            if y == 0:output = BORDERS[self.borderstyle][2]
            if y != 0:output+=BORDERS[self.borderstyle][6]
            
            for x in range(self.boxesx):
                if y == 0:
                    if x!=self.boxesx-1:
                        output+=self.titles[y][x]+BORDERS[self.borderstyle][0]*(self.sizesx[x]-len(self.titles[y][x]))+BORDERS[self.borderstyle][8]
                    else:
                        output+=self.titles[y][x]+BORDERS[self.borderstyle][0]*(self.sizesx[x]-len(self.titles[y][x]))+BORDERS[self.borderstyle][3]+"\n"
                elif y!=0:
                    if x!=self.boxesx-1:
                        output+=self.titles[y][x]+BORDERS[self.borderstyle][0]*(self.sizesx[x]-len(self.titles[y][x]))+BORDERS[self.borderstyle][10]
                    else:
                        output+=self.titles[y][x]+BORDERS[self.borderstyle][0]*(self.sizesx[x]-len(self.titles[y][x]))+BORDERS[self.borderstyle][7]+"\n"
            for _ in range(self.sizesy[y]):
                for i in range(self.boxesx):
                    output +=(BORDERS[self.borderstyle][1]+(" "*self.sizesx[i]))
                output+=BORDERS[self.borderstyle][1]+"\n"
            
        output+=BORDERS[self.borderstyle][4]
        for i in range(self.boxesx-1):
            output +=((BORDERS[self.borderstyle][0]*self.sizesx[i])+BORDERS[self.borderstyle][9])
        output+=BORDERS[self.borderstyle][0]*(self.sizesx[x])+BORDERS[self.borderstyle][5]+"\n"

        return output

class Label:
    def __init__(self, text: str, posx: int, posy: int):
        self.text = text
        self.posx = posx
        self.posy = posy

    def draw(self):
        output = ""
        for i in range(self.posy - 1):
            output += ("¤" * (len(self.text)+self.posx-1)) + "\n"
        output += ("¤" * (self.posx - 1)) + self.text+ "\n"
        return output

class Textbox:
    def __init__(self, id: int, width: int, posx: int, posy: int, ispassword:bool):
        self.id = id
        self.width = width
        self.text = ""
        self.posx = posx
        self.posy = posy
        self.active = False
        self.ispassword = ispassword

    def keypress(self, key):
        if len(self.text) < self.width:
            if len(str(key)[1:-1]) == 1:
                self.text += str(key)[1:-1]
            elif (str(key)) == "Key.space":
                self.text += " "
        if (str(key)) == "Key.backspace":
            self.text = self.text[:-1]

    def draw(self):
        output = ""
        if self.ispassword:text = (len(self.text)*"*") + "_" * (self.width - len(self.text))   
        else:text = self.text + "_" * (self.width - len(self.text))
        for i in range(self.posy - 1):
            output += ("¤" * (len(text)+self.posx-1)) + "\n"
        if self.active:
            output += ("¤" * (self.posx - 1))+text+"*"+"\n"
        else:
            output += ("¤" * (self.posx - 1))+text+"\n"
        return output

def render_screen(a):
    pass

def str_to_matrix(text: str) -> list[list[str]]:
    return [list(line) for line in text.splitlines()]

def matrix_to_str(matrix: list[list[str]]) -> str:
    return '\n'.join(''.join(row) for row in matrix)

def manage_layers(layers: list[str]) -> str:
    base = layers[0]
    base_matrix = str_to_matrix(base)
    height = len(base_matrix)
    width = max(len(row) for row in base_matrix)

    for row in base_matrix:
        while len(row) < width:
            row.append("¤")

    for layer in layers[1:]:
        layer_matrix = str_to_matrix(layer)
        for y in range(height):
            for x in range(width):
                if y < len(layer_matrix) and x < len(layer_matrix[y]):
                    if layer_matrix[y][x] != "¤":
                        base_matrix[y][x] = layer_matrix[y][x]

    return matrix_to_str(base_matrix)

def run(objects):
    index = 0
    win = window.CursesDrawer()


    t = threading.Thread(target=win.start, daemon=True)
    t.start()


    running = True
    while running:
        key = win.get_key()
        if key is not None:
            #win.draw(f"Key: {key}")
            if key == 258:
                index += 1

            if key == 259:
                if index - 1 >= 0:
                    index -= 1

            for obj in objects:
                if isinstance(obj, (Textbox)):#, Button, Checkbox, Listbox, Table, Slider, MultilineTextbox))
                    obj.active = False
                    if obj.id == index:
                        obj.active = True

            if 32 <= key <= 126:
                char = chr(key)
                for obj in objects:
                    if isinstance(obj, Textbox) and obj.active:
                        obj.keypress(char)
                        print(char)



            # draw
            layers = []
            for obj in objects:
                layers.append(obj.draw())
            win.draw(manage_layers(layers))

            if key == 27:  # ESC
                running = False
                win.stop()

        time.sleep(0.05)

if __name__ == "__main__":
    run([])
