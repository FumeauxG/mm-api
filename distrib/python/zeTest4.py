import keyboard
import time
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
    x = x*10
    y = y*10
    z = z*10
    scale = 1
    cmd = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand("units")

    cmd.AppendToolParameterCommand("worldX",x)
    cmd.AppendToolParameterCommand("worldY",y)
    cmd.AppendToolParameterCommand("worldZ",z)
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

#------------------------------------------------------------------------------------------------------------------------------
pathTemp = pathIn.split("\\")
print(pathTemp)

cmd = mmapi.StoredCommands()
cmd_key = cmd.AppendSceneCommand_FindObjectByName(pathTemp[1])
remote.runCommand(cmd)
result_val = mmapi.any_result()
bFound = cmd.GetSceneCommandResult_FindObjectByName(cmd_key, result_val)
print(result_val.i)
mainId = result_val.i;

# read the open file
pathObject = "C:/Gaetan/_Bachelor/mmAPI/mm-api/distrib/python/objet/cube.stl"
pathTemp = pathObject.split("\\")
print(pathTemp)

#import cube
cmd = mmapi.StoredCommands()
key = cmd.AppendSceneCommand_AppendMeshFile(pathObject);
remote.runCommand(cmd)

#id cube
cmd = mmapi.StoredCommands()
cmd_key = cmd.AppendSceneCommand_FindObjectByName("cube.stl")
remote.runCommand(cmd)
result_val = mmapi.any_result()
bFound = cmd.GetSceneCommandResult_FindObjectByName(cmd_key, result_val)
print(result_val.i)
supportId = result_val.i;

v = mmapi.vec3f()
v.x = x
v.y = y
v.z = z

cmd.AppendBeginToolCommand("transform")
cmd.AppendToolParameterCommand("scale",v)
cmd.AppendCompleteToolCommand("accept")
remote.runCommand(cmd)


# align the shape in the center
# construct commands to run
cmd = mmapi.StoredCommands()
cmd.AppendBeginToolCommand("align")
cmd.AppendCompleteToolCommand("accept")
# execute  commands
remote.runCommand(cmd);

cmd.AppendBeginToolCommand("transform")
remote.runCommand(cmd)
scaleX = 1
scaleY = 1
scaleZ = 1
v.x = 1
v.y = 1
v.z = 1

while True:
    if keyboard.is_pressed('q'):
        v.x = 1 + 1/x
        v.y = 1
        v.z = 1
        cmd.AppendToolParameterCommand("scale",v)
        remote.runCommand(cmd)
        x = x + 1;
        time.sleep(.300)
    if keyboard.is_pressed('w'):
        v.x = 1 - 1/x
        v.y = 1
        v.z = 1
        cmd.AppendToolParameterCommand("scale",v)
        remote.runCommand(cmd)
        x = x - 1;
        time.sleep(.300)
        
    if keyboard.is_pressed('a'):
        v.y = 1 + 1/y
        v.x = 1
        v.z = 1
        cmd.AppendToolParameterCommand("scale",v)
        remote.runCommand(cmd)
        y = y + 1;
        time.sleep(.300)
    if keyboard.is_pressed('s'):
        v.y = 1 - 1/y
        v.x = 1
        v.z = 1
        cmd.AppendToolParameterCommand("scale",v)
        remote.runCommand(cmd)
        y = y - 1;
        time.sleep(.300)
        
    if keyboard.is_pressed('y'):
        v.z = 1 + 1/z
        v.x = 1
        v.y = 1
        cmd.AppendToolParameterCommand("scale",v)
        remote.runCommand(cmd)
        z = z + 1;
        time.sleep(.300)
    if keyboard.is_pressed('x'):
        v.z = 1 - 1/z
        v.x = 1
        v.y = 1
        cmd.AppendToolParameterCommand("scale",v)
        remote.runCommand(cmd)
        z = z - 1;
        time.sleep(.300)
        
    if keyboard.is_pressed('1'):
        cmd.AppendCompleteToolCommand("accept")
        remote.runCommand(cmd)
        break
 
#Select the two objects 
select_objects = mmapi.vectori();
select_objects.push_back(supportId);
select_objects.push_back(mainId);
cmd2 = mmapi.StoredCommands()
cmd2.AppendSceneCommand_SelectObjects(select_objects)
remote.runCommand(cmd2)

#Boolean difference
cmd = mmapi.StoredCommands()
cmd.AppendBeginToolCommand("difference")
cmd.AppendToolParameterCommand("postReduce",False)
remote.runCommand(cmd)

print("Click accept")
while True:
    if keyboard.is_pressed('1'):
        break     
 
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

