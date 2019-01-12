#coding:utf8
from django.shortcuts import render,HttpResponseRedirect,render_to_response,redirect
from django.http import HttpResponse
import time,os,sys,re,paramiko,git
from operator import itemgetter, attrgetter
from functools import wraps
    

from .models import CompanyTable,HistoryTable,ProviderTable,ServerRoomTable,CabinetTable,EquipmentTypeTable,\
EquipmentTable,OccupationTable,PrivateTable,ServiceTypeTable,ProjectTable,ServiceTable,NodeTable,\
EnviromentTable,PortTable,LogPathTable,DeployLogTable,DeployHostTable,User,EventTable

# Create your views here.
def HelloWorld ( request ) :
    return HttpResponse ( 'hello world!' )

#################################################
def Check_login(f):
    @wraps(f)
    def inner(request,*args,**kwargs):
        if request.session.get('is_login')=='1':
            return f(request,*args,**kwargs)
        else:
            return redirect('/login') 
    return inner

def Login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)
        if len(user)==0:
            return HttpResponse(username+' 不存在')
        elif user[0].password!=password:
            return HttpResponse('密码不正确')
        else:
            request.session['is_login']='1'  
            request.session['user_id']=user[0].id
            #return render(request,'index.html',{"user":user[0]})
            return HttpResponse('/index')#返回一个url，带着request往回传，这个“它会带着request往浏览器传，我之前不知道。”
            #？除了request，HttpRespose()还会往回传什么？我看网页上，HttpResponse()还有很多其他用法
            #从这里开始页面有了cookie，原来的login页面是没有cookie的。也或者说是有了session
            #只有当登陆了才能获得到session，没登陆是不能获得session的
    return render(request,'login.html')

@Check_login
def Index(request):
    user_id1=request.session.get('user_id')
    userobj=User.objects.filter(id=user_id1)
    if userobj:
        return render(request,'index.html',{"user":userobj[0]})

def Logout(request):
    request.session['is_login']='0'  
    return redirect('/login') 

def Regist(request):
    if request.method=='POST':
        username=request.POST.get('username',None)
        if username:
            password=request.POST.get('password',None)
            if password:
                userObjects=User.objects.filter(username=username)
                if userObjects:
                    return HttpResponse('用户名已存在')
                else:
                    new=User()
                    new.username=username
                    new.password=password
                    new.save()
                    #自动登录
                    request.session['is_login']='1'
                    userObjects=User.objects.filter(username=username)
                    request.session['user_id']=userObjects[0].id
                    return HttpResponse('/index')
                    #return render(request,'index.html',{"user":userObjects[0]})
                    #return HttpResponse('Regist ok!')
            else:
                return HttpResponse('Password is not empty!')
        else:
            return HttpResponse('Username is not empty!')
    elif request.method=='GET':
        return render(request,'regist.html')
        

@Check_login    
def Company ( request ) :
    companies= CompanyTable.objects.all()
    
    if request.method == 'POST':
        companyId=request.POST.get('companyId',None)
        if companyId != '':
            companyObject=companyObject=CompanyTable.objects.get(id=companyId)
            
        companyName = request.POST.get('companyName',None)
        companyFullName = request.POST.get('companyFullName',None)
        companyUploadPath = request.POST.get('companyUploadPath',None)
        if companyUploadPath == '':
            commonUploadPath='/var/upload/'
            companyUploadPath=commonUploadPath+companyName
            
        if companyUploadPath != None:
            if os.path.exists(companyUploadPath):
                print('存在')
            else:
                print('不存在')
                os.system('mkdir -p '+companyUploadPath)

        #delete
        if request.POST.get('delSign',None) == 'true':
            uploadPath=companyObject.uploadPath
            os.system('rm -fr '+uploadPath)
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
            new.uploadPath= companyUploadPath
            new.save()
            new= HistoryTable()
            new.contant="add "+companyName+" to company"
            new.save()
            return HttpResponse('company '+companyName+' add scusses!')

        else:
            #update
            
            companyObject.name=companyName
            companyObject.fullName=companyFullName
            companyObject.uploadPath=companyUploadPath
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
    equipments=EquipmentTable.objects.all()
    serverRoomsNew=[]
    for serverRoom in serverRooms: 
        deployHost=DeployHostTable.objects.get(serverRoom=serverRoom)
        serverRoom.deployHost=deployHost.host.ipAddress
        serverRoomsNew.append(serverRoom)
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
        serverRoomDeployHost= request.POST.get('serverRoomDeployHost',None)
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
            new = DeployHostTable()
            new.serverRoom=ServerRoomTable.objects.get(name=serverRoomName)
            new.host=EquipmentTable.objects.get(ipAddress=serverRoomDeployHost)
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
            deployHostObject = DeployHostTable.objects.get(serverRoom=serverRoomObject)
            deployHostObject.host=EquipmentTable.objects.get(ipAddress=serverRoomDeployHost)
            deployHostObject.save()
            
            new= HistoryTable()
            new.contant="update "+serverRoomName+" to serverRoom"
            new.save()
            return HttpResponse('serverRoom '+serverRoomName+' update scusses!')
    return render_to_response ('serverRoom.html',{'serverRooms':serverRoomsNew,'providers':providers,'companies':companies,'equipments':equipments})

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
        equipmentControlPort = request.POST.get('equipmentControlPort',None)
        print(equipmentControlPort)
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
            new.controlPort= equipmentControlPort
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
            equipmentObject.controlPort= equipmentControlPort
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
        serviceTypeVersion = request.POST.get('serviceTypeVersion',None)
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
            new.version= serviceTypeVersion
            new.portNumber= serviceTypePortNumber
            new.logPathType= serviceTypeLogPathType
            new.save()
            new= HistoryTable()
            new.contant="add "+serviceTypeName+" to serviceType"
            new.save()
            return HttpResponse('serviceType '+serviceTypeName+' add scusses!')

        else:
            #update
            serviceTypeObject.name=serviceTypeName
            serviceTypeObject.version= serviceTypeVersion
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
    equipments=EquipmentTable.objects.all()
    
    if request.method == 'POST':
        serviceId=request.POST.get('serviceId',None)
        if serviceId != '':
            serviceObject=ServiceTable.objects.get(id=serviceId)
            
        serviceName = request.POST.get('serviceName',None)
        serviceProject = request.POST.get('serviceProject',None)
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
        serviceJavaVersion = request.POST.get('serviceJavaVersion',None)
        serviceCodeSrc = request.POST.get('serviceCodeSrc',None)
        serviceMavenCodePath = request.POST.get('serviceMavenCodePath',None)
        serviceTargetFilePath = request.POST.get('serviceTargetFilePath',None)
        serviceMavenParameter = request.POST.get('serviceMavenParameter',None)
        
        serviceNginxIp = request.POST.get('serviceNginxIp',None)
        if serviceNginxIp != None:
            serviceNginxIpObject=EquipmentTable.objects.get(ipAddress=serviceNginxIp)
           
        serviceDomainName=request.POST.get('serviceDomainName',None)

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
            new.javaVersion= serviceJavaVersion
            new.codeSrc=serviceCodeSrc
            new.mavenCodePath=serviceMavenCodePath
            new.targetFilePath=serviceTargetFilePath
            print(serviceTargetFilePath)
            new.mavenParameter=serviceMavenParameter
            new.nginxIp=serviceNginxIpObject
            new.domainName=serviceDomainName
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
            serviceObject.javaVersion= serviceJavaVersion
            serviceObject.codeSrc=serviceCodeSrc
            serviceObject.mavenCodePath=serviceMavenCodePath
            serviceObject.targetFilePath=serviceTargetFilePath
            serviceObject.mavenParameter=serviceMavenParameter
            serviceObject.nginxIp=serviceNginxIpObject
            serviceObject.domainName=serviceDomainName
            
            localtime = time.strftime( "%Y%m%d%H%M%S" , time.localtime() )
            serviceObject.ctime= localtime
            serviceObject.save()
            new= HistoryTable()
            new.contant="update "+serviceName+" to service"
            new.save()
            return HttpResponse('service '+serviceName+' update scusses!')
                
    return render_to_response ( 'service.html',{'services':services,'projectes':projectes,'privates':privates,'serviceTypes':serviceTypes,'equipments':equipments} )

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
@Check_login 
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
            nodeService=ServiceTable.objects.get(name=nodeServiceName ,project=nodeProject)
        
        nodeNodeNumber = request.POST.get('nodeNodeNumber',None)
        
        nodeIpIp = request.POST.get('nodeIp',None)
        if nodeIpIp != None:
            nodeIp= EquipmentTable.objects.get(ipAddress = nodeIpIp)
        
        nodePortList = request.POST.get('nodePortList',None)
        nodeLogPathList = request.POST.get('nodeLogPathList',None)
        nodeBranch = request.POST.get('nodeBranch',None)
        nodeSpringBootStartProfile = request.POST.get('nodeSpringBootStartProfile',None)
        nodeMemory_value = request.POST.get('nodeMemory_value',None)
        #delete
        if request.POST.get('delSign',None) == 'true':

            portList=nodeObject.portList.split(',')
            del portList[int(nodeObject.service.serviceType.portNumber)]
            for i in portList:
                PortTable.objects.get(portNumber=i).delete()
                new= HistoryTable()
                new.contant="del "+i+" from portTable"
                new.save()
                
            #logPathList=nodeLogPathList.split(',')
            #for i in logPathList:
            LogPathTableObject=LogPathTable.objects.get(logPath=nodeLogPathList , node=nodeObject.id)
            LogPathTableObject.delete()
            new= HistoryTable()
            new.contant="del nodeObject.id: "+str(nodeObject.id)+" logPath: "+nodeLogPathList+" from LogPathTable"
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
            #端口范围从8081-65535
            #构建一个数组
            #把已有的端口号做成一个数组
            #对比两个数组，把不匹配的做成一个数组
            #从这个数组的开头选出三个端口号
            portBegin=8081
            portRange=[]
            while portBegin>=8080:
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
            
            serviceTypes=['tomcat','springBoot','dubbo']
            for i in serviceTypes:
                if nodeService.serviceType.name==i:
                    nodeService.serviceType.name='java'
                    if new.service.serviceType.logPathType == 'a':
                        logPath=commonLogPath+nodeService.serviceType.name+'/'+nodeEnviromentName+'-'+nodeServerRoomName+'-'+nodeProjectName+'-'+nodeServiceName
                    elif new.service.serviceType.logPathType == 'b':
                        print('b')
                        logPath=commonLogPath+nodeService.serviceType.name+'/'+nodeEnviromentName+'-'+nodeServerRoomName+'-'+nodeProjectName+'-'+nodeServiceName+'-'+nodeNodeNumber
            
            logPathObject=LogPathTable()
            logPathObject.logPath=logPath
            logPathObject.node=new.id
            logPathObject.save()
            new.logPathList= logPath
            new.branch=nodeBranch
            new.springBootStartProfile = nodeSpringBootStartProfile
            new.memory = nodeMemory_value
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

            portBegin=8081
            portRange=[]
            while portBegin>=8080:
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
                    if (int(i) <8080 or int(i)>65535):
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
            nodeObject.branch=nodeBranch
            nodeObject.springBootStartProfile = nodeSpringBootStartProfile
            nodeObject.memory = nodeMemory_value
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

