for dir in `ls moz`;
do
    for subdir in `ls moz/$dir`;
    do
      npx ajv -s validation-schema/schema.json -d "moz/$dir/*.json";
    done
done