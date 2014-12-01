#!/bin/bash
# ref., http://tclip.blog.fc2.com/blog-entry-117.html

sleep_time='10m'

if test $# -le 0  ; then
    echo "USAGE: ./restart.sh COMMAND [OPTION]"
    exit -1
fi

ret=-1

while test ${ret} -ne 0;
do
    echo "----> start: $*"
    eval "$@"
    ret=$?
    echo "----< end : ret = $ret"
    if [ ${ret} -eq 0 ]; then break; fi
    sleep ${sleep_time} || break;
done
