cp=/jenkins/workspace
export PYTHONPATH=${PYTHONPATH}:$cp/CXB-Firefox/CX/Library
cd $cp/CXB-Firefox
git checkout uat
cd $cp/CXB-Firefox/CX
git pull
export DISPLAY=:19
echo "display is set"
#firefox &
sleep 5
#nohup firefox &
#echo "firefox is started"
output=$cp/report/
if [ -d "$output" ]; then
    echo "file is existed"
    rm -R "$output"
    mkdir "$output"
    echo "delete and create $ouput"
else
    mkdir "$output"
    echo "create $output"
fi
pybot --suite Call_Queue_Page  --outputdir "$cp/report" "$cp/CXB-Firefox/CX"
