from .main import reformat
import sys

# CLI interface
if __name__ == "__main__":
    print(reformat(sys.argv[1]))
