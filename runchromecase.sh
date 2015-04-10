cp=/jenkins/workspace
export PYTHONPATH=${PYTHONPATH}:$cp/rf_tests/Automation/CXBProject/CX/Library
export DISPLAY=:19
echo "display is set"
#firefox &
sleep 5
#nohup firefox &
#echo "firefox is started"
output=$cp/chromereport/
if [ -d "$output" ]; then
    echo "file is existed"
    rm -R "$output"
    mkdir "$output"
    echo "delete and create $ouput"
else
    mkdir "$output"
    echo "create $output"
fi
pybot --test Reg_CT_03-6 --outputdir "$cp/chromereport" "$cp/rf_tests/Automation/CXBProject/CX"
