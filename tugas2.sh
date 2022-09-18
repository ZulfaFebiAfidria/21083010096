#!/bin/bash
clear

echo -n "masukan umur :";
read umur;

if [ $umur -gt 17 ]
then
   echo " $umur tahun sudah mendapatkan KTP"
elif [ $umur -lt 17 ]
then 
   echo " $umur tahun belom mendapatkan KTP"
else
   echo " $umur tahun belom bisa membuat KTP"
fi
