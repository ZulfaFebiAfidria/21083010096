#!/bin/bash

printf "makanan apa yang kamu suka ?\n"
printf "seblak ?\n"
printf "bakso ?\n"
printf "indomie ?\n"

read makanan

case "$makanan" in
  "seblak")
    echo "seblak goyang lidah enak pwoll!"
    ;;
  "bakso")
    echo "bakso mas budi mantapz!"
    ;;
  "indomie")
    echo "indomie enak poll"
    ;;
  *)
    echo "Makanan yang kamu suka gaenak hehe"
    ;;
esac
