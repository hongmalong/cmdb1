#!/bin/bash
#
# 
#
# chkconfig: 345 99 28
# description: Starts/Stops serviceName service
#
 
export JAVA_HOME=serviceJavaHome
export PATH=$JAVA_HOME/bin:$PATH
 
export SERVICE_NAME=serviceName
export SERVICE_HOME=serviceWorkDir
export SERVICE_USER=serviceUser
SERVICE_USAGE="Usage: $0 {\e[00;32mstart\e[00m|\e[00;31mstop\e[00m|\e[00;32mstatus\e[00m|\e[00;31mrestart\e[00m}"

SHUTDOWN_WAIT=7
 
service_pid() {
  #cat $SERVICE_HOME/server.pid
  echo `ps -fe | grep $SERVICE_HOME | grep -v grep | tr -s " "|cut -d" " -f2`
  #echo `ps -fe | grep $SERVICE_NAME | grep -v grep | tr -s " "|cut -d" " -f2`
}

start() {
  pid=$(service_pid)
  if [ -n "$pid" ]
  then
    echo -e "\e[00;31m$SERVICE_NAME service is already running (pid: $pid)\e[00m"
  else
    # Start Service
    echo -e "\e[00;32mStarting $SERVICE_NAME service\e[00m"
    #ulimit -n 100000
    #umask 007
    if [ `user_exists $SERVICE_USER` = "1" ]
    then
      su $SERVICE_USER -c "$SERVICE_HOME/serviceStartScript"
      #$SERVICE_HOME/serviceStartScript
    else
      sh $SERVICE_HOME/serviceStartScript
      #$SERVICE_HOME/serviceStartScript
    fi
    status
  fi
  return 0
}
 
status(){
  pid=$(service_pid)
  if [ -n "$pid" ]; then echo -e "\e[00;32m$SERVICE_NAME service is running with pid: $pid\e[00m"
    else echo -e "\e[00;31m$SERVICE_NAME service is not running\e[00m"
  fi
}
 
stop() {
  pid=$(service_pid)
  if [ -n "$pid" ]
  then
    # Stop Service
    echo -e "\e[00;31mStoping $SERVICE_NAME service\e[00m"
    sh $SERVICE_HOME/serviceStopScript
 
    let kwait=$SHUTDOWN_WAIT
    count=0;
    until [ `ps -p $pid | grep -c $pid` = '0' ] || [ $count -gt $kwait ]
    do
      echo -n -e "\n\e[00;31mwaiting for processes to exit\e[00m";
      sleep 1
      let count=$count+1;
    done
 
    if [ $count -gt $kwait ]; then
      echo -n -e "\n\e[00;31mkilling processes which didn't stop after $SHUTDOWN_WAIT seconds\e[00m"
      kill -9 $pid
    fi
  else
    echo -e "\e[00;31m$SERVICE_NAME service is not running\e[00m"
  fi
 
  return 0
}
 
user_exists(){
  if id -u $1 >/dev/null 2>&1; then
    echo "1"
  else
    echo "0"
  fi
}
 
case $1 in
  start)
    start
    ;;
  stop)  
    stop
    ;;
  restart)
    stop
    start
    ;;
  status)
    status
    ;;
  *)
    echo -e $SERVICE_USAGE
    ;;
esac    
exit 0

