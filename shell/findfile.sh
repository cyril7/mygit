#!/bin/bash
findfile()
{
    for filename in $(ls)
    do
        if [ -f "$filename" ];then
            echo "$filename"
        elif [ -L "$filename" ];then
            echo "this is a link";
        else
            cd "$filename";
            findfile;
            cd ..
        fi
    done
}

findfile
