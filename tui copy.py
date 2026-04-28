import threading
import time
import window

def draw(objects):
    layers = []
    for obj in objects:
        layers.append(obj.draw())
    win.draw(manage_layers(layers))


def render_screen(a):
    

def run(objects):
    win = window.CursesDrawer()

    # curses futtatása külön threadben
    t = threading.Thread(target=win.start, daemon=True)
    t.start()

    # fő loop a modulban
    running = True
    while running:
        key = win.get_key()
        if key is not None:
            screen = render_screen(objects)
            win.draw(f"Key: {key}")

            if key == 27:  # ESC
                running = False
                win.stop()

        # itt lehet más logika
        time.sleep(0.05)

# ha scriptként futtatod:
if __name__ == "__main__":
    run([])
