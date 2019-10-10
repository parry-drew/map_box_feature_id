#!/usr/bin/env python
# -*- coding: utf-8 -*-
# C:\Python27\ArcGIS10.6\python.exe MapBoxFeatureID.py

import json, arcpy

def main():
    input = raw_input('DRAG YOUR GEOJSON HERE ---> : ')
    p = 0
    with open(input, 'r') as jf:
        data = json.loads(jf.read())
        for item in data["features"]:
            p += 1
            item["id"] = p

    with open(input, 'w') as jf:
        json.dump(data, jf)

if __name__ == '__main__':
    main()


https://github.com/parry-drew/Save_A_Copy_Batch
