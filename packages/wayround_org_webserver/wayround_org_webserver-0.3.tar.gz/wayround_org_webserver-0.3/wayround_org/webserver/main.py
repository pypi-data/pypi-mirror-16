#!/usr/bin/python3


def main():

    import sys

    del sys.path[0]

    import logging

    import wayround_org.utils.program

    wayround_org.utils.program.logging_setup(loglevel='INFO')

    import wayround_org.webserver.commands

    commands = wayround_org.webserver.commands.commands()

    ret = wayround_org.utils.program.program('wrows', commands, None)

if __name__ == '__main__':
    exit(main())
