#!/usr/bin/python

import sys
sys.path.append('dockerenv')

from dockerenv import main


if __name__ == '__main__':
    main(
        base_image = 'python:3.5.0-slim',
        script_dirs = ['brewery/setup'],
    )

