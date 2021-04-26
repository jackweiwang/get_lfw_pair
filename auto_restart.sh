cd $(dirname $0)
pwd

#touch run.pid
if ps -ef | grep $(cat run.pid) 2>/dev/null;  then
    # 有 pid
    n=$(ps -ef | grep $(cat run.pid) 2>/dev/null | wc -l)
else
    n=0
fi

echo "pid number $n"

if [ $n -gt 1 ]; then
    echo "already running ..."
    ps -ef | grep $(cat run.pid)

    kill -9 $(cat run.pid)
    bash ${PWD}/scripts/run.sh &> /dev/null &
    #fi
else
    bash ${PWD}/scripts/run.sh &> /dev/null &
    echo 'is started'
    ps -ef | grep $(cat run.pid)
    #ps -ef | grep python3
fi

