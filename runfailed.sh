cp=/jenkins/workspace
export PYTHONPATH=${PYTHONPATH}:$cp/Angel-automation-failedcase-test/Automation/CXBProject/CX/Library
export DISPLAY=:19
echo "display is set"
#firefox &
sleep 5
#nohup firefox &
#echo "firefox is started"
output=$cp/failedreport/
if [ -d "$output" ]; then
    echo "file is existed"
    rm -R "$output"
    mkdir "$output"
    echo "delete and create $ouput"
else
    mkdir "$output"
    echo "create $output"
fi
#pybot --test Reg_CT_54 --outputdir "$cp/report" "$cp/CXBChrome/CX"
pybot --suite Transaction_Page --outputdir "$cp/failedreport" "$cp/Angel-automation-failedcase-test/Automation/CXBProject/CX"
