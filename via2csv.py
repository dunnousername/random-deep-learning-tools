#!/usr/bin/env python3
# converts VIA JSON annotations to standard csv annotations, like the ones vott uses
# this does NOT support multiple labels; it assumes all regions are unlabeled but present
# args: via2csv.py (input json) (output csv)

import sys
import json

j = json.load(open(sys.argv[1], 'r'))

regions = []

label = 'spider'

for value in j.values():
    fn = value['filename']
    for region in value['regions']:
        s = region['shape_attributes']
        regions.append(('"' + fn + '"', s['x'], s['y'], s['x'] + s['width'], s['y'] + s['height'], label))

with open(sys.argv[2], 'w+') as f:
    f.write('"image","xmin","ymin","xmax","ymax","label"\n')
    for region in regions:
        f.write(','.join([str(x) for x in region]) + '\n')