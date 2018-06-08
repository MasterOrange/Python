#!/usr/bin/python3.5

# runs blast

import subprocess
import argparse


from sys import argv

name, prog, db, qu = argv


def blast(prog='program', db='database', qu='query'):
    subprocess.call(['/usr/local/blast/current/bin/'+prog, '-db', db, \
            '-query', qu])

# blast(prog, db, qu)

def otherblast()
