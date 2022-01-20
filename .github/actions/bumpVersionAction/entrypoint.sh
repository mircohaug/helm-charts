#!/bin/sh -l
ls -la
env
python scripts/bump-version.py "$@"
