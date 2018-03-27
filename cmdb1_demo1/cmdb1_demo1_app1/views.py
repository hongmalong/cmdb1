#coding:utf8
from django.shortcuts import render,HttpResponseRedirect,render_to_response
from django.http import HttpResponse
import time

from .models import CompanyTable,HistoryTable,ProviderTable,ServerRoomTable,CabinetTable,EquipmentTypeTable,\
EquipmentTable,OccupationTable,PrivateTable,ServiceTypeTable,ProjectTable,ServiceTable,NodeTable,\
EnviromentTable,PortTable,LogPathTable

# Create your views here.
def HelloWorld ( request ) :
    return HttpResponse ( 'hello world!' )
    
def Company ( request ) :
    companies= CompanyTable.objects.all() 
    
    if request.method == 'POST':
        companyId=request.POST.get('companyId',None)
        if companyId != '':
            companyObject=companyObject=CompanyTable.objects.get(id=companyId)
            
        companyName = request.POST.get('companyName',None)
        companyFullName = request.POST.get('companyFullName',None)
        
        #delete
        if request.POST.get('delSign',None) == 'true':            
            companyObject.delete()
            new= HistoryTable()
            new.contant="del "+companyObject.name+" from company"
            new.save()
            return HttpResponse(companyObject.name+"已删除")
        
        #add
        if request.POST.get('companyId',None) == '':
            companies=CompanyTable.objects.all()
            new= CompanyTable()
            
            if len(companies) != 0:
                new.id=(companies[len(companies)-1]).id+1
            else:
                new.id=1
            
            new.name= companyName
            new.fullName= companyFullName
            new.save()
            new= HistoryTable()
            new.contant="add "+companyName+" to company"
            new.save()
            return HttpResponse('company '+companyName+' add scusses!')

        else:
            #update
            
            companyObject.name=companyName
            companyObject.fullName=companyFullName
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            companyObject.ctime= localtime
            companyObject.save()
            new= HistoryTable()
            new.contant="update "+companyName+" to company"
            new.save()
            return HttpResponse('company '+companyName+' update scusses!')
                
    return render_to_response ( 'company.html',{'companies':companies} )
    
def Provider ( request ) :
    providers= ProviderTable.objects.all()
    
    if request.method == 'POST':
        providerId = request.POST.get('providerId',None)
        if providerId != '':
            providerObject=ProviderTable.objects.get(id=providerId)
            
        providerName = request.POST.get('providerName',None)
        providerContacts = request.POST.get('providerContacts',None)
        providerTelephone = request.POST.get('providerTelephone',None)
        providerEmail = request.POST.get('providerEmail',None)
        providerAddress = request.POST.get('providerAddress',None)
        providerWebsite = request.POST.get('providerWebsite',None)
        
        #delete
        if request.POST.get('delSign',None) == 'true':            
            providerObject.delete()
            new= HistoryTable()
            new.contant="del "+providerObject.name+" from provider"
            new.save()
            return HttpResponse(providerObject.name+"已删除")
        
        #add
        if request.POST.get('providerId',None) == '':
            new= ProviderTable()
            
            if len(providers) != 0:
                new.id=(providers[len(providers)-1]).id+1
            else:
                new.id=1
            
            new.name= providerName
            new.contacts= providerContacts
            new.telephone= providerTelephone
            new.email= providerEmail
            new.address= providerAddress
            new.website= providerWebsite
            new.save()
            new= HistoryTable()
            new.contant="add "+providerName+" to provider"
            new.save()
            return HttpResponse('provider '+providerName+' add scusses!')

        else:
            #update
            providerObject.name=providerName
            providerObject.contacts=providerContacts
            providerObject.telephone=providerTelephone
            providerObject.email=providerEmail
            providerObject.address=providerAddress
            providerObject.website=providerWebsite
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            providerObject.ctime= localtime
            providerObject.save()
            new= HistoryTable()
            new.contant="update "+providerName+" to provider"
            new.save()
            return HttpResponse('provider '+providerName+' update scusses!')

    return render_to_response ( 'provider.html',{'providers':providers} )

