#!/bin/bash 

# set up the beep socket environment 

export BEEP_SOCKET_RECV_PORT=2001
export BEEP_SOCKET_SEND_PORT=2000
export BEEP_SOCKET_SSH_ARGS="-R "$BEEP_SOCKET_SEND_PORT":localhost:"$BEEP_SOCKET_RECV_PORT