def Unzip(srcPath,targetPath,targetChildPath,host,sshPort,sshName,event,node):
    CheckPathAndAdd(host,sshPort,sshName,targetPath,event,node)
    #outLogFile=targetPath+'/nohup.out'
    command='tar zxf '+srcPath+' -C '+targetPath+'\n'
    #command='yum install httpd'
    #RemoteControl(host,sshPort,sshName,command,event,node)

    RemoterControlInvoke4ok13(host,sshPort,sshName,command,event,node)

    temporaryPath=targetPath+targetChildPath
    #time.sleep(3)
    exist=RemoteFileExist(host,sshPort,sshName,temporaryPath)
    if exist == 'exist':
        log=host+" : "+'成功:解压缩'+srcPath+' to '+temporaryPath
        DeployLog(log,event,node)
        return 'done'
    else:
        log=host+" : "+'失败:解压'+srcPath
        DeployLog(log,event,node)
        log=host+" : "+'false'
        DeployLog(log,event,node)
        return log

def Mv(srcPath,targetPath,host,sshPort,sshName,event,node):
    command=('mv -f '+srcPath+' '+targetPath)
    RemoteControl(host,sshPort,sshName,command,event,node)
    exist=RemoteFileExist(host,sshPort,sshName,targetPath)
    if exist == 'exist':
        log=host+" : "+(' 成功:mv '+srcPath+' to '+targetPath)
        DeployLog(log,event,node)
    else:
        log=host+" : "+('失败：mv '+srcPath+' to '+targetPath)
        DeployLog(log,event,node)        
        log=host+" : "+'false'
        DeployLog(log,event,node)
        return log
        
def Sed(src,target,filePath,host,sshPort,sshName,event,node):
    command=("grep -n '"+src+"' "+filePath)
    result=RemoteControl(host,sshPort,sshName,command,event,node)
    if len(result)==0:
        log=host+" : "+'未找到: '+src+(' ')+filePath
        DeployLog(log,event,node)
    else:
        command=("sed -i 's%"+src+"%"+target+"%g' "+filePath)
        result=RemoteControl(host,sshPort,sshName,command,event,node)
        if len(result)==0:
            log=host+" : "+'成功：替换 '+filePath+' : '+src+' to '+target
            DeployLog(log,event,node)
        else:
            log=host+" : "+'失败：替换 '+filePath+' : '+src+' to '+target
            DeployLog(log,event,node)
            log=host+" : "+'false'
            DeployLog(log,event,node)
            return log
            
def RemoteControl(host,port,userName,command,event,node):
    import paramiko,time,sys
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport((host, port))
    transport.connect(username=userName, pkey=private_key)
    ssh = paramiko.SSHClient()
    ssh._transport = transport
    log=host+' : '+command
    DeployLog(log,event,node)
    stdin, stdout, stderr = ssh.exec_command(command)
    stderrList=stderr.readlines()
    stdoutList=stdout.readlines()
    result=stderrList+stdoutList
    if len(result) != 0:
        if len(result) !=1:
            for i in result:
                if len(i) ==0:
                    break
                log='&nbsp;&nbsp;'+i.strip('/n')
                if '正在检出文件' in log:
                    #这一步出现在git拉取代码文件的过程中
                    break
                DeployLog(log,event,node)
        else:
            for i in result:
                log=host+" : "+'结果：'+i.strip()
                DeployLog(log,event,node)
    else:
        log=host+" : "+'没有返回结果'
        DeployLog(log,event,node)
    transport.close()
    return result

def RemoterControlInvoke(host,port,userName,command,event,node):
    #这个方法暂时不可用。如果想测试，可以用有道云笔记中的例子测试《python 交互式远程操作》
    import paramiko,time,sys
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport((host,port))
    transport.connect(username=userName, pkey=private_key)
    a=transport.open_session()
    a.settimeout(100)
    a.get_pty()
    a.invoke_shell()
    log=host+" : "+command
    DeployLog(log,event,node)
    a.send(command+' \n')
    b=bytes.decode(a.recv(10240))
    log=host+" : "+b+' 开始循环等待反馈'
    DeployLog(log,event,node)
    #如果b不以#结束，就执行循环
    i=1
    while not b.endswith("# "):
        #循环的过程是，再去获取b，存入数据库，比较它是否是#空格结尾
        b=bytes.decode(a.recv(10240))
        #由于获取频率太快，所以经常一句话获取不完，所以，当收到的结果结尾不包含空格，也就是不是一句完整的话，的时候，不往数据库里存数据。直接进行下一次循环
        #if not b.endswith(" "):
        #   continue
        #i=1
        ##正则可以用多个分隔符进行分割            
        #c=re.split('["\r\n""\r"]',b)            
        #for j in c:            
        #    print(len(j))            
        #    if len(j) == 0:            
        #        continue            
        #        #continue停止本次循环            
        #    log=host+" : 第"+str(i)+'次循环 '+j            
        #    DeployLog(log,event,node)            
        #if 'Progress' in b:
        #    continue
        log=host+" : 第"+str(i)+'次循环 '+b            
        DeployLog(log,event,node) 
        #这里获取的速度太快了，可能获取的结果不是一句完整的话，目前还没有办法解决这个现象。
        i+=1
        if b.endswith(' [y/N]: '):
            a.send('y\n')
        #以后有别的判断的，可以修改判断值和发送值。来实现自动应答。
        #上面的内容保留是因为正则的使用，需要留底。
            
            

    #i=1
    #正则可以用多个分隔符进行分割
    #c=re.split('["\r\n""\r"]',b)
    #for j in c:
    #    print(len(j))
    #    if len(j) == 0:
    #       continue
    #       #continue停止本次循环
    #    log=host+" : 第"+str(i)+'次循环 '+j
    #    DeployLog(log,event,node)
    #    i+=1
    a.close()
    transport.close()

