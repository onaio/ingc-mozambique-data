# Generates schemas for all layers based on draft-04 json schema
# https://json-schema.org/specification.html

for dir in `ls moz`;
do
    for subdir in `ls moz/$dir`;
    do
        if [ "${subdir##*.}" = "json" ];
            then
                json-schema-generator "moz/$dir/$subdir" -o "validation-schema/$subdir"
        fi
    done
done