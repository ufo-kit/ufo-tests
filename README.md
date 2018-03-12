## ufo-tests

Validity and regression tests for [UFO](https://github.com/ufo-kit/ufo-core).


### Running tests

Get the input data by running

    ./setup.sh

Execute

    ./run.py

and all test scripts will be run and evaluated. The output contains success
state as well as the sum of absolute difference to the expected reference
output.


### Adding a new test

1. Think of a name for the test, for example `threshold`.
2. Compute the expected reference, call it `threshold-ref.tif` and place it
   into the `reference/` dir.
3. Add an entry to `tests.json`.
4. Profit.