def ServerRoom ( request ) :
    companies= CompanyTable.objects.all()
    providers= ProviderTable.objects.all()
    serverRooms= ServerRoomTable.objects.all()
    
    if request.method == 'POST':
        serverRoomId = request.POST.get('serverRoomId',None)
        if serverRoomId != '':
            serverRoomObject=ServerRoomTable.objects.get(id=serverRoomId)
            
        serverRoomName = request.POST.get('serverRoomName',None)
        serverRoomProviderName = request.POST.get('serverRoomProvider',None)
        if serverRoomProviderName != None:
            serverRoomProvider=ProviderTable.objects.get(name=serverRoomProviderName)
            
        serverRoomCompanyFullName = request.POST.get('serverRoomCompany',None)
        if serverRoomCompanyFullName != None:
            serverRoomCompany = CompanyTable.objects.get( fullName = serverRoomCompanyFullName ) 
            
        serverRoomContacts = request.POST.get('serverRoomContacts',None)
        serverRoomTelephone = request.POST.get('serverRoomTelephone',None)
        serverRoomEmail = request.POST.get('serverRoomEmail',None)
        serverRoomAddress = request.POST.get('serverRoomAddress',None)
        serverRoomWebsite = request.POST.get('serverRoomWebsite',None)
        
        #delete
        if request.POST.get('delSign',None) == 'true':            
            serverRoomObject.delete()
            new= HistoryTable()
            new.contant="del "+serverRoomObject.name+" from serverRoom"
            new.save()
            return HttpResponse(serverRoomObject.name+"已删除")
        
        #add
        if request.POST.get('serverRoomId',None) == '':
            new= ServerRoomTable()
            
            if len(serverRooms) != 0:
                new.id=(serverRooms[len(serverRooms)-1]).id+1
            else:
                new.id=1
            
            new.name= serverRoomName
            new.provider= serverRoomProvider
            new.company= serverRoomCompany
            new.contacts= serverRoomContacts
            new.telephone= serverRoomTelephone
            new.email= serverRoomEmail
            new.address= serverRoomAddress
            new.website= serverRoomWebsite
            new.save()
            new= HistoryTable()
            new.contant="add "+serverRoomName+" to serverRoom"
            new.save()
            return HttpResponse('serverRoom '+serverRoomName+' add scusses!')

        else:
            #update
            serverRoomObject.name=serverRoomName
            serverRoomObject.provider=serverRoomProvider
            serverRoomObject.company=serverRoomCompany
            serverRoomObject.contacts=serverRoomContacts
            serverRoomObject.telephone=serverRoomTelephone
            serverRoomObject.email=serverRoomEmail
            serverRoomObject.address=serverRoomAddress
            serverRoomObject.website=serverRoomWebsite
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            serverRoomObject.ctime= localtime
            serverRoomObject.save()
            new= HistoryTable()
            new.contant="update "+serverRoomName+" to serverRoom"
            new.save()
            return HttpResponse('serverRoom '+serverRoomName+' update scusses!')
    return render_to_response ('serverRoom.html',{'serverRooms':serverRooms,'providers':providers,'companies':companies})

def Cabinet ( request ) :
    serverRooms = ServerRoomTable.objects.all()
    cabinets= CabinetTable.objects.all()
    
    if request.method == 'POST':
        cabinetId = request.POST.get('cabinetId',None)
        if cabinetId != '':
            cabinetObject=CabinetTable.objects.get(id=cabinetId)

        cabinetName = request.POST.get('cabinetName',None)
        cabinetHouseNumber = request.POST.get('cabinetHouseNumber',None)
        cabinetFloor = request.POST.get('cabinetFloor',None)
        cabinetServerRoomName = request.POST.get('cabinetServerRoom',None)
        print(cabinetServerRoomName)
        if cabinetServerRoomName != None:
            cabinetServerRoom= ServerRoomTable.objects.get(name = cabinetServerRoomName)
        
        
        #delete
        if request.POST.get('delSign',None) == 'true':
            
            
            cabinetObject.delete()
            new= HistoryTable()
            new.contant="del "+cabinetObject.name+" from cabinet"
            new.save()
            return HttpResponse(cabinetObject.name+"已删除")
        
        #add
        if request.POST.get('cabinetId',None) == '':
            new= CabinetTable()
            
            if len(cabinets) != 0:
                new.id=(cabinets[len(cabinets)-1]).id+1
            else:
                new.id=1
            
            new.name= cabinetName
            new.houseNumber= cabinetHouseNumber
            new.floor= cabinetFloor
            new.serverRoom= cabinetServerRoom
            new.save()
            new= HistoryTable()
            new.contant="add "+cabinetName+" to cabinet"
            new.save()
            return HttpResponse('cabinet '+cabinetName+' add scusses!')

        else:
            #update
            cabinetObject.name=cabinetName
            cabinetObject.houseNumber=cabinetHouseNumber
            cabinetObject.floor=cabinetFloor
            cabinetObject.serverRoom=cabinetServerRoom
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            cabinetObject.ctime= localtime
            cabinetObject.save()
            new= HistoryTable()
            new.contant="update "+cabinetName+" to cabinet"
            new.save()
            return HttpResponse('cabinet '+cabinetName+' update scusses!')
    return render_to_response ('cabinet.html',{'cabinets':cabinets,'serverRooms':serverRooms})

