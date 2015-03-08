import os
import time   
import re

i=0 
logfile = "/var/www/trash03_02/testforsed.txt"
openfluidProject_folder = "/home/openfluid202-from-git/lib-from-michael/BourdicOF" #Path without / in the end
while (i<1):
    # Check empty file
    if os.stat(logfile).st_size ==  0: 
        time.sleep(1)
    else :
        i=1
        #################################
        # PART 0 : Create new Openfluid files
        #################################
        # Read first line of the log
        first = open(logfile).readline()
        # Parse first line of the log file
        parse_list = first.split(";")
        # Get id from the first line of the log
        parse_logid = parse_list[0]
        # Create Openfluid files with custom name
        os.system("cp -R "+openfluidProject_folder+ " "+openfluidProject_folder+parse_logid)
        
        #################################
        # PART 1 : Edit created Openfluid files
        #################################
        # I - List activated simulators 
        # -------------------------------
        # I.A - List checked simulators from Mapfish client
        # -------------------------------
        # Parse simulators
        parse_simulators = parse_list[2].split(",")
        #print parse_simulators
        # -------------------------------
        # I.B - List checked simulators from Mapfish client
        # -------------------------------    
        # SU 
        parse_su = parse_list[3].split(",")
        #print parse_su
        edited_monitoringfluidx_su = ""
        for u in parse_su : 
            if edited_monitoringfluidx_su == "" :
                edited_monitoringfluidx_su = edited_monitoringfluidx_su + u
                #print u
            else : 
                edited_monitoringfluidx_su = edited_monitoringfluidx_su + ";" + u
        # RS
        parse_rs = parse_list[4].split(",")
        #print parse_rs
        edited_monitoringfluidx_rs = ""
        for u in parse_rs : 
            if edited_monitoringfluidx_rs == "" :
                edited_monitoringfluidx_rs = edited_monitoringfluidx_rs + u
                #print u
            else : 
                edited_monitoringfluidx_rs = edited_monitoringfluidx_rs + ";" + u
       
        # II - Edits the Openfluid config files
        # -------------------------------
        # II.A - Enable/disable simulators in model.fluidx   
        # -------------------------------        
        # Initializes the editor variable  
        edited_modelfluidx = ""
        # Reads each line of the file
        for line in open(openfluidProject_folder+parse_logid+"/IN/model.fluidx"):
            # If the line simulator corresponds to the deactivated simulator
            if any(s in line for s in parse_simulators):
                # Replace 0 to 1 and add the editor variable
                edited_modelfluidx = edited_modelfluidx + line.replace('0','1')
                #print line
            else :
                # Add the editor variable
                edited_modelfluidx = edited_modelfluidx + line
        # Rewrite the file with the editor variable                
        f = open(openfluidProject_folder+parse_logid+"/IN/model.fluidx", 'w')
        f.write(edited_modelfluidx)
        f.close()
        # Delete current line in the log file (the first one)
        #os.system("sed -i '1,1d' "+logfile)
        # -------------------------------    
        # II.B - Enable/disable simulators in model.fluidx   
        # -------------------------------          
        # Edit "Parcelles" line in monitoringfluix
        os.system("sed -i 's#\"geoserie.FinalSU.vars\" value=\"\"#\"geoserie.FinalSU.vars\" value=\"%s\"#g' %s" % (edited_monitoringfluidx_su,openfluidProject_folder+parse_logid+"/IN/monitoring.fluidx"))
        # Edit "Reseau hydro" line in monitoringfluix
        os.system("sed -i 's#\"geoserie.FinalRS.vars\" value=\"\"#\"geoserie.FinalRS.vars\" value=\"%s\"#g' %s" % (edited_monitoringfluidx_su,openfluidProject_folder+parse_logid+"/IN/monitoring.fluidx"))
        # ------------------------------- 
        # Delete current line in the log file (the first one)
        #os.system("sed -i '1,1d' "+logfile)

        #################################
        # PART 2 : Openfluid simulation
        #################################

        # Launch simulation
        # os.system("openfluid -w /home/openfluid202-from-git/lib-from-michael/BourdicOF/ -c")
        # Send mail
        #  os.system("b=$(sed -n '4p' /var/www/pywps/processes/bourdic_v2_railing.txt) ; c=$(echo $b | cut -d'=' -f 2) ; sh /var/www/pywps/processes/bourdic_v2_mail.sh $c")
