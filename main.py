import sys

def main(argc, argv):
    if argc != 0:
        print("what")
        sys.exit(1)
    return 0

if __name__ == "__main__":
    main(len(sys.argv) - 1, sys.argv[1:])
