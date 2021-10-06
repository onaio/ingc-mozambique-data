for dir in `ls moz`;
do
    for subdir in `ls moz/$dir`;
    do
        if [ "${subdir##*.}" = "json" ];
            then
                npx ajv -s "validation-schema/$subdir" -d "moz/$dir/$subdir" --strict=false;
        fi
    done
done