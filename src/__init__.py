import sys, os, pathlib

path = pathlib.Path(os.getcwd()) / 'src'
sys.path.insert(1, str(path))