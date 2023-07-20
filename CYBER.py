import os, sys

try:

    __import__("menu").oxx()

except Exception as e:

    exit(str(e))
