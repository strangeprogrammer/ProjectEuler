#!/bin/bash

SUM=0

for INDEX in $(seq 1 1 999)
do
	if [ "$(($INDEX % 3))" = "0" ]
	then
		SUM=$(($SUM+$INDEX))
		continue
	elif [ "$(($INDEX % 5))" = "0" ]
	then
		SUM=$(($SUM+$INDEX))
		continue
	fi
done

echo $SUM
