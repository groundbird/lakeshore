#!/bin/sh

CURRDIR=`pwd`
CMD=${CURRDIR}/lakeshore.py
FILENAME=`date '+%Y-%m-%d_%H%M%S'`

if [ ! -d "${CURRDIR}/data" ]; then
    mkdir data
    echo 'Make data/'
fi

ln -sf ${FILENAME}.dat ${CURRDIR}/data/lastest
python ${CMD} | tee ${CURRDIR}/data/${FILENAME}.dat
