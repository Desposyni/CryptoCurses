#! /usr/local/bin/python3

import curses
from CryptoQuote.CryptoQuote import *


def main(screen):
    curses.use_default_colors()
    screen.refresh()
    menu = curses.newwin(1, 60, 0, 0)
    puzzle = curses.newwin(26, 80, 1, 0)

    def draw_menu():
        menu.addstr(0, 0, '  [N]ew Quote  |  [O]pen  |  [A]nswer  |  [Q]uit  ', curses.A_STANDOUT)
        menu.refresh()

    def draw_puzzle(page, quote, author):
        puzzle.clear()

        # draw_menu()

        words = []
        y, x = puzzle.getmaxyx()
        wrap = x if x < 80 else 80
        line = 4
        for word in quote.split():
            if len(' '.join(words)) + len(word) < wrap:
                words.append(word)
            else:
                puzzle.addstr(line, 0, ' '.join(words))
                line += 3
                words = [word]
        else:
            puzzle.addstr(line, 0, ' '.join(words))
            line += 3
            puzzle.addstr(line, 0, ' ' * ((wrap if wrap < len(quote) else len(quote)) - len(author)))
            puzzle.addstr(author, curses.A_BOLD)
            line += 2

            curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
            puzzle.attron(curses.color_pair(1))
            puzzle.addstr(line, 0, f'http://www.quotationspage.com/quote/{page}.html', curses.A_UNDERLINE)
            puzzle.attroff(curses.color_pair(1))
        puzzle.refresh()

    def draw_answer(quote, author):
        words = []
        y, x = puzzle.getmaxyx()
        wrap = x if x < 80 else 80
        line = 3
        for word in quote.split():
            if len(' '.join(words)) + len(word) < wrap:
                words.append(word)
            else:
                puzzle.addstr(line, 0, ' '.join(words))
                line += 3
                words = [word]
        else:
            puzzle.addstr(line, 0, ' '.join(words))
            line += 3
            puzzle.addstr(line, 0, ' ' * ((wrap if wrap < len(quote) else len(quote)) - len(author)))
            puzzle.addstr(author, curses.A_BOLD)
        puzzle.refresh()

    # how to print the cipher wrapped for curses
    # for i, e in enumerate(sorted(cipher.items())):
    #     k, v = e
    #     puzzle.addstr(i // 13 + 4, i * 4 % (13 * 4), f'{k}:{v}')

    draw_menu()
    puzzle.addstr(0, 0, "Welcome to CryptoQuote!")
    puzzle.addstr(2, 0, "Press 'N' to get a random quote")
    puzzle.addstr(3, 0, "          quote number will be displayed in a URL")
    puzzle.addstr(4, 0, "Press 'O' to attempt to open a specific quote number")
    puzzle.addstr(5, 0, "          If the quote number doesn't exist,")
    puzzle.addstr(6, 0, "          a random quote will be chosen instead")
    puzzle.addstr(7, 0, "Press 'A' to reveal the answer")
    puzzle.addstr(8, 0, "Press 'Q' to exit the game")
    puzzle.addstr(10, 0, "go to https://github.com/Desposyni/CryptoCurses")
    puzzle.addstr(11, 0, "      for source code and to submit issues")
    menu.refresh()
    puzzle.refresh()

    cipher = {}
    page = 0
    quote = ''
    author = ''

    while (key := puzzle.getkey()) not in ('q', 'Q'):
        if key in ('o', 'O'):
            puzzle.addstr(1, 0, "Enter a number between 1 - 42500: ")
            puzzle.refresh()
            curses.echo()
            try:
                page = int(puzzle.getstr(5))
            except ValueError:
                puzzle.clear()
                draw_menu()
                puzzle.addstr(2, 0, "Invalid Input")
                puzzle.refresh()
                quote = ''
            else:
                puzzle.addstr(f'Trying to open page {page}')
                puzzle.refresh()
                curses.napms(1000)
                key = 'n'
            finally:
                curses.noecho()

        if key in ('n', 'N'):
            cipher = get_cipher()
            page, quote, author = get_quote(page)
            e_quote, e_author = map(lambda p: encipher(cipher, p), (quote, author))
            draw_puzzle(page, e_quote, e_author)
            page = 0
        elif key in ('a', 'A') and quote:
            draw_answer(quote, author)
            page = 0
        puzzle.addstr(0, 0, f'You Pressed {key}')
        puzzle.refresh()


curses.wrapper(main)
