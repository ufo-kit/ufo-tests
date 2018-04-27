#!/usr/bin/env python

import argparse
import json
import itertools
import string
import logging
import subprocess
import shlex
import tifffile
import numpy as np
import colorama
from colorama import Fore as FG, Back as BG, Style as ST


def lines(fp):
    while True:
        line = fp.readline()
        if line:
            yield line.rstrip()
        else:
            break


def monitor_process(cmd):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # swallow all output on stdout
    for line in lines(proc.stdout):
        pass

    for line in lines(proc.stderr):
        print(FG.RED + ST.BRIGHT + str(line) + ST.RESET_ALL)

    proc.wait()
    return proc


def run_all(test):
    output = '/tmp/test.tif'
    params = test['params']
    template = string.Template(test['command'])
    elements = list(itertools.product(*params.values()))
    epsilons = test['epsilon'] or [None]*len(elements)

    for elem, epsilon in zip(elements, epsilons):
        fixed = dict(zip(params.keys(), elem))
        keys = sorted(fixed.keys())
        param_name = '-' + '-'.join(('{}_{}'.format(k, fixed[k]) for k in keys)) if keys else ''
        reference = 'reference/{}{}-ref.tif'.format(test['name'], param_name)

        fixed['output'] = output
        fixed['reference'] = reference

        cmd = template.substitute(**fixed)
        proc = monitor_process(shlex.split(cmd))

        if proc.returncode:
            print(FG.RED + ST.BRIGHT + 'FAIL  ' + ST.RESET_ALL + test['name'])
            continue

        a = tifffile.imread(output)
        r = tifffile.imread(reference)
        rmse = np.sqrt(np.sum((a - r)**2) / (a.shape[0] * a.shape[1]))

        p = ' '.join(('{}={}'.format(k, fixed[k]) for k in keys)) + ' ' if keys else ''

        if epsilon is not None:
            s = '{} ({}RMSE_is={:3.5f} RMS_exp<{})'.format(test['name'], p, rmse, epsilon)
        else:
            s = '{} ({}RMSE_is={:3.5f})'.format(test['name'], p, rmse)

        if (epsilon is not None and rmse < epsilon) or rmse == 0.0:
            print(FG.GREEN + ST.BRIGHT + 'PASS  ' + ST.RESET_ALL + s)
        else:
            print(FG.RED + ST.BRIGHT + 'FAIL  ' + ST.RESET_ALL + s)


if __name__ == '__main__':
    colorama.init()

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', default=None, help="Single test to run")
    args = parser.parse_args()

    tests = json.load(open('tests.json'))

    if args.test:
        try:
            run_all(next(x for x in tests if x['name'] == args.test))
        except StopIteration:
            print("Error: test `{}' not found.".format(args.test))
    else:
        for test in tests:
            run_all(test)
