#! /usr/bin/python3

import curses
from CryptoQuote.CryptoQuote import *


def main(screen):
    curses.use_default_colors()

    def draw_menu():
        screen.addstr(0, 0, '  [N]ew Quote  |  [O]pen  |  [A]nswer  |  [Q]uit  ', curses.A_STANDOUT)
        screen.refresh()

    def draw_puzzle(page, quote, author):
        screen.clear()
        draw_menu()

        words = []
        y, x = screen.getmaxyx()
        wrap = x if x < 80 else 80
        line = 4
        for word in quote.split():
            if len(' '.join(words)) + len(word) < wrap:
                words.append(word)
            else:
                screen.addstr(line, 0, ' '.join(words))
                line += 3
                words = [word]
        else:
            screen.addstr(line, 0, ' '.join(words))
            line += 3
            screen.addstr(line, 0, ' ' * ((wrap if wrap < len(quote) else len(quote)) - len(author)))
            screen.addstr(author, curses.A_BOLD)
            line += 2

            curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
            screen.attron(curses.color_pair(1))
            screen.addstr(line, 0, f'http://www.quotationspage.com/quote/{page}.html', curses.A_UNDERLINE)
            screen.attroff(curses.color_pair(1))
        screen.refresh()

    def draw_answer(quote, author):
        words = []
        y, x = screen.getmaxyx()
        wrap = x if x < 80 else 80
        line = 3
        for word in quote.split():
            if len(' '.join(words)) + len(word) < wrap:
                words.append(word)
            else:
                screen.addstr(line, 0, ' '.join(words))
                line += 3
                words = [word]
        else:
            screen.addstr(line, 0, ' '.join(words))
            line += 3
            screen.addstr(line, 0, ' ' * ((wrap if wrap < len(quote) else len(quote)) - len(author)))
            screen.addstr(author, curses.A_BOLD)
        screen.refresh()

    # how to print the cipher wrapped for curses
    # for i, e in enumerate(sorted(cipher.items())):
    #     k, v = e
    #     screen.addstr(i // 13 + 4, i * 4 % (13 * 4), f'{k}:{v}')

    draw_menu()
    cipher = {}
    page = 0
    quote = ''
    author = ''

    while (key := screen.getkey()) not in ('q', 'Q'):
        if key in ('o', 'O'):
            screen.addstr(1, 0, "Enter a number between 1 - 42500: ")
            screen.refresh()
            curses.echo()
            try:
                page = int(screen.getstr(5))
            except ValueError:
                screen.clear()
                draw_menu()
                screen.addstr(2, 0, "Invalid Input")
                screen.refresh()
                quote = ''
            else:
                screen.addstr(f'Trying to open page {page}')
                screen.refresh()
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
        screen.addstr(1, 0, f'You Pressed {key}')
        screen.refresh()


curses.wrapper(main)