def RemoterControlInvoke4ok(host,port,userName,commands,event,node):
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #此时会话已打开
    a.settimeout(100)
    a.get_pty()
    a.invoke_shell()
    #command='yum install httpd \n'
    #command='tar zvxf /rgec/src/apache-maven-3.5.3-bin.tar.gz -C /rgec/app/ \n'

    #commands='cd /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/git_clone/d.mypharma.com\n;mvn  -s  /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/settings.xml  clean package -P dev_wh  -Dmaven.test.skip=true\n;/bin/ls -l\n;/bin/ls -l \n'

    #commands='cd /tmp \n;pwd \n'
    commandList=commands.split(';')
    #command='ls \n'
    c=str.encode('# ')
    d=str.encode('\n')
    f=str.encode('\r')
    g=str.encode('')
    l=str.encode(' ')
    k=str.encode(' \r')
    p=str.encode('\x1b')
    s=str.encode('[[1;34m')
    t=str.encode('[m]')
    v=str.encode('[1m')
    w=str.encode('[1;32m')
    x=str.encode('[m')
    y=str.encode('[[1;33m')
    z=str.encode('[36m')
    z1=str.encode('[0;32m')
    z2=str.encode('[0;1m')
    z7='\xe6\x80\xbb\xe7\x94\xa8\xe9\x87\x8f 12'
    z6=z7.encode('raw_unicode_escape')
    z11=str.encode('[0;36m')
    
    needReplaceList=[p,s,t,v,w,x,y,z,z1,z2,z6,z11]
    m=1
    b=a.recv(10240)
    for command in commandList:
        #print((b.decode()).strip('\n'))
        #print('发送第'+str(m)+'次命令前获取b的值，同上，开始循环获取消息')
        n=1
        while not b.endswith(c):
            for u in needReplaceList:
                b=b.replace(u,g)
                #print(b)
            if b.endswith(d):
                b=b.replace(k,g)
                #print(b)
                bList=b.split(d)
                for q in bList:
                    if q == g:
                        continue
                    else:
                        DeployLog(host+' : '+q.decode(),event,node)
                        ###print(q.decode())
                b=a.recv(10240)
            else:
                if not b.endswith(f):
                    b+=a.recv(10240)
                #print(b)
            #print('第'+str(n)+'次获取到的消息是：上面的值。判断b的值是否是#空格结尾，如果是，就结束循环。如果不是，就进行下一次循环')
            n+=1
            #print('n is: '+str(n))
        #print(b)
        #for u in needReplaceList:
        #    b=b.replace(u,g)
        bList=b.split(f)
        z3=g
        for q in bList:
            if q == g:
                continue
            elif q== l:
                continue
            else:
                if q.endswith(l):
                    ##print('q 是以空格结尾的，不要打印q，而是继承它')
                    if q.endswith(c):
                        z4=q.replace(d,g)
                        DeployLog(host+' : '+z4.decode(),event,node)
                        ###print(z4.decode())
                    else:
                        z3=q
                else:
                    ##print('q 不是以空格结尾的,打印它。首先继承上次循环的结果')
                    q=z3+q
                    q=q.replace(d,g)
                    DeployLog(host+' : '+q.decode(),event,node)
                    ###print(q.decode())
        ##print('目前b的结果是#空格结束，理论上再次获取会是一直等待，所以可以发送第'+str(m)+'条命令了')
        a.send(command)
        ##print('第'+str(m)+'条命令发送完成，开始接收数据，理论上会是命令结尾')
        b=a.recv(10240)
        #print(b.replace(k,g))
            
        if m==len(commandList):
            ##print('此时已经循环到最后一条命令，要请求这条命令的运行结果')
            b=a.recv(10240)
            #print(b)
            if not b.endswith(c):
                while not b.endswith(c):
                    if not b.endswith(d):
                        b+=a.recv(10240)
                        #print('b不以#结束')
                    else:
                        #print(b)
                        for u in needReplaceList:
                            b=b.replace(u,g)
                        bList=b.split(d)
                        for z8 in bList:
                            if z8!=g:
                                z8=z8.replace(f,g)
                                DeployLog(host+' : '+z8.decode(),event,node)
                                ###print(z8.decode())
                        b=a.recv(10240)
            else:
                #print(b)
                for u in needReplaceList:
                    b=b.replace(u,g)
                #print(b)
                z9=str.encode('\r\n')
                bList=b.split(z9)
                #print(bList)
                for  z10 in bList:
                    if z10 != g:
                        DeployLog(host+' : '+z10.decode(),event,node)
                        ###print(z10.decode())
            
            ##print('while循环结束')
        m+=1
        
    
    ##print('结束for 循环')
    
    a.close()
    transport.close()


def RemoterControlInvoke4ok13(host,port,userName,commands,event,node):
    #这个方法tar 和maven，非交互式的都可以了。现在复制它，开发需要交互式的过程
    #yum交互过程开发完了。期待，日后有其他的交互行为使用这个方法处理过程。
    #以下过程都只对分片结果进行处理
    #1.去除颜色
    #2.去掉' \r'
    #2.5.对while外，#前面的n进行分片。while上下都处理了
    #2.6.进行完2.5后，去除一次'\r'
    #3.去除运行半截的结果
    #3.5去除打包过程中下载的半截提示。
    #4.去除提示
    #5.输出decode化
    #6.收集内容，反馈给调用方。用于判断是否运行成功。
    #6.1去除maven打包下载的过程
    #7.把print的内容写进mysql
    result=''
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport((host,port))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #此时会话已打开
    a.settimeout(1000)
    a.get_pty()
    a.invoke_shell()
    #commands='yum install httpd\n'
    #commands='tar zvxf /rgec/src/apache-maven-3.5.3-bin.tar.gz -C /rgec/app/\n'

    #commands='cd /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/git_clone/d.mypharma.com\n;mvn  -s  /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/settings.xml  clean package -P dev_wh  -Dmaven.test.skip=true\n;/bin/ls -l\n;\n'
    commands=commands+';\n;\n'
    #print(commands)
    #commands='cd /tmp \n;pwd\n'
    commandList=commands.split(';')
    #command='ls \n'
    c=str.encode('# ')
    d=str.encode('\n')
    f=str.encode('\r')
    g=str.encode('')
    l=str.encode(' ')
    k=str.encode(' \r')
    p=str.encode('\x1b')
    s=str.encode('[[1;34m')
    t=str.encode('[m]')
    v=str.encode('[1m')
    w=str.encode('[1;32m')
    x=str.encode('[m')
    y='[\x1b[1;33m'
    y1=y.encode('raw_unicode_escape')
    z=str.encode('[36m')
    z1=str.encode('[0;32m')
    z2=str.encode('[0;1m')
    z7='\xe6\x80\xbb\xe7\x94\xa8\xe9\x87\x8f 12'
    z6=z7.encode('raw_unicode_escape')
    z11=str.encode('[0;36m')
    z9=str.encode(' KB')
    z13=str.encode('  ')
    z15=str.encode('Progress ')
    z17=str.encode('[y/N]: ')
    z18=str.encode('[[1;33m')
    z22=str.encode('##')
    z23=str.encode('[1;34m')
    z24=str.encode('[m] [1m')
    z25=str.encode('[m')
    z26=str.encode('[00;32m')
    z27=str.encode('[00m')
    z28=str.encode('(yes/no)? ')
    z29=str.encode('正在检出文件')
    z30=str.encode('[[1;36m')
    
    needReplaceList=[p,s,t,v,w,x,z,z1,z2,z6,z11,z18,y1,z13,z23,z24,z25,z26,z27,z30]
    doingList=[z22,z15,z29]
    m=1
    b=a.recv(10240)
    for command in commandList:
        #print(b)这里必须给b分片，虽然第一条命令不会有其他片，但是，最后那一次是以#号结尾的，它进不了while里面进行处理。所以要在这里给他分片。
        #第一条命令的开头不会受到影响，只会影响到最后1条。
        #bList=b.split(d)
        #print('这是在while之上分片处理的过程')
        #for z20 in bList:
        #    z20=z20.replace(f,g)
        #    print(z20)
        #print('发送第'+str(m)+'次命令前获取b的值，同上，开始循环获取消息,直到，获得得到#空格结尾，才可以输入第'+str(m)+'条命令')
        n=1
        while not b.endswith(c):
            #print('如果b是以n结尾的，那么就可以分片了。分完了片，在获取b，在判断它是不是以#空格结尾。')
            if b.endswith(d):
                #print('b是以n结尾的，开始分片')
                for i in b.split(d):
                    #如果i等于空，就不输出
                    if i !=g:
                        for u in needReplaceList:
                            i=i.replace(u,g)
                        i=i.replace(k,g)
                        iList=i.split(f)
                        for z19 in iList:
                            z19=z19.replace(f,g)
                            if z19!=g:
                                if z22 not in z19:
                                    #如果z19中不包含##就打印这一条。这个问题存在于yum安装过程中下载软件包的位置。
                                    #就是把下载过程屏蔽了。
                                    if z15 not in z19:
                                    #如果z19中不包含Progress ，就打印出来，这个问题存在与maven打包下载依赖的位置。
                                    #就把这个下载过程屏蔽了。
                                    #z29，不包含'正在检出文件',就打印，这个问题存在于git拉取文件过程中
                                        if z29 not in z19:
                                            #print(z19)
                                            DeployLog(z19.decode(),event,node)
                                            result+=z19.decode()
                        #print(i) 输出z19，就不用输出i了。
                b=a.recv(10240)
                #print('分完了片，在获取b，它的值是:')
                #print(b)
            else:
                #print('b不是以n结尾，叠加它')
                #print('b叠加前是')
                #print(b)
                #print('b是否以[y/N]: 结尾，如果是，就发送y,然后在获取结果。如果不是，那就继续获取b')
                if b.endswith(z17):
                    a.send('y\n')
                if b.endswith(z28):
                    a.send('yes\n')
                z16=a.recv(10240)
                #print('z16的值是')
                #print(z16)
                #print('开始叠加')
                b=b+z16
                #print('叠加后是')
                #print(b)
            n+=1
            #print(n)
            #time.sleep(1)
        if m == len(commandList):
            #print('已经进行到最后一条，不再发送命令，停止for循环。')
            DeployLog('已经进行到最后一条，不再发送命令，停止for循环。',event,node)
        else:
            #print('这不是最后一条命令，需要再次发送命令')
            #print('b的值现在是#空格结尾了，结束while循环，输入命令')
            #print('虽然b是以#空格结尾，但是我不保证#号前面没有n，所以，我要分片处理b')
            bList=b.split(d)
            for z21 in bList:
                z21=z21.replace(f,g)
                #print(z21.decode())
                DeployLog(z21.decode(),event,node)
                result+=z21.decode()
                #print('这是在while循环之下分片的结果')
            a.send(command)
            #print('第'+str(m)+'条命令发送完成，开始接收数据，理论上会是命令结尾')
            b=a.recv(10240)
        #如果不是最后一条命令，那么b的结果处理过程是在上面进行的。
        #如果是最后一条命令，那么b的结果处理过程是在下面进行的。
        #为什么呢？
        #因为上面的过程是
        #1.判断结果是否是#空格结尾
        #    不是，判断是否是n结尾
        #        是，分片;重新获取新b
        #        不是，叠加获取新b
        #    是，结束循环
        #2.发送命令，获取结果，进入下一次for循环，在下一次for循环中处理b的结果
        #可以这样吗，判断时候命令是最后一个命令，然后，
        #如果是最后一条命令，就在处理完b的结果，就结束for循环
        m+=1
        
    
   #print('结束for 循环')
    
    a.close()
    transport.close()   
    return result
   
