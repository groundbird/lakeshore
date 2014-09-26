#!/bin/sh

DATADIR=/home/hikaru/lakeshore/data
FILENAME=`date '+%Y-%m-%d_%H%M%S'`
COMMAND=/home/hikaru/lakeshore/lakeshore.py
ln -sf ${FILENAME}.dat ${DATADIR}/lastest
${COMMAND} | tee ${DATADIR}/${FILENAME}.dat
