cp=/jenkins/workspace
export PYTHONPATH=${PYTHONPATH}:$cp/Angel-automation-feature-test/Automation/CXBProject/CX/Library
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
#pybot --test Reg_CT_54 --outputdir "$cp/report" "$cp/CXBChrome/CX"
pybot -i Debug --outputdir "$cp/report" "$cp/rf_tests/Automation/CXBProject/CX"
