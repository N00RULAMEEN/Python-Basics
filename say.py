import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow(f"Hi my Dear {sys.argv[1]}")
    cowsay.trex(f"Hi my Dear {sys.argv[1]}")

