#coding:utf8
from django.db import models

import time
#python manage.py migrate

# Create your models here.
class CompanyTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=50,null=True)
    fullName = models.CharField(max_length=50,null=True)
    uploadPath = models.CharField(max_length=50,null=True)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)
    def __unicode__(self):
        return self.name

class ProviderTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=250,null=False)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)
    contacts= models.CharField(max_length=50,null=True)
    telephone= models.CharField(max_length=50,null=True)
    email= models.CharField(max_length=50,null=True)
    address= models.CharField(max_length=500,null=True)
    website= models.CharField(max_length=500,null=True)
    def __unicode__(self):
        return self.name
    
class ServerRoomTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=50,null=True)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)
    provider= models.ForeignKey(ProviderTable,null=True, blank=True,on_delete=models.CASCADE)
    company=  models.ForeignKey(CompanyTable,null=True, blank=True,on_delete=models.CASCADE)
    contacts= models.CharField(max_length=50,null=True)
    telephone= models.CharField(max_length=50,null=True)
    email= models.CharField(max_length=50,null=True)
    address= models.CharField(max_length=500,null=True)
    website= models.CharField(max_length=500,null=True)
    def __unicode__(self):
        return self.name

class CabinetTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=50,null=True)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)
    houseNumber= models.CharField(max_length=50,null=True)
    floor= models.CharField(max_length=50,null=True)
    serverRoom= models.ForeignKey(ServerRoomTable,null=True, blank=True,on_delete=models.CASCADE)
    def __unicode__(self):
        return self.name
        
class EquipmentTypeTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=50,null=True)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime) 
    def __unicode__(self):
        return self.name

class EquipmentTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=50,null=True)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)
    provider= models.ForeignKey(ProviderTable,null=True, blank=True,on_delete=models.CASCADE)
    ipAddress= models.CharField(max_length=50,null=True)
    controlPort= models.CharField(max_length=50,null=True)
    cabinet= models.ForeignKey(CabinetTable,null=True, blank=True,on_delete=models.CASCADE)
    sequence= models.CharField(max_length=50,null=True)
    equipmentType= models.ForeignKey(EquipmentTypeTable,null=True, blank=True,on_delete=models.CASCADE)
    def __unicode__(self):
        return self.name

class DeployHostTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    serverRoom=models.ForeignKey(ServerRoomTable,null=True,blank=True,on_delete=models.CASCADE)
    host=models.ForeignKey(EquipmentTable,null=True,blank=True,on_delete=models.CASCADE)
    def __unicode__(self):
        return self.host.ipAddress

class OccupationTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=50,null=True)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)
    def __unicode__(self):
        return self.name
        
class PrivateTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=50,null=True)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)
    company= models.ForeignKey(CompanyTable,null=True, blank=True,on_delete=models.CASCADE)
    telephone= models.CharField(max_length=50,null=True)
    email= models.CharField(max_length=50,null=True)
    address= models.CharField(max_length=50,null=True)
    occupation= models.ForeignKey(OccupationTable,null=True, blank=True,on_delete=models.CASCADE)
    def __unicode__(self):
        return self.name

class ServiceTypeTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=50,null=True)
    version = models.CharField(max_length=50,null=True)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    portNumber= models.CharField(max_length=49,null=True,default=localtime)
    ctime= models.CharField(max_length=49,null=True,default=localtime)  
    logPathType=models.CharField(max_length=49,null=True)
    def __unicode__(self):
        return self.name

class ProjectTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=50,null=True)
    company= models.ForeignKey(CompanyTable,null=True, blank=True,on_delete=models.CASCADE)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)
    def __unicode__(self):
        return self.name
        
class ServiceTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=50,null=True)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)
    project= models.ForeignKey(ProjectTable,null=True, blank=True,on_delete=models.CASCADE,related_name ='project')
    programmer= models.ForeignKey(PrivateTable,null=True, blank=True,on_delete=models.CASCADE,related_name ='programmer')
    testEngineer= models.ForeignKey(PrivateTable,null=True, blank=True,on_delete=models.CASCADE,related_name = "softwareTestEngineer")
    productManager= models.ForeignKey(PrivateTable,null=True, blank=True,on_delete=models.CASCADE,related_name = "productManager")
    operationEngineer= models.ForeignKey(PrivateTable,null=True, blank=True,on_delete=models.CASCADE,related_name = "operationEngineer")
    serviceType= models.ForeignKey(ServiceTypeTable,null=True, blank=True,on_delete=models.CASCADE)
    javaVersion = models.CharField(max_length=50,null=True)
    codeSrc = models.CharField(max_length=501,null=True)
    mavenCodePath = models.CharField(max_length=500,null=True)
    targetFilePath = models.CharField(max_length=500,null=True)
    mavenParameter = models.CharField(max_length=500,null=True)
    nginxIp = models.ForeignKey(EquipmentTable,null=True, blank=True,on_delete=models.CASCADE)
    domainName= models.CharField(max_length=50,null=True)
    def __unicode__(self):
        return self.name
        
class EnviromentTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=50,null=True)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)
    company=  models.ForeignKey(CompanyTable,null=True, blank=True,on_delete=models.CASCADE)
    def __unicode__(self):
        return self.name
        
class NodeTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    enviroment = models.ForeignKey(EnviromentTable,null=True, blank=True,on_delete=models.CASCADE)
    serverRoom = models.ForeignKey(ServerRoomTable,null=True, blank=True,on_delete=models.CASCADE)
    project = models.ForeignKey(ProjectTable,null=True, blank=True,on_delete=models.CASCADE)
    service= models.ForeignKey(ServiceTable,null=True, blank=True,on_delete=models.CASCADE)
    nodeNumber= models.CharField(max_length=500,null=True)
    ip = models.ForeignKey(EquipmentTable,null=True, blank=True,on_delete=models.CASCADE)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)    
    portList= models.CharField(max_length=500,null=True)
    logPathList= models.CharField(max_length=500,null=True)
    branch=models.CharField(max_length=50,null=True)
    springBootStartProfile = models.CharField(max_length=500,null=True)
    memory = models.CharField(max_length=500,null=True)
    def __unicode__(self):
        return self.name

class PortTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    portNumber = models.CharField(max_length=50,null=True)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)
    node= models.CharField(max_length=50,null=True)
    def __unicode__(self):
        return self.portNumber
        
class LogPathTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    logPath = models.CharField(max_length=500,null=True)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)
    node= models.CharField(max_length=500,null=True)
    def __unicode__(self):
        return self.id

class HistoryTable ( models.Model ) :
    id = models.AutoField('ID',primary_key=True)
    contant = models.CharField(max_length=5000,null=True)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)
    def __unicode__(self):
        return self.id

class DeployLogTable (models.Model ):
    id = models.AutoField('ID',primary_key=True)
    eventId = models.CharField(max_length=5000,null=True)
    log=models.CharField(max_length=6587,null=True)
    localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
    ctime= models.CharField(max_length=49,null=True,default=localtime)
    node = models.ForeignKey(NodeTable,null=True, blank=True,on_delete=models.CASCADE)
    def __unicode__(self):
        return self.eventId
        
class User(models.Model):
    username=models.CharField(max_length=16)
    password=models.CharField(max_length=32)