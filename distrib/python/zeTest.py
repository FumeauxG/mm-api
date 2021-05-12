import mmapi
from mmRemote import *;

path = "C:/Gaetan/_Bachelor/mmAPI/mm-api/distrib/python/0/0.stl";

# initialize connection
remote = mmRemote();
remote.connect();

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

cmd.AppendToolParameterCommand("maxDraftAngle",70)      #Max Angle
cmd.AppendToolParameterCommand("density",0.9)           #Density 0 to 1
cmd.AppendToolParameterCommand("layerHeight",0.15)      #Layer Height
cmd.AppendToolParameterCommand("postTopSize",3)         #Post Diameter
cmd.AppendToolParameterCommand("postTipSize",3)         #Tip Diameter
cmd.AppendToolParameterCommand("postDiscSize",10)       #Base Diameter    

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

# export the support
cmd = mmapi.StoredCommands()
cmd.AppendSceneCommand_ExportMeshFile_CurrentSelection(path)
remote.runCommand(cmd)

#done!
remote.shutdown();

