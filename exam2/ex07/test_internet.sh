#!/bin/bash

 set +e
curl -s -I www.google.com >/dev/null
now = date + "%Y-%m-%d:%H:%M:%S"

if [ $? == 0 ]; then
    echo "$now" + "internet OK"
else
    echo "$now" + "internet FAIL"
fi
