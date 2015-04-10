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
python /jenkins/workspace/Angel-automation-failedcase-test/Automation/CXBProject/start_from_jenkins_linux.py -u $baseUrl -b $browser -e $loginEmail -p $loginPassword -m $runningModeule -o $outputDir -j $project -t $RecordORTest -i $suite -r $runfailedcase
