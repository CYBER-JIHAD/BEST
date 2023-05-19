import os, sys

try:

    __import__("mainx").CYB()

except Exception as e:

    exit(str(e))
