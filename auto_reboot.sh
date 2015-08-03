#!/bin/sh
DIRNAME=lakeshore

! (screen -ls | grep -q $DIRNAME ) && \
screen -dmS $DIRNAME sh -c "cd $HOME/$DIRNAME && ./restart.sh ./logger.sh"
