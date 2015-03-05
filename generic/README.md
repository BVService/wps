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

| identifier | user's email  | Name of the simulators                                                                                 | plot indicators                                                                             | riversystem indicators                                      |
|------------|---------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| 1          | me@mymail.com | stat.upper.su,water.surf.totalvolume-su,water.surf.max-outflow-su,stat.upper.rs,water.surf.overflow-rs | ;stat.upper.number=>UpNum,water.surf.V.total-su=>VolTot,water.surf.Q.maxdownstream-su=>QMax | stat.upper.number=>UpNum,water.surf.H.overflow-rs=>HeighMax |

model.fluidx
===============

Model.fluidx is a configuration file for the modeling performed with the OpenFLUID software.
Here is an extract : 
```
<simulator ID="land.surf.representation.geomhydas" enabled="1">
<param name="GraphAnalysis" value="true"/>
<param name="FluidxFile" value="true"/>
<param name="LineLayers" value="reachs=/GeoData/bourdic_rs.shp"/>
<param name="PolygonLayers" value="fields=/GeoData/bourdic_su.shp"/>
<param name="RasterLayers" value="dem=/GeoData/bourdic_dem.tif"/>
</simulator>
```
The file contains a list of simulators that can be activated or deactivated by adding 1 or 0 to Enable.