def RemoteFileExist(host,port,userName,path):
    import paramiko,time,sys
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    try:
        transport = paramiko.Transport((host, port))
        transport.connect(username=userName, pkey=private_key)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.stat(path)
        result="exist"
        transport.close()
    except Exception as msg:
        #result="not exist"
        #print("*** file open error", msg)
        if 'Unable to connect' in str(msg):
            result='Unable to connect to '+host
        else:
            result='not exist'
    return(result)
    
def addRemoteUser(userName,host,sshPort,sshName,event,node):
    command="grep "+userName+" /etc/passwd"
    result=RemoteControl(host,sshPort,sshName,command,event,node)
    if len(result) == 0:
        command="useradd "+userName
        result=RemoteControl(host,sshPort,sshName,command,event,node)
        command="grep "+userName+" /etc/passwd"
        result=RemoteControl(host,sshPort,sshName,command,event,node)
        if len(result) == 0:
            log=host+" : "+'失败：创建'+userName
            DeployLog(log,event,node)
            log=host+" : "+'false'
            DeployLog(log,event,node)
            return log
            
def addRemoteGroup(groupName,host,sshPort,sshName,event,node):
    command="grep "+groupName+" /etc/group"
    result=RemoteControl(host,sshPort,sshName,command,event,node)
    if len(result) == 0:
        command="groupadd "+groupName
        result=RemoteControl(host,sshPort,sshName,command,event,node)
        command="grep "+groupName+" /etc/group"
        result=RemoteControl(host,sshPort,sshName,command,event,node)
        if len(result) == 0:
            log=host+" : "+'失败：创建'+groupName
            DeployLog(log,event,node)
            log=host+" : "+'false'
            DeployLog(log,event,node)
            return log
     
def Upload(host,sshPort,sshName,oldFileName,newFileName,event,node):
    exist=RemoteFileExist(host,sshPort,sshName,newFileName)
    if exist !='exist':
        log=host+" : "+'不存在路径：'+newFileName+',开始上传'
        DeployLog(log,event,node)
        import paramiko,time,sys
        private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
        transport = paramiko.Transport((host,sshPort))
        transport.connect(username=sshName, pkey=private_key)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(oldFileName,newFileName)
        transport.close()
        exist=RemoteFileExist(host,sshPort,sshName,newFileName)
        if exist =='exist':
            log=host+" : "+('成功：上传完成 ,路径：'+newFileName)
            DeployLog(log,event,node)
        else:
            log=host+" : "+('失败：上传失败 ,路径：'+newFileName)
            DeployLog(log,event,node)
            log=host+" : "+'false'
            DeployLog(log,event,node)
            return log
    else:
        log=host+" : "+'存在路径：'+newFileName+'不需要上传'
        DeployLog(log,event,node)

def Rm(host,sshPort,sshName,path,event,node):
    log=host+" : "+'删除: '+path
    DeployLog(log,event,node)
    command='rm -rf '+path
    RemoteControl(host,sshPort,sshName,command,event,node)
    exist=RemoteFileExist(host,sshPort,sshName,path)
    if exist =='exist':
        log=host+" : "+('失败：删除,路径：'+path)
        DeployLog(log,event,node)
        log=host+" : "+'false'
        DeployLog(log,event,node)
        return log
    else:
        log=host+" : "+('成功：删除 ,路径：'+path)
        DeployLog(log,event,node)
     
'''
def CheckUploadAndContinu(host,sshPort,sshName,path,event,node):
    exist=RemoteFileExist(host,sshPort,sshName,path)
    if exist =='exist':
        log=host+" : "+('成功上传 ,路径：'+path)
        DeployLog(log,event,node)
    else:
        log=host+" : "+('失败上传 ,路径：'+path)
        DeployLog(log,event,node)
        log=host+" : "+'false'
        DeployLog(log,event,node)
        return log
'''
def StartApp(appName,appPort,host,sshPort,sshName,event,node,company):
    log=host+" : "+appName+'执行启动'
    DeployLog(log,event,node)
    #command=('su - '+company+' -c "/etc/init.d/'+appName+' start"')
    command="/etc/init.d/"+appName+" start"
    RemoteControl(host,sshPort,sshName,command,event,node)
    time.sleep(10)
    command="netstat -tupln |grep "+str(appPort)+"|awk -F ' |:' '{print $19}'"
    result=RemoteControl(host,sshPort,sshName,command,event,node)
    if len(result)!=0:
        if result[0].strip() == appPort:
            log=host+" : "+'成功启动：'+appName
            DeployLog(log,event,node)
            return log
    else:
        log=host+" : "+'失败启动：'+appName
        DeployLog(log,event,node)
        log=host+" : "+'false'
        DeployLog(log,event,node)
        return log

def CheckPathAndAdd(host,sshPort,sshName,path,event,node):
    exist=RemoteFileExist(host,sshPort,sshName,path)
    if exist == 'exist': 
        log=host+" : "+path+' 存在'
        DeployLog(log,event,node)
    else:
        log=host+" : "+path+' 不存在，执行创建作业'
        DeployLog(log,event,node)
        RemoteControl(host,sshPort,sshName,'mkdir -pv '+path,event,node)
        exist=RemoteFileExist(host,sshPort,sshName,path)
        if exist == 'exist': 
            log=host+" : "+'成功创建:'+path
            DeployLog(log,event,node)
        else:
            log=host+" : "+'失败创建'+path
            DeployLog(log,event,node)
            log=host+" : "+'false'
            DeployLog(log,event,node)
            return log
 
