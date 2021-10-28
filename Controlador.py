# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:41:18 2020

@author: Mauricio
"""
from Vista import VistaEntregable1;
from Modelo import ModeloEntregable1;
from PyQt5.QtWidgets import QApplication;
import sys;
class ControladorEntregable1(object):
    def __init__(self, v, m):#Define the ControladorEntregable1 constructor
        self.__viewControler = v;
        self.__modelControler = m;
        
    def sendDirectory(self,dirDirection):
        '''
        Parameters
        ----------
        dirDirection : TYPE->str, string with the directory´s file path
            DESCRIPTION.
            This method creates a bool variable named flag. The value of this
            bool variable depends of the returned value of
            self.__modelControler.loadDirectory(). Then, this flag is sent to
            the view.
        Returns
        -------
        None.
        '''
        flag = self.__modelControler.loadDirectory(dirDirection);
        self.__viewControler.loadConfirmation(flag);
        
    def getDicomInfo(self):
        '''
            DESCRIPTION.
            This method create a dict variable named theDict. The value of this
            dict variable depends of the returned value of
            self.__modelControler.getData(). Then, this flag is sent to the
            view
        Returns
        -------
        None.
        '''
        theDict = self.__modelControler.getData();
        self.__viewControler.showInfo(theDict);
        
    def hasLoadedSomething(self):
        '''
        Returns
        -------
        TYPE->bool
            DESCRIPTION.
            This method confirms if there is any information stored in the model
        '''
        flag = self.__modelControler.loadingConfirmation();
        return flag;
    
    def getSagitalSlice(self,value):
        '''
        Parameters
        ----------
        value : TYPE->int
            DESCRIPTION.
            This method send to the view the particular sagittal slice
            according to the value entered
        Returns
        -------
        None.
        '''
        return(self.__modelControler.searchSagitalSlice(value));
    
    def getCoronalSlice(self,value):
        '''
        Parameters
        ----------
        value : TYPE->int
            DESCRIPTION.
            This method send to the view the particular coronal slice
            according to the value entered
        Returns
        -------
        None.
        '''
        return(self.__modelControler.searchCoronalSlice(value));
    
    def getAxialSlice(self,value):
        '''
        Parameters
        ----------
        value : TYPE->int
            DESCRIPTION.
            This method send to the view the particular axial slice
            according to the value entered
        Returns
        -------
        None.
        '''
        return(self.__modelControler.searchAxialSlice(value));
    
    def sendProgressInfo(self,text):
        #This method send to the view the text to be shown
        self.__viewControler.putProgressText(text);
        
    def sendProgressNumber(self,num):
        #This method send to the view the value of the progress bar
        self.__viewControler.putProgressNumber(num);
        
    def deploySecondView(self,window):
        #This mehod shows the entered window
        window.show();
        
    def saveInfo(self,aDict):
        #This method send the information readed in the view to be saved as a
        #DICOM file
        self.__modelControler.saveDicom(aDict);
    
class EjecutableEntregable1(object):
    def __init__(self):#Define the EjecutableEntregable1 constructor
        #Create the necessary variables
        self.__miApp = QApplication(sys.argv);
        self.__miVista = VistaEntregable1();
        self.__miModelo = ModeloEntregable1();
        self.__miControlador = ControladorEntregable1(self.__miVista,
                                                      self.__miModelo);
        #Set the same controller to the model and the view
        self.__miVista.setControler(self.__miControlador);
        self.__miModelo.setControler(self.__miControlador);
        #Excecute main code
        self.__main();
        
    def __main(self):
        self.__miVista.show();
        sys.exit(self.__miApp.exec());
        
var = EjecutableEntregable1();#Just create a variable of type EjecutableEntregable1()
#PLEASE IGNORE THE INFORMATION BELOW
'''
https://pydicom.github.io/pydicom/stable/auto_examples/input_output/plot_read_dicom.html
https://pydicom.github.io/pydicom/1.1/working_with_pixel_data.html
https://pydicom.github.io/pydicom/stable/auto_examples/image_processing/reslice.html#sphx-glr-download-auto-examples-image-processing-reslice-py
https://pydicom.github.io/pydicom/stable/auto_examples/image_processing/reslice.html
https://pythonprogramming.net/progress-bar-pyqt-tutorial/


Para la interfaz: QSlider
https://www.tutorialspoint.com/pyqt/pyqt_qslider_widget_signal.htm
QSpinBok
https://www.tutorialspoint.com/pyqt/pyqt_qspinbox_widget.htm

Para embeber una figura canvas
https://stackoverflow.com/questions/48264553/matplotlib-navigation-toolbar-embeded-in-pyqt5-window-reset-original-view-cras
https://matplotlib.org/3.1.1/users/navigation_toolbar.html#:~:text=Press%20the%20right%20mouse%20button,axis%20and%20up%2Fdown%20motions.
https://yapayzekalabs.blogspot.com/2018/11/pyqt5-gui-qt-designer-matplotlib.html
https://www.learnpyqt.com/courses/graphics-plotting/plotting-matplotlib/

Para desplegar nuevas ventanas
https://www.youtube.com/watch?v=GkgMTyiLtWk
https://www.youtube.com/watch?v=mcT_bK1px_g
https://stackoverflow.com/questions/51456403/mouseover-event-for-a-pyqt5-label
http://zetcode.com/gui/pyqt5/dragdrop/

DCMTK -> Para guardar archivos DICOM
https://pydicom.github.io/pydicom/stable/auto_examples/input_output/plot_write_dicom.html
https://anaconda.org/bioconda/dcmtk


'''