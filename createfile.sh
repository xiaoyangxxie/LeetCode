cp=/jenkins/workspace
echo $cp
output=$cp/AutomationReport/
if [ -d "$output" ]; then
    echo "file is existed"
    rm -R "$output"
    mkdir "$output"
    echo "delete and create $ouput"
    cd $cp/AutomationReport/
    mkdir "report"
else
    mkdir "$output"
    echo "create $output"
    cd $cp/AutomationReport/
    mkdir "report"
fi
