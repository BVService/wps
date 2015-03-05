inserver.py
===============

inserver.py is a daemon which check if the log file (railing.txt) is empty or not.
If the log file is not empty, the daemon parse the first line. 
Collected informations are used to configure and execute the OpenFLUID modeling software.

Each line of the log file (railing.txt) contains the following information separated by semicolons:
- An identifier
- The user's email address
- The name simulators that will be activated in the model.fluidx file (Enable = 0 becomes Enable = 1)
- The name of the plot indicators that will be used in the monitoring.fluidx
- The name of the riversystem indicators that will be used in the monitoring.fluidx

Here is an extract of railing.txt:
`1;mail@gmail.com;stat.upper.su,water.surf.totalvolume-su,water.surf.max-outflow-su,stat.upper.rs,water.surf.overflow-rs;stat.upper.number=>UpNum,water.surf.V.total-su=>VolTot,water.surf.Q.maxdownstream-su=>QMax;stat.upper.number=>UpNum,water.surf.H.overflow-rs=>HeighMax;`
