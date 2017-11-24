#!/bin/bash
inotifywait -mrq --timefmt "%y/%m/%d %T" --format "%T %Xe %w%f" -e open $1|while read t1 t2 e f
do
	echo $t1,$t2,$e,$f
	lsof $1 
	#lsof -i @192.168.6.155
	#lsof /usr/lib/x86_64-linux-gnu/libcurl-gnutls.so.4 2>/dev/null
	# echo $file
	echo "--------------------------------------------------------"
done