def EquipmentType ( request ) :
    equipmentTypes = EquipmentTypeTable.objects.all()
    
    if request.method == 'POST':
        equipmentTypeId = request.POST.get('equipmentTypeId',None)
        if equipmentTypeId != '':
            equipmentTypeObject=EquipmentTypeTable.objects.get(id=equipmentTypeId)
        equipmentTypeName = request.POST.get('equipmentTypeName',None)
        
        #delete
        if request.POST.get('delSign',None) == 'true':
            equipmentTypeObject.delete()
            new= HistoryTable()
            new.contant="del "+equipmentTypeObject.name+" from equipmentType"
            new.save()
            return HttpResponse(equipmentTypeObject.name+"已删除")
        
        #add
        if request.POST.get('equipmentTypeId',None) == '':
            new= EquipmentTypeTable()
            
            if len(equipmentTypes) != 0:
                new.id=(equipmentTypes[len(equipmentTypes)-1]).id+1
            else:
                new.id=1
            
            new.name= equipmentTypeName
            new.save()
            new= HistoryTable()
            new.contant="add "+equipmentTypeName+" to equipmentType"
            new.save()
            return HttpResponse('equipmentType '+equipmentTypeName+' add scusses!')

        else:
            #update
            equipmentTypeObject.name=equipmentTypeName
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            equipmentTypeObject.ctime= localtime
            equipmentTypeObject.save()
            new= HistoryTable()
            new.contant="update "+equipmentTypeName+" to equipmentType"
            new.save()
            return HttpResponse('equipmentType '+equipmentTypeName+' update scusses!')
    return render_to_response ('equipmentType.html',{'equipmentTypes':equipmentTypes})
    
def Equipment ( request ) :
    providers= ProviderTable.objects.all()
    cabinets= CabinetTable.objects.all()
    equipments= EquipmentTable.objects.all()
    equipmentTypes= EquipmentTypeTable.objects.all()
    
    if request.method == 'POST':
        equipmentId = request.POST.get('equipmentId',None)
        if equipmentId !='':
            equipmentObject=EquipmentTable.objects.get(id=equipmentId)
        equipmentName = request.POST.get('equipmentName',None)
        equipmentProviderName = request.POST.get('equipmentProvider',None)
        if equipmentProviderName != None:
            equipmentProvider = ProviderTable.objects.get(name = equipmentProviderName )
        
        equipmentIpAddress = request.POST.get('equipmentIpAddress',None)
        equipmentCabinetName = request.POST.get('equipmentCabinet',None)
        if equipmentCabinetName != None:
            equipmentCabinet = CabinetTable.objects.get(name = equipmentCabinetName)
        
        equipmentSequence = request.POST.get('equipmentSequence',None)
        equipmentEquipmentTypeName = request.POST.get('equipmentEquipmentType',None)
        if equipmentEquipmentTypeName != None:
            equipmentEquipmentType= EquipmentTypeTable.objects.get(name = equipmentEquipmentTypeName)
        
        #delete
        if request.POST.get('delSign',None) == 'true':

            equipmentObject.delete()
            new= HistoryTable()
            new.contant="del "+equipmentObject.name+" from equipment"
            new.save()
            return HttpResponse(equipmentObject.name+"已删除")
        
        #add
        if request.POST.get('equipmentId',None) == '':
            new= EquipmentTable()
            
            if len(equipments) != 0:
                new.id=(equipments[len(equipments)-1]).id+1
            else:
                new.id=1
            
            new.name= equipmentName
            new.provider= equipmentProvider
            new.ipAddress= equipmentIpAddress
            new.cabinet= equipmentCabinet
            new.sequence= equipmentSequence
            new.equipmentType= equipmentEquipmentType
            new.save()
            new= HistoryTable()
            new.contant="add "+equipmentName+" to equipment"
            new.save()
            return HttpResponse('equipment '+equipmentName+' add scusses!')

        else:
            #update
            equipmentObject.name=equipmentName
            equipmentObject.provider=equipmentProvider
            equipmentObject.ipAddress=equipmentIpAddress
            equipmentObject.cabinet=equipmentCabinet
            equipmentObject.sequence=equipmentSequence
            equipmentObject.equipmentType=equipmentEquipmentType
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            equipmentObject.ctime= localtime
            equipmentObject.save()
            new= HistoryTable()
            new.contant="update "+equipmentName+" to equipment"
            new.save()
            return HttpResponse('equipment '+equipmentName+' update scusses!')
    return render_to_response ('equipment.html',{'equipments':equipments,'providers':providers,'cabinets':cabinets,'equipmentTypes':equipmentTypes})

def Occupation ( request ) :
    occupationes= OccupationTable.objects.all() 
    
    if request.method == 'POST':
        occupationId=request.POST.get('occupationId',None)
        if occupationId != '':
            occupationObject=OccupationTable.objects.get(id=occupationId)
            
        occupationName = request.POST.get('occupationName',None)
        
        #delete
        if request.POST.get('delSign',None) == 'true':
            occupationObject.delete()
            new= HistoryTable()
            new.contant="del "+occupationObject.name+" from occupation"
            new.save()
            return HttpResponse(occupationObject.name+"已删除")
        
        #add
        if request.POST.get('occupationId',None) == '':
            new= OccupationTable()
            
            if len(occupationes) != 0:
                new.id=(occupationes[len(occupationes)-1]).id+1
            else:
                new.id=1
            
            new.name= occupationName
            new.save()
            new= HistoryTable()
            new.contant="add "+occupationName+" to occupation"
            new.save()
            return HttpResponse('occupation '+occupationName+' add scusses!')

        else:
            #update
            occupationObject.name=occupationName
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            occupationObject.ctime= localtime
            occupationObject.save()
            new= HistoryTable()
            new.contant="update "+occupationName+" to occupation"
            new.save()
            return HttpResponse('occupation '+occupationName+' update scusses!')
                
    return render_to_response ( 'occupation.html',{'occupationes':occupationes} )
    
