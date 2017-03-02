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
    rmse = np.sqrt(np.sum((a - r)**2) / (a.shape[0] * a.shape[1]))
    print(rmse)
    sys.exit(0 if rmse <= args.epsilon else 1)
