#!/usr/bin/env python3
# a tool that allows you to convert outputs from TrainYourOwnYOLO (YoloV3 implementation) to a standard label csv
# it lets you choose what bounding boxes you want to keep, and which to discard.
# args: verifier.py (input csv) (output csv)
# requires opencv2 with python bindings

import time
import sys
import csv

import cv2

# change these labels to match the label indices
labels = ['spider']

def main(path, output_filename):
    with open(output_filename, 'w+') as of:
        of.write('"image","xmin","ymin","xmax","ymax","label"\n')
        with open(path, 'r') as f:
            data = [a for a in csv.DictReader(f)]
        regions = {}
        for line in data:
            fn = line['image_path']
            p1 = (int(line['xmin']), int(line['ymin']))
            p2 = (int(line['xmax']), int(line['ymax']))
            label = line['label']
            confidence = float(line['confidence'])
            if fn not in regions:
                regions[fn] = []
            regions[fn].append((p1, p2, label, confidence))
        stop = False
        print('o = keep, p = next')
        for fn in regions.keys():
            im = cv2.imread(fn, cv2.IMREAD_COLOR)
            for region in regions[fn]:
                im = cv2.rectangle(im, region[0], region[1], (36, 255, 12), 1)
                cv2.putText(im, '{} {}'.format(labels[int(region[2])], region[3]), (region[0][0], region[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            cv2.imshow('image', im)
            while True:
                key = cv2.waitKey(0)
                if key == ord('q'):
                    stop = True
                    break
                elif key == ord('o'):
                    for region in regions[fn]:
                        of.write(','.join(str(x) for x in [
                            '"' + fn + '"',
                            region[0][0],
                            region[0][1],
                            region[1][0],
                            region[1][1],
                            labels[int(region[2])]
                        ]) + '\n')
                    time.sleep(0.2)
                    break
                elif key == ord('p'):
                    time.sleep(0.2)
                    break
            if stop:
                cv2.destroyAllWindows()
                return

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])