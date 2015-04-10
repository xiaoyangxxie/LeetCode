cp=/jenkins/workspace
export PYTHONPATH=${PYTHONPATH}:$cp/angel_cxb_linux_firefox/Automation/CXBProject/CX/Library
cd $cp/angel_cxb_linux_firefox/Automation/CXBProject
hg pull
hg update
export DISPLAY=:19
echo "display is set"
#firefox &
sleep 5
#nohup firefox &
#echo "firefox is started"
output=$cp/rf_report/
if [ -d "$output" ]; then
    echo "file is existed"
    rm -R "$output"
    mkdir "$output"
    echo "delete and create $ouput"
else
    mkdir "$output"
    echo "create $output"
fi
pybot --test Advanced_Option_TC-16.1 --outputdir "$cp/rf_report" "$cp/angel_cxb_linux_firefox/Automation/CXBProject/CX"
