#!/bin/bash

FIBOS=(1 2)

while [ ${FIBOS[${#FIBOS[@]}-1]} -lt 4000000 ]
do
	LASTLAST=${FIBOS[${#FIBOS[@]}-2]}
	LAST=${FIBOS[${#FIBOS[@]}-1]}
	
	FIBOS=(${FIBOS[@]} $(($LASTLAST+$LAST)))
	
done

SUM=0
for INDEX in $(seq 0 1 $((${#FIBOS[@]}-1)))
do
	CURFIBO=${FIBOS[$INDEX]}
	if [ $(($CURFIBO%2)) -eq 0 ]
	then
		SUM=$(($SUM+$CURFIBO))
	fi
done

echo $SUM
