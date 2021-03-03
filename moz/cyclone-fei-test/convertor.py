import csv
import json
import shutil 
import codecs

# Read values from CSV
csvFilename = 'informacao.csv'

d = {}

with open(csvFilename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            d[row[0]] = row[1]
            print(f'\t{row[0]} is a Key with {row[1]} as Value.')
            line_count += 1
    print(f'Processed {line_count} lines. and eventDirName is { d }')

# declare source directory from Github and destination of new event
eventDirName = d['eventDirName']
src = '../cyclone-layer-templates'
dst = '../' + eventDirName # TODO make dynamic
event_label = d['event_label']
menu_credit = d['menu_credit']
credit_src_url = d['credit_src_url']
monthyear = d['monthyear']

credit = "<a href=" + credit_src_url + " target=_blank data-credit=credit>" + menu_credit + "</a>"
category = event_label + ' - 2021'
geojson_file_line = d['geojson_file_line']
geojson_file_points = d['geojson_file_points']
geojson_file_polygon = d['geojson_file_polygon']

timeField = d['timeField']

baseURLGit = 'https://raw.githubusercontent.com/onaio/ingc-mozambique-data/master/moz/'


# Copy directory tree (cp -R src dst) 
# shutil.copytree(src, dst) 

# Update values for Grouped Layer File
with open(dst + '/cyclone-grouped-layer.json', 'r') as file:
     json_data = json.load(file)
    # Replace new values for 
     json_data["label"] = event_label
     json_data["layers"] = [baseURLGit + eventDirName + "/cyclonepath-forecast-line.json", 
                            baseURLGit + eventDirName + "/cyclonepath-forecast-points.json",
                            baseURLGit + eventDirName + "/cyclonepath-forecast-polygon.json"]
     json_data["menu-credit"] = menu_credit
     json_data["credit"] = credit
     json_data["category"] = category

with open(dst + '/cyclone-grouped-layer.json', 'w') as file:
    json.dump(json_data, file, indent=2)

# Update values for Forecast Line File
with open(dst + '/cyclonepath-forecast-line.json', 'r') as file:
     json_data = json.load(file)
    # Replace new values for 
     json_data["label"] = event_label + monthyear
     json_data["source"]["data"] = baseURLGit + eventDirName + "/" + geojson_file_line
     # TODO: Add dynamic categories info
     json_data["menu-credit"] = menu_credit
     json_data["credit"] = credit
     json_data["category"] = category

with open(dst + '/cyclonepath-forecast-line.json', 'w') as file:
    json.dump(json_data, file, indent=2)

# Update values for Forecast Points File
with open(dst + '/cyclonepath-forecast-points.json', 'r') as file:
     json_data = json.load(file)
    # Replace new values for 
     json_data["label"] = event_label + monthyear
     json_data["source"]["data"] = baseURLGit + eventDirName + "/" + geojson_file_points
     # TODO: Add dynamic categories info
     json_data["layout"]["text-field"] = "{" + timeField + "}"
     json_data["credit"] = credit

with open(dst + '/cyclonepath-forecast-points.json', 'w') as file:
    json.dump(json_data, file, indent=2)

# Update values for Forecast Polygon File
with open(dst + '/cyclonepath-forecast-polygon.json', 'r') as file:
     json_data = json.load(file)
    # Replace new values for 
     json_data["label"] = event_label + monthyear
     json_data["source"]["data"] = baseURLGit + eventDirName + "/" + geojson_file_polygon
     # TODO: Add dynamic categories info
     json_data["menu-credit"] = menu_credit
     json_data["credit"] = credit
     json_data["category"] = category

with open(dst + '/cyclonepath-forecast-polygon.json', 'w') as file:
    json.dump(json_data, file, indent=2)