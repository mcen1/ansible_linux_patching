#!/bin/bash
df -k /boot | grep -vE '^Filesystem|tmpfs|cdrom' | while read output;
do
  usep=$(echo $output | awk '{ print $4}'  )
  usep=${usep%.*}
  if [[ $usep -lt 90000 ]]; then
    echo "WASHME"
  fi
done

