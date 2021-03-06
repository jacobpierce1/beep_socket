Welcome to the beep socket library. Add the following to your .bashrc (or other shell environment): 

	```
	BEEP_SOCKET_PATH=<path to this directory> 
	export PATH=$PATH:$BEEP_SOCKET_PATH 
	source $BEEP_SOCKET_PATH/beep_socket_env.sh 
	```

Access a server from your local machine like so: 

	```
	>>>  ssh $BEEP_SOCKET_SSH_ARGS <user@host>
	```

Open a new terminal on your local machine and run 

	```
	>>>  beep_socket_recv.sh
	```

You can then send the signal to beep on the server connection via

	```
	>>>  beep_socket_send.sh
	```

For typical usage, you can send a beep at the end of compilation (or another time-consuming task) like so: 

	```
	>>>  make ; beep_socket_send.sh
	```

Note that the above will send a signal at the end of compilation even if it fails. 