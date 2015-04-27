#!/bin/sh

#
# script to run something at arbitrary intervals
# Format: runner <sec> [norun]
# norun stops the script from running for sec 

WAITLOOP=10		# HOW LONG TO WAIT BETWEEN TRIES

PAUSE=$1

if test "$2"
then
	if test "$2" = "norun"
	then
		NORUN=$1
	else
		SCRIPT=$2
	fi
fi


#Pop the first two args off the arg stack so that
#we can pass the rest into the script if needed
shift
shift

#Please note that this this is incomplete if arguments could be strings, because of well crappy 
#bash parsing and string maniuplation
REST="$*"
	
if test "$NORUN"		# NORUN
then
	# WE SHOULD TOUCH THIS WITH THE EXPIRATION DATE
	# THEN IT CAN AUTOREMOVE
	if test -f /etc/issue
	then
		DATE=`date -d "+$PAUSE seconds"`
		echo "RUNNING SUSPENDED UNTIL [$DATE]"
		touch -d "$DATE" /tmp/norun
	else
		TIME=`date +%s`
		TIME=`expr $TIME + $PAUSE`	# EPOCH TIME TO STOP
		# echo "EXPIRE @ $TIME"
		DATE=`date -r $TIME +%m%d%H%M`
		echo "RUNNING SUSPENDED UNTIL [$DATE]"
		touch -t $DATE /tmp/norun
	fi
	exit				# OUR WORK IS DONE
fi

while true
do
	if test -f "/tmp/norun"
	then
		touch /tmp/now
		EXPIRED=`find /tmp/norun ! -newer /tmp/now`
		rm /tmp/now
		# IF WE'RE EXPIRED, THEN REMOVE
		if test "$EXPIRED"
		then
			echo "REMOVING EXPIRED norun FILE"
			rm -f /tmp/norun
		else
			echo "NORUN ENABLED... PAUSING FOR $WAITLOOP SECONDS"
			sleep $WAITLOOP		# WAIT 30 SECONDS
			continue
		fi
	fi

	# IF WE'RE HERE WE'RE GOING TO TRY TO START SOMETHING
	# CHECK IF ANOTHER INSTANCE IS ALREADY RUNNING... IF IT
	# IS, JUST PAUSE

	echo "TRYING TO RUN"
	if test -f /tmp/runner		# IS ANOTHER RUNNING?
	then
		PID=`cat /tmp/runner`
		if test "$PID" != "$$"	# NOT US...
		then
			kill -0 $PID 2>/dev/null
			if test "$?" = "0"
			then
				echo "Process $PID is still running..."
				exit
			fi
		fi
	fi
	echo $$ > /tmp/runner
	#
	# RUN OUR STUFF HERE
	#
	NOW=`date`

	echo "RUNNING OUR THING at $NOW"

	sh $SCRIPT $REST
	sleep $PAUSE
done
