#!/bin/bash
 
basepath=$(dirname $0)
base=$(basename $0 .sh)

python $basepath/beep_socket_recv.py
