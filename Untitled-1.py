import curses
from curses import wrapper
def star_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "welcome to the game ")
    stdscr.refresh()
    stdscr.getkey()


def wpm_test(stdscr):
    target_text="hello its me practcing on python programming"
    current_text=[]

    while True:
        stdscr.clear()
        stdscr.addstr(target_text)
        for char in current_text:
            if current_text.index(char) == target_text.ind
            stdscr.addstr(char, curses.color_pair(1))
        stdscr.refresh()

        key = stdscr.getkey()
        if ord(key) == 27:
            break
        elif key in ("KEY_BACKSPACE",'\b',"\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)
        print(current_text)


def main(stdscr):
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.refresh()
    #stdscr.getkey()
    star_screen(stdscr)
    wpm_test(stdscr)


wrapper(main)