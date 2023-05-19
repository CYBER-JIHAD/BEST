import os, sys

try:

    __import__("main").xo()

except Exception as e:

    exit(str(e))
