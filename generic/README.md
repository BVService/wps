inserver.py
===============

inserver.py is a daemon which check if the log file (**railing.txt**) is empty or not.
If the log file is not empty, the daemon parse the first line. 
Collected informations are used to configure **model.fluidx** and **monitoring.fluidx** and then execute the OpenFLUID modeling software.

railing.txt
===============

Each line of railing.txt contains the following informations separated by semicolons:
- An identifier
- The user's email address
- The name of the simulators that will be activated in the model.fluidx file (*Enable = 0 becomes Enable = 1*)
- The name of the plot indicators that will be used in the monitoring.fluidx
- The name of the riversystem indicators that will be used in the monitoring.fluidx

Here is an extract of railing.txt:
```
1;me@mymail.com;stat.upper.su,water.surf.totalvolume-su,water.surf.max-outflow-su,stat.upper.rs,water.surf.overflow-rs;stat.upper.number=>UpNum,water.surf.V.total-su=>VolTot,water.surf.Q.maxdownstream-su=>QMax;stat.upper.number=>UpNum,water.surf.H.overflow-rs=>HeighMax;
```

Which represents the following information : 

| identifier | user's email  | Name of the simulators                                                                                 | plot indicators                                                                            | riversystem indicators                                      |
|------------|---------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| 1          | me@mymail.com | stat.upper.su,water.surf.totalvolume-su,water.surf.max-outflow-su,stat.upper.rs,water.surf.overflow-rs | stat.upper.number=>UpNum,water.surf.V.total-su=>VolTot,water.surf.Q.maxdownstream-su=>QMax | stat.upper.number=>UpNum,water.surf.H.overflow-rs=>HeighMax |

model.fluidx
===============

Model.fluidx is a configuration file for the modeling performed with the OpenFLUID software. The file contains a list of simulators that can be activated by **inserver.py** by replacing `enable = "0"` to `enable = "1"`. Here is an extract : 
```
<simulator ID="water.surf.max-outflow-su" enabled="1">
</simulator>
<simulator ID="water.surf.overflow-rs" enabled="1">
</simulator>
<simulator ID="water.surf.totalvolumeoverflow-rs" enabled="1">
</simulator> 
```
The simulators are activated by **inserver.py** when simulators contained in the column "Name of the simulators" of **railing.txt** and those in **model.fluidx** match.

monitoring.fluidx
===============

Monitoring.fluidx is a configuration file for the modeling performed with the OpenFLUID software. 
The file contains a list of observer that can be modified by **inserver.py**. The calculations for the plots are located into the line `<param name="geoserie.FinalSU.vars" value="">` while the calculations for the water system are located into the line `<param name="geoserie.FinalRS.vars" value="">`.
Here is an extract : 
```
<observer ID="export.vars.files.geovector" enabled="1">
<param name="format" value="ESRI Shapefile" />
<param name="outsubdir" value="outshapefile" />
<param name="geoserie.FinalSU.sourcefile" value="../OUT/shapefiles/SU_topology.shp" />
<param name="geoserie.FinalSU.vars" value="stat.upper.number=>UpNum;water.surf.V.total-su=>VolTot;water.surf.Q.maxdownstream-su=>QMax" />
<param name="geoserie.FinalSU.unitsclass" value="SU" />
<param name="geoserie.FinalSU.when" value="final" />
<param name="geoserie.FinalRS.sourcefile" value="../OUT/shapefiles/RS_topology.shp" />
<param name="geoserie.FinalRS.vars" value="stat.upper.number=>UpNum;water.surf.H.overflow-rs=>HeighMax" />
<param name="geoserie.FinalRS.unitsclass" value="RS" />
<param name="geoserie.FinalRS.when" value="final" />
</observer>
```
