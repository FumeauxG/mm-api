import glob
import mmapi
from mmRemote import *;

txtfiles = []
for file in glob.glob("C:/Gaetan/_Bachelor/mmAPI/mm-api/distrib/python/test/*.stl"):
    txtfiles.append(file)
 
# entry file 
pathIn = txtfiles[0];

pathTemp = pathIn.split('.')

# out file
pathOut = pathTemp[0] + '_support.' + pathTemp[1]

# initialize connection
remote = mmRemote();
remote.connect();

# delete all
cmd = mmapi.StoredCommands()
cmd.AppendSceneCommand_DeleteSelectedObjects();
remote.runCommand(cmd)

# read the open file
cmd = mmapi.StoredCommands()
key = cmd.AppendSceneCommand_AppendMeshFile(pathIn);
remote.runCommand(cmd)

# align the shape in the center
# construct commands to run
cmd = mmapi.StoredCommands()
cmd.AppendBeginToolCommand("align")
cmd.AppendCompleteToolCommand("accept")
# execute  commands
remote.runCommand(cmd);

# creation of support
# construct commands to run
cmd = mmapi.StoredCommands()
cmd.AppendBeginToolCommand("overhangs")
cmd.AppendToolUtilityCommand("generateSupport")
cmd.AppendToolUtilityCommand("convertToSolid",0)
cmd.AppendCompleteToolCommand("accept")
# execute  commands
remote.runCommand(cmd);

# delete the shape (keep the support)
cmd = mmapi.StoredCommands()
cmd.AppendSceneCommand_DeleteSelectedObjects();
remote.runCommand(cmd)

# get all the objects (here the support)
cmd1 = mmapi.StoredCommands()
key1 = cmd1.AppendSceneCommand_ListObjects()
remote.runCommand(cmd1)
objects = mmapi.vectori()
cmd1.GetSceneCommandResult_ListObjects(key1, objects)

# select the support
select_objects = mmapi.vectori();
for object in objects:
    select_objects.push_back(object);
cmd2 = mmapi.StoredCommands()
cmd2.AppendSceneCommand_SelectObjects(select_objects)
remote.runCommand(cmd2)

# export the support
cmd = mmapi.StoredCommands()
cmd.AppendSceneCommand_ExportMeshFile_CurrentSelection(pathOut)
remote.runCommand(cmd)

#done!
remote.shutdown();

