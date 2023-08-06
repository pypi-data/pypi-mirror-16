#!/usr/bin/env python2.7
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments_colorizer import colorizer
import sys
import argparse
from os import linesep

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='colorize-html',
                                     description='Add syntax highlighting to code in html. Built using Pygments. http://pygments.org/',
                                     usage='%(prog)s [options]')
    parser.add_argument('-f', '--htmlfile', help='The html file to process')
    parser.add_argument('-s', '--style', help='The style of syntax highlighting. See --list_styles for a full list')
    parser.add_argument('--list_styles', action='store_true', help='List of possible syntax styles to use')
    parser.add_argument('-d', '--default', help='Default lexer to use (i.e. csharp, python). See --list_lexers or --find_lexer for a full list')
    parser.add_argument('--list_lexers', action='store_true', help='List of lexers to choose from')
    parser.add_argument('--find_lexer', help='Find a lexer')
    parser.add_argument('--div_style',
                        help='The inline css style to apply to the <div> tag surrounding each code block (Ignored if --div_file is used)')
    parser.add_argument('--div_file',
                        help='The file to use as the inline css style to apply to the <div> tag surrounding each code block')
    parser.add_argument('-l', '--linenos', action='store_true', help='Add line numbers to the code blocks')
    parser.add_argument('-i', '--inline', action='store_true',
                        help='Create css styles inline on each tag as opposed to a separate styles section')
    parser.add_argument('-o', '--out', help='Write results to this file')
    parser.add_argument('--css_file',
                        help='Write code styles to this file. This still writes new styles into the style tag (Ignored if --inline is used)')
    parser.add_argument('--log', action='store_true', help='Log errors to "log.txt" in the same directory')
    args = parser.parse_args()

    if args.list_styles:
        for style in get_all_styles():
            print(style)
        exit()
    if args.list_lexers:
        for lexer in get_all_lexers():
            print(lexer[0] + ' :: [' + str.join(', ', [alias for alias in lexer[1]]) + ']')
        exit()
    if args.find_lexer:
        for lexer in get_all_lexers():
            if args.find_lexer in lexer[1]:
                print(lexer[0] + ' :: [' + str.join(', ', [alias for alias in lexer[1]]) + ']')
                exit()
        print('Lexer not found.')
        exit()

    piped_input = sys.stdin.read() if not sys.stdin.isatty() else ''

    if not args.htmlfile and not piped_input:
        print('usage: colorize-html [options]')
        print('colorize-html: error: use \'colorize-html -f htmlfile\' to colorize code in an html file, or -h for help')
        exit()

    if args.style and not args.style in get_all_styles():
        print('Style not found. Use --list_styles to see a list of available styles.')
        exit()

    if args.default and not args.default in [a for l in get_all_lexers() for a in l[1]]:
        print('Default lexer not found. Use --list_lexers to see a list of available lexers.')
        exit()

    success = False
    log = None
    converted = 0
    html_hilite = ''
    script = ''
    try:
        if piped_input:
            html = piped_input
        else:
            with open(args.htmlfile) as f:
                html = f.read()

        inline_div = args.div_style if args.div_style else ''
        if args.div_file:
            with open(args.div_file) as fb:
                inline_div = fb.read()

        style = args.style if args.style else 'default'
        default = args.default if args.default else ''
        success, log, converted, html_hilite, script = colorizer(html, default, style, inline_div, args.inline, args.linenos)

        if success:
            if args.out:
                with open(args.out, 'w') as f:
                    f.write(html_hilite)
            else:
                print(html_hilite)

            if args.css_file:
                with open(args.css_file, 'w') as fcss:
                    fcss.write(script)

            if args.log:
                with open('log.txt', 'w') as flog:
                    flog.write(str.join(linesep, log))

            print('%d code blocks colorized!' % (converted))
            if not args.default:
                print('If the html output is not as expected try adding the --default option to specify a default lexer')
        else:

            if args.log:
                with open('log.txt', 'w') as flog:
                    flog.write(str.join(linesep, log))

            print('Colorizer did not convert any code blocks. Use the --log switch to enable error logging.')
            if not args.default:
                print('You also might try using the --default option to specify a default lexer')

    except IOError as e:
        print('An I/O error occurred: ' + e.strerror)
    except ParseError as e:
        print('An error occurred parsing the html document: ')
