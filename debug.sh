cp=/jenkins/workspace
export PYTHONPATH=${PYTHONPATH}:$cp/Angel-automation-failedcase-test/Automation/CXBProject/CX/Library
export DISPLAY=:19
output=$cp/AutomationFailedReport/
if [ -d "$output" ]; then
    echo "file is existed"
    rm -R "$output"
    mkdir "$output"
    echo "delete and create $ouput"
    cd $output
    mkdir "report"
else
    mkdir "$output"
    echo "create $output"
    cd $output
    mkdir "report"
fi
pybot --test Reg_Sch_08 --outputdir "$cp/report" "$cp/Angel-automation-failedcase-test/Automation/CXBProject/CX"