def Private ( request ) :
    privates= PrivateTable.objects.all()
    companies= CompanyTable.objects.all()
    occupationes= OccupationTable.objects.all()
    
    if request.method == 'POST':
        privateId = request.POST.get('privateId',None)
        if privateId != '':
            privateObject= PrivateTable.objects.get(id = privateId)
        
        privateName = request.POST.get('privateName',None)
        privateCompanyFullName = request.POST.get('privateCompany',None)
        if privateCompanyFullName != None:
            privateCompany = CompanyTable.objects.get( fullName = privateCompanyFullName ) 
            
        privateTelephone = request.POST.get('privateTelephone',None)
        privateEmail = request.POST.get('privateEmail',None)
        privateAddress = request.POST.get('privateAddress',None)
        privateOccupationName = request.POST.get('privateOccupation',None)
        if privateOccupationName != None:
            privateOccupation= OccupationTable.objects.get(name = privateOccupationName )
        
        #delete
        if request.POST.get('delSign',None) == 'true':            
            privateObject.delete()
            new= HistoryTable()
            new.contant="del "+privateObject.name+" from private"
            new.save()
            return HttpResponse(privateObject.name+"已删除")
        
        #add
        if request.POST.get('privateId',None) == '':
            new= PrivateTable()
            
            if len(privates) != 0:
                new.id=(privates[len(privates)-1]).id+1
            else:
                new.id=1
            
            new.name= privateName
            new.company= privateCompany
            new.telephone= privateTelephone
            new.email= privateEmail
            new.address= privateAddress
            new.occupation= privateOccupation
            new.save()
            new= HistoryTable()
            new.contant="add "+privateName+" to private"
            new.save()
            return HttpResponse('private '+privateName+' add scusses!')

        else:
            #update
            privateObject.name=privateName
            privateObject.company=privateCompany
            privateObject.telephone=privateTelephone
            privateObject.email=privateEmail
            privateObject.address=privateAddress
            privateObject.occupation=privateOccupation
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            privateObject.ctime= localtime
            privateObject.save()
            new= HistoryTable()
            new.contant="update "+privateName+" to private"
            new.save()
            return HttpResponse('private '+privateName+' update scusses!')
    return render_to_response ('private.html',{'privates':privates,'companies':companies,'occupationes':occupationes})

def ServiceType ( request ) :
    serviceTypes= ServiceTypeTable.objects.all() 
    
    if request.method == 'POST':
        serviceTypeId=request.POST.get('serviceTypeId',None)
        if serviceTypeId != '':
            serviceTypeObject=serviceTypeObject=ServiceTypeTable.objects.get(id=serviceTypeId)
            
        serviceTypeName = request.POST.get('serviceTypeName',None)
        serviceTypePortNumber = request.POST.get('serviceTypePortNumber',None)
        serviceTypeLogPathType = request.POST.get('serviceTypeLogPathType',None)
        
        #delete
        if request.POST.get('delSign',None) == 'true':
            serviceTypeObject.delete()
            new= HistoryTable()
            new.contant="del "+serviceTypeObject.name+" from serviceType"
            new.save()
            return HttpResponse(serviceTypeObject.name+"已删除")
        
        #add
        if request.POST.get('serviceTypeId',None) == '':
            new= ServiceTypeTable()
            
            if len(serviceTypes) != 0:
                new.id=(serviceTypes[len(serviceTypes)-1]).id+1
            else:
                new.id=1
            
            new.name= serviceTypeName
            new.portNumber= serviceTypePortNumber
            new.save()
            new= HistoryTable()
            new.contant="add "+serviceTypeName+" to serviceType"
            new.save()
            return HttpResponse('serviceType '+serviceTypeName+' add scusses!')

        else:
            #update
            serviceTypeObject.name=serviceTypeName
            serviceTypeObject.portNumber=serviceTypePortNumber
            serviceTypeObject.logPathType=serviceTypeLogPathType
            print(serviceTypeLogPathType)
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            serviceTypeObject.ctime= localtime
            serviceTypeObject.save()
            new= HistoryTable()
            new.contant="update "+serviceTypeName+" to serviceType"
            new.save()
            return HttpResponse('serviceType '+serviceTypeName+' update scusses!')
                
    return render_to_response ( 'servicetype.html',{'serviceTypes':serviceTypes} )

