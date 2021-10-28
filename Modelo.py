# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:41:20 2020

@author: Mauricio
"""
import numpy as np;
import pydicom;
import os;
import tempfile;
from PIL import Image;
from pydicom.dataset import FileDataset, FileMetaDataset;
class ModeloEntregable1(object):
    def __init__(self):#Define the ModeloEntregable1 constructor
        #Create all the necessary variables for the application
        self.__directionFile = "";
        self.__date = "";
        self.__time = "";
        self.__accessNumber = "";
        self.__referenceDoctorName = "";
        self.__patientName = "";
        self.__patientID = "";
        self.__birthday = "";
        self.__gender = "";
        self.__study = "";
        self.__seriesNumber = "";
        self.__rows = 0;
        self.__columns = 0;
        self.__slices = 0;
        self.__x_space = 0.0;
        self.__y_space = 0.0;
        self.__thickness = 0.0;
        self.__slicerCount = 0.0;
        self.__images = [];
      
    def setControler(self, c):
        #Set the controler to the object ModeloEntregable1()
        self.__controlerModel = c;
        
    def loadDirectory(self, dirDirection):
        '''
        Parameters
        ----------
        dirDirection : TYPE->str, the same string with the directory´s file path
        implemented in ControladorEntregale1().sendDirectory() method
            DESCRIPTION.
            This method read each all the DICOM files in the directory selected
            and set all the values of the ModeloEntregable1's attributes
        Returns
        -------
        TYPE->bool, True or False
            DESCRIPTION.
            If the load has been successful, it returns True. Otherwise returns
            False
        '''
        self.__directionFile = dirDirection;
        dicomList = [];
        #Itinerate in all the files placed in the directory
        self.__controlerModel.sendProgressInfo("Loading directories names...");
        self.__controlerModel.sendProgressNumber(0);
        for dirName, subdirList, fileList in os.walk(self.__directionFile):
            for filename in fileList:
                if filename.endswith(".dcm"):
                    #print(filename);
                    #Add all the .dcm files finded in the directory
                    #to separate direction files
                    dicomList.append(os.path.join(dirName,filename));
        self.__controlerModel.sendProgressInfo("Completed");
        self.__controlerModel.sendProgressNumber(100);
        # print(dicomList);
        # print(dicomList[0]);#First direction file
        # print(dicomList[2]);#Second direction file
        
        # This does not work for directories, only for single files
        # fName = open(self.__directionFile,'r');
        # ##Bla bla bla...
        
        # Getting the main data
        if(len(dicomList)==0):
            return False;
        else:
            self.__controlerModel.sendProgressInfo("reading the DICOM´s main info...");
            self.__controlerModel.sendProgressNumber(0);
            data = pydicom.dcmread(dicomList[0],force=True);
            self.__controlerModel.sendProgressNumber(100);
            self.__controlerModel.sendProgressInfo("getting the DICOM´s main info...");
            self.__controlerModel.sendProgressNumber(0);
            self.__date = data[0x0008,0x0020].value;
            self.__controlerModel.sendProgressNumber(6);
            self.__time = data[0x0008,0x0030].value;
            self.__controlerModel.sendProgressNumber(12);
            self.__accessNumber = data[0x0008,0x0050].value;
            self.__controlerModel.sendProgressNumber(18);
            self.__referenceDoctorName = str(data[0x0008,0x0090].value);
            self.__controlerModel.sendProgressNumber(24);
            self.__patientName = str(data[0x0010,0x0010].value);
            self.__controlerModel.sendProgressNumber(30);
            self.__patientID = data[0x0010,0x0020].value;
            self.__controlerModel.sendProgressNumber(36);
            self.__birthday = data[0x0010,0x0030].value;
            self.__controlerModel.sendProgressNumber(42);
            self.__gender = data[0x0010,0x0040].value;
            self.__controlerModel.sendProgressNumber(48);
            self.__study = data[0x0020,0x0010].value;
            self.__controlerModel.sendProgressNumber(54);
            self.__seriesNumber = str(data[0x0020,0x0011].value);
            self.__controlerModel.sendProgressNumber(60);
            # Get other main info
            self.__rows = int(data.Rows);
            self.__controlerModel.sendProgressNumber(66);
            self.__columns = int(data.Columns);
            self.__controlerModel.sendProgressNumber(72);
            self.__slices = len(dicomList);
            self.__controlerModel.sendProgressNumber(78);
            self.__x_space = float(data.PixelSpacing[0]);
            self.__controlerModel.sendProgressNumber(84);
            self.__y_space = float(data.PixelSpacing[1]);
            self.__controlerModel.sendProgressNumber(90);
            self.__thickness = float(data.SliceThickness);
            self.__controlerModel.sendProgressNumber(96);
            self.__images = np.zeros((self.__rows, self.__columns, self.__slices), 
                                   dtype=data.pixel_array.dtype);
            self.__controlerModel.sendProgressNumber(100);
            self.__controlerModel.sendProgressInfo("reading files selected...");
            self.__controlerModel.sendProgressNumber(0);
            #Read the data in each file
            dicomInfo = [];
            actualNumberFile = 0;
            for filename in dicomList:
                item = pydicom.dcmread(filename);
                self.__controlerModel.sendProgressNumber(int(
                    (actualNumberFile/len(dicomList))*100));
                actualNumberFile+=1;
                dicomInfo.append(item);
            self.__controlerModel.sendProgressInfo("sorting by slice location...");
            self.__controlerModel.sendProgressNumber(0);
            #Now, organize the dicomList in the correct order.
            #Just in case it is disorganized
            dicomInfo = sorted(dicomInfo, key=lambda s:s.SliceLocation);
            self.__controlerModel.sendProgressNumber(100);
            self.__controlerModel.sendProgressInfo("getting images...");
            self.__controlerModel.sendProgressNumber(0);
            #Then get all the images and store it in self.__images
            counter = 0
            for fileitems in dicomInfo:
                # # read the file
                # ds = pydicom.dcmread(filename)
                # # store the raw image data
                self.__images[:, :, counter] = fileitems.pixel_array;
                counter = counter + 1;
                self.__controlerModel.sendProgressNumber(int(
                    (counter/len(dicomInfo))*100));
            self.__controlerModel.sendProgressInfo("Completed, load successful");
            self.__controlerModel.sendProgressNumber(100);
            return True;
    
    def getData(self):
        #This method returns all the main data of a DICOM file
        modelDict = {};
        modelDict['Fecha AAAA/MM/DD'] = self.__date;
        modelDict['Hora HHMMSS'] = self.__time;
        modelDict['Numero Acceso'] = self.__accessNumber;
        modelDict['Nombre Medico Referente'] = self.__referenceDoctorName;
        modelDict['Nombre Paciente'] = self.__patientName;
        modelDict['ID Paciente'] = self.__patientID;
        modelDict['Fecha De Nacimiento'] = self.__birthday;
        modelDict['Genero'] = self.__gender;
        modelDict['Estudio'] = self.__study;
        modelDict['Numero Serie'] = self.__seriesNumber;
        modelDict['Filas'] = self.__rows;
        modelDict['Columnas'] = self.__columns;
        modelDict['Capas'] = self.__slices;
        return modelDict;
    
    def loadingConfirmation(self):
        #This method returns True or False depending if self.__images is empty
        if(len(self.__images)==0):
            return False;
        else:
            return True;
        
    def searchSagitalSlice(self,value):
        #This method returns the sagittal image stored in self.__images
        return(np.flip(self.__images[:,(value-1),:].transpose()));
    
    def searchCoronalSlice(self,value):
        #This method returns the coronal image stored in self.__images
        return(np.flip(self.__images[(value-1),:,:].transpose()));
    
    def searchAxialSlice(self,value):
        #This method returns the axial image stored in self.__images
        return(self.__images[:,:,(value-1)]);
    
    def saveDicom(self,aDict):
        '''
        Parameters
        ----------
        aDict : TYPE->dict
            DESCRIPTION.
            This method save the info get by the view that was stored in a
            dictionary
        Returns
        -------
        None.
        '''
        #print(aDict['directionImage']);
        file = tempfile.NamedTemporaryFile(suffix=('.dcm')).name;
        metadata = FileMetaDataset();
        # metadata.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.2';
        # metadata.MediaStorageSOPInstanceUID = "1.2.3";
        # metadata.ImplementationClassUID = "1.2.3.4";
        data = FileDataset(file, metadata);
        data.StudyDate = aDict['date'];
        data.StudyTime = aDict['time'];
        data.AccessionNumber = aDict['accessNumber'];
        data.ReferringPhysicianName = aDict['referenceDoctorName'];
        data.PatientName = aDict['patientName'];
        data.PatientID = aDict['patientID'];
        data.PatientBirthDate = aDict['birthday'];
        data.PatientSex = aDict['gender'];
        data.StudyID = aDict['study'];
        data.SeriesNumber = aDict['seriesNumber'];
        photo = Image.open(aDict['directionImage']);
        vector = np.asarray(photo);
        data.PixelData = vector.tobytes(); #aDict['directionImage'];
        photo.close();
        data.Rows = vector.shape[0];
        data.Columns = vector.shape[1];
        data.PixelSpacing = [1,1];
        data.SliceThickness = "1.0";
        data.SliceLocation = str(self.__slicerCount);
        self.__slicerCount+=1;
        # data.save_as(aDict['date']+"-"+str(self.__slicerCount)+".dcm");
        # data.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian;
        pydicom.filewriter.dcmwrite(aDict['date']+"-"+
                                    str(self.__slicerCount)+".dcm",
                                    data);
        '''
        Pydicom->meta_data
        https://pydicom.github.io/pydicom/dev/reference/generated/pydicom.filewriter.dcmwrite.html
        http://dicom.nema.org/medical/dicom/current/output/chtml/part05/chapter_10.html
        '''
        
    
    