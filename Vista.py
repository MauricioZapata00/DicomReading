# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:41:20 2020

@author: Mauricio
"""
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QVBoxLayout,QWidget,QLabel,QMessageBox;
from matplotlib.backends.backend_qt5agg import FigureCanvas;
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar;
from matplotlib.figure import Figure;
from PyQt5.uic import loadUi;
from PyQt5.QtGui import QPixmap;
from PyQt5.QtCore import Qt;
class VistaEntregable1(QMainWindow):
    def __init__(self):## Define the VistaEntregable1 constructor
        super(VistaEntregable1,self).__init__(None);
        loadUi('VentanaPrincipal.ui',self);
        #Add a new layout to each Qwidets to plot images
        self.__sagitalLayout = QVBoxLayout();
        self.__coronalLayout = QVBoxLayout();
        self.__axialLayout = QVBoxLayout();
        self.GraficoSagital.setLayout(self.__sagitalLayout);
        self.GraficoCoronal.setLayout(self.__coronalLayout);
        self.GraficoAxial.setLayout(self.__axialLayout);
        #Create new objects defined by myself for this layouts
        self.__imageSagital = canvasWidget(self.GraficoSagital);
        self.__imageCoronal = canvasWidget(self.GraficoCoronal);
        self.__imageAxial = canvasWidget(self.GraficoAxial);
        #Add this objects (canvasWidget) to the layouts
        self.__sagitalLayout.addWidget(self.__imageSagital);
        self.__coronalLayout.addWidget(self.__imageCoronal);
        self.__axialLayout.addWidget(self.__imageAxial);
        #Create toolbars for each plot image
        self.__sagitalToolbar = NavigationToolbar(self.__imageSagital,self);
        self.__coronalToolbar = NavigationToolbar(self.__imageCoronal,self);
        self.__axialToolbar = NavigationToolbar(self.__imageAxial,self);
        #Add the toolbars
        self.__sagitalLayout.addWidget(self.__sagitalToolbar);
        self.__coronalLayout.addWidget(self.__coronalToolbar);
        self.__axialLayout.addWidget(self.__axialToolbar);
        #Excecute the setUp();
        self.__setUp();
        
    def __setUp(self):
        '''
        Connect to each bottom and other view's characteristics to his
        respective function
        '''
        self.BotonCargarDicom.clicked.connect(self.__loadDicom);
        self.BotonMostrarInfo.clicked.connect(self.__askForInfo);
        self.BotonCrearDicom.clicked.connect(self.__createDicom);
        self.SagitalSlider.valueChanged.connect(self.__updateSagitalSlider);
        self.SagitalSpinBox.valueChanged.connect(self.__updateSagitalSpinBox);
        self.CoronalSlider.valueChanged.connect(self.__updateCoronalSlider);
        self.CoronalSpinBox.valueChanged.connect(self.__updateCoronalSpinBox);
        self.AxialSlider.valueChanged.connect(self.__updateAxialSlider);
        self.AxialSpinBox.valueChanged.connect(self.__updateAxialSpinBox);
        
    def __loadDicom(self):
        self.Salida.setText("Cargando archivos seleccionados...");
        #Get the direction of the directory
        self.__dirDirection = QFileDialog.getExistingDirectory(self,
                            'Select the directory','.',QFileDialog.ShowDirsOnly);
        #Send the direction to the controler
        self.__controlerView.sendDirectory(self.__dirDirection);
        
    def __askForInfo(self):
        #Get the info previously loaded
        self.__controlerView.getDicomInfo();
        
    def __createDicom(self):
        '''  
        Returns nothing
        -------
        This method first create a new window (VentanaGuardarDicom() 
        object) defined by myself and then send this window to the controller
        to be shown
        '''
        #Aquí le paso el mismo controlador a la segunda ventana
        self.__secondaryView = VentanaGuardarDicom(self.__controlerView);
        self.__controlerView.deploySecondView(self.__secondaryView);
    
    def __updateSagitalSlider(self):
        '''
        Returns nothing
        -------
        Ask if there is any info previously loaded, depending of this statement
        the method get the sagittal image and then plot it at any time the 
        sagittal slider has change
        '''
        flag = self.__controlerView.hasLoadedSomething();
        if(flag):
            #Also change the present value of the sagittal spinbox
            self.SagitalSpinBox.setValue(self.SagitalSlider.value());
            sagitalImage = self.__controlerView.getSagitalSlice(
                            self.SagitalSlider.value());
            self.__imageSagital.plotSlice(sagitalImage);
            
    def __updateSagitalSpinBox(self):
        '''
        Returns nothing
        -------
        Ask if there is any info previously loaded, depending of this statement
        the method get the sagittal image and then plot it at any time the 
        sagittal spinbox has change
        '''
        flag = self.__controlerView.hasLoadedSomething();
        if(flag):
            #Also change the present value of the sagittal slider
            self.SagitalSlider.setValue(self.SagitalSpinBox.value());
            sagitalImage = self.__controlerView.getSagitalSlice(
                            self.SagitalSlider.value());
            self.__imageSagital.plotSlice(sagitalImage);
    
    def __updateCoronalSlider(self):
        '''
        Returns nothing
        -------
        Ask if there is any info previously loaded, depending of this statement
        the method get the coronal image and then plot it at any time the 
        coronal slider has change
        '''
        flag = self.__controlerView.hasLoadedSomething();
        if(flag):
            #Also change the present value of the coronal spinbox
            self.CoronalSpinBox.setValue(self.CoronalSlider.value());
            coronalImage = self.__controlerView.getCoronalSlice(
                            self.CoronalSlider.value());
            self.__imageCoronal.plotSlice(coronalImage);
            
    def __updateCoronalSpinBox(self):
        '''
        Returns nothing
        -------
        Ask if there is any info previously loaded, depending of this statement
        the method get the coronal image and then plot it at any time the 
        coronal spinbox has change
        '''
        flag = self.__controlerView.hasLoadedSomething();
        if(flag):
            #Also change the present value of the coronal slider
            self.CoronalSlider.setValue(self.CoronalSpinBox.value());
            coronalImage = self.__controlerView.getCoronalSlice(
                            self.CoronalSlider.value());
            self.__imageCoronal.plotSlice(coronalImage);
            
    def __updateAxialSlider(self):
        '''
        Returns nothing
        -------
        Ask if there is any info previously loaded, depending of this statement
        the method get the axial image and then plot it at any time the 
        axial slider has change
        '''
        flag = self.__controlerView.hasLoadedSomething();
        if(flag):
            #Also change the present value of the axial spinbox
            self.AxialSpinBox.setValue(self.AxialSlider.value());
            axialImage = self.__controlerView.getAxialSlice(
                            self.AxialSlider.value());
            self.__imageAxial.plotSlice(axialImage);
            
    def __updateAxialSpinBox(self):
        '''
        Returns nothing
        -------
        Ask if there is any info previously loaded, depending of this statement
        the method get the axial image and then plot it at any time the 
        axial spinbox has change
        '''
        flag = self.__controlerView.hasLoadedSomething();
        if(flag):
            #Also change the present value of the axial slider
            self.AxialSlider.setValue(self.AxialSpinBox.value());
            axialImage = self.__controlerView.getAxialSlice(
                            self.AxialSlider.value());
            self.__imageAxial.plotSlice(axialImage);
    
    def setControler(self, c):
        #Set the controler to the object VistaEntregable1()
        self.__controlerView = c;
        
    def loadConfirmation(self, flag):
        '''
        Parameters
        ----------
        flag : TYPE->bool
            DESCRIPTION.
            This method is excecute when the load of files is in the final
            step, depending on 'flag', it shows the information in the 
            'self.QLabel.Salida'
        Returns
        -------
        None.

        '''
        if(flag):
            self.Salida.setText("Archivos cargados exitosamente.");
        else:
            self.Salida.setText("No se encontraron archivos.");
            
    def showInfo(self,theDict):
        '''
        Parameters
        ----------
        theDict : TYPE->dict
            DESCRIPTION.
            This method uses the info stored in Model() object and depending
            on this, it plots the DICOM images
        Returns
        -------
        None.
        '''
        if(theDict['Capas']==0):
            self.Salida.setText("No se han cargado archivos o "+
                                "el directoriono no contiene archivos");
        else:
            cont = 0;
            for values in theDict:
                #Add items to the self.QList.ListaInformacion
                self.ListaInformacion.insertItem(cont,values + "\t" +theDict[values]);
                cont+=1;
                if(cont>=9):
                    break;
            self.Salida.setText("Numero de filas: " + str(theDict['Filas'])
                                + "\tNumero de columnas : " + str(theDict['Columnas'])
                                + "\nNumero de Capas: " + str(theDict['Capas']));
            # Set the limits and caracteristics to SagitalSlider
            self.SagitalSlider.setMinimum(1);
            self.SagitalSlider.setMaximum(theDict['Capas']);
            self.SagitalSlider.setSingleStep(1);
            self.SagitalSlider.setTickInterval(1);
            self.SagitalSlider.setValue(1);
            # Set the limits and caracteristics to SagitalSpinBox
            self.SagitalSpinBox.setMinimum(1);
            self.SagitalSpinBox.setMaximum(theDict['Capas']);
            self.SagitalSpinBox.setSingleStep(1);
            # Set the limits and caracteristics to CoronalSlider
            self.CoronalSlider.setMinimum(1);
            self.CoronalSlider.setMaximum(theDict['Capas']);
            self.CoronalSlider.setSingleStep(1);
            self.CoronalSlider.setTickInterval(1);
            self.CoronalSlider.setValue(1);
            # Set the limits and caracteristics to CoronalSpinBox
            self.CoronalSpinBox.setMinimum(1);
            self.CoronalSpinBox.setMaximum(theDict['Capas']);
            self.CoronalSpinBox.setSingleStep(1);
            # Set the limits and caracteristics to AxialSlider
            self.AxialSlider.setMinimum(1);
            self.AxialSlider.setMaximum(theDict['Capas']);
            self.AxialSlider.setSingleStep(1);
            self.AxialSlider.setTickInterval(1);
            self.AxialSlider.setValue(1);
            # Set the limits and caracteristics to AxialSpinBox
            self.AxialSpinBox.setMinimum(1);
            self.AxialSpinBox.setMaximum(theDict['Capas']);
            self.AxialSpinBox.setSingleStep(1);
            # Put the first 3 planes slices
            sagitalImage = self.__controlerView.getSagitalSlice(
                            self.SagitalSlider.value());
            self.__imageSagital.plotSlice(sagitalImage);
            coronalImage = self.__controlerView.getCoronalSlice(
                            self.CoronalSlider.value());
            self.__imageCoronal.plotSlice(coronalImage);
            axialImage = self.__controlerView.getAxialSlice(
                            self.AxialSlider.value());
            self.__imageAxial.plotSlice(axialImage);
            
    def putProgressText(self,text):
        #This method only puts information in self.QLabel.InfoAMostrar
        self.InfoAMostrar.setText(text);
        
    def putProgressNumber(self,num):
        #This method only change the value of self.QProgressBar.BarraProgreso
        self.BarraProgreso.setValue(num);
        
class VentanaGuardarDicom(QWidget):#Window used to generate DICOM files
    def __init__(self,controler):#VentanaGuardarDicom Constructor
        super(VentanaGuardarDicom,self).__init__(None);
        loadUi('VentanaSecundaria.ui',self);
        #Set a VentanaGuardarDicom controler
        self.__VGDControler = controler;
        #Create a new layout to drag and drop jpg files
        self.__imageLayout = QVBoxLayout();
        self.CampoImagen.setLayout(self.__imageLayout);
        #Create a new DicomDragAndDrop (defined by myself) object
        self.__DicomDragAndDrop = DragAndDropLabel(self.__imageLayout);
        #Add this DicomDragAndDrop object to the layout
        self.__imageLayout.addWidget(self.__DicomDragAndDrop);
        self.__setUp();
        
    def __setUp(self):
        '''
        Connect to each bottom and other view's characteristics to his
        respective function
        '''
        self.BotonGuardar.clicked.connect(self.__generateDicom);
        
    def __generateDicom(self):
        '''
        This method get the text in every QTextEdit in VentanaGuardarDicom()
        object, if all the texts are != "" it sends this info to the controller
        to be saved

        Returns
        -------
        None.
        '''
        #Reading every QTextEdit data
        date = self.CampoFecha.text();
        #print(date);
        time = self.CampoHora.text();
        accessNumber = self.CampoNumAcceso.text();
        referenceDoctorName = self.CampoNomDocRef.text();
        patientName = self.CampoNomPaciente.text();
        patientID = self.CampoIDPaciente.text();
        birthday = self.CampoFechaNacimiento.text();
        gender = self.CampoGenero.text();
        study = self.CampoEstudio.text();
        seriesNumber = self.CampoNumSerie.text();
        directionImage = self.__DicomDragAndDrop.getFilePath();
        viewDict = {};
        if(date == "" or
           time == "" or
           accessNumber == "" or
           referenceDoctorName == "" or
           patientName == "" or
           patientID == "" or
           birthday == "" or
           gender == "" or
           study == "" or
           seriesNumber == "" or
           directionImage == ""):#If there is anything == ""->'Empty', make this action
            #Clear all the wrong entered info
            self.__clearFields();
            self.__DicomDragAndDrop.makeDefault();
            #In this case a QMessageBox is shown indicating the failure trying
            #to save the DICOM file
            msg = QMessageBox();
            msg.setWindowTitle("¡Error!");
            msg.setText("No se llenaron los campos requeridos.");
            msg.setIcon(QMessageBox.Critical);
            msg.exec_();
        else:
            viewDict['date'] = date;
            viewDict['time'] = time;
            viewDict['accessNumber'] = accessNumber;
            viewDict['referenceDoctorName'] = referenceDoctorName;
            viewDict['patientName'] = patientName;
            viewDict['patientID'] = patientID;
            viewDict['birthday'] = birthday;
            viewDict['gender'] = gender;
            viewDict['study'] = study;
            viewDict['seriesNumber'] = seriesNumber;
            viewDict['directionImage'] = directionImage;
            #Send the info to the controller
            self.__VGDControler.saveInfo(viewDict);
            #Clear all the entered info
            self.__clearFields();
            self.__DicomDragAndDrop.makeDefault();
            #In this case a QMessageBox is shown indicating the success trying
            #to save the DICOM file
            msg = QMessageBox();
            msg.setWindowTitle("Carga exitosa");
            msg.setText("Se ha creado un nuevo archivo .dcm \ncon la información establecida.");
            msg.setIcon(QMessageBox.Information);
            msg.exec_();
            
    def __clearFields(self):
        #This method clear all the data stored in each QTextEdit
        self.CampoFecha.clear();
        self.CampoHora.clear();
        self.CampoNumAcceso.clear();
        self.CampoNomDocRef.clear();
        self.CampoNomPaciente.clear();
        self.CampoIDPaciente.clear();
        self.CampoFechaNacimiento.clear();
        self.CampoGenero.clear();
        self.CampoEstudio.clear();
        self.CampoNumSerie.clear();

class DragAndDropLabel(QLabel):
    def __init__(self, qvbox):#DragAndDrop constructor
        super().__init__();
        #Set the DragAndDrop layout
        self.__DADLabelLayout = qvbox;
        #Accept generic drag and drop events
        self.setAcceptDrops(True);
        self.makeDefault();
        self.__filePath = "";
        
    def makeDefault(self):
        #This method stablish the default value to the layout
        self.setText("Suelta una imagen aquí");
        self.setAlignment(Qt.AlignCenter);
        
    def getFilePath(self):
        #This method returns the filePath of the dropped .jpg image
        return(self.__filePath);
    
    def dragEnterEvent(self,event):
        #This method allows the drag event but it does nothing
        if(event.mimeData().hasImage):
            event.accept();
        else:
            event.ignore();
        
    def dragMoveEvent(self,event):
        #This method allows the move event but it does nothing
        if(event.mimeData().hasImage):
            event.accept();
        else:
            event.ignore();
        
    def dropEvent(self,event):
        #This method allows the drop event
        if(event.mimeData().hasImage):
            #First, get the file path of the image
            self.__filePath = event.mimeData().urls()[0].toLocalFile();
            #Then create a QPixmap using the same dropped image
            self.__DicomPixMap = QPixmap(self.__filePath);
            #Show the image dropped by the user
            self.setPixmap(self.__DicomPixMap);
            #DO NOT FORGET TO ACCEPT THE EVENT USING 'event.accept()'
            #OTHERWISE IT WON´T DO ANYTHING
            event.accept();
        else:
            event.ignore();

class canvasWidget(FigureCanvas):
    def __init__(self,parent = None):#canvasWidget constructor
        self.__canvasFigure = Figure(figsize=(251,241),dpi=100);
        self.__canvasAxes = self.__canvasFigure.add_subplot(111);
        FigureCanvas.__init__(self,self.__canvasFigure);
        
        
    def plotSlice(self,image):
        #This method plots the image entered
        self.__canvasAxes.clear();
        self.__canvasAxes.imshow(image,cmap='bone');
        self.__canvasAxes.figure.canvas.draw();
                
                
                
                