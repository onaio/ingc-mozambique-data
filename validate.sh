cmd_status=0
for dir in `ls moz`;
do
    for subdir in `ls moz/$dir`;
    do
        if [ "${subdir##*.}" = "json" ];
            then
                npx ajv test -s validation-schema/schema.json -d "moz/$dir/$subdir" --valid --strict=false
                test_status=$?
                if [ "$test_status" -gt "0" ]; then
                    cmd_status=$test_status
                fi
        fi
    done
done

exit $cmd_status