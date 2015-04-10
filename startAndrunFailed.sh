cp=/jenkins/workspace
export PYTHONPATH=${PYTHONPATH}:$cp/Angel-automation-firefox/Automation/CXBProject/CX/Library
export DISPLAY=:19
python /jenkins/workspace/Angel-automation-firefox/Automation/CXBProject/start_from_jenkins_linux.py -u $baseUrl -b $browser -e $loginEmail -p $loginPassword -m $runningModeule -a $tag -o $outputDir -j $project -t $RecordORTest
