import keyboard
import time
import math
import glob
import mmapi
from mmRemote import *;

delay = .200

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
#angle management
while True:
    if keyboard.is_pressed('q'):
        #rotation in degrees
        rX = math.radians(-90)
        rY = 0
        rZ = 0

        #convert degrees to the transformation vector stuff
        r1 = math.cos(rY ) * math.cos(rZ)
        r2 = math.sin(rZ)
        r3 = -math.sin(rY) * math.cos(rZ)
        r4 = -math.cos(rY) * math.sin(rZ) * math.cos(rX) + math.sin(rY) * math.sin(rX)
        r5 = math.cos(rZ) * math.cos(rX)
        r6 = math.sin(rY) * math.sin(rZ) * math.cos(rX) + math.cos(rY) * math.sin(rX)
        r7 = math.cos(rY) * math.sin(rZ) * math.sin(rX) + math.sin(rY) * math.cos(rX)
        r8 = -math.cos(rZ) * math.sin(rX)
        r9 = -math.sin(rY) * math.sin(rZ) * math.sin(rX) + math.cos(rY) * math.cos(rX)

        cmd.AppendBeginToolCommand("transform")
        cmd.AppendToolParameterCommand("rotation",r1,r2,r3,r4,r5,r6,r7,r8,r9)
        cmd.AppendCompleteToolCommand("accept")
        remote.runCommand(cmd)
        time.sleep(delay)
    if keyboard.is_pressed('a'):
        #rotation in degrees
        rX = 0
        rY = math.radians(-90)
        rZ = 0

        #convert degrees to the transformation vector stuff
        r1 = math.cos(rY ) * math.cos(rZ)
        r2 = math.sin(rZ)
        r3 = -math.sin(rY) * math.cos(rZ)
        r4 = -math.cos(rY) * math.sin(rZ) * math.cos(rX) + math.sin(rY) * math.sin(rX)
        r5 = math.cos(rZ) * math.cos(rX)
        r6 = math.sin(rY) * math.sin(rZ) * math.cos(rX) + math.cos(rY) * math.sin(rX)
        r7 = math.cos(rY) * math.sin(rZ) * math.sin(rX) + math.sin(rY) * math.cos(rX)
        r8 = -math.cos(rZ) * math.sin(rX)
        r9 = -math.sin(rY) * math.sin(rZ) * math.sin(rX) + math.cos(rY) * math.cos(rX)

        cmd.AppendBeginToolCommand("transform")
        cmd.AppendToolParameterCommand("rotation",r1,r2,r3,r4,r5,r6,r7,r8,r9)
        cmd.AppendCompleteToolCommand("accept")
        remote.runCommand(cmd)
        time.sleep(delay)       
    if keyboard.is_pressed('y'):
        #rotation in degrees
        rX = 0
        rY = 0
        rZ = math.radians(-90)

        #convert degrees to the transformation vector stuff
        r1 = math.cos(rY ) * math.cos(rZ)
        r2 = math.sin(rZ)
        r3 = -math.sin(rY) * math.cos(rZ)
        r4 = -math.cos(rY) * math.sin(rZ) * math.cos(rX) + math.sin(rY) * math.sin(rX)
        r5 = math.cos(rZ) * math.cos(rX)
        r6 = math.sin(rY) * math.sin(rZ) * math.cos(rX) + math.cos(rY) * math.sin(rX)
        r7 = math.cos(rY) * math.sin(rZ) * math.sin(rX) + math.sin(rY) * math.cos(rX)
        r8 = -math.cos(rZ) * math.sin(rX)
        r9 = -math.sin(rY) * math.sin(rZ) * math.sin(rX) + math.cos(rY) * math.cos(rX)

        cmd.AppendBeginToolCommand("transform")
        cmd.AppendToolParameterCommand("rotation",r1,r2,r3,r4,r5,r6,r7,r8,r9)
        cmd.AppendCompleteToolCommand("accept")
        remote.runCommand(cmd)
        time.sleep(delay)
        
  
    if keyboard.is_pressed('1'):
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
        break

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

#Cube or cylender
while True:
    if keyboard.is_pressed('1'):
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
        break;
    if keyboard.is_pressed('2'):
        # read the open file
        pathObject = "C:/Gaetan/_Bachelor/mmAPI/mm-api/distrib/python/objet/cylender.stl"
        pathTemp = pathObject.split("\\")
        print(pathTemp)

        #import cylender
        cmd = mmapi.StoredCommands()
        key = cmd.AppendSceneCommand_AppendMeshFile(pathObject);
        remote.runCommand(cmd)

        #id cylender
        cmd = mmapi.StoredCommands()
        cmd_key = cmd.AppendSceneCommand_FindObjectByName("cylender.stl")
        remote.runCommand(cmd)
        result_val = mmapi.any_result()
        bFound = cmd.GetSceneCommandResult_FindObjectByName(cmd_key, result_val)
        print(result_val.i)
        supportId = result_val.i;
        break;

