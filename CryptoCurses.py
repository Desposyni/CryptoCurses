#! /usr/bin/python3

import curses
from CryptoQuote.CryptoQuote import *


def main(screen):
    cipher = get_cipher()
    page, quote, author = get_quote()

    for k, v in sorted(cipher.items()):
        screen.addstr(0, 0, f'{k}:{v}')
        screen.addstr(1, 0, ' , ') if k not in ['M', 'Z'] else screen.addstr('\n')
    screen.addstr(2,0, f'Height = {curses.LINES}, Width = {curses.COLS}')
    screen.addstr(3, 0, f'http://www.quotationspage.com/quote/{page}.html')
    screen.addstr(4, 0, f'{quote}')
    screen.addstr(5, 0, f'{author:>{len(quote)}}')
    screen.addstr(6, 0, f'{encipher(cipher, quote)}')
    screen.addstr(7, 0, f'{encipher(cipher, author):>{len(quote)}}')
    screen.refresh()
    curses.napms(10000)


curses.wrapper(main)
