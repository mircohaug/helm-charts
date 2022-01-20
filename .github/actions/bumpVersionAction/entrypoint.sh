#!/bin/sh -l
git log -n 5 --oneline
python /bump-version.py "$@"
git log -n 5 --oneline
