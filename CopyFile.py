__author__ = 'xyang'
import glob
import shutil

targetDir = "D:\\NGTTProject\\aPage\\Multi_ASR\\800-002-1020"
existFile = "D:\\NGTTProject\\aPage\\Multi_ASR\\800-002-1020\\newcard_*.vxml"
sourceFile = "D:\\NGTTProject\\aPage\\Multi_ASR\\800-002-1020\\card_*.vxml"

def copyfile(match,name):
    exitfile = getMachedFile(match)
    print exitfile
    for file in glob.glob(sourceFile):
        #print file,type(file)
        filename = file.split('\\')
        #print filename[5]
        newfile = name + filename[5]
        print newfile
        if newfile in exitfile:
            print "file is existed,escape this step"

        else:
            shutil.copyfile(file,newfile)
            shutil.move(newfile,targetDir)

def getMachedFile(match):
    filelist = []
    exitfile = glob.iglob(match)
    for p in exitfile:
        plist = p.split('\\')
        pfilename = plist[5]
        filelist.append(pfilename)
    return filelist

if __name__ == '__main__':
    copyfile(existFile,"new")
    #getMachedFile(targetDir)