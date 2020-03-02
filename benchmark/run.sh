#!/usr/bin/env bash


fruit_count=1000000

benchmark_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

find $benchmark_dir -name "*.py" -print -exec /usr/bin/time -l {} $fruit_count \;
