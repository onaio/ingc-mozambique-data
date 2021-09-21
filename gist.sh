#!/usr/bin/env bash
# Runs all .json or .js files through pythons json lint tool before commiting,
# to make sure that you don't commit broken json objects.

git_dir=$(git rev-parse --show-toplevel)

for file in $(git diff-index --name-only --diff-filter=ACM --cached HEAD -- \
    | grep -P '\.((js)|(json))$'); do
    python -mjson.tool $file 2> /dev/null
    if [ $? -ne 0 ] ; then
        echo "Lint check of JSON object failed. Your changes were not commited."
        echo "in $git_dir/$file:"
        python -mjson.tool $file
        exit 1
    fi
done