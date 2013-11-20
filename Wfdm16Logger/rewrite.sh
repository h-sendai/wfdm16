#!/bin/sh

for i in *.h *.cpp; do
    sed -i.bak \
    -e 's/samplelogger/wfdm16logger/g' \
    -e 's/SampleLogger/Wfdm16Logger/g' \
    -e 's/SAMPLELOGGER/WFDM16LOGGER/g' \
    $i
done
