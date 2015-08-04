from pywps.Process import WPSProcess       
import os
import time
import datetime
import subprocess                  
class Process(WPSProcess):
####################################################################################

####################################################################################

    def __init__(self):

        # Process initialization
        WPSProcess.__init__(self,
            identifier = "wab",
            title="openfluid_sync_fromqgis",
            abstract="""WPS test""",
            version = "1.0",
            storeSupported = True,
            statusSupported = True)

        # Adding process inputs

# --------------------------------- PARAM INPUT ---------------------------------
        self.input1OnlyInPython = self.addLiteralInput(identifier="L_input_param1",
                    title = "Email (ex jean.dupont@free.fr)",
                    type = type("")) 

        # self.input1010OnlyInPython = self.addLiteralInput(identifier="L_input_param2",
                    # title = "insert title",
                    # type = type(""))

# --------------------------------- WMS INPUT ---------------------------------

        self.input9OnlyInPython = self.addLiteralInput(identifier = "L_input_wms1",
                    title = "Modele numerique de terrain",
                    abstract = "MNT Bourdic", 
                    type = type(""))

        self.input10OnlyInPython = self.addLiteralInput(identifier = "L_input_wms2", 
                                          title = "Parcellaire",
                                          abstract = "Parcellaire",
                                          type = type(""))

# --------------------------------- SCROLL INPUT ---------------------------------
 
        self.input105OnlyInPython = self.addLiteralInput(identifier = "L_input_scroll1", 
                    title = "Modele numerique de terrain",
                    abstract = "Veuillez inserer le scroll input 1",
                    type = type(""),
                    allowedValues=[10,4],
                    default=4)

        self.input106OnlyInPython = self.addLiteralInput(identifier = "L_input_scroll2", 
                    title = "Parcellaire",
                    abstract = "Veuillez inserer le scroll input 2",
                    type = type(""),
                    allowedValues=["parcelles1.shp"],
                    default="parcelles1.shp")

# --------------------------------- COORDXY INPUT ---------------------------------

        self.input14OnlyInPython = self.addLiteralInput(identifier = "L_input_coordxy1", 
                    title = "Cliquez ici puis sur la carte pour selectionner les coordonnees",
                    abstract = "Veuillez selectionner une coordonnee",
                    type = type(""))

        # self.input15OnlyInPython = self.addLiteralInput(identifier = "L_input_coordxy2", # input_param1, input_url1
                    # title = "Input 2 (X,Y) : Cliquez ici puis sur la carte pour selectionner les coordonnees",
                    # abstract = "Veuillez selectionner une coordonnee",
                    # type = type(""))

# --------------------------------- GML INPUT ---------------------------------

        # self.input54OnlyInPython = self.addComplexInput(identifier = "C_input_gml1", 
                    # title = "Input 1 (GML)",
                    # abstract = "",
                    # formats = [{'mimeType': 'text/xml'}])

# --------------------------------- CHECKBOX INPUT ---------------------------------
# Pas d'accent dans les titles

        self.input16OnlyInPython = self.addLiteralInput(identifier="L_input_checkbox1",
                    title = "Nombre de parcelles connectees en amont ",
                    type = type("")) 

        self.input17OnlyInPython = self.addLiteralInput(identifier="L_input_checkbox2",
                    title = "Surface totale des parcelles connectees en amont (m2) ",
                    type = type("")) 

        self.input18OnlyInPython = self.addLiteralInput(identifier="L_input_checkbox3",
                    title = "Volume total ruissele (m3) ",
                    type = type(""))

# Output

        self.output1OnlyInPython = self.addLiteralOutput(identifier="L_output_param1",
                    title="test")
					
        self.output3OnlyInPython = self.addLiteralOutput(identifier="L_output_wms1",
                    title="test")

        self.output4OnlyInPython = self.addLiteralOutput(identifier="L_output_wms2",
                    title="test")

    def execute(self):

        # Get current date for custome var
        current_datetime = time.strftime("%Y%m%d-%H%M%S")

        #Output
        self.output1OnlyInPython.setValue("End of simulation") 
        # self.output3OnlyInPython.setValue("http://bvservice.fr/geoserver/moulinet/wms?moulinet:moulinet_bv") 
        self.output3OnlyInPython.setValue("http://bvservice.fr/geoserver/wms?moulinet:moulinet_bv") 
        self.output4OnlyInPython.setValue("http://bvservice.fr/geoserver/wms?moulinet:moulinet_os") 
        #self.output3OnlyInPython.setValue(current_datetime) 
        return