def Project ( request ) :    
    projects= ProjectTable.objects.all()
    companies= CompanyTable.objects.all()
    
    if request.method == 'POST':
        projectId = request.POST.get('projectId',None)
        print(projectId)
        if projectId != '':
            projectObject=ProjectTable.objects.get(id=projectId)
            
        projectName = request.POST.get('projectName',None)
        projectCompanyFullName = request.POST.get('projectCompany',None)
        if projectCompanyFullName != None:
            projectCompany= CompanyTable.objects.get(fullName=projectCompanyFullName)
        
        #delete
        if request.POST.get('delSign',None) == 'true':            
            projectObject.delete()
            new= HistoryTable()
            new.contant="del "+projectObject.name+" from project"
            new.save()
            return HttpResponse(projectObject.name+"已删除")
        
        #add
        if request.POST.get('projectId',None) == '':
            new= ProjectTable()
            
            if len(projects) != 0:
                new.id=(projects[len(projects)-1]).id+1
            else:
                new.id=1
            
            new.name= projectName
            new.company=projectCompany
            new.save()
            new= HistoryTable()
            new.contant="add "+projectName+" to project"
            new.save()
            return HttpResponse('project '+projectName+' add scusses!')

        else:
            #update
            projectObject.name=projectName
            projectObject.company= projectCompany
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            projectObject.ctime= localtime
            projectObject.save()
            new= HistoryTable()
            new.contant="update "+projectName+" to project"
            new.save()
            return HttpResponse('project '+projectName+' update scusses!')

    return render_to_response ( 'project.html',{'projects':projects,'companies':companies} )

def Service ( request ) :
    services= ServiceTable.objects.all() 
    projectes= ProjectTable.objects.all()
    privates= PrivateTable.objects.all()
    serviceTypes= ServiceTypeTable.objects.all()
    
    if request.method == 'POST':
        serviceId=request.POST.get('serviceId',None)
        if serviceId != '':
            serviceObject=ServiceTable.objects.get(id=serviceId)
            
        serviceName = request.POST.get('serviceName',None)
        serviceProject = request.POST.get('serviceProject',None)
        print(serviceProject)
        if serviceProject != None:
            serviceProjectObject=ProjectTable.objects.get(name=serviceProject)
            
        serviceProgrammer = request.POST.get('serviceProgrammer',None)
        if serviceProgrammer != None:
            serviceProgrammerObject=PrivateTable.objects.get(name=serviceProgrammer)
        
        serviceTestEngineer = request.POST.get('serviceTestEngineer',None)
        if serviceTestEngineer != None:
            serviceTestEngineerObject=PrivateTable.objects.get(name=serviceTestEngineer)
            
        serviceProductManager = request.POST.get('serviceProductManager',None)
        if serviceProductManager != None:
            serviceProductManagerObject=PrivateTable.objects.get(name=serviceProductManager)
            
        serviceOperationEngineer = request.POST.get('serviceOperationEngineer',None)
        if serviceOperationEngineer != None:
            serviceOperationEngineerObject=PrivateTable.objects.get(name=serviceOperationEngineer)
            
        serviceServiceType = request.POST.get('serviceServiceType',None)
        if serviceServiceType != None:
            serviceServiceTypeObject=ServiceTypeTable.objects.get(name=serviceServiceType)
        
        #delete
        if request.POST.get('delSign',None) == 'true':
            serviceObject.delete()
            new= HistoryTable()
            new.contant="del "+serviceObject.name+" from service"
            new.save()
            return HttpResponse(serviceObject.name+"已删除")
        
        #add
        if request.POST.get('serviceId',None) == '':
            new= ServiceTable()
            
            if len(services) != 0:
                new.id=(services[len(services)-1]).id+1
            else:
                new.id=1
            
            new.name= serviceName
            new.project= serviceProjectObject
            new.programmer= serviceProgrammerObject
            new.testEngineer= serviceTestEngineerObject
            new.productManager= serviceProductManagerObject
            new.operationEngineer= serviceOperationEngineerObject
            new.serviceType= serviceServiceTypeObject
            new.save()
            new= HistoryTable()
            new.contant="add "+serviceName+" to service"
            new.save()
            return HttpResponse('service '+serviceName+' add scusses!')

        else:
            #update
            serviceObject.name=serviceName
            serviceObject.project= serviceProjectObject
            serviceObject.programmer= serviceProgrammerObject
            serviceObject.testEngineer= serviceTestEngineerObject
            serviceObject.productManager= serviceProductManagerObject
            serviceObject.operationEngineer= serviceOperationEngineerObject
            serviceObject.serviceType= serviceServiceTypeObject
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            serviceObject.ctime= localtime
            serviceObject.save()
            new= HistoryTable()
            new.contant="update "+serviceName+" to service"
            new.save()
            return HttpResponse('service '+serviceName+' update scusses!')
                
    return render_to_response ( 'service.html',{'services':services,'projectes':projectes,'privates':privates,'serviceTypes':serviceTypes} )

def Enviroment ( request ) :
    companies= CompanyTable.objects.all()
    enviroments= EnviromentTable.objects.all()
    
    if request.method == 'POST':
        enviromentId = request.POST.get('enviromentId',None)
        if enviromentId != '':
            enviromentObject=EnviromentTable.objects.get(id=enviromentId)
            
        enviromentName = request.POST.get('enviromentName',None)
            
        enviromentCompanyFullName = request.POST.get('enviromentCompany',None)
        if enviromentCompanyFullName != None:
            enviromentCompany = CompanyTable.objects.get( fullName = enviromentCompanyFullName ) 
        
        #delete
        if request.POST.get('delSign',None) == 'true':            
            enviromentObject.delete()
            new= HistoryTable()
            new.contant="del "+enviromentObject.name+" from enviroment"
            new.save()
            return HttpResponse(enviromentObject.name+"已删除")
        
        #add
        if request.POST.get('enviromentId',None) == '':
            new= EnviromentTable()
            
            if len(enviroments) != 0:
                new.id=(enviroments[len(enviroments)-1]).id+1
            else:
                new.id=1
            
            new.name= enviromentName
            new.company= enviromentCompany
            new.save()
            new= HistoryTable()
            new.contant="add "+enviromentName+" to enviroment"
            new.save()
            return HttpResponse('enviroment '+enviromentName+' add scusses!')

        else:
            #update
            enviromentObject.name=enviromentName
            enviromentObject.company=enviromentCompany
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            enviromentObject.ctime= localtime
            enviromentObject.save()
            new= HistoryTable()
            new.contant="update "+enviromentName+" to enviroment"
            new.save()
            return HttpResponse('enviroment '+enviromentName+' update scusses!')
    return render_to_response ('enviroment.html',{'enviroments':enviroments,'companies':companies})
