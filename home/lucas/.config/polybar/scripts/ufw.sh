#!/bin/bash

status=$(sudo ufw status 2>/dev/null)

# Left click
if [[ "$1" == "toggle" ]]; then
	if [[ "${status}" != *inactive* ]]; then
  		sudo ufw disable
  		notify-send "FireWall" "FireWall Ativado!"
  	else
		sudo ufw enable
		notify-send "FireWall" "FireWall Desativado!"	
	fi
fi

if [[ $? -gt 0 ]]; then
  exit
fi

if [[ "${status}" != *inactive* ]]; then
  echo ""
else
  echo ""
fi
