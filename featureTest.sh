cp=/jenkins/workspace
export PYTHONPATH=${PYTHONPATH}:$cp/Angel-automation-feature-test/Automation/CXBProject/CX/Library
export DISPLAY=:19
echo "display is set"
#firefox &
sleep 5
#nohup firefox &
#echo "firefox is started"
output=$cp/featurereport/
if [ -d "$output" ]; then
    echo "file is existed"
    rm -R "$output"
    mkdir "$output"
    echo "delete and create $ouput"
else
    mkdir "$output"
    echo "create $output"
fi
#pybot --suite $feature --outputdir "$cp/featurereport" "$cp/angel_cxb_linux_firefox/Automation/CXBProject/CX"
pybot -i $feature  --outputdir "$cp/featurereport" "$cp/Angel-automation-feature-test/Automation/CXBProject/CX"
