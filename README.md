## ufo-tests

Validity and regression tests for [UFO](https://github.com/ufo-kit/ufo-core).


### Running tests

Get the input data from TO-BE-CHANGED.

Execute

    ./run.sh

and all test scripts will be run and evaluated. The output contains success
state as well as the sum of absolute difference to the expected reference
output.


### Adding a new test

1. Think of a name for the test, for example `threshold`.
2. Compute the expected reference, call it `test-threshold-ref.tif` and place it
   into the `reference/` dir.
3. Create a test shell script called `test-threshold.sh` and place it into
   the root dir. The script must write its output to a file that is identified
   by the first argument passed to the test script.
4. Profit.