"""   
def Ip ( request ) :    
    companies= CompanyTable.objects.all()
    ips= IpTable.objects.all()
    
    if request.method == 'POST':
        ipId = request.POST.get('ipId',None)
        if ipId != '':
            ipObject=IpTable.objects.get(id=ipId)
            
        ipIp = request.POST.get('ipIp',None)
            
        ipCompanyFullName = request.POST.get('ipCompany',None)
        if ipCompanyFullName != None:
            ipCompany = CompanyTable.objects.get( fullName = ipCompanyFullName ) 
        
        #delete
        if request.POST.get('delSign',None) == 'true':            
            ipObject.delete()
            new= HistoryTable()
            new.contant="del "+ipObject.name+" from ip"
            new.save()
            return HttpResponse(ipObject.name+"已删除")
        
        #add
        if request.POST.get('ipId',None) == '':
            new= IpTable()
            
            if len(ips) != 0:
                new.id=(ips[len(ips)-1]).id+1
            else:
                new.id=1
            
            new.ip= ipIp
            
            new.company= ipCompany
            new.save()
            new= HistoryTable()
            new.contant="add "+ipIp+" to ip"
            new.save()
            return HttpResponse('ip '+ipIp+' add scusses!')

        else:
            #update
            ipObject.ip=ipIp
            ipObject.company=ipCompany
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            ipObject.ctime= localtime
            ipObject.save()
            new= HistoryTable()
            new.contant="update "+ipIp+" to ip"
            new.save()
            return HttpResponse('ip '+ipIp+' update scusses!')
    return render_to_response ('ip.html',{'ips':ips,'companies':companies})
"""   
def Node ( request ) :
    nodes= NodeTable.objects.all()
    enviroments = EnviromentTable.objects.all()
    serverRooms = ServerRoomTable.objects.all()
    projects = ProjectTable.objects.all()
    services = ServiceTable.objects.all()
    equipments=EquipmentTable.objects.all()
    ports=PortTable.objects.all()
    #节点和端口对应
    #tomcat 3个端口
    #zookeeper 9个端口
    #redis 6个端口+10000
    #不能在服务页面绑定端口号，不同环境端口不同
    #zookeeper两个端口相同的节点有可能部署在同一个服务器上，所以端口号不能一样。所有节点的端口号都不能重复，为的是全部节点都部署在同一个服务器上时，不冲突。
    #可以把端口号绑定在节点上，但是不能在节点上规划出端口数量，只能给出列表
    #在端口表，同一个端口可以对应多个节点
    #在节点表，应该体现ip+port
    
    if request.method == 'POST':
        nodeId = request.POST.get('nodeId',None)
        if nodeId != '':
            nodeObject=NodeTable.objects.get(id=nodeId)
        
        nodeEnviromentName = request.POST.get('nodeEnviroment',None)
        if nodeEnviromentName != None:
            nodeEnviroment=EnviromentTable.objects.get(name=nodeEnviromentName)
            
        nodeServerRoomName = request.POST.get('nodeServerRoom',None)
        if nodeServerRoomName != None:
            nodeServerRoom=ServerRoomTable.objects.get(name=nodeServerRoomName)
            
        nodeProjectName = request.POST.get('nodeProject',None) 
        if nodeProjectName != None:
            nodeProject=ProjectTable.objects.get(name=nodeProjectName)
            
        nodeServiceName = request.POST.get('nodeService',None)
        if nodeServiceName != None:
            nodeService=ServiceTable.objects.get(name=nodeServiceName)
        
        nodeNodeNumber = request.POST.get('nodeNodeNumber',None)
        
        nodeIpIp = request.POST.get('nodeIp',None)
        if nodeIpIp != None:
            nodeIp= EquipmentTable.objects.get(ipAddress = nodeIpIp)
        
        nodePortList = request.POST.get('nodePortList',None)
        nodeLogPathList = request.POST.get('nodeLogPathList',None)
        print(nodeLogPathList)

        #delete
        if request.POST.get('delSign',None) == 'true':

            portList=nodeObject.portList.split(',')
            del portList[int(nodeObject.service.serviceType.portNumber)]
            for i in portList:
                PortTable.objects.get(portNumber=i).delete()
                print(i)
                new= HistoryTable()
                new.contant="del "+i+" from portTable"
                new.save()
                
            logPathList=nodeLogPathList.split(',')
            for i in logPathList:
                LogPathTable.objects.get(logPath=i).delete()
                new= LogPathTable()
                new.contant="del "+i+" from LogPathTable"
                new.save()
            
            nodeObject.delete()
            new= HistoryTable()
            new.contant="del "+nodeObject.enviroment.name+"_"+nodeObject.serverRoom.name+"_"+nodeObject.project.name+"_"+\
                        nodeObject.service.name+"_"+nodeObject.nodeNumber+" "+nodeObject.ip.ipAddress+":"+\
                        nodeObject.portList+" from node"
            new.save()
            return HttpResponse(nodeObject.enviroment.name+"_"+nodeObject.serverRoom.name+"_"+nodeObject.project.name+"_"+\
                        nodeObject.service.name+"_"+nodeObject.nodeNumber+" "+nodeObject.ip.ipAddress+":"+\
                        nodeObject.portList+"已删除")
        
        #add
        if request.POST.get('nodeId',None) == '':
            new= NodeTable()
            
            new.id=0
            if len(nodes) != 0:
                new.id=(nodes[len(nodes)-1]).id+1
            else:
                new.id=1
            
            new.enviroment= nodeEnviroment
            new.serverRoom= nodeServerRoom
            new.project= nodeProject
            new.service= nodeService
            new.nodeNumber= nodeNodeNumber
            new.ip= nodeIp
            #端口范围从8000-65535
            #构建一个数组
            #把已有的端口号做成一个数组
            #对比两个数组，把不匹配的做成一个数组
            #从这个数组的开头选出三个端口号
            portBegin=8000
            portRange=[]
            while portBegin>=8000:
                portRange.append(portBegin)
                portBegin+=1
                if portBegin==65535:
                    break
            
            currentPortList=[]
            ports=PortTable.objects.all()
            portsLen=len(ports)
            if portsLen !=0:
                while 1>0:
                    currentPortList.append(ports[portsLen-1].portNumber)
                    portsLen-=1
                    if portsLen==0:
                        break
            
                for  i in currentPortList:
                    if int(i) in portRange:
                        portRange.remove(int(i))

            ports=[]
            portList=''
            i=0
            for i in range(int(nodeService.serviceType.portNumber)):
                ports.append(portRange[i])
                portList+=(str(portRange[i])+',')
                i+=1
                if i == int(nodeService.serviceType.portNumber):
                    break

            for  i in ports:
                portObject=PortTable()
                portObject.portNumber=str(i)
                portObject.node=new.id
                portObject.save()
            
                
            new.portList=portList
            
            #nodeLogPathList
            #日志列表是个列表
            #对于不同类型的服务，产生的日志路径是不同的
            #所以要在服务类型那里定义日志列表的路径
            #例如tomcat路径是autodeploy后面加tomcat，然后加环境-机房-项目-服务-节点
            #java日志是autodeploy后面加java，然后加环境-机房-项目-服务-节点
            #可以设置个开关，日志路径模型是a，就用a模型带节点的；如果类型是b，那就用b的类型
            #zookeeper是autodeploy后面加zookeeper，然后加环境-机房-项目-服务-节点
            #redis是autodeploy后面加redis，然后加环境-机房-项目-服务-节点
            #redis_cluster是autodeploy后面加redis_cluster，然后加环境-机房-项目-服务-节点
            
            commonLogPath='/'+nodeProject.company.name+'/log/autodepoly/'
    
            if nodeService.serviceType.name=='tomcat':
                nodeService.serviceType.name='java'
                if new.service.serviceType.logPathType == 'a':
                    logPath=commonLogPath+nodeService.serviceType.name+'/'+nodeEnviromentName+'-'+nodeServerRoomName+'-'+nodeProjectName+'-'+nodeServiceName
                elif new.service.serviceType.logPathType == 'b':
                    logPath=commonLogPath+nodeService.serviceType.name+'/'+nodeEnviromentName+'-'+nodeServerRoomName+'-'+nodeProjectName+'-'+nodeServiceName+'-'+nodeNodeNumber
            
            logPathObject=LogPathTable()
            logPathObject.logPath=logPath
            logPathObject.node=new.id
            logPathObject.save()
            new.logPathList= logPath
            new.save()
            new= HistoryTable()
            new.contant="add "+nodeEnviroment.name+"_"+nodeServerRoom.name+"_"+nodeProject.name+"_"+\
                        nodeService.name+"_"+nodeNodeNumber+" "+nodeIp.ipAddress+":"+\
                        nodePortList+" to node"
            new.save()
            return HttpResponse('node '+nodeEnviroment.name+"_"+nodeServerRoom.name+"_"+nodeProject.name+"_"+\
                        nodeService.name+"_"+nodeNodeNumber+" "+nodeIp.ipAddress+":"+\
                        nodePortList+' add scusses!')

        else:
            #update
            nodeObject.enviroment= nodeEnviroment
            nodeObject.serverRoom= nodeServerRoom
            nodeObject.project= nodeProject
            nodeObject.service= nodeService
            nodeObject.nodeNumber= nodeNodeNumber
            nodeObject.ip= nodeIp
            oldNodePortList=(nodeObject.portList).split(',')
            oldNodePortList.remove('')
            newNodePortList=(nodePortList).split(',')
            if '' in newNodePortList:
                newNodePortList.remove('')

            portBegin=8000
            portRange=[]
            while portBegin>=8000:
                portRange.append(portBegin)
                portBegin+=1
                if portBegin==8010:
                    break
            
            currentPortList=[]
            ports=PortTable.objects.all()
            portsLen=len(ports)
            if portsLen !=0:
                while 1>0:
                    currentPortList.append(ports[portsLen-1].portNumber)
                    portsLen-=1
                    if portsLen==0:
                        break
            
                for  i in currentPortList:
                    if int(i) in portRange:
                        portRange.remove(int(i))
            
            needAddPortListAndNotRepeat=[]
            RepeatPortList=[]
            for i in newNodePortList:
                if int(i) in portRange:
                    needAddPortListAndNotRepeat.append(i)
                else:
                    RepeatPortList.append(i)
                    
            RepeatPortListNotInOldNodePortList=[]
            for i in RepeatPortList:
                if i not in oldNodePortList:
                    RepeatPortListNotInOldNodePortList.append(i)
                else:
                    if newNodePortList.count(i)>1:
                        RepeatPortListNotInOldNodePortList.append(i)
        
            if RepeatPortListNotInOldNodePortList:
                for i in RepeatPortListNotInOldNodePortList:
                    if (int(i) <8000 or int(i)>65535):
                        return HttpResponse('超出范围: '+str(i))
                    else:
                        return HttpResponse('重复的端口是'+str(RepeatPortListNotInOldNodePortList))

            needDeletePortList=[]
            for i in oldNodePortList:
                if i not in newNodePortList:
                    needDeletePortList.append(i)
                    
            for i in needDeletePortList:
                needDeletePortListObject=PortTable.objects.get(portNumber=i)
                needDeletePortListObject.delete()
            
            needAddPortList=[]
            for i in newNodePortList:
                if i not in oldNodePortList:
                    needAddPortList.append(i)
            
            for i in needAddPortList:
                portObject=PortTable()
                portObject.portNumber=i
                portObject.node=nodeObject.id
                portObject.save()

            nodeObject.portList=nodePortList
            oldNodeLogPathList=nodeObject.logPathList
            newNodeLogPathList=nodeLogPathList
            oldNodeLogPathListList=oldNodeLogPathList.split(',')
            newNodeLogPathListList=newNodeLogPathList.split(',')
            for i in oldNodeLogPathListList:
                if i not in newNodeLogPathListList:
                    print(i+' need del')
                    (LogPathTable.objects.get(logPath=i)).delete()

            for i in newNodeLogPathListList:
                if i not in oldNodeLogPathListList:
                    print(i+' need add')
                    new=LogPathTable()
                    new.logPath=i
                    new.node=nodeObject.id
                    new.save()

                   
            nodeObject.logPathList= newNodeLogPathList
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            nodeObject.ctime= localtime
            nodeObject.save()
            new= HistoryTable()
            new.contant="update "+nodeEnviroment.name+"_"+nodeServerRoom.name+"_"+nodeProject.name+"_"+\
                        nodeService.name+"_"+nodeNodeNumber+" "+nodeIp.ipAddress+":"+\
                        nodePortList+" to node"
            new.save()
            return HttpResponse('node '+nodeEnviroment.name+"_"+nodeServerRoom.name+"_"+nodeProject.name+"_"+\
                        nodeService.name+"_"+nodeNodeNumber+" "+nodeIp.ipAddress+":"+\
                        nodePortList+' update scusses!')
                        
    return render_to_response ('node.html',{'nodes':nodes,'enviroments':enviroments,'serverRooms':serverRooms,'projects':projects,'services':services,'equipments':equipments,'ports':ports})
    
def Port ( request ) :
    return HttpResponse ( 'hello world!' )
    
def LogPath ( request ) :
    return HttpResponse ( 'hello world!' )






