def InstallTomcat(host,sshName,sshPort,tomcatPortList,appPath,event,node,tomcatVersion,company,javaVersion,appName):
    softSrcPath='/'+company+'/src'
    tomcatSrcPath=softSrcPath+'/apache-tomcat-'+tomcatVersion+'.tar.gz'
    exist=RemoteFileExist(host,sshPort,sshName,tomcatSrcPath)
    if exist != 'exist':
        log=host+" : "+(tomcatSrcPath+'不存在，需要上传')
        DeployLog(log,event,node)
        CheckPathAndAdd(host,sshPort,sshName,softSrcPath,event,node)
        Upload(host,sshPort,sshName,tomcatSrcPath,tomcatSrcPath,event,node)
        log=host+" : "+'可以开始安装tomcat了。'
        DeployLog(log,event,node)
    else:
        log=host+" : "+(tomcatSrcPath+' 已存在,不需要上传，可以开始安装tomcat了。')
        DeployLog(log,event,node)
    appPathList=appPath.split('/')
    appPathListLen=len(appPathList)
    commonAppPath=''
    j=0
    for i in appPathList:
        commonAppPath+=(i+'/')
        j+=1
        if j==(appPathListLen-1):
            break
    CheckPathAndAdd(host,sshPort,sshName,commonAppPath,event,node)
    temporaryPath=(commonAppPath+'apache-tomcat-'+tomcatVersion)
    Unzip(tomcatSrcPath,commonAppPath,'apache-tomcat-'+tomcatVersion,host,sshPort,sshName,event,node)
    Mv(temporaryPath,appPath,host,sshPort,sshName,event,node)
    #替换服务文件内容
    tomcatHttpPort=tomcatPortList[0]
    tomcatDebugPort=tomcatPortList[1]
    tomcatShutdownPort=tomcatPortList[2]
    Sed(str(8080),str(tomcatHttpPort),appPath+"/conf/server.xml",host,sshPort,sshName,event,node)
    Sed(str(8009),str(tomcatDebugPort),appPath+"/conf/server.xml",host,sshPort,sshName,event,node)
    Sed(str(8005),str(tomcatShutdownPort),appPath+"/conf/server.xml",host,sshPort,sshName,event,node)
    appAccessLogDir='/'+company+"/log/autodeploy/tomcat/"+appName+"/access"
    Sed('logs',appAccessLogDir,appPath+"/conf/server.xml",host,sshPort,sshName,event,node)
    #Sed('webapps','webapps/Root',appPath+"/conf/server.xml",host,sshPort,sshName,event,node)
    
    CheckPathAndAdd(host,sshPort,sshName,appAccessLogDir,event,node)
    appCoreLogDir='/'+company+"/log/autodeploy/tomcat/"+appName+"/core"
    Sed('\${catalina.base}/logs',appCoreLogDir,appPath+"/conf/logging.properties",host,sshPort,sshName,event,node)
    Sed('FINE','SEVERE',appPath+"/conf/logging.properties",host,sshPort,sshName,event,node)
    CheckPathAndAdd(host,sshPort,sshName,appCoreLogDir,event,node)
    
    #插入启动参数
    javaCommonPath='/'+company+'/app/java/'
    javaHome=javaCommonPath+'/'+javaVersion
    command=("sed -i '96c JAVA_HOME=\""+javaHome+"\"' "+appPath+"/bin/catalina.sh")
    result=RemoteControl(host,sshPort,sshName,command,event,node)
    log=host+" : "+'成功：替换java路径'
    DeployLog(log,event,node)
    appDebugPath='/'+company+"/log/autodeploy/tomcat/"+appName+"/debug"
    CheckPathAndAdd(host,sshPort,sshName,appDebugPath,event,node)
    Memory='512M'    
    javaOpts="-server -Xms"+Memory+" -Xmx"+Memory+" -XX:PermSize=256m -XX:MaxPermSize=256m -Xss512k -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -Xloggc:"+appDebugPath+"/gc.log.$(date +%Y%m%d_%H%M%S) -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath="+appDebugPath+"/dump.$(date +%Y%m%d_%H%M%S)  -Dfile.encoding=UTF-8 -Djava.awt.headless=true"
    command=("sed -i '97c JAVA_OPTS=\""+javaOpts+"\"' "+appPath+"/bin/catalina.sh")
    result=RemoteControl(host,sshPort,sshName,command,event,node)
    time.sleep(5)
    log=host+" : "+'成功:替换javaOpts'
    DeployLog(log,event,node)
    Rm(host,sshPort,sshName,appPath+'/webapps/*',event,node)
    #部署系统默认启动文件/etc/init.d/*
    tomcatStartFileTemplate=softSrcPath+'/'+tomcatVersion+'-tomcat-init.sh'
    appTomcatStartFile='/etc/init.d/'+appName
    Upload(host,sshPort,sshName,tomcatStartFileTemplate,appTomcatStartFile,event,node)
    #替换tomcatHome
    Sed('tomcatHome',appPath,appTomcatStartFile,host,sshPort,sshName,event,node)
    #替换tomcatUser
    Sed('tomcatUser',company,appTomcatStartFile,host,sshPort,sshName,event,node)
    #替换tomcatName
    Sed('tomcatName',appName,appTomcatStartFile,host,sshPort,sshName,event,node)
    #创建tomcat运行用户
    addRemoteUser(company,host,sshPort,sshName,event,node)
    #赋予权限
    command="chmod +x /etc/init.d/"+appName
    result=RemoteControl(host,sshPort,sshName,command,event,node)
    pathList=[appPath,appDebugPath,appAccessLogDir,appCoreLogDir,"/etc/init.d/"+appName]
    for i in pathList:
        command="chown -R "+company+"."+company+" "+i
        result=RemoteControl(host,sshPort,sshName,command,event,node)
    #检测java是否存在
    exist=RemoteFileExist(host,sshPort,sshName,javaHome)
    if exist == 'exist':
        log=host+" : "+javaHome+'存在'
        DeployLog(log,event,node)
    else:
        log=host+" : "+javaHome+'不存在'
        DeployLog(log,event,node)
        javaSoftSrcPath=softSrcPath+'/'+javaVersion+'.tar.gz'
        Upload(host,sshPort,sshName,javaSoftSrcPath,javaSoftSrcPath,event,node)
        CheckPathAndAdd(host,sshPort,sshName,javaCommonPath,event,node)
        Unzip(javaSoftSrcPath,javaCommonPath,javaVersion,host,sshPort,sshName,event,node)
    StartApp(appName,tomcatHttpPort,host,sshPort,sshName,event,node,company)
    #sftp.get('/filedir/oldtext.txt', r'C:\Users\duany_000\Desktop\oldtext.txt')

def DeployLog(log,event,node):
    new=DeployLogTable()
    new.log=log
    new.event=event
    new.node=node
    print(len(log))
    new.save()
    
def GetSshPort(host,company):
    companyObject=CompanyTable.objects.get(name=company)
    serverRooms=ServerRoomTable.objects.filter(company=companyObject)
    cabinets=[]
    for  serverRoom in serverRooms:
        a=CabinetTable.objects.filter(serverRoom=serverRoom)
        for i in a:
            cabinets.append(i)
    equipments=[]
    for cabinet in cabinets:
        a=EquipmentTable.objects.filter(cabinet = cabinet)
        for equipment in a:
            equipments.append(equipment)
    equipment=''
    for equipment in equipments:
        if equipment.ipAddress==host:
            hostObject=equipment
    sshPort=int(hostObject.controlPort)
    return sshPort
    
def PullGit(deployHost,company,gitPath,branch,event,appName,node,mavenCodePath,gitCloneDir):
    #gitCloneDir='/'+company+'/var/autodeploy/'+appName+'/'+event.eventId+'/git_clone/'
    log=deployHost+" : 创建目录,git克隆目录: "+gitCloneDir
    DeployLog(log,event,node)
    sshPort=GetSshPort(deployHost,company)
    sshName='root'
    CheckPathAndAdd(deployHost,sshPort,sshName,gitCloneDir,event,node)
    command='cd '+gitCloneDir+';git clone '+gitPath
    result=RemoteControl(deployHost,sshPort,sshName,command,event,node)
    command='cd '+gitCloneDir+'/'+mavenCodePath+';git checkout '+branch
    result=RemoteControl(deployHost,sshPort,sshName,command,event,node)
    for i in result:
        if 'error' in i:
            log=deployHost+' : false'
            DeployLog(log,event,node)
            return log
    return result

