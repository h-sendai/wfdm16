#!/bin/sh

for i in *.h *.cpp; do
    sed -i.bak \
    -e 's/cometcdcreader/wfdm16reader/g' \
    -e 's/CometCdcReader/Wfdm16Reader/g' \
    -e 's/COMETCDCREADER/WFDM16READER/g' \
    $i
done
