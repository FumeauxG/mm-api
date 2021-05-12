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

# get all the objects
cmd1 = mmapi.StoredCommands()
key1 = cmd1.AppendSceneCommand_ListObjects()
remote.runCommand(cmd1)
objects = mmapi.vectori()
cmd1.GetSceneCommandResult_ListObjects(key1, objects)

# select all the objects
select_objects = mmapi.vectori();
for object in objects:
    select_objects.push_back(object);
cmd2 = mmapi.StoredCommands()
cmd2.AppendSceneCommand_SelectObjects(select_objects)
remote.runCommand(cmd2)

# delete all
cmd = mmapi.StoredCommands()
cmd.AppendSceneCommand_DeleteSelectedObjects();
remote.runCommand(cmd)

# read the open file
cmd = mmapi.StoredCommands()
key = cmd.AppendSceneCommand_AppendMeshFile(pathIn);
remote.runCommand(cmd)

###########################################################################
# Modify partition
cmd = mmapi.StoredCommands()
cmd.AppendBeginToolCommand("units")
key = cmd.AppendGetToolParameterCommand("worldX")
remote.runCommand(cmd)
result_val = mmapi.any_result()
bFound = cmd.GetToolParameterCommandResult(key, result_val)

if bFound:
    if result_val.type == 0:
        x = result_val.f
    elif result_val.type == 1:
        x = result_val.i
    elif result_val.type == 2:
        x = result_val.b
    elif result_val.type == 3:
        x = (result_val.x, result_val.y, result_val.z)
    elif result_val.type == 4:
        x = result_val.m
key = cmd.AppendGetToolParameterCommand("worldY")
remote.runCommand(cmd)
result_val = mmapi.any_result()
bFound = cmd.GetToolParameterCommandResult(key, result_val)

if bFound:
    if result_val.type == 0:
        y = result_val.f
    elif result_val.type == 1:
        y = result_val.i
    elif result_val.type == 2:
        y = result_val.b
    elif result_val.type == 3:
        y = (result_val.x, result_val.y, result_val.z)
    elif result_val.type == 4:
        y = result_val.m
key = cmd.AppendGetToolParameterCommand("worldZ")
remote.runCommand(cmd)
result_val = mmapi.any_result()
bFound = cmd.GetToolParameterCommandResult(key, result_val)

if bFound:
    if result_val.type == 0:
        z = result_val.f
    elif result_val.type == 1:
        z = result_val.i
    elif result_val.type == 2:
        z = result_val.b
    elif result_val.type == 3:
        z = (result_val.x, result_val.y, result_val.z)
    elif result_val.type == 4:
        z = result_val.m        
cmd.AppendCompleteToolCommand("accept")
remote.runCommand(cmd)

print(x)
print(y)
print(z)
scale = 0
if (x<5) or (y<5) or (z<5):
    scale = 1
    cmd = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand("units")

    cmd.AppendToolParameterCommand("worldX",x*10)
    cmd.AppendToolParameterCommand("worldY",y*10)
    cmd.AppendToolParameterCommand("worldZ",z*10)
    cmd.AppendCompleteToolCommand("accept")
    remote.runCommand(cmd)
###########################################################################

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

cmd.AppendToolParameterCommand("overhangAngleTolerance",65) #Angle Thresh
cmd.AppendToolParameterCommand("contactTolerance",0)        #Contact Tol
cmd.AppendToolParameterCommand("verticalOffset",0)          #Y-offset

cmd.AppendToolParameterCommand("maxDraftAngle",60)      #Max Angle
cmd.AppendToolParameterCommand("density",0.9)           #Density 0 to 1
cmd.AppendToolParameterCommand("layerHeight",0.15)      #Layer Height
cmd.AppendToolParameterCommand("postTopSize",1)         #Post Diameter
cmd.AppendToolParameterCommand("postTipSize",1)         #Tip Diameter
cmd.AppendToolParameterCommand("postDiscSize",1)       #Base Diameter    

cmd.AppendToolParameterCommand("postTipHeight",2)       #Tip Height
cmd.AppendToolParameterCommand("postDiscHeight",0.4)    #Base Height
cmd.AppendToolParameterCommand("strutDensity",0)        #Strut Density 0 to 1
cmd.AppendToolParameterCommand("solidMinOffset",0.3)    #Solid Min Offset
cmd.AppendToolParameterCommand("postResolution",8)      #Post Sides
cmd.AppendToolParameterCommand("optimizeRounds",100)    #Optimization
cmd.AppendToolParameterCommand("allowTopSupport",False) #Allow Top Connections

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

###########################################################################
# Modify partition
cmd = mmapi.StoredCommands()
cmd.AppendBeginToolCommand("units")
key = cmd.AppendGetToolParameterCommand("worldX")
remote.runCommand(cmd)
result_val = mmapi.any_result()
bFound = cmd.GetToolParameterCommandResult(key, result_val)

if bFound:
    if result_val.type == 0:
        x = result_val.f
    elif result_val.type == 1:
        x = result_val.i
    elif result_val.type == 2:
        x = result_val.b
    elif result_val.type == 3:
        x = (result_val.x, result_val.y, result_val.z)
    elif result_val.type == 4:
        x = result_val.m
key = cmd.AppendGetToolParameterCommand("worldY")
remote.runCommand(cmd)
result_val = mmapi.any_result()
bFound = cmd.GetToolParameterCommandResult(key, result_val)

if bFound:
    if result_val.type == 0:
        y = result_val.f
    elif result_val.type == 1:
        y = result_val.i
    elif result_val.type == 2:
        y = result_val.b
    elif result_val.type == 3:
        y = (result_val.x, result_val.y, result_val.z)
    elif result_val.type == 4:
        y = result_val.m
key = cmd.AppendGetToolParameterCommand("worldZ")
remote.runCommand(cmd)
result_val = mmapi.any_result()
bFound = cmd.GetToolParameterCommandResult(key, result_val)

if bFound:
    if result_val.type == 0:
        z = result_val.f
    elif result_val.type == 1:
        z = result_val.i
    elif result_val.type == 2:
        z = result_val.b
    elif result_val.type == 3:
        z = (result_val.x, result_val.y, result_val.z)
    elif result_val.type == 4:
        z = result_val.m        
cmd.AppendCompleteToolCommand("accept")
remote.runCommand(cmd)

print(x)
print(y)
print(z)

if scale == 1:
    cmd = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand("units")

    cmd.AppendToolParameterCommand("worldX",x/10)
    cmd.AppendToolParameterCommand("worldY",y/10)
    cmd.AppendToolParameterCommand("worldZ",z/10)
    cmd.AppendCompleteToolCommand("accept")
    remote.runCommand(cmd)
###########################################################################

# export the support
cmd = mmapi.StoredCommands()
cmd.AppendSceneCommand_ExportMeshFile_CurrentSelection(pathOut)
remote.runCommand(cmd)

raw_input("Press Enter to close...")

#done!
remote.shutdown();

