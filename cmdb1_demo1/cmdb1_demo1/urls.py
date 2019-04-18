"""cmdb1_demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
import cmdb1_demo1_app1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cmdb1_demo1_app1.views.HelloWorld),
    path('company',cmdb1_demo1_app1.views.Company),
    path('provider',cmdb1_demo1_app1.views.Provider),
    path('serverroom',cmdb1_demo1_app1.views.ServerRoom),
    path('cabinet',cmdb1_demo1_app1.views.Cabinet),
    path('equipmentType',cmdb1_demo1_app1.views.EquipmentType),
    path('equipment',cmdb1_demo1_app1.views.Equipment),
    path('occupation',cmdb1_demo1_app1.views.Occupation),
    path('private',cmdb1_demo1_app1.views.Private),
    path('serviceType',cmdb1_demo1_app1.views.ServiceType),
    path('project',cmdb1_demo1_app1.views.Project),
    path('service',cmdb1_demo1_app1.views.Service),
    path('enviroment',cmdb1_demo1_app1.views.Enviroment),
    path('node',cmdb1_demo1_app1.views.Node),
    path('port',cmdb1_demo1_app1.views.Port),
    path('logPath',cmdb1_demo1_app1.views.LogPath),
    path('do',cmdb1_demo1_app1.views.Do),
    path('selectService',cmdb1_demo1_app1.views.GetRange),
    path('getGitList',cmdb1_demo1_app1.views.GetGitList),
    
    #path('upload',cmdb1_demo1_app1.views.Upload),
    re_path('viewDeployLog_nodeId_(?P<id>[\w]+)$',cmdb1_demo1_app1.views.ViewDeployLog_nodeId),
    re_path('viewDeployLog_eventId_(?P<id>[\w]+)$',cmdb1_demo1_app1.views.ViewDeployLog_event),
    
    path('login',cmdb1_demo1_app1.views.Login),
    path('index',cmdb1_demo1_app1.views.Index),
    path('logout',cmdb1_demo1_app1.views.Logout),
    path('regist',cmdb1_demo1_app1.views.Regist),
    path('stopProcess',cmdb1_demo1_app1.views.StopProcess)


]
 