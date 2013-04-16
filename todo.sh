#!/bin/bash


read -p "Type here: " result;
if [ "$result" == "exit" ]; then
	exit	
else
	echo "$result" >> ~/.conkyrc
        echo "$result added to todo"
        sh ~/todo.sh

fi
