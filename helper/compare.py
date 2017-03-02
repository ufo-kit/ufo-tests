import sys
import argparse
import tifffile
import numpy as np


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--reference', required=True)
    parser.add_argument('--epsilon', type=float, default=0.0)
    args = parser.parse_args()

    a = tifffile.imread(args.input)
    r = tifffile.imread(args.reference)
    diff = np.sum(np.abs(a - r))
    print(diff)
    sys.exit(0 if diff == 0.0 else 1)
