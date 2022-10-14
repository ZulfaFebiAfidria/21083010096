#!/bin/bash

declare -a IPSMahasiswa

printf "Input : "
read n

for ((i=0; i<n; i=i+1))
do
    read IPSMahasiswa[$i]
done

for ((i=0; i<n; i=i+1))
do
    let IPS=IPS+IPSMahasiswa[i]
done

printf "\nIPS mhs : %i / %i\n" $IPS $n

let IPK=IPS/n
printf "IPK mhs : %i\n" $IPK