def CheckCommonTools(host,sshPort,sshName,fullPath,oldFileName,newFileName,targetPath,targetChildPath,event,node):
    #检查远程文件名是否存在，没有就上传，解压缩。
    result=RemoteFileExist(host,sshPort,sshName,fullPath)
    if 'not' in result:
        log=host+" : "+fullPath+'不存在，需要上传'
        DeployLog(log,event,node)
        
        Upload(host,sshPort,sshName,oldFileName,newFileName,event,node)
        
        log=host+" : "+newFileName+'已到位，下一步开始解压'
        DeployLog(log,event,node)
        result=Unzip(newFileName,targetPath,targetChildPath,host,sshPort,sshName,event,node)
        if result == 'done':
            #判断远程服务器上的PATH中是否有targetPath，如果有就不插入了
                command=("grep -n "+targetPath+' /etc/profile')
                result=RemoteControl(host,sshPort,sshName,command,event,node)
                if len(result)==0:
                    log=host+" : "+'未找到: '+targetPath+' /etc/profile '
                    DeployLog(log,event,node)
                    command='echo export PATH='+targetPath+targetChildPath+'/bin:\$PATH >> /etc/profile;. /etc/profile'
                    RemoteControl(host,sshPort,sshName,command,event,node)
                    result='done'
                else:
                    log='环境变量中已经有这个工具的位置了，不需要再插入 /etc/profile'
                    DeployLog(log,event,node)
                    result='done'
    return result
        
def PackageMaven(event,appName,company,host,node,mavenCodePath,packagePro,gitCloneDir):
    
    #1.生成maven临时本地仓库
    #2.填写临时maven配置文件
    #3.开始打包
    srcSettingFilePath='/'+company+'/src/mavenSetting.xml'
    #rootDIR='/'+company+'/var/autodeploy/'+appName+'/'+event.eventId+'/'
    rootDIR=gitCloneDir.replace('/git-clone','')
    settingFilePath=rootDIR+'settings.xml'
    sshPort=GetSshPort(host,company)
    sshName='root'
    Upload(host,sshPort,sshName,srcSettingFilePath,settingFilePath,event,node)
    manager='ggc'
    mavenLocalrepoDir=rootDIR+'mavenLocalrepoDir'
    mavenServerUserId='nexus-snapshots'
    mavenServerUserName='admin'
    mavenServerUserPassword='YLRoyP(-0rQPvpwSPIk{47056UIcWvms'
    mavenRepUrl='http://mvn.rograndec.net/nexus/content/groups/public/'
    mavenComplieJdk='8'
    replaceList=['manager','mavenLocalrepoDir','mavenServerUserId','mavenServerUserName','mavenServerUserPassword','mavenRepUrl','mavenComplieJdk']
    for i in replaceList:
        Sed(i,locals()[i],settingFilePath,host,sshPort,sshName,event,node)
    #packagePro=' clean package -P dev_wh'
    mavenPackageLog=rootDIR+'mavenPackage.log'
    commands='cd '+gitCloneDir+mavenCodePath+'\n;mvn -s '+settingFilePath+packagePro+'\n;/bin/ls -l\n'
    #用交互式方式开始打包，先好检测是否有maven软件，检测上传部署maven的过程应该是个函数
    #mvn -s /rgec/var/autodeploy/dev-wh-mph-gppayservice/20180607_471718/maven_setting/settings.xml clean deploy -P dev_wh -Dmaven.test.skip=true
    #打包前，判断打包服务器是否有maven，如果没有就自动部署
    oldFileName='/'+company+'/src/'+'apache-maven-3.5.3-bin.tar.gz'
    newFileName=oldFileName
    targetPath='/'+company+'/app/'
    targetChildPath='apache-maven-3.5.3'
    fullPath=targetPath+targetChildPath+'/bin/mvn'
    result=CheckCommonTools(host,sshPort,sshName,fullPath,oldFileName,newFileName,targetPath,targetChildPath,event,node)
    if result != 'done':
        if result != 'exist':
            return 'false'
    log=host+" : "+'开始打包'
    DeployLog(log,event,node)
    #print('pppppppppppppp')
    result=RemoterControlInvoke4ok13(host,sshPort,sshName,commands,event,node)
    if 'BUILD SUCCESS' in result:
        log='BUILD SUCCESS'
        DeployLog(log,event,node)
        return log
    else:
        log='false'
        DeployLog(log,event,node)
        return log
    #print('llllllllllll')

def DeployForTomcat(deployHost,serviceHost,company,appName,appSrcPackagePath,appTargetPackagePath,appUnzipPackageDir,appServicePath,event,node):
    #把软件包传上去
    #停止服务
    #下线nginx，因为tomcat启动速度比程序启动速度快。程序启动没完成前，不能对外提供服务。
    #删除老文件目录
    #创建新文件目录
    #把软件包解压缩进去
    #删除软件包
    #强制链接到服务webapps目录下
    #启动服务
    #如果有检测端口是否存在
    #如果有检测心跳页面是否存在
    #完
    deployHostSshPort=GetSshPort(deployHost,company)
    serviceSshPort=GetSshPort(serviceHost,company)
    appDataPath='/'+company+'/data/autodeploy/tomcat-webapps/'+appName
    #print(appDataPath)
    CheckPathAndAdd(serviceHost,serviceSshPort,'root',appDataPath,event,node)
    commands='scp -P '+str(serviceSshPort)+' '+appSrcPackagePath+' '+'root'+'@'+serviceHost+':'+appDataPath+'\n'
    result=RemoterControlInvoke4ok13(deployHost,deployHostSshPort,'root',commands,event,node)
    #先要判断nginx配置文件是否存在
    nginxVhostConfig='/'+company+'/app/nginx/conf/vhost/'+appName+'.conf'
    serviceIP=serviceHost
    servicePort=((node.portList).split(','))[0]
    nginxIp=node.service.nginxIp.ipAddress
    nginxSshPort=node.service.nginxIp.controlPort
    serverName=appName
    serviceDomainName=node.service.domainName
    enviroment=node.enviroment.name
    project=node.project.name
    service=node.service.name
    ipPort=serviceIP+':'+servicePort
    result=RemoteFileExist(nginxIp,int(nginxSshPort),'root',nginxVhostConfig)
    #第二次发布，先下线nginxNode
    if result=='exist' :
        #1.知道nginx配置文件
        #nginxVhostConfig
        #2.知道要替换的字符串
        #ipPort
        #用它来判断需要替换的字符串
        command='cd /'+company+'/app/nginx/conf/vhost/;grep '+ipPort+' *.conf'
        result=RemoteControl(nginxIp,int(nginxSshPort),'root',command,event,node)
        resultLine=[]
        if type(result)==type(resultLine):
            resultLine=(result[0]).strip()
        else:
            resultLine=result
        needReplaceString=(resultLine.split(';'))[0]
        #拿到需要替换的字符串
        #2.1.如果第一次发布失败了，会多一个down；
        #2.2.那么第二次发布，就会往后面补一个down。
        #2.3.所以，这后面不知道要跟多少个down呢
        #3.知道替换成的字符串
        newString=needReplaceString+' down '
        #4.替换#5.核查替换完后，有没有“替换成的字符串”
        Sed(needReplaceString,newString,'/'+company+'/app/nginx/conf/vhost/*.conf',nginxIp,int(nginxSshPort),'root',event,node)
    else :
        print('把nginx配置文件传上去')
        commonNginxVhostConfig='/'+company+'/src/nginx-vhost.conf'
        Upload(serviceHost,serviceSshPort,'root',commonNginxVhostConfig,nginxVhostConfig,event,node)
        #替换nginx文件中变量值
        needReplaceList=['serverName','serviceIP','servicePort','serviceDomainName','company','enviroment','project','service']
        for i in needReplaceList:
            Sed(i,locals()[i],nginxVhostConfig,serviceHost,serviceSshPort,'root',event,node)
        serviceNginxLogHome='/'+company+'/log/vhost/'+enviroment+'/'+project+'-'+service+'/'
        CheckPathAndAdd(nginxIp,int(nginxSshPort),'root',serviceNginxLogHome,event,node)
    #重载nginx
    commands='/etc/init.d/nginx reload\n'
    result=RemoterControlInvoke4ok13(serviceHost,serviceSshPort,'root',commands,event,node)
    #stop service；
    commands='/etc/init.d/'+appName+' stop\n'
    result=RemoterControlInvoke4ok13(serviceHost,serviceSshPort,'root',commands,event,node)

    commands='rm -fr '+appDataPath+'/'+'ROOT\n'
    #commands=commands+';mkdir -p '+appDataPath+'\n'
    #这次解压缩的结果是一个目录
    commands=commands+';unzip '+appTargetPackagePath+' -d '+appDataPath+'/'+appUnzipPackageDir+'\n'
    appDataFullPath=appDataPath+'/'+appUnzipPackageDir
    commands=commands+';ln -sf '+appDataFullPath+' '+appServicePath+'/webapps/'+appUnzipPackageDir+'\n'
    commands=commands+';/etc/init.d/'+appName+' start\n'
    result=RemoterControlInvoke4ok13(serviceHost,serviceSshPort,'root',commands,event,node)
    #nginx上线
    #1.知道nginx配置文件
    #nginxVhostConfig
    #2.知道要替换的字符串
    #ipPort
    #用它来判断需要替换的字符串
    command='cd /'+company+'/app/nginx/conf/vhost/;grep '+ipPort+' *.conf'
    result=RemoteControl(nginxIp,int(nginxSshPort),'root',command,event,node)
    resultLine=[]
    if type(result)==type(resultLine):
        resultLine=(result[0]).strip()
    else:
        resultLine=result
    needReplaceString=(resultLine.split(';'))[0]
    #print(needReplaceString)
    #拿到需要替换的字符串
    newString=needReplaceString.replace(' down ','')
    #4.替换
    Sed(needReplaceString,newString,'/'+company+'/app/nginx/conf/vhost/*.conf',nginxIp,int(nginxSshPort),'root',event,node)
    #5.重载nginx
    commands='/etc/init.d/nginx reload\n'
    result=RemoterControlInvoke4ok13(serviceHost,serviceSshPort,'root',commands,event,node)
    
