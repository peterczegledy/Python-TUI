import curses
import queue
import time

class CursesDrawer:
    def __init__(self):
        self.stdscr = None
        self.draw_queue = queue.Queue()
        self.key_queue = queue.Queue()
        self.running = True

    def start(self):
        curses.wrapper(self._main)

    def _main(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)
        self.stdscr.nodelay(True)
        self.stdscr.keypad(True)
        self.loop()

    def stop(self):
        self.running = False

    def draw(self, text):
        self.draw_queue.put(str(text))

    def get_key(self):
        """FŐ PROGRAM HÍVJA"""
        try:
            return self.key_queue.get_nowait()
        except queue.Empty:
            return None

    def loop(self):
        while self.running:
            key = self.stdscr.getch()
            if key != -1:
                self.key_queue.put(key)

                if key == 27:
                    self.stop()

            if not self.draw_queue.empty():
                text = self.draw_queue.get()
                self.stdscr.clear()
                self.stdscr.addstr(0, 0, text)
                self.stdscr.refresh()

            time.sleep(0.05)
