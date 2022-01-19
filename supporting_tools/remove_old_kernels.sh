#!/bin/bash
COUNT=$(yum list installed kernel.x86_64|grep kernel|wc -l)
if [ $COUNT -gt 2 ]; then
    echo "Removing old kernels..."
    let KEEP=$((COUNT-1))
    yum remove -y $(yum list installed kernel|grep kernel|head -${KEEP}|awk '{print "kernel-"$2}')
    if [ $? -ne 0 ]; then
        echo "FAILED to remove old kernels"
        exit 1
    fi
fi

COUNT=$(yum list installed kernel-uek.x86_64|grep 'kernel\-uek'|wc -l)
if [ $COUNT -gt 2 ]; then
    echo "Removing old UEK kernels..."
    let KEEP=$((COUNT-1))
    yum remove -y $(yum list installed kernel-uek|grep 'kernel\-uek'|head -${KEEP}|awk '{print "kernel-uek-"$2}')
    if [ $? -ne 0 ]; then
        echo "FAILED to remove old UEK kernels"
        exit 1
    fi
fi