#/bin/bash
#This script is to start CXB Project from shell command
#Author: Amy
basepath=$(pwd)
echo $basepath
export PYTHONPATH=${PYTHONPATH}:$basepath/CX/Library
while getopts ":a:b:c:d:e:f:g:" opt

do

        case $opt in

                a )
                        baseurl=$OPTARG;;
                b )
 		        loginEmail=$OPTARG;;
                c )
                        loginPassword=$OPTARG;;
                d )
                        runningModeule=$OPTARG;;
                e )
                        suite=$OPTARG;;
                f )
                        tag=$OPTARG;;
                g )
                        outputDir=$OPTARG;;
                ? )
                        echo "error"                    
                        exit 1;;
                esac
done
shift $(($OPTIND - 1))
echo "$baseurl"
if test -z "$baseurl" 
then
   echo "please insert -a baseurl"
   exit 1
else
   echo "base url is not null"
fi
if test -z "$loginEmail"
then
   echo "please insert -b loginEmail"
   exit 1
else
   echo "loginEmail is not null"
fi

if test -z "$loginPassword"
then
   echo "please insert -c loginPassword"
   exit 1
else
   echo "loginPassword is not null"
fi

if test -z "$runningModeule"
then
   echo "please insert -d runningModeule"
   exit 1
else
   echo "runningModeule is not null"
fi

if test -z "$suite"
then
   echo "please insert -e suite"
   exit 1
else
   echo "suite is not null"
fi

if test -z "$tag"
then
   echo "please insert -f tag"
else
   echo "tag is not null"
fi

if test -z "$outputDir"
then
   echo "please insert -g outputdir"
   exit 1
else
   echo "outputdir is not null"
fi

if [ -d "$outputDir" ]; then
    echo "file is existed"
    rm -R "$outputDir"
    mkdir "$outputDir"
    echo "delete and create $outputDir"
else
    mkdir "$outputDir"
    echo "create $outputDir"
fi

python $basepath/start_from_jenkins_linux.py -u "$baseurl" -b ff -e "$loginEmail" -p "$loginPassword" -m "$runningModeule" -i "$suite"  -a "$tag" -o "$outputDir" -j CX -t r
