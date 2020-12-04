#!/usr/bin/env bash
#
# IMPORTANT: Change this file only in directory Standalone!

uwsgi --socket 0.0.0.0:4000 --protocol=http -w app:app