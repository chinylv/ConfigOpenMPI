#!/bin/bash
#coding=utf8

ecp_arr=(116 182 184 219 500)

declare -a ass_arr

for i in ${ecp_arr[*]} ; do
    tvar=`echo $i |sed 's/^00*//g'`
    ass_arr[$tvar]='skip';
done

#echo ${ass_arr[*]}
#echo ${!ass_arr[*]}

#echo ${ass_arr[1]}
#echo ${ass_arr[8]}

for i in `seq -w 1 332` ; do
    tvar=`echo $i |sed 's/^00*//g'`
    if [ ! "${ass_arr[$tvar]}" ]; then
        #printf "node$i\t${ass_arr[$tvar]}";
        printf "node$i\t";
        rsh node$i "python /home/charles/reconfmpi/runconf.py && sleep 0.05";
        sleep 0.05;
        #python runconf.py;
    fi
done
