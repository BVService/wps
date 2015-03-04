from pywps.Process import WPSProcess       
import os
import time
import subprocess                  
class Process(WPSProcess):
####################################################################################
#The script is an asynchronous WPS which execute a modeling from OpenFLUID software.
#For this, the script fills a log file on the server from the parameters selected by 
#the user in the window addon of the MapFishApp viewer. This log file will then be 
#read by a daemon on the server to configure and execute the OpenFLUID modeling software.
####################################################################################

    def __init__(self):

        # Process initialization
        WPSProcess.__init__(self,
            identifier = "wps_generic",
            title="wps_generic",
            abstract="""WPS pour le Bourdic""",
            version = "1.0",
            storeSupported = True,
            statusSupported = True)

        # Adding process inputs

        self.input1OnlyInPython = self.addLiteralInput(identifier="L_input_param1",
                    title = "Email (ex jean.dupont@free.fr)",
                    type = type("")) 

        #self.input1OnlyInPython = self.addLiteralInput(identifier = "L_input_param1", # input_param1, input_url1
                    #title = "Input 1 (parametre litteral)",
                    #abstract = "Field of type INTEGER specifying a time delay in seconds.",
                    #type = type(2))
                    #(1,2,3,(5,9),10,"a",("d","g")))

        #self.input2OnlyInPython = self.addLiteralInput(identifier = "L_input_param2", # input_param1, input_url1
                    #title = "Input 2 (parametre litteral)",
                    #abstract = "Field of type INTEGER specifying a time delay in seconds.",
                    #type = type(1.0))

        #self.input3OnlyInPython = self.addLiteralInput(identifier = "L_input_param3", # input_param1, input_url1
                    #title = "Input 3 (parametre litteral)",
                    #abstract = "Field of type INTEGER specifying a time delay in seconds.",
                    #type = type(1.0))

        #self.input40OnlyInPython = self.addLiteralInput(identifier = "L_input_param4", # input_param1, input_url1
                    #title = "Input 4 (parametre litteral)",
                    #abstract = "Field of type INTEGER specifying a time delay in seconds.",
                    #type = type(1.0))

        ##self.input4OnlyInPython = self.addLiteralInput(identifier = "L_input_wms1", # input_param1, input_url1
                    #title = "Input 1 (parametre wms)",
                    #abstract = "Veuillez inserer le WMS input 1", # [ExtJS_Info:menuId#01,foo,bar]",
                    #type = type(""))

        #self.input5OnlyInPython = self.addLiteralInput(identifier = "L_input_wms2", # input_param1, input_url1
                                          #title = "Input 2 (parametre wms)",
                                          #abstract = "Veuillez inserer le WMS input 2",
                                          #type = type(""))

        #self.input6OnlyInPython = self.addLiteralInput(identifier = "L_input_wms3", # input_param1, input_url1
                                          #title = "Input 3 (parametre wms)",
                                          #abstract = "Veuillez inserer le WMS input 3",
                                          #type = type(""))

        #self.input7OnlyInPython = self.addLiteralInput(identifier = "L_input_wms4", # input_param1, input_url1
                                          #title = "Input 4 (parametre wms)",
                                          #abstract = "Veuillez inserer le WMS input 4",
                                          #type = type(""))

        #self.input8OnlyInPython = self.addLiteralInput(identifier = "L_input_wms5", # input_param1, input_url1
                                          #title = "Input 5 (parametre wms)",
                                          #abstract = "Veuillez inserer le WMS input 5",
                                          #type = type(""))

        self.input9OnlyInPython = self.addLiteralInput(identifier = "L_input_scroll1", # input_param1, input_url1
                    title = "Modele numerique de terrain",
                    abstract = "Veuillez inserer le scroll input 1",
                    type = type(""),
                    #allowedValues=["mnt1.tif"],
                    default="mnt1.tif")

        self.input10OnlyInPython = self.addLiteralInput(identifier = "L_input_scroll2", # input_param1, input_url1
                    title = "Parcellaire",
                    abstract = "Veuillez inserer le scroll input 2",
                    type = type(""),
                    #allowedValues=["parcelles1.shp"],
                    default="parcelles1.shp")
                    
        self.input11OnlyInPython = self.addLiteralInput(identifier = "L_input_scroll3", # input_param1, input_url1
                    title = "Reseau hydrographique ou fosses",
                    abstract = "Veuillez inserer le scroll input 3",
                    type = type(""),
                    #allowedValues=["hydro4.shp"],
                    default="hydro4.shp")

        #self.input10OnlyInPython = self.addLiteralInput(identifier = "L_input_scroll2", # input_param1, input_url1
                    #title = "Input 2 (scroll)",
                    #abstract = "Veuillez inserer le scroll input 2",
                    #type = type(2),
                    #allowedValues=[7,8],
                    #default=7)

        #self.input11OnlyInPython = self.addLiteralInput(identifier = "L_input_scroll3", # input_param1, input_url1
                                          #title = "Input 3 (scroll)",
                                          #abstract = "Veuillez inserer le scroll input 3",
                                          #type = type(2),
                                          #allowedValues=[10,4],
                                          #default=10)

        #self.input12OnlyInPython = self.addLiteralInput(identifier = "L_input_scroll4", # input_param1, input_url1
                                          #title = "Input 4 (scroll)",
                                          #abstract = "Veuillez inserer le scroll input 4",
                                          #type = type(2),
                                          #allowedValues=[1,2],
                                          #default=1)

        #self.input13OnlyInPython = self.addLiteralInput(identifier = "L_input_scroll5", # input_param1, input_url1
                                          #title = "Input 5 (scroll)",
                                          #abstract = "Veuillez inserer le scroll input 5",
                                          #type = type(2),
                                          #allowedValues=[74,14],
                                          #default=14)

        #self.input14OnlyInPython = self.addLiteralInput(identifier = "L_input_coordxy1", # input_param1, input_url1
                    #title = "Input 1 (X,Y) : Cliquez ici puis sur la carte pour selectionner les coordonnees",
                    #abstract = "Veuillez selectionner une coordonnee",
                    #type = type(""))

        #self.input15OnlyInPython = self.addLiteralInput(identifier = "L_input_coordxy2", # input_param1, input_url1
                    #title = "Input 2 (X,Y) : Cliquez ici puis sur la carte pour selectionner les coordonnees",
                    #abstract = "Veuillez selectionner une coordonnee",
                    #type = type(""))

        #self.input16OnlyInPython = self.addLiteralInput(identifier = "L_input_coordxy3", # input_param1, input_url1
                                          #title = "Input 3 (X,Y) : Cliquez ici puis sur la carte pour selectionner les coordonnees",
                                          #abstract = "Veuillez selectionner une coordonnee",
                                          #type = type(""),
                                          #default=1)

        #self.input17OnlyInPython = self.addLiteralInput(identifier = "L_input_coordxy4", # input_param1, input_url1
                                          #title = "Input 4 (X,Y) : Cliquez ici puis sur la carte pour selectionner les coordonnees",
                                          #abstract = "Veuillez selectionner une coordonnee",
                                          #type = type(""),
                                          #default=1)

        #self.input18OnlyInPython = self.addLiteralInput(identifier = "L_input_coordxy5", # input_param1, input_url1
                                          #title = "Input 5 (X,Y) : Cliquez ici puis sur la carte pour selectionner les coordonnees",
                                          #abstract = "Veuillez selectionner une coordonnee",
                                          #type = type(""),
                                          #default=1)

        #self.input19OnlyInPython = self.addLiteralInput(identifier = "L_input_gml1", # input_param1, input_url1
                                          #title = "Input 1 (GML)",
                                          #abstract = "",
                                          #type = type(""))

        #self.input20OnlyInPython = self.addComplexInput(identifier = "C_input_gml1", # input_param1, input_url1
                    #title = "Input 1 (GML)",
                    #abstract = "",
                    #formats = [{'mimeType': 'text/xml'}])

        #self.input21OnlyInPython = self.addComplexInput(identifier = "C_input_gml2", # input_param1, input_url1
                    #title = "Input 2 (GML)",
                    #abstract = "",
                    #formats = [{'mimeType': 'text/xml'}])

        #self.input22OnlyInPython = self.addComplexInput(identifier = "C_input_gml3", # input_param1, input_url1
                    #title = "Input 3 (GML)",
                    #abstract = "",
                    #formats = [{'mimeType': 'text/xml'}])

        # Pas d'accent dans les titles

        self.input16OnlyInPython = self.addLiteralInput(identifier="L_input_checkbox1",
                    title = "Nombre de parcelles connectees en amont ",
                    type = type("")) # For string add "typestring"

        self.input17OnlyInPython = self.addLiteralInput(identifier="L_input_checkbox2",
                    title = "Surface totale des parcelles connectees en amont (m2) ",
                    type = type("")) 

        self.input18OnlyInPython = self.addLiteralInput(identifier="L_input_checkbox3",
                    title = "Volume total ruissele (m3) ",
                    type = type("")) 

        self.input19OnlyInPython = self.addLiteralInput(identifier="L_input_checkbox4",
                    title = "Hauteur infiltree totale (m) ",
                    type = type("")) 

        self.input20OnlyInPython = self.addLiteralInput(identifier="L_input_checkbox5",
                    title = "Debit maximum (m3/s) ",
                    type = type("")) 
                    
        self.input21OnlyInPython = self.addLiteralInput(identifier="L_input_checkbox6",
                    title = "Volume contributif de chaque parcelle au reseau (m3) ",
                    type = type("")) 

        self.input22OnlyInPython = self.addLiteralInput(identifier="L_input_checkbox7",
                    title = "Nombre de fosse connectes en amont ",
                    type = type("")) 
                    
        self.input23OnlyInPython = self.addLiteralInput(identifier="L_input_checkbox8",
                    title = "Longueur totale de reseau en amont (m) ",
                    type = type("")) 

        self.input24OnlyInPython = self.addLiteralInput(identifier="L_input_checkbox9",
                    title = "Volume total transfere (m3) ",
                    type = type("")) 
                    
        self.input25OnlyInPython = self.addLiteralInput(identifier="L_input_checkbox10",
                    title = "Hauteur maximum debordee (m) ",
                    type = type("")) 
                    
        self.input26OnlyInPython = self.addLiteralInput(identifier="L_input_checkbox11",
                    title = "Volume total deborde (m3)  ",
                    type = type("")) 
                    