def DeployForSpringBoot(serviceHost,event,node,deployHost,company):
    #def DeployForSpringBoot(serviceHost,event,node,deployHost,company):
    #1.上传
    #2.停止原服务
    #3.删除原包
    #4.部署服务：软件包，启动文件，日志目录
    #5.启动服务
    enviroment=node.enviroment
    serverRoom=node.serverRoom
    project=node.project
    service=node.service
    
    serviceName=enviroment.name+'-'+serverRoom.name+'-'+project.name+'-'+service.name
    servicePackagePath='/'+company+'/var/autodeploy/'+serviceName+'/'+event.eventId+'/git-clone/'+service.targetFilePath
    serviceHome='/'+company+'/data/autodeploy/springBoot/'+serviceName+'/'
    serviceUploadPackagePath=serviceHome+serviceName+'.jar'
    deployHostSshPort=GetSshPort(deployHost,company)
    serviceSshPort=GetSshPort(serviceHost,company)
    CheckPathAndAdd(serviceHost,serviceSshPort,'root',serviceHome,event,node)
    #创建serviceHome
    #停止服务
    serviceInitFile='/etc/init.d/'+serviceName
    commands=serviceInitFile+' stop\n'
    result=RemoterControlInvoke4ok13(deployHost,deployHostSshPort,'root',commands,event,node)
    #上传软件包,原来存在的话，覆盖
    commands='scp -P '+str(serviceSshPort)+' '+servicePackagePath+' '+'root'+'@'+serviceHost+':'+serviceUploadPackagePath+'\n'
    result=RemoterControlInvoke4ok13(deployHost,deployHostSshPort,'root',commands,event,node)
    
    sprintBootCommonInitFile='/'+company+'/src/sprintBootCommonInitFile.sh'
    serviceJavaHome='/'+company+'/app/java/'+service.javaVersion
    serviceMemory=node.memory
    serviceStartProfile=node.springBootStartProfile
    serviceLogHome='/'+company+'/log/autodeploy/java/'+serviceName
    needReplaceList=['serviceName','serviceJavaHome','serviceMemory','serviceStartProfile','serviceLogHome','serviceHome']
    #上传init文件
    commands='scp -P '+str(serviceSshPort)+' '+sprintBootCommonInitFile+' '+'root'+'@'+serviceHost+':'+'/etc/init.d/'+serviceName+'\n'
    result=RemoterControlInvoke4ok13(deployHost,deployHostSshPort,'root',commands,event,node)
    #循环替换文中内容
    for i  in needReplaceList:
        Sed(i,locals()[i],serviceInitFile,serviceHost,serviceSshPort,'root',event,node)
    #创建日志目录
    CheckPathAndAdd(serviceHost,serviceSshPort,'root',serviceLogHome,event,node)
    #复权
    command="chmod +x /etc/init.d/"+serviceName
    result=RemoteControl(serviceHost,serviceSshPort,'root',command,event,node)
    command='chown -R '+company+'.'+company+' '+serviceLogHome
    result=RemoteControl(serviceHost,serviceSshPort,'root',command,event,node)
    #启动服务
    servicePort=((node.portList).split(','))[0]
    StartApp(serviceName,servicePort,serviceHost,serviceSshPort,'root',event,node,company)
    
def DeployForDubbo(serviceHost,event,node,deployHost,company):
    #1.上传
    #2.停止原服务
    #3.删除原包
    #4.部署服务：软件包，启动文件，日志目录
    #5.启动服务
    #servicePackagePath='/rgec/var/autodeploy/test-gm-mph-cmsservice/20180705090439964/git-clone/mph-cms-service-group/mph-cms-impl/target/mph-dubbo-deploy.tar.gz'
    #serviceUploadPackagePath='/rgec/data/autodeploy/dubbo/test-gm-mph-cmsservice'
    
    enviroment=node.enviroment
    serverRoom=node.serverRoom
    project=node.project
    service=node.service
    
    serviceName=enviroment.name+'-'+serverRoom.name+'-'+project.name+'-'+service.name
    servicePackagePath='/'+company+'/var/autodeploy/'+serviceName+'/'+event.eventId+'/git-clone/'+service.targetFilePath
    serviceHome='/'+company+'/data/autodeploy/dubbo/'+serviceName+'/'
    serviceUploadPackagePath=serviceHome+serviceName+'.tar.gz'
    deployHostSshPort=GetSshPort(deployHost,company)
    serviceSshPort=GetSshPort(serviceHost,company)
    CheckPathAndAdd(serviceHost,serviceSshPort,'root',serviceHome,event,node)
    #创建serviceHome
    #停止服务
    serviceInitFile='/etc/init.d/'+serviceName
    commands=serviceInitFile+' stop\n'
    result=RemoterControlInvoke4ok13(serviceHost,serviceSshPort,'root',commands,event,node)
    #上传软件包,原来存在的话，覆盖
    commands='scp -P '+str(serviceSshPort)+' '+servicePackagePath+' '+'root'+'@'+serviceHost+':'+serviceUploadPackagePath+'\n'
    result=RemoterControlInvoke4ok13(deployHost,deployHostSshPort,'root',commands,event,node)
    #起个什么名字好呢？
    #它是dubbo打包时候的目录名
    serviceTarDir=(((service.targetFilePath).split('/'))[-1]).replace('.tar.gz','')
    #它是dubbo包解压缩后的路径，dubbo init文件用的就是这个路径做serviceHome。
    serviceWorkDir=serviceHome+serviceTarDir
    #删除老目录
    commands='rm -rf '+serviceWorkDir+'\n'
    #解压缩。
    commands+='cd '+serviceHome+'\n;tar zxvf '+serviceUploadPackagePath+'\n'
    #删除原包
    commands+='rm -f '+serviceUploadPackagePath+'\n'
    result=RemoterControlInvoke4ok13(serviceHost,serviceSshPort,'root',commands,event,node)
    sprintBootCommonInitFile='/'+company+'/src/dubboCommonInitFile.sh'
    serviceJavaHome='/'+company+'/app/java/'+service.javaVersion
    #serviceMemory=node.memory
    #serviceStartProfile=node.springBootStartProfile
    serviceLogHome='/'+company+'/log/autodeploy/java/'+serviceName
    serviceUser=company

    serviceStartScript='/bin/start.sh'
    serviceStopScript='/bin/stop.sh'
    needReplaceList=['serviceName','serviceJavaHome','serviceLogHome','serviceWorkDir','serviceUser','serviceStartScript','serviceStopScript']
    #上传init文件
    commands='scp -P '+str(serviceSshPort)+' '+sprintBootCommonInitFile+' '+'root'+'@'+serviceHost+':'+'/etc/init.d/'+serviceName+'\n'
    result=RemoterControlInvoke4ok13(deployHost,deployHostSshPort,'root',commands,event,node)
    #循环替换文中内容
    for i  in needReplaceList:
        Sed(i,locals()[i],serviceInitFile,serviceHost,serviceSshPort,'root',event,node)
    #创建日志目录
    CheckPathAndAdd(serviceHost,serviceSshPort,'root',serviceLogHome,event,node)
    #复权
    command="chmod +x /etc/init.d/"+serviceName
    result=RemoteControl(serviceHost,serviceSshPort,'root',command,event,node)
    command='chown -R '+company+'.'+company+' '+serviceLogHome
    result=RemoteControl(serviceHost,serviceSshPort,'root',command,event,node)
    #启动服务
    servicePort=((node.portList).split(','))[0]
    StartApp(serviceName,servicePort,serviceHost,serviceSshPort,'root',event,node,company)
    
