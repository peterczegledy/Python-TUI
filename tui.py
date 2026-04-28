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
        borderstyle: The style of the border: 1 single / 2 double
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
            for j in range(self.sizesy[y]):
                for i in range(self.boxesx):
                    output +=(BORDERS[self.borderstyle][1]+(" "*self.sizesx[i]))
                output+=BORDERS[self.borderstyle][1]+"\n"
            
        output+=BORDERS[self.borderstyle][4]
        for i in range(self.boxesx-1):
            output +=((BORDERS[self.borderstyle][0]*self.sizesx[i])+BORDERS[self.borderstyle][9])
        output+=BORDERS[self.borderstyle][0]*(self.sizesx[x])+BORDERS[self.borderstyle][5]+"\n"

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

    # curses futtatása külön threadben
    t = threading.Thread(target=win.start, daemon=True)
    t.start()

    # fő loop a modulban
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

            layers = []
            for obj in objects:
                layers.append(obj.draw())
            win.draw(manage_layers(layers))

            if key == 27:  # ESC
                running = False
                win.stop()

        # itt lehet más logika
        time.sleep(0.05)

# ha scriptként futtatod:
if __name__ == "__main__":
    run([])
