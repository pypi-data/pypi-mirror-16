#!/bin/sh
# Run the pyessv test suite.
#

DREQ_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DREQ_DIR
export PYTHONPATH=PYTHONPATH:$DREQ_DIR
nosetests -v -s tests
