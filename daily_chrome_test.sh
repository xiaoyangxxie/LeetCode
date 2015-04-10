cp=/jenkins/workspace
export PYTHONPATH=${PYTHONPATH}:$cp/Angel-automation-chrome/Automation/CXBProject/CX/Library
export DISPLAY=:19
output=$cp/AutomationReportChrome/
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
python /jenkins/workspace/Angel-automation-chrome/Automation/CXBProject/start_from_jenkins_linux.py -u $baseUrl -b $browser -e $loginEmail -p $loginPassword -m $runningModeule -a $tag -o $outputDir -j $project -t $RecordORTest
