#!/bin/bash

function kernelErase() {
  MYKERN=$1
  for F in $(rpm -qa $MYKERN | grep -v $ACTIVEKERN); do
    if [[ ${#F} -gt 8 ]]; then
      echo "Erasing inactive kernel $F"
      yum erase -y $F
    fi
  done
}

ACTIVEKERN=$(uname -a | awk '{print $3}')
echo Active kernel is $ACTIVEKERN
if [[ $ACTIVEKERN == *"uek"* ]]; then
  echo "Kernel is UEK"
  kernelErase "kernel-uek"
else
  echo "Kernel is non-UEK"
  kernelErase "kernel"
fi