# Output

        self.output1OnlyInPython = self.addLiteralOutput(identifier="L_output_wms1",
                    title="test")

        #self.output3OnlyInPython = self.addLiteralOutput(identifier="L_output_param1",
                    #title="test")

        #self.output2OnlyInPython = self.addLiteralOutput(identifier="L_output_wms2",
                    #title="test")
        
        #self.dataIn = self.addComplexInput(identifier="data",
        #            title="Vecteur utilise pour la simulation openfluid",
        #            formats = [{'mimeType':'text/xml'}])

        self.output1OnlyInPython = self.addLiteralOutput(identifier = "L_output_param1",
                title="Output literal data")

    def execute(self):

        # Definition du path vers le repertoire de sortie du serveur
        #outputPath = "/home/jvh/openfluid/workspace/output/output_bourdic/" #Bug si place dans le def_init
        # Copie la couche input deposee par defaut dans le repertoire /tmp vers le repertoire wpsoutput
        #self.cmd("cp %s %s" % (self.dataIn.getValue(),outputPath))
        # Renomme le vecteur fourni en input (dataingetvalue) par la valeur definie en litteral input (input1OnlyInPythongetvalue)
        #self.cmd("mv %s%s %s%s.gml" % (outputPath,self.dataIn.getValue(),outputPath,'Bourdic_parcelles_RGF93'))
        #Converti le .gml fourni en input vers le format .shp 
        #os.system("ogr2ogr -f 'ESRI Shapefile' %s%s.shp %s%s.gml" % (outputPath,'Bourdic_parcelles_RGF93',outputPath,'Bourdic_parcelles_RGF93'))

        #trigger de declenchement pour openfluid
        os.system("sed -i s/launch_openfluid=off/launch_openfluid=on/g /var/www/pywps/processes/bourdic_v2_railing.txt")
        #recupere le mail de l'utilisateur contenu dans le litteral input input1OnlyInPython
        #os.system("sed -i s/mail=/mail=%s/g /var/www/pywps/processes/bourdic_v2_railing.txt" % (self.input1OnlyInPython.getValue()))
        
        #recupere le mail de l'utilisateur contenu dans le litteral input input1OnlyInPython
        #os.system("cmd=$(tail -1 /var/www/trash03_02/testforsed.txt | cut -d';' -f 1) ; echo '$((cmd+1));v.jonath@live.fr;prout;' >> /var/www/trash03_02/testforsed.txt")
        # Read first line
        #first = open("/var/www/trash03_02/testforsed.txt").readline()
        
        # Check which simulators are used
        # Create empty var
        simulators_used = ""
        parcelles_fields_checked = ""
        rh_fields_checked = ""
        # IF 16 (Nombre de parcelles) is True or 17 (Surface parcelles amont) --> Enable stat.upper.su
        if self.input16OnlyInPython.getValue() == "True" or self.input17OnlyInPython.getValue() == "True" : 
            if simulators_used == "" :
                simulators_used = simulators_used + "stat.upper.su"
            elif simulators_used != "" :
                simulators_used = simulators_used + ",stat.upper.su"            
        if self.input16OnlyInPython.getValue() == "True" : 
            # If not empty add comma before
            if parcelles_fields_checked == "" :
                #simulators_used = simulators_used + "stat.upper.su"
                parcelles_fields_checked = parcelles_fields_checked + "stat.upper.number=>UpNum"
            elif parcelles_fields_checked != "" :
                #simulators_used = simulators_used + ",stat.upper.su"
                parcelles_fields_checked = parcelles_fields_checked + ",stat.upper.number=>UpNum"
        if self.input17OnlyInPython.getValue() == "True" : 
            # If not empty add comma before
            if parcelles_fields_checked == "" :
                #simulators_used = simulators_used + "stat.upper.su"
                parcelles_fields_checked = parcelles_fields_checked + "stat.upper.surface=>UpArea"
            elif parcelles_fields_checked != "" :
                #simulators_used = simulators_used + ",stat.upper.su"
                parcelles_fields_checked = parcelles_fields_checked + ",stat.upper.surface=>UpArea"
        # IF 18 (Volume total ruisselle) is True --> Enable water.surf.totalvolume-su
        if self.input18OnlyInPython.getValue() == "True" : 
            if simulators_used == "" :
                simulators_used = simulators_used + "water.surf.totalvolume-su"
                parcelles_fields_checked = parcelles_fields_checked + "water.surf.V.total-su=>VolTot"
            elif simulators_used != "" :    
                simulators_used = simulators_used + ",water.surf.totalvolume-su"
                parcelles_fields_checked = parcelles_fields_checked + ",water.surf.V.total-su=>VolTot"
         # IF 19 (Hauteur infiltree totale) is True --> Enable water.surf.totalinfiltration-su
        if self.input19OnlyInPython.getValue() == "True" : 
            if simulators_used == "" :
                simulators_used = simulators_used + "water.surf.totalinfiltration-su"
                parcelles_fields_checked = parcelles_fields_checked + "water.surf.H.totalinfiltration-su=>InfilTot"
            elif simulators_used != "" :  
                simulators_used = simulators_used + ",water.surf.totalinfiltration-su"
                parcelles_fields_checked = parcelles_fields_checked + ",water.surf.H.totalinfiltration-su=>InfilTot"                
         # IF 20 (Debit max) is True --> Enable water.surf.max-outflow-su
        if self.input20OnlyInPython.getValue() == "True" : 
            if simulators_used == "" :
                simulators_used = simulators_used + "water.surf.max-outflow-su"
                parcelles_fields_checked = parcelles_fields_checked + "water.surf.Q.maxdownstream-su=>QMax"    
            elif simulators_used != "" :    
                simulators_used = simulators_used + ",water.surf.max-outflow-su"
                parcelles_fields_checked = parcelles_fields_checked + ",water.surf.Q.maxdownstream-su=>QMax"    
         # IF 21 (Volume contributif parcelles) is True --> Enable water.surf.totalvolumecontrib-su
        if self.input21OnlyInPython.getValue() == "True" : 
            if simulators_used == "" :
                simulators_used = simulators_used + "water.surf.totalvolumecontrib-su"
                parcelles_fields_checked = parcelles_fields_checked + "water.surf.V.contribDownstream-su=>ConVol"
            elif simulators_used != "" :    
                simulators_used = simulators_used + ",water.surf.totalvolumecontrib-su"
                parcelles_fields_checked = parcelles_fields_checked + ",water.surf.V.contribDownstream-su=>ConVol"
         # IF 22 (Nombre fosses en amont ou Longueur totale reseau) is True --> Enable water.surf.totalvolumecontrib-su
        if self.input22OnlyInPython.getValue() == "True" or self.input23OnlyInPython.getValue() == "True" :
            if simulators_used == "" :
                simulators_used = simulators_used + "stat.upper.rs"        
            elif simulators_used != "" :    
                simulators_used = simulators_used + ",stat.upper.rs"        
        if self.input22OnlyInPython.getValue() == "True" : 
            #if simulators_used == "" :
                #simulators_used = simulators_used + "stat.upper.rs"
            #elif simulators_used != "" :    
                #simulators_used = simulators_used + ",stat.upper.rs"
            if rh_fields_checked == "" :
                rh_fields_checked = rh_fields_checked + "stat.upper.number=>UpNum"
            elif rh_fields_checked != "" :
                rh_fields_checked = rh_fields_checked + ",stat.upper.number=>UpNum"
        if self.input23OnlyInPython.getValue() == "True" : 
            #if simulators_used == "" :
                #simulators_used = simulators_used + "stat.upper.rs"
                #rh_fields_checked = rh_fields_checked + "stat.upper.length=>UpLength"
            #elif simulators_used != "" :    
                #simulators_used = simulators_used + ",stat.upper.rs"
            if rh_fields_checked == "" :
                rh_fields_checked = rh_fields_checked + "stat.upper.number=>UpNum"            
            elif rh_fields_checked != "" :
                rh_fields_checked = rh_fields_checked + ",stat.upper.length=>UpLength"
         # IF 24 (Volume total transfere) is True --> Enable water.surf.totalvolume-rs
        if self.input24OnlyInPython.getValue() == "True"  : 
            if simulators_used == "" :
                simulators_used = simulators_used + "water.surf.totalvolume-rs"
                rh_fields_checked = rh_fields_checked + "water.surf.V.total-rs=>VolTot"
            elif simulators_used != "" :    
                simulators_used = simulators_used + ",water.surf.totalvolume-rs"
            if rh_fields_checked == "" :
                rh_fields_checked = rh_fields_checked + "water.surf.V.total-rs=>VolTot"            
            elif rh_fields_checked != "" :
                rh_fields_checked = rh_fields_checked + ",water.surf.V.total-rs=>VolTot"
         # IF 25 (Hauteur maximale debordee) is True --> Enable water.surf.overflow-rs
        if self.input25OnlyInPython.getValue() == "True"  : 
            if simulators_used == "" :
                simulators_used = simulators_used + "water.surf.overflow-rs"
                rh_fields_checked = rh_fields_checked + "water.surf.H.overflow-rs=>HeighMax"
            elif simulators_used != "" :    
                simulators_used = simulators_used + ",water.surf.overflow-rs"
            if rh_fields_checked == "" :
                rh_fields_checked = rh_fields_checked + "water.surf.H.overflow-rs=>HeighMax"
            elif rh_fields_checked != "" :
                rh_fields_checked = rh_fields_checked + ",water.surf.H.overflow-rs=>HeighMax"
         # IF 26 (Volume total deborde) is True --> water.surf.totalvolumeoverflow-rs
        if self.input26OnlyInPython.getValue() == "True"  : 
            if simulators_used == "" :
                simulators_used = simulators_used + "water.surf.totalvolumeoverflow-rs"
                rh_fields_checked = rh_fields_checked + "water.surf.V.overflow-rs=>OverTot"
            elif simulators_used != "" :    
                simulators_used = simulators_used + ",water.surf.totalvolumeoverflow-rs"
            if rh_fields_checked == "" :
                rh_fields_checked = rh_fields_checked + "water.surf.V.overflow-rs=>OverTot"
            elif rh_fields_checked != "" :
                rh_fields_checked = rh_fields_checked + ",water.surf.V.overflow-rs=>OverTot"
        #simulators_used = simulators_used + ";"
        #rh_fields_checked = rh_fields_checked + ";" 
                
        # Check if logfile is empty
        if os.stat("/var/www/trash03_02/testforsed.txt").st_size == 0 :
            # Write
            fichier = open("/var/www/trash03_02/testforsed.txt", "a")
            fichier.write("1"+";"+self.input1OnlyInPython.getValue()+";"+simulators_used+";"+parcelles_fields_checked+";"+rh_fields_checked+";")
            fichier.close()
        else : 
            #Read last line
            last = subprocess.check_output(['tail', '-1', "/var/www/trash03_02/testforsed.txt"])
            # Parse 
            parse_list = last.split(";")
            # Parse simulators : 
            parse_simulators = parse_list[0] # ['11']
            parse_simulators_plus1 = int(parse_simulators)+1 # 11
            # Write
            fichier = open("/var/www/trash03_02/testforsed.txt", "a")
            fichier.write("\n"+str(parse_simulators_plus1)+";"+self.input1OnlyInPython.getValue()+";"+simulators_used+";"+parcelles_fields_checked+";"+rh_fields_checked+";") # 1;jojo@live.fr;
            fichier.close()

        #Output
        self.output1OnlyInPython.setValue("End of simulation") #Return "End of simulation"

        return