def Do(request):
    companyName='rgec'
    #这里以后会采集用户信息，来判断他的公司名称。目前就先写死。
    result=''
    if request.method == 'POST':
        #eventId=request.POST.get('eventId',None)
        #a=time.strftime("%Y%m%d%H%M%S")
        #b=time.time()
        #c=(b-int(b))*1000
        #d="%03d"%(c)
        #e=str(a)+str(d)
        eventId=time.strftime("%Y%m%d%H%M%S")+"%03d"%((time.time()-int(time.time()))*1000)
        event=EventTable()
        event.eventId=eventId
        event.save()
        nodeId = request.POST.get('nodeId',None)
        nodeBranch = request.POST.get('nodeBranch',None)
        if nodeId != '':
            nodeObject=NodeTable.objects.get(id=nodeId)
            enviroment=nodeObject.enviroment.name
            serverRoom=nodeObject.serverRoom.name
            project=nodeObject.project.name
            service=nodeObject.service.name
            serviceType=nodeObject.service.serviceType.name
            host=nodeObject.ip.ipAddress
            controlPort=nodeObject.ip.controlPort
            portList=(nodeObject.portList.split(','))
            appName=enviroment+'-'+serverRoom+'-'+project+'-'+service
            company=nodeObject.project.company.name
            appPath=''
            if serviceType=='tomcat':
                tomcatVersion=nodeObject.service.serviceType.version 
                javaVersion=nodeObject.service.javaVersion
                appPath='/'+companyName+'/app/autodepoly/'+serviceType+'/'+appName+'-tomcat-'+tomcatVersion
                exist=RemoteFileExist(host,int(controlPort),'root',appPath)
                if 'Unable to connect ' in exist:
                    return HttpResponse(exist)
                elif exist != 'exist':
                    log=host+" : "+(appPath+'目录不存在，需要安装tomcat')
                    DeployLog(log,event,nodeObject)
                    result=InstallTomcat(host,'root',int(controlPort),portList,appPath,event,nodeObject,tomcatVersion,company,javaVersion,appName)
                    if result == 'false':
                        return HttpResponse('搭建tomcat失败')
            log=appPath+'目录已存在，此时，该开始拉代码了'
            DeployLog(log,event,nodeObject)
            serverRoomObject=nodeObject.serverRoom
            deployHost=(DeployHostTable.objects.get(serverRoom=serverRoomObject)).host.ipAddress
            projectObject=ProjectTable.objects.get(name=project)
            serviceObject=ServiceTable.objects.get(name=service,project=projectObject)
            gitPath=serviceObject.codeSrc
            
            mavenCodePath=serviceObject.mavenCodePath
            packagePro=serviceObject.mavenParameter
            #print(serviceObject.id)
            #print(packagePro)
            #mavenParameter=enviroment+'_'+serverRoom
            packagePro='   '+serviceObject.mavenParameter+' '+enviroment+'_'+serverRoom
            gitCloneDir='/'+company+'/var/autodeploy/'+appName+'/'+event.eventId+'/git-clone/'
            result=PullGit(deployHost,company,gitPath,nodeBranch,event,appName,nodeObject,mavenCodePath,gitCloneDir)
            if 'false' in result:
                return HttpResponse(result)
            log='拉完代码了，开始打包'
            DeployLog(log,event,nodeObject)
            javaVersion=nodeObject.service.javaVersion
            if javaVersion != None:
                result=PackageMaven(event,appName,company,deployHost,nodeObject,mavenCodePath,packagePro,gitCloneDir)
                if result == 'false':
                    return HttpResponse(result)
            serviceHost=host
            #服务部署的服务器地址:192.168.20.99
            appSrcPackagePath=gitCloneDir+nodeObject.service.targetFilePath
            #服务打完包的路径:/rgec/var/autodeploy/dev-gm-mph-www/20180702082446848/git-clone/d.mypharma.com/target/ROOT.war
            mavenTargetFile=((nodeObject.service.targetFilePath).split('/'))[-1]
            #服务打包后的文件名:ROOT.war
            if serviceType=='tomcat':
                appTargetPackagePath='/'+company+'/data/autodeploy/tomcat-webapps/'+appName+'/'+mavenTargetFile
                #print(appTargetPackagePath)
                #上传后的服务文件名:/rgec/data/autodeploy/tomcat-webapps/dev-gm-mph-www/ROOT.war
                appServicePath=appPath
                appUnzipPackageDir=mavenTargetFile.replace('.war','')
                #服务解压缩后的相对目录。:ROOT
                result=DeployForTomcat(deployHost,serviceHost,company,appName,appSrcPackagePath,appTargetPackagePath,appUnzipPackageDir,appServicePath,event,nodeObject)
                '''
                #deployHost:192.168.20.98
                #serviceHost:192.168.20.99
                #company:rgec
                #appName:dev-gm-mph-www
                #appSrcPackagePath:/rgec/var/autodeploy/dev-gm-mph-www/20180702082446848/git-clone/d.mypharma.com/target/ROOT.war
                #appTargetPackagePath:/rgec/data/autodeploy/tomcat-webapps/dev-gm-mph-www/ROOT.war
                #appUnzipPackageDir:ROOT
                #appServicePath:/rgec/app/autodepoly/tomcat/dev-gm-mph-www-tomcat-7.0.59
                '''
            if serviceType=='sprintBoot':
                DeployForSpringBoot(serviceHost,event,nodeObject,deployHost,company)
            if serviceType=='dubbo':
                DeployForDubbo(serviceHost,event,nodeObject,deployHost,company)
                
            log='ok done'
            DeployLog(log,event,nodeObject)
            return HttpResponse('done')
        else:
            result='请先提交，然后在执行'
            return HttpResponse(result)
    return HttpResponse(result)

def ViewDeployLog_nodeId(request,id):
    if request.method=='GET':
        #获取eventid的列表
        eventIds=[]
        node=NodeTable.objects.get(id=id)
        for i in DeployLogTable.objects.filter(node=node):
            #实在不会自动获取表名了
            eventIds.append(i.event.eventId)
        eventIds=list(set(eventIds))
        eventIds=sorted(eventIds,reverse=True)
    return render_to_response('viewDeployLog.html',{'eventIds':eventIds})

def ViewDeployLog_eventId(request,id):
    if request.method == 'POST': 
        sign=request.POST.get('sign',None)
    logs=[]
    if sign=='getLogs':
        logIdObjects=DeployLogTable.objects.filter(event.eventId=id)
        for i in logIdObjects:
            log=i.log
            logs.append(log+'@@')
    return HttpResponse(logs)
'''
def SelectService(request):
    if request.method=='POST':
        projectName=request.POST.get('projectName',None)
        projectObject=ProjectTable.objects.get(name=projectName)
        serviceObjects=ServiceTable.objects.filter(project=projectObject)
        services=''
        n=1
        for i in serviceObjects:
            if n != len(serviceObjects):
                services+=(i.name+'@@')
            else:
                services+=i.name
            n+=1
    return HttpResponse(services)
'''
def GetRange(request):
    if request.method=='POST':
        AName=request.POST.get('AName',None)
        
        ATable=request.POST.get('ATable',None)
        BTable=request.POST.get('BTable',None)
        BColmn=request.POST.get('BColmn',None)
        ATable=eval(ATable)
        AObject=ATable.objects.get(name=AName)
        param={BColmn:AObject}
        BTableObject=eval(BTable)
        BObjects=BTableObject.objects.filter(**param)
        result=''
        n=1
        for i in BObjects:
            if n != len(BObjects):
                result+=(i.name+'@@')
            else:
                result+=i.name
            n+=1
    return HttpResponse(result)

def Help(request):
    return HttpResponse('ok')

def GetGitList(request):
    g = git.cmd.Git()
    heads=g.ls_remote('https://git_autodeploy:123abc45@git.rograndec.com/mph/www.mypharma.com.git')
    headsList=heads.split('\n')
    branchs=[]
    for i in headsList:
        if '{}' not in i:
            branchAll=(i.split('\t'))[-1]
            branch=(branchAll.split('/'))[-1]
            branchs.append(branch)
    branchs=list(set(branchs))
    branchs.sort()
    branchsa=[]
    branchsHead=[]
    for i in branchs:
        if '.' in i:
            branchs.remove(i)
            c=i.split('.')
            d=[]
            for j in c:
                d.append(int(j))
            branchsa.append(d)
        else:
            branchsHead.append(i)
            
    branchsa=sorted(branchsa,key=itemgetter(0,1,2,-1),reverse=True)
    
    branchTag=[]
    for i in branchsa:
        m=''
        p=1
        for n in i:
            if p == len(i) :
                m+=str(n)
            else:
                m+=str(n)+'.'
            p+=1
        branchTag.append(m)
        
    branchTagStr=''
    n=1
    for q in branchTag:
        if n==len(branchTag):
            branchTagStr+=q
        else:
            branchTagStr+=q+'@@'
        n+=1
        #print(q)
    #for p in branchsHead:
    #    print(p)   
    return HttpResponse(branchTagStr)
    

##############################################################