v = mmapi.vec3f()
v.x = x
v.y = y
v.z = z

cmd.AppendBeginToolCommand("transform")
cmd.AppendToolParameterCommand("dimensions",v)
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


translate = mmapi.vec3f()

translate.x = 0
translate.y = 0
translate.z = 0

xTemp = x
x = z 
z = y 
y = xTemp 

while True:
    if keyboard.is_pressed('q'):
        x = x + 1
        v.x = x
        v.y = y
        v.z = z
        cmd.AppendToolParameterCommand("dimensions",v)
        remote.runCommand(cmd)
        time.sleep(delay)
    if keyboard.is_pressed('w'):
        x = x - 1
        v.x = x
        v.y = y
        v.z = z
        cmd.AppendToolParameterCommand("dimensions",v)
        remote.runCommand(cmd)
        time.sleep(delay)
        
    if keyboard.is_pressed('a'):
        y = y + 1
        v.x = x
        v.y = y
        v.z = z
        cmd.AppendToolParameterCommand("dimensions",v)
        remote.runCommand(cmd)
        time.sleep(delay)
    if keyboard.is_pressed('s'):
        y = y - 1
        v.x = x
        v.y = y
        v.z = z
        cmd.AppendToolParameterCommand("dimensions",v)
        remote.runCommand(cmd)
        time.sleep(delay)
        
    if keyboard.is_pressed('y'):
        z = z + 1
        v.x = x
        v.y = y
        v.z = z
        cmd.AppendToolParameterCommand("dimensions",v)
        remote.runCommand(cmd)
        time.sleep(delay)
    if keyboard.is_pressed('x'):
        z = z - 1
        v.x = x
        v.y = y
        v.z = z
        cmd.AppendToolParameterCommand("dimensions",v)
        remote.runCommand(cmd)
        time.sleep(delay)


    if keyboard.is_pressed('e'):
        translate.x = 1
        translate.y = 0
        translate.z = 0
        cmd.AppendToolParameterCommand("translationWorld",translate)
        remote.runCommand(cmd)
        translate.x = 0
        translate.y = 0
        translate.z = 0
        cmd.AppendToolParameterCommand("translationWorld",translate)
        remote.runCommand(cmd)
        time.sleep(delay)
    if keyboard.is_pressed('r'):
        translate.x = -1
        translate.y = 0
        translate.z = 0
        cmd.AppendToolParameterCommand("translationWorld",translate)
        remote.runCommand(cmd)
        translate.x = 0
        translate.y = 0
        translate.z = 0
        cmd.AppendToolParameterCommand("translationWorld",translate)
        remote.runCommand(cmd)
        time.sleep(delay)
        
    if keyboard.is_pressed('d'):
        translate.x = 0
        translate.y = 1
        translate.z = 0
        cmd.AppendToolParameterCommand("translationWorld",translate)
        remote.runCommand(cmd)
        translate.x = 0
        translate.y = 0
        translate.z = 0
        cmd.AppendToolParameterCommand("translationWorld",translate)
        remote.runCommand(cmd)
        time.sleep(delay)
    if keyboard.is_pressed('f'):
        translate.x = 0
        translate.y = -1
        translate.z = 0
        cmd.AppendToolParameterCommand("translationWorld",translate)
        remote.runCommand(cmd)
        translate.x = 0
        translate.y = 0
        translate.z = 0
        cmd.AppendToolParameterCommand("translationWorld",translate)
        remote.runCommand(cmd)
        time.sleep(delay)
        
    if keyboard.is_pressed('c'):
        translate.x = 0
        translate.y = 0
        translate.z = 1
        cmd.AppendToolParameterCommand("translationWorld",translate)
        remote.runCommand(cmd)
        translate.x = 0
        translate.y = 0
        translate.z = 0
        cmd.AppendToolParameterCommand("translationWorld",translate)
        remote.runCommand(cmd)
        time.sleep(delay)
    if keyboard.is_pressed('v'):
        translate.x = 0
        translate.y = 0
        translate.z = -1
        cmd.AppendToolParameterCommand("translationWorld",translate)
        remote.runCommand(cmd)
        translate.x = 0
        translate.y = 0
        translate.z = 0
        cmd.AppendToolParameterCommand("translationWorld",translate)
        remote.runCommand(cmd)
        time.sleep(delay)
        
  
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

