def RemoterControlInvoke4ok2(host,port,userName,commands,eventId,node):
    #�������tar ��maven���ǽ���ʽ�Ķ������ˡ����ڸ�������������Ҫ����ʽ�Ĺ���
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #��ʱ�Ự�Ѵ�
    a.settimeout(100)
    a.get_pty()
    a.invoke_shell()
    #command='yum install httpd\n'
    #commands='tar zvxf /rgec/src/apache-maven-3.5.3-bin.tar.gz -C /rgec/app/\n'

    #commands='cd /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/git_clone/d.mypharma.com\n;mvn  -s  /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/settings.xml  clean package -P dev_wh  -Dmaven.test.skip=true\n;/bin/ls -l\n;\n'
    commands=commands+';\n'
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
    y=str.encode('[[1;33m')
    z=str.encode('[36m')
    z1=str.encode('[0;32m')
    z2=str.encode('[0;1m')
    z7='\xe6\x80\xbb\xe7\x94\xa8\xe9\x87\x8f 12'
    z6=z7.encode('raw_unicode_escape')
    z11=str.encode('[0;36m')
    z9=str.encode(' KB')
    z13=str.encode('  ')
    z15=str.encode('Progress ')
    
    needReplaceList=[p,s,t,v,w,x,y,z,z1,z2,z6,z11]
    m=1
    b=a.recv(10240)
    for command in commandList:
        print(b)
        print('���͵�'+str(m)+'������ǰ��ȡb��ֵ��ͬ�ϣ���ʼѭ����ȡ��Ϣ,ֱ������õõ�#�ո��β���ſ��������'+str(m)+'������')
        n=1
        while not b.endswith(c):
            print('���b����n��β�ģ���ô�Ϳ��Է�Ƭ�ˡ�������Ƭ���ڻ�ȡb�����ж����ǲ�����#�ո��β��')
            if b.endswith(d):
                print('b����n��β�ģ���ʼ��Ƭ')
                for i in b.split(d):
                    #���i���ڿգ��Ͳ����
                    if i !=l:
                        print(i)
                b=a.recv(10240)
                print('������Ƭ���ڻ�ȡb������ֵ��:')
                print(b)
            else:
                print('b,������n��β��������')
                print('b,����ǰ��')
                print(b)
                z16=a.recv(10240)
                print('z16��ֵ��')
                print(z16)
                print('��ʼ����')
                b=b+z16
                print('���Ӻ���')
                print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('�Ѿ����е����һ�������ٷ������ֹͣforѭ����')
        else:
            print('b��ֵ������#�ո��β�ˣ�����whileѭ������������')
            a.send(command)
            print('��'+str(m)+'���������ɣ���ʼ�������ݣ������ϻ��������β')
            b=a.recv(10240)
        #����������һ�������ôb�Ľ�������������������еġ�
        #��������һ�������ôb�Ľ�������������������еġ�
        #Ϊʲô�أ�
        #��Ϊ����Ĺ�����
        #1.�жϽ���Ƿ���#�ո��β
        #    ���ǣ��ж��Ƿ���n��β
        #        �ǣ���Ƭ;���»�ȡ��b
        #        ���ǣ����ӻ�ȡ��b
        #    �ǣ�����ѭ��
        #2.���������ȡ�����������һ��forѭ��������һ��forѭ���д���b�Ľ��
        #�����������ж�ʱ�����������һ�����Ȼ��
        #��������һ��������ڴ�����b�Ľ�����ͽ���forѭ��
        m+=1
        
    
   #print('����for ѭ��')
    
    a.close()
    transport.close()

def RemoterControlInvoke4ok3(host,port,userName,commands2,eventId,node):
    #�������tar ��maven���ǽ���ʽ�Ķ������ˡ����ڸ�������������Ҫ����ʽ�Ĺ���
    #yum�������̿������ˡ��ڴ����պ��������Ľ�����Ϊʹ���������������̡�
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #��ʱ�Ự�Ѵ�
    a.settimeout(100)
    a.get_pty()
    a.invoke_shell()
    commands='yum install httpd\n'
    #commands='tar zvxf /rgec/src/apache-maven-3.5.3-bin.tar.gz -C /rgec/app/\n'

    #commands='cd /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/git_clone/d.mypharma.com\n;mvn  -s  /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/settings.xml  clean package -P dev_wh  -Dmaven.test.skip=true\n;/bin/ls -l\n;\n'
    commands=commands+';\n'
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
    y=str.encode('[[1;33m')
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
    
    needReplaceList=[p,s,t,v,w,x,y,z,z1,z2,z6,z11]
    m=1
    b=a.recv(10240)
    for command in commandList:
        print(b)
        print('���͵�'+str(m)+'������ǰ��ȡb��ֵ��ͬ�ϣ���ʼѭ����ȡ��Ϣ,ֱ������õõ�#�ո��β���ſ��������'+str(m)+'������')
        n=1
        while not b.endswith(c):
            print('���b����n��β�ģ���ô�Ϳ��Է�Ƭ�ˡ�������Ƭ���ڻ�ȡb�����ж����ǲ�����#�ո��β��')
            if b.endswith(d):
                print('b����n��β�ģ���ʼ��Ƭ')
                for i in b.split(d):
                    #���i���ڿգ��Ͳ����
                    if i !=g:
                        print(i)
                b=a.recv(10240)
                print('������Ƭ���ڻ�ȡb������ֵ��:')
                print(b)
            else:
                print('b������n��β��������')
                print('b����ǰ��')
                print(b)
                print('b�Ƿ���[y/N]: ��β������ǣ��ͷ���y\n,Ȼ���ڻ�ȡ�����������ǣ��Ǿͼ�����ȡb')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                print('z16��ֵ��')
                print(z16)
                print('��ʼ����')
                b=b+z16
                print('���Ӻ���')
                print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('�Ѿ����е����һ�������ٷ������ֹͣforѭ����')
        else:
            print('b��ֵ������#�ո��β�ˣ�����whileѭ������������')
            a.send(command)
            print('��'+str(m)+'���������ɣ���ʼ�������ݣ������ϻ��������β')
            b=a.recv(10240)
        #����������һ�������ôb�Ľ�������������������еġ�
        #��������һ�������ôb�Ľ�������������������еġ�
        #Ϊʲô�أ�
        #��Ϊ����Ĺ�����
        #1.�жϽ���Ƿ���#�ո��β
        #    ���ǣ��ж��Ƿ���n��β
        #        �ǣ���Ƭ;���»�ȡ��b
        #        ���ǣ����ӻ�ȡ��b
        #    �ǣ�����ѭ��
        #2.���������ȡ�����������һ��forѭ��������һ��forѭ���д���b�Ľ��
        #�����������ж�ʱ�����������һ�����Ȼ��
        #��������һ��������ڴ�����b�Ľ�����ͽ���forѭ��
        m+=1
        
    
   #print('����for ѭ��')
    
    a.close()
    transport.close()
    
def RemoterControlInvoke4ok4(host,port,userName,commands2,eventId,node):
    #�������tar ��maven���ǽ���ʽ�Ķ������ˡ����ڸ�������������Ҫ����ʽ�Ĺ���
    #yum�������̿������ˡ��ڴ����պ��������Ľ�����Ϊʹ���������������̡�
    #���¹��̶�ֻ�Է�Ƭ������д���
    #1.ȥ����ɫ
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #��ʱ�Ự�Ѵ�
    a.settimeout(100)
    a.get_pty()
    a.invoke_shell()
    #commands='yum install httpd\n'
    #commands='tar zvxf /rgec/src/apache-maven-3.5.3-bin.tar.gz -C /rgec/app/\n'

    commands='cd /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/git_clone/d.mypharma.com\n;mvn  -s  /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/settings.xml  clean package -P dev_wh  -Dmaven.test.skip=true\n;/bin/ls -l\n;\n'
    commands=commands+';\n'
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
    
    needReplaceList=[p,s,t,v,w,x,z,z1,z2,z6,z11,z18,y1]
    m=1
    b=a.recv(10240)
    for command in commandList:
        print(b)
        print('���͵�'+str(m)+'������ǰ��ȡb��ֵ��ͬ�ϣ���ʼѭ����ȡ��Ϣ,ֱ������õõ�#�ո��β���ſ��������'+str(m)+'������')
        n=1
        while not b.endswith(c):
            print('���b����n��β�ģ���ô�Ϳ��Է�Ƭ�ˡ�������Ƭ���ڻ�ȡb�����ж����ǲ�����#�ո��β��')
            if b.endswith(d):
                print('b����n��β�ģ���ʼ��Ƭ')
                for i in b.split(d):
                    #���i���ڿգ��Ͳ����
                    if i !=g:
                        for u in needReplaceList:
                            i=i.replace(u,g)
                        print(i)
                b=a.recv(10240)
                print('������Ƭ���ڻ�ȡb������ֵ��:')
                print(b)
            else:
                print('b������n��β��������')
                print('b����ǰ��')
                print(b)
                print('b�Ƿ���[y/N]: ��β������ǣ��ͷ���y\n,Ȼ���ڻ�ȡ�����������ǣ��Ǿͼ�����ȡb')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                print('z16��ֵ��')
                print(z16)
                print('��ʼ����')
                b=b+z16
                print('���Ӻ���')
                print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('�Ѿ����е����һ�������ٷ������ֹͣforѭ����')
        else:
            print('b��ֵ������#�ո��β�ˣ�����whileѭ������������')
            a.send(command)
            print('��'+str(m)+'���������ɣ���ʼ�������ݣ������ϻ��������β')
            b=a.recv(10240)
        #����������һ�������ôb�Ľ�������������������еġ�
        #��������һ�������ôb�Ľ�������������������еġ�
        #Ϊʲô�أ�
        #��Ϊ����Ĺ�����
        #1.�жϽ���Ƿ���#�ո��β
        #    ���ǣ��ж��Ƿ���n��β
        #        �ǣ���Ƭ;���»�ȡ��b
        #        ���ǣ����ӻ�ȡ��b
        #    �ǣ�����ѭ��
        #2.���������ȡ�����������һ��forѭ��������һ��forѭ���д���b�Ľ��
        #�����������ж�ʱ�����������һ�����Ȼ��
        #��������һ��������ڴ�����b�Ľ�����ͽ���forѭ��
        m+=1
        
    
   #print('����for ѭ��')
    
    a.close()
    transport.close()
    
def RemoterControlInvoke4ok5(host,port,userName,commands2,eventId,node):
    #�������tar ��maven���ǽ���ʽ�Ķ������ˡ����ڸ�������������Ҫ����ʽ�Ĺ���
    #yum�������̿������ˡ��ڴ����պ��������Ľ�����Ϊʹ���������������̡�
    #���¹��̶�ֻ�Է�Ƭ������д���
    #1.ȥ����ɫ
    #2.ȥ��\r
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #��ʱ�Ự�Ѵ�
    a.settimeout(100)
    a.get_pty()
    a.invoke_shell()
    #commands='yum install httpd\n'
    #commands='tar zvxf /rgec/src/apache-maven-3.5.3-bin.tar.gz -C /rgec/app/\n'

    commands='cd /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/git_clone/d.mypharma.com\n;mvn  -s  /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/settings.xml  clean package -P dev_wh  -Dmaven.test.skip=true\n;/bin/ls -l\n;\n'
    commands=commands+';\n'
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
    
    needReplaceList=[p,s,t,v,w,x,z,z1,z2,z6,z11,z18,y1]
    m=1
    b=a.recv(10240)
    for command in commandList:
        print(b)
        print('���͵�'+str(m)+'������ǰ��ȡb��ֵ��ͬ�ϣ���ʼѭ����ȡ��Ϣ,ֱ������õõ�#�ո��β���ſ��������'+str(m)+'������')
        n=1
        while not b.endswith(c):
            print('���b����n��β�ģ���ô�Ϳ��Է�Ƭ�ˡ�������Ƭ���ڻ�ȡb�����ж����ǲ�����#�ո��β��')
            if b.endswith(d):
                print('b����n��β�ģ���ʼ��Ƭ')
                for i in b.split(d):
                    #���i���ڿգ��Ͳ����
                    if i !=g:
                        for u in needReplaceList:
                            i=i.replace(u,g)
                        i=i.replace(k,g)
                        print(i)
                b=a.recv(10240)
                print('������Ƭ���ڻ�ȡb������ֵ��:')
                print(b)
            else:
                print('b������n��β��������')
                print('b����ǰ��')
                print(b)
                print('b�Ƿ���[y/N]: ��β������ǣ��ͷ���y\n,Ȼ���ڻ�ȡ�����������ǣ��Ǿͼ�����ȡb')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                print('z16��ֵ��')
                print(z16)
                print('��ʼ����')
                b=b+z16
                print('���Ӻ���')
                print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('�Ѿ����е����һ�������ٷ������ֹͣforѭ����')
        else:
            print('b��ֵ������#�ո��β�ˣ�����whileѭ������������')
            a.send(command)
            print('��'+str(m)+'���������ɣ���ʼ�������ݣ������ϻ��������β')
            b=a.recv(10240)
        #����������һ�������ôb�Ľ�������������������еġ�
        #��������һ�������ôb�Ľ�������������������еġ�
        #Ϊʲô�أ�
        #��Ϊ����Ĺ�����
        #1.�жϽ���Ƿ���#�ո��β
        #    ���ǣ��ж��Ƿ���n��β
        #        �ǣ���Ƭ;���»�ȡ��b
        #        ���ǣ����ӻ�ȡ��b
        #    �ǣ�����ѭ��
        #2.���������ȡ�����������һ��forѭ��������һ��forѭ���д���b�Ľ��
        #�����������ж�ʱ�����������һ�����Ȼ��
        #��������һ��������ڴ�����b�Ľ�����ͽ���forѭ��
        m+=1
        
    
   #print('����for ѭ��')
    
    a.close()
    transport.close()
    
def RemoterControlInvoke4ok6(host,port,userName,commands2,eventId,node):
    #�������tar ��maven���ǽ���ʽ�Ķ������ˡ����ڸ�������������Ҫ����ʽ�Ĺ���
    #yum�������̿������ˡ��ڴ����պ��������Ľ�����Ϊʹ���������������̡�
    #���¹��̶�ֻ�Է�Ƭ������д���
    #1.ȥ����ɫ
    #2.ȥ��' \r'
    #2.5.��while�⣬#ǰ���n���з�Ƭ��while���¶�������
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #��ʱ�Ự�Ѵ�
    a.settimeout(100)
    a.get_pty()
    a.invoke_shell()
    #commands='yum install httpd\n'
    #commands='tar zvxf /rgec/src/apache-maven-3.5.3-bin.tar.gz -C /rgec/app/\n'

    commands='cd /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/git_clone/d.mypharma.com\n;mvn  -s  /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/settings.xml  clean package -P dev_wh  -Dmaven.test.skip=true\n;/bin/ls -l\n;\n'
    commands=commands+';\n'
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
    
    needReplaceList=[p,s,t,v,w,x,z,z1,z2,z6,z11,z18,y1]
    m=1
    b=a.recv(10240)
    for command in commandList:
        #print(b)��������b��Ƭ����Ȼ��һ�������������Ƭ�����ǣ������һ������#�Ž�β�ģ���������while������д�������Ҫ�����������Ƭ��
        #��һ������Ŀ�ͷ�����ܵ�Ӱ�죬ֻ��Ӱ�쵽���1����
        bList=b.split(d)
        print('������while֮�Ϸ�Ƭ����Ĺ���')
        for z20 in bList:
            print(z20)
        print('���͵�'+str(m)+'������ǰ��ȡb��ֵ��ͬ�ϣ���ʼѭ����ȡ��Ϣ,ֱ������õõ�#�ո��β���ſ��������'+str(m)+'������')
        n=1
        while not b.endswith(c):
            print('���b����n��β�ģ���ô�Ϳ��Է�Ƭ�ˡ�������Ƭ���ڻ�ȡb�����ж����ǲ�����#�ո��β��')
            if b.endswith(d):
                print('b����n��β�ģ���ʼ��Ƭ')
                for i in b.split(d):
                    #���i���ڿգ��Ͳ����
                    if i !=g:
                        for u in needReplaceList:
                            i=i.replace(u,g)
                        i=i.replace(k,g)
                        iList=i.split(f)
                        for z19 in iList:
                            print(z19)
                        #print(i) ���z19���Ͳ������i�ˡ�
                b=a.recv(10240)
                print('������Ƭ���ڻ�ȡb������ֵ��:')
                print(b)
            else:
                print('b������n��β��������')
                print('b����ǰ��')
                print(b)
                print('b�Ƿ���[y/N]: ��β������ǣ��ͷ���y\n,Ȼ���ڻ�ȡ�����������ǣ��Ǿͼ�����ȡb')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                print('z16��ֵ��')
                print(z16)
                print('��ʼ����')
                b=b+z16
                print('���Ӻ���')
                print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('�Ѿ����е����һ�������ٷ������ֹͣforѭ����')
        else:
            print('�ⲻ�����һ�������Ҫ�ٴη�������')
            print('b��ֵ������#�ո��β�ˣ�����whileѭ������������')
            print('��Ȼb����#�ո��β�������Ҳ���֤#��ǰ��û��n�����ԣ���Ҫ��Ƭ����b')
            bList=b.split(d)
            for z21 in bList:
                print(z21)
                print('������whileѭ��֮�·�Ƭ�Ľ��')
            a.send(command)
            print('��'+str(m)+'���������ɣ���ʼ�������ݣ������ϻ��������β')
            b=a.recv(10240)
        #����������һ�������ôb�Ľ�������������������еġ�
        #��������һ�������ôb�Ľ�������������������еġ�
        #Ϊʲô�أ�
        #��Ϊ����Ĺ�����
        #1.�жϽ���Ƿ���#�ո��β
        #    ���ǣ��ж��Ƿ���n��β
        #        �ǣ���Ƭ;���»�ȡ��b
        #        ���ǣ����ӻ�ȡ��b
        #    �ǣ�����ѭ��
        #2.���������ȡ�����������һ��forѭ��������һ��forѭ���д���b�Ľ��
        #�����������ж�ʱ�����������һ�����Ȼ��
        #��������һ��������ڴ�����b�Ľ�����ͽ���forѭ��
        m+=1
        
    
   #print('����for ѭ��')
    
    a.close()
    transport.close()
    
def RemoterControlInvoke4ok7(host,port,userName,commands2,eventId,node):
    #�������tar ��maven���ǽ���ʽ�Ķ������ˡ����ڸ�������������Ҫ����ʽ�Ĺ���
    #yum�������̿������ˡ��ڴ����պ��������Ľ�����Ϊʹ���������������̡�
    #���¹��̶�ֻ�Է�Ƭ������д���
    #1.ȥ����ɫ
    #2.ȥ��' \r'
    #2.5.��while�⣬#ǰ���n���з�Ƭ��while���¶�������
    #3.������2.5��ȥ��һ��'\r'
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #��ʱ�Ự�Ѵ�
    a.settimeout(100)
    a.get_pty()
    a.invoke_shell()
    #commands='yum install httpd\n'
    #commands='tar zvxf /rgec/src/apache-maven-3.5.3-bin.tar.gz -C /rgec/app/\n'

    commands='cd /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/git_clone/d.mypharma.com\n;mvn  -s  /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/settings.xml  clean package -P dev_wh  -Dmaven.test.skip=true\n;/bin/ls -l\n;\n'
    commands=commands+';\n'
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
    
    needReplaceList=[p,s,t,v,w,x,z,z1,z2,z6,z11,z18,y1]
    m=1
    b=a.recv(10240)
    for command in commandList:
        #print(b)��������b��Ƭ����Ȼ��һ�������������Ƭ�����ǣ������һ������#�Ž�β�ģ���������while������д�������Ҫ�����������Ƭ��
        #��һ������Ŀ�ͷ�����ܵ�Ӱ�죬ֻ��Ӱ�쵽���1����
        #bList=b.split(d)
        #print('������while֮�Ϸ�Ƭ����Ĺ���')
        #for z20 in bList:
        #    z20=z20.replace(f,g)
        #    print(z20)
        #print('���͵�'+str(m)+'������ǰ��ȡb��ֵ��ͬ�ϣ���ʼѭ����ȡ��Ϣ,ֱ������õõ�#�ո��β���ſ��������'+str(m)+'������')
        n=1
        while not b.endswith(c):
            print('���b����n��β�ģ���ô�Ϳ��Է�Ƭ�ˡ�������Ƭ���ڻ�ȡb�����ж����ǲ�����#�ո��β��')
            if b.endswith(d):
                print('b����n��β�ģ���ʼ��Ƭ')
                for i in b.split(d):
                    #���i���ڿգ��Ͳ����
                    if i !=g:
                        for u in needReplaceList:
                            i=i.replace(u,g)
                        i=i.replace(k,g)
                        iList=i.split(f)
                        for z19 in iList:
                            z19=z19.replace(f,g)
                            if z19!=g:
                                print(z19)
                        #print(i) ���z19���Ͳ������i�ˡ�
                b=a.recv(10240)
                print('������Ƭ���ڻ�ȡb������ֵ��:')
                print(b)
            else:
                print('b������n��β��������')
                print('b����ǰ��')
                print(b)
                print('b�Ƿ���[y/N]: ��β������ǣ��ͷ���y\n,Ȼ���ڻ�ȡ�����������ǣ��Ǿͼ�����ȡb')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                print('z16��ֵ��')
                print(z16)
                print('��ʼ����')
                b=b+z16
                print('���Ӻ���')
                print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('�Ѿ����е����һ�������ٷ������ֹͣforѭ����')
        else:
            print('�ⲻ�����һ�������Ҫ�ٴη�������')
            print('b��ֵ������#�ո��β�ˣ�����whileѭ������������')
            print('��Ȼb����#�ո��β�������Ҳ���֤#��ǰ��û��n�����ԣ���Ҫ��Ƭ����b')
            bList=b.split(d)
            for z21 in bList:
                z21=z21.replace(f,g)
                print(z21)
                print('������whileѭ��֮�·�Ƭ�Ľ��')
            a.send(command)
            print('��'+str(m)+'���������ɣ���ʼ�������ݣ������ϻ��������β')
            b=a.recv(10240)
        #����������һ�������ôb�Ľ�������������������еġ�
        #��������һ�������ôb�Ľ�������������������еġ�
        #Ϊʲô�أ�
        #��Ϊ����Ĺ�����
        #1.�жϽ���Ƿ���#�ո��β
        #    ���ǣ��ж��Ƿ���n��β
        #        �ǣ���Ƭ;���»�ȡ��b
        #        ���ǣ����ӻ�ȡ��b
        #    �ǣ�����ѭ��
        #2.���������ȡ�����������һ��forѭ��������һ��forѭ���д���b�Ľ��
        #�����������ж�ʱ�����������һ�����Ȼ��
        #��������һ��������ڴ�����b�Ľ�����ͽ���forѭ��
        m+=1
        
    
   #print('����for ѭ��')
    
    a.close()
    transport.close()
   
def RemoterControlInvoke4ok8(host,port,userName,commands2,eventId,node):
    #�������tar ��maven���ǽ���ʽ�Ķ������ˡ����ڸ�������������Ҫ����ʽ�Ĺ���
    #yum�������̿������ˡ��ڴ����պ��������Ľ�����Ϊʹ���������������̡�
    #���¹��̶�ֻ�Է�Ƭ������д���
    #1.ȥ����ɫ
    #2.ȥ��' \r'
    #2.5.��while�⣬#ǰ���n���з�Ƭ��while���¶�������
    #2.6.������2.5��ȥ��һ��'\r'
    #3.ȥ�����а�صĽ��
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #��ʱ�Ự�Ѵ�
    a.settimeout(100)
    a.get_pty()
    a.invoke_shell()
    commands='yum install httpd\n'
    #commands='tar zvxf /rgec/src/apache-maven-3.5.3-bin.tar.gz -C /rgec/app/\n'

    #commands='cd /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/git_clone/d.mypharma.com\n;mvn  -s  /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/settings.xml  clean package -P dev_wh  -Dmaven.test.skip=true\n;/bin/ls -l\n;\n'
    commands=commands+';\n'
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

    
    needReplaceList=[p,s,t,v,w,x,z,z1,z2,z6,z11,z18,y1]
    m=1
    b=a.recv(10240)
    for command in commandList:
        #print(b)��������b��Ƭ����Ȼ��һ�������������Ƭ�����ǣ������һ������#�Ž�β�ģ���������while������д�������Ҫ�����������Ƭ��
        #��һ������Ŀ�ͷ�����ܵ�Ӱ�죬ֻ��Ӱ�쵽���1����
        #bList=b.split(d)
        #print('������while֮�Ϸ�Ƭ����Ĺ���')
        #for z20 in bList:
        #    z20=z20.replace(f,g)
        #    print(z20)
        #print('���͵�'+str(m)+'������ǰ��ȡb��ֵ��ͬ�ϣ���ʼѭ����ȡ��Ϣ,ֱ������õõ�#�ո��β���ſ��������'+str(m)+'������')
        n=1
        while not b.endswith(c):
            print('���b����n��β�ģ���ô�Ϳ��Է�Ƭ�ˡ�������Ƭ���ڻ�ȡb�����ж����ǲ�����#�ո��β��')
            if b.endswith(d):
                print('b����n��β�ģ���ʼ��Ƭ')
                for i in b.split(d):
                    #���i���ڿգ��Ͳ����
                    if i !=g:
                        for u in needReplaceList:
                            i=i.replace(u,g)
                        i=i.replace(k,g)
                        iList=i.split(f)
                        for z19 in iList:
                            z19=z19.replace(f,g)
                            if z19!=g:
                                print(z19)
                        #print(i) ���z19���Ͳ������i�ˡ�
                b=a.recv(10240)
                #print('������Ƭ���ڻ�ȡb������ֵ��:')
                #print(b)
            else:
                print('b������n��β��������')
                #print('b����ǰ��')
                #print(b)
                print('b�Ƿ���[y/N]: ��β������ǣ��ͷ���y\n,Ȼ���ڻ�ȡ�����������ǣ��Ǿͼ�����ȡb')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                #print('z16��ֵ��')
                #print(z16)
                #print('��ʼ����')
                b=b+z16
                #print('���Ӻ���')
                #print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('�Ѿ����е����һ�������ٷ������ֹͣforѭ����')
        else:
            print('�ⲻ�����һ�������Ҫ�ٴη�������')
            print('b��ֵ������#�ո��β�ˣ�����whileѭ������������')
            print('��Ȼb����#�ո��β�������Ҳ���֤#��ǰ��û��n�����ԣ���Ҫ��Ƭ����b')
            bList=b.split(d)
            for z21 in bList:
                z21=z21.replace(f,g)
                print(z21)
                print('������whileѭ��֮�·�Ƭ�Ľ��')
            a.send(command)
            print('��'+str(m)+'���������ɣ���ʼ�������ݣ������ϻ��������β')
            b=a.recv(10240)
        #����������һ�������ôb�Ľ�������������������еġ�
        #��������һ�������ôb�Ľ�������������������еġ�
        #Ϊʲô�أ�
        #��Ϊ����Ĺ�����
        #1.�жϽ���Ƿ���#�ո��β
        #    ���ǣ��ж��Ƿ���n��β
        #        �ǣ���Ƭ;���»�ȡ��b
        #        ���ǣ����ӻ�ȡ��b
        #    �ǣ�����ѭ��
        #2.���������ȡ�����������һ��forѭ��������һ��forѭ���д���b�Ľ��
        #�����������ж�ʱ�����������һ�����Ȼ��
        #��������һ��������ڴ�����b�Ľ�����ͽ���forѭ��
        m+=1
        
    
   #print('����for ѭ��')
    
    a.close()
    transport.close()   
    
def RemoterControlInvoke4ok9(host,port,userName,commands2,eventId,node):
    #�������tar ��maven���ǽ���ʽ�Ķ������ˡ����ڸ�������������Ҫ����ʽ�Ĺ���
    #yum�������̿������ˡ��ڴ����պ��������Ľ�����Ϊʹ���������������̡�
    #���¹��̶�ֻ�Է�Ƭ������д���
    #1.ȥ����ɫ
    #2.ȥ��' \r'
    #2.5.��while�⣬#ǰ���n���з�Ƭ��while���¶�������
    #2.6.������2.5��ȥ��һ��'\r'
    #3.ȥ�����а�صĽ��
    #3.5ȥ��������������صİ����ʾ��
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #��ʱ�Ự�Ѵ�
    a.settimeout(100)
    a.get_pty()
    a.invoke_shell()
    commands='yum install httpd\n'
    #commands='tar zvxf /rgec/src/apache-maven-3.5.3-bin.tar.gz -C /rgec/app/\n'

    #commands='cd /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/git_clone/d.mypharma.com\n;mvn  -s  /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/settings.xml  clean package -P dev_wh  -Dmaven.test.skip=true\n;/bin/ls -l\n;\n'
    commands=commands+';\n'
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
    
    needReplaceList=[p,s,t,v,w,x,z,z1,z2,z6,z11,z18,y1]
    m=1
    b=a.recv(10240)
    for command in commandList:
        #print(b)��������b��Ƭ����Ȼ��һ�������������Ƭ�����ǣ������һ������#�Ž�β�ģ���������while������д�������Ҫ�����������Ƭ��
        #��һ������Ŀ�ͷ�����ܵ�Ӱ�죬ֻ��Ӱ�쵽���1����
        #bList=b.split(d)
        #print('������while֮�Ϸ�Ƭ����Ĺ���')
        #for z20 in bList:
        #    z20=z20.replace(f,g)
        #    print(z20)
        #print('���͵�'+str(m)+'������ǰ��ȡb��ֵ��ͬ�ϣ���ʼѭ����ȡ��Ϣ,ֱ������õõ�#�ո��β���ſ��������'+str(m)+'������')
        n=1
        while not b.endswith(c):
            print('���b����n��β�ģ���ô�Ϳ��Է�Ƭ�ˡ�������Ƭ���ڻ�ȡb�����ж����ǲ�����#�ո��β��')
            if b.endswith(d):
                print('b����n��β�ģ���ʼ��Ƭ')
                for i in b.split(d):
                    #���i���ڿգ��Ͳ����
                    if i !=g:
                        for u in needReplaceList:
                            i=i.replace(u,g)
                        i=i.replace(k,g)
                        iList=i.split(f)
                        for z19 in iList:
                            z19=z19.replace(f,g)
                            if z19!=g:
                                if z22 not in z19:
                                    #���z19�в�����##�ʹ�ӡ��һ����������������yum��װ�����������������λ�á�
                                    #���ǰ����ع��������ˡ�
                                    print(z19)
                        #print(i) ���z19���Ͳ������i�ˡ�
                b=a.recv(10240)
                #print('������Ƭ���ڻ�ȡb������ֵ��:')
                #print(b)
            else:
                print('b������n��β��������')
                #print('b����ǰ��')
                #print(b)
                print('b�Ƿ���[y/N]: ��β������ǣ��ͷ���y\n,Ȼ���ڻ�ȡ�����������ǣ��Ǿͼ�����ȡb')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                #print('z16��ֵ��')
                #print(z16)
                #print('��ʼ����')
                b=b+z16
                #print('���Ӻ���')
                #print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('�Ѿ����е����һ�������ٷ������ֹͣforѭ����')
        else:
            print('�ⲻ�����һ�������Ҫ�ٴη�������')
            print('b��ֵ������#�ո��β�ˣ�����whileѭ������������')
            print('��Ȼb����#�ո��β�������Ҳ���֤#��ǰ��û��n�����ԣ���Ҫ��Ƭ����b')
            bList=b.split(d)
            for z21 in bList:
                z21=z21.replace(f,g)
                print(z21)
                print('������whileѭ��֮�·�Ƭ�Ľ��')
            a.send(command)
            print('��'+str(m)+'���������ɣ���ʼ�������ݣ������ϻ��������β')
            b=a.recv(10240)
        #����������һ�������ôb�Ľ�������������������еġ�
        #��������һ�������ôb�Ľ�������������������еġ�
        #Ϊʲô�أ�
        #��Ϊ����Ĺ�����
        #1.�жϽ���Ƿ���#�ո��β
        #    ���ǣ��ж��Ƿ���n��β
        #        �ǣ���Ƭ;���»�ȡ��b
        #        ���ǣ����ӻ�ȡ��b
        #    �ǣ�����ѭ��
        #2.���������ȡ�����������һ��forѭ��������һ��forѭ���д���b�Ľ��
        #�����������ж�ʱ�����������һ�����Ȼ��
        #��������һ��������ڴ�����b�Ľ�����ͽ���forѭ��
        m+=1
        
    
   #print('����for ѭ��')
    
    a.close()
    transport.close()   
    
def RemoterControlInvoke4ok10(host,port,userName,commands2,eventId,node):
    #�������tar ��maven���ǽ���ʽ�Ķ������ˡ����ڸ�������������Ҫ����ʽ�Ĺ���
    #yum�������̿������ˡ��ڴ����պ��������Ľ�����Ϊʹ���������������̡�
    #���¹��̶�ֻ�Է�Ƭ������д���
    #1.ȥ����ɫ
    #2.ȥ��' \r'
    #2.5.��while�⣬#ǰ���n���з�Ƭ��while���¶�������
    #2.6.������2.5��ȥ��һ��'\r'
    #3.ȥ�����а�صĽ��
    #3.5ȥ��������������صİ����ʾ��
    #4.ȥ����ʾ
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #��ʱ�Ự�Ѵ�
    a.settimeout(100)
    a.get_pty()
    a.invoke_shell()
    #commands='yum install httpd\n'
    #commands='tar zvxf /rgec/src/apache-maven-3.5.3-bin.tar.gz -C /rgec/app/\n'

    commands='cd /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/git_clone/d.mypharma.com\n;mvn  -s  /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/settings.xml  clean package -P dev_wh  -Dmaven.test.skip=true\n;/bin/ls -l\n;\n'
    commands=commands+';\n'
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
    
    needReplaceList=[p,s,t,v,w,x,z,z1,z2,z6,z11,z18,y1]
    m=1
    b=a.recv(10240)
    for command in commandList:
        #print(b)��������b��Ƭ����Ȼ��һ�������������Ƭ�����ǣ������һ������#�Ž�β�ģ���������while������д�������Ҫ�����������Ƭ��
        #��һ������Ŀ�ͷ�����ܵ�Ӱ�죬ֻ��Ӱ�쵽���1����
        #bList=b.split(d)
        #print('������while֮�Ϸ�Ƭ����Ĺ���')
        #for z20 in bList:
        #    z20=z20.replace(f,g)
        #    print(z20)
        #print('���͵�'+str(m)+'������ǰ��ȡb��ֵ��ͬ�ϣ���ʼѭ����ȡ��Ϣ,ֱ������õõ�#�ո��β���ſ��������'+str(m)+'������')
        n=1
        while not b.endswith(c):
            #print('���b����n��β�ģ���ô�Ϳ��Է�Ƭ�ˡ�������Ƭ���ڻ�ȡb�����ж����ǲ�����#�ո��β��')
            if b.endswith(d):
                #print('b����n��β�ģ���ʼ��Ƭ')
                for i in b.split(d):
                    #���i���ڿգ��Ͳ����
                    if i !=g:
                        for u in needReplaceList:
                            i=i.replace(u,g)
                        i=i.replace(k,g)
                        iList=i.split(f)
                        for z19 in iList:
                            z19=z19.replace(f,g)
                            if z19!=g:
                                if z22 not in z19:
                                    #���z19�в�����##�ʹ�ӡ��һ����������������yum��װ�����������������λ�á�
                                    #���ǰ����ع��������ˡ�
                                    print(z19)
                        #print(i) ���z19���Ͳ������i�ˡ�
                b=a.recv(10240)
                #print('������Ƭ���ڻ�ȡb������ֵ��:')
                #print(b)
            else:
                #print('b������n��β��������')
                #print('b����ǰ��')
                #print(b)
                #print('b�Ƿ���[y/N]: ��β������ǣ��ͷ���y,Ȼ���ڻ�ȡ�����������ǣ��Ǿͼ�����ȡb')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                #print('z16��ֵ��')
                #print(z16)
                #print('��ʼ����')
                b=b+z16
                #print('���Ӻ���')
                #print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('�Ѿ����е����һ�������ٷ������ֹͣforѭ����')
        else:
            #print('�ⲻ�����һ�������Ҫ�ٴη�������')
            #print('b��ֵ������#�ո��β�ˣ�����whileѭ������������')
            #print('��Ȼb����#�ո��β�������Ҳ���֤#��ǰ��û��n�����ԣ���Ҫ��Ƭ����b')
            bList=b.split(d)
            for z21 in bList:
                z21=z21.replace(f,g)
                print(z21)
                #print('������whileѭ��֮�·�Ƭ�Ľ��')
            a.send(command)
            #print('��'+str(m)+'���������ɣ���ʼ�������ݣ������ϻ��������β')
            b=a.recv(10240)
        #����������һ�������ôb�Ľ�������������������еġ�
        #��������һ�������ôb�Ľ�������������������еġ�
        #Ϊʲô�أ�
        #��Ϊ����Ĺ�����
        #1.�жϽ���Ƿ���#�ո��β
        #    ���ǣ��ж��Ƿ���n��β
        #        �ǣ���Ƭ;���»�ȡ��b
        #        ���ǣ����ӻ�ȡ��b
        #    �ǣ�����ѭ��
        #2.���������ȡ�����������һ��forѭ��������һ��forѭ���д���b�Ľ��
        #�����������ж�ʱ�����������һ�����Ȼ��
        #��������һ��������ڴ�����b�Ľ�����ͽ���forѭ��
        m+=1
        
    
   #print('����for ѭ��')
    
    a.close()
    transport.close()
    
def RemoterControlInvoke4ok11(host,port,userName,commands2,eventId,node):
    #�������tar ��maven���ǽ���ʽ�Ķ������ˡ����ڸ�������������Ҫ����ʽ�Ĺ���
    #yum�������̿������ˡ��ڴ����պ��������Ľ�����Ϊʹ���������������̡�
    #���¹��̶�ֻ�Է�Ƭ������д���
    #1.ȥ����ɫ
    #2.ȥ��' \r'
    #2.5.��while�⣬#ǰ���n���з�Ƭ��while���¶�������
    #2.6.������2.5��ȥ��һ��'\r'
    #3.ȥ�����а�صĽ��
    #3.5ȥ��������������صİ����ʾ��
    #4.ȥ����ʾ
    #5.���decode��
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #��ʱ�Ự�Ѵ�
    a.settimeout(100)
    a.get_pty()
    a.invoke_shell()
    #commands='yum install httpd\n'
    #commands='tar zvxf /rgec/src/apache-maven-3.5.3-bin.tar.gz -C /rgec/app/\n'

    commands='cd /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/git_clone/d.mypharma.com\n;mvn  -s  /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/settings.xml  clean package -P dev_wh  -Dmaven.test.skip=true\n;/bin/ls -l\n;\n'
    commands=commands+';\n'
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
    
    needReplaceList=[p,s,t,v,w,x,z,z1,z2,z6,z11,z18,y1]
    m=1
    b=a.recv(10240)
    for command in commandList:
        #print(b)��������b��Ƭ����Ȼ��һ�������������Ƭ�����ǣ������һ������#�Ž�β�ģ���������while������д�������Ҫ�����������Ƭ��
        #��һ������Ŀ�ͷ�����ܵ�Ӱ�죬ֻ��Ӱ�쵽���1����
        #bList=b.split(d)
        #print('������while֮�Ϸ�Ƭ����Ĺ���')
        #for z20 in bList:
        #    z20=z20.replace(f,g)
        #    print(z20)
        #print('���͵�'+str(m)+'������ǰ��ȡb��ֵ��ͬ�ϣ���ʼѭ����ȡ��Ϣ,ֱ������õõ�#�ո��β���ſ��������'+str(m)+'������')
        n=1
        while not b.endswith(c):
            #print('���b����n��β�ģ���ô�Ϳ��Է�Ƭ�ˡ�������Ƭ���ڻ�ȡb�����ж����ǲ�����#�ո��β��')
            if b.endswith(d):
                #print('b����n��β�ģ���ʼ��Ƭ')
                for i in b.split(d):
                    #���i���ڿգ��Ͳ����
                    if i !=g:
                        for u in needReplaceList:
                            i=i.replace(u,g)
                        i=i.replace(k,g)
                        iList=i.split(f)
                        for z19 in iList:
                            z19=z19.replace(f,g)
                            if z19!=g:
                                if z22 not in z19:
                                    #���z19�в�����##�ʹ�ӡ��һ����������������yum��װ�����������������λ�á�
                                    #���ǰ����ع��������ˡ�
                                    print(z19.decode())
                        #print(i) ���z19���Ͳ������i�ˡ�
                b=a.recv(10240)
                #print('������Ƭ���ڻ�ȡb������ֵ��:')
                #print(b)
            else:
                #print('b������n��β��������')
                #print('b����ǰ��')
                #print(b)
                #print('b�Ƿ���[y/N]: ��β������ǣ��ͷ���y,Ȼ���ڻ�ȡ�����������ǣ��Ǿͼ�����ȡb')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                #print('z16��ֵ��')
                #print(z16)
                #print('��ʼ����')
                b=b+z16
                #print('���Ӻ���')
                #print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('�Ѿ����е����һ�������ٷ������ֹͣforѭ����')
        else:
            #print('�ⲻ�����һ�������Ҫ�ٴη�������')
            #print('b��ֵ������#�ո��β�ˣ�����whileѭ������������')
            #print('��Ȼb����#�ո��β�������Ҳ���֤#��ǰ��û��n�����ԣ���Ҫ��Ƭ����b')
            bList=b.split(d)
            for z21 in bList:
                z21=z21.replace(f,g)
                print(z21.decode())
                #print('������whileѭ��֮�·�Ƭ�Ľ��')
            a.send(command)
            #print('��'+str(m)+'���������ɣ���ʼ�������ݣ������ϻ��������β')
            b=a.recv(10240)
        #����������һ�������ôb�Ľ�������������������еġ�
        #��������һ�������ôb�Ľ�������������������еġ�
        #Ϊʲô�أ�
        #��Ϊ����Ĺ�����
        #1.�жϽ���Ƿ���#�ո��β
        #    ���ǣ��ж��Ƿ���n��β
        #        �ǣ���Ƭ;���»�ȡ��b
        #        ���ǣ����ӻ�ȡ��b
        #    �ǣ�����ѭ��
        #2.���������ȡ�����������һ��forѭ��������һ��forѭ���д���b�Ľ��
        #�����������ж�ʱ�����������һ�����Ȼ��
        #��������һ��������ڴ�����b�Ľ�����ͽ���forѭ��
        m+=1
        
    
   #print('����for ѭ��')
    
    a.close()
    transport.close()
    
def RemoterControlInvoke4ok12(host,port,userName,commands,eventId,node):
    #�������tar ��maven���ǽ���ʽ�Ķ������ˡ����ڸ�������������Ҫ����ʽ�Ĺ���
    #yum�������̿������ˡ��ڴ����պ��������Ľ�����Ϊʹ���������������̡�
    #���¹��̶�ֻ�Է�Ƭ������д���
    #1.ȥ����ɫ
    #2.ȥ��' \r'
    #2.5.��while�⣬#ǰ���n���з�Ƭ��while���¶�������
    #2.6.������2.5��ȥ��һ��'\r'
    #3.ȥ�����а�صĽ��
    #3.5ȥ��������������صİ����ʾ��
    #4.ȥ����ʾ
    #5.���decode��
    #6.�ռ����ݣ����������÷��������ж��Ƿ����гɹ���
    #6.1ȥ��maven������صĹ���
    result=''
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #��ʱ�Ự�Ѵ�
    a.settimeout(100)
    a.get_pty()
    a.invoke_shell()
    #commands='yum install httpd\n'
    #commands='tar zvxf /rgec/src/apache-maven-3.5.3-bin.tar.gz -C /rgec/app/\n'

    #commands='cd /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/git_clone/d.mypharma.com\n;mvn  -s  /rgec/var/autodeploy/dev_gm_mph_www/20180613174607597/settings.xml  clean package -P dev_wh  -Dmaven.test.skip=true\n;/bin/ls -l\n;\n'
    commands=commands+';\n;\n'
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
    
    needReplaceList=[p,s,t,v,w,x,z,z1,z2,z6,z11,z18,y1,z13]
    m=1
    b=a.recv(10240)
    for command in commandList:
        #print(b)��������b��Ƭ����Ȼ��һ�������������Ƭ�����ǣ������һ������#�Ž�β�ģ���������while������д�������Ҫ�����������Ƭ��
        #��һ������Ŀ�ͷ�����ܵ�Ӱ�죬ֻ��Ӱ�쵽���1����
        #bList=b.split(d)
        #print('������while֮�Ϸ�Ƭ����Ĺ���')
        #for z20 in bList:
        #    z20=z20.replace(f,g)
        #    print(z20)
        #print('���͵�'+str(m)+'������ǰ��ȡb��ֵ��ͬ�ϣ���ʼѭ����ȡ��Ϣ,ֱ������õõ�#�ո��β���ſ��������'+str(m)+'������')
        n=1
        while not b.endswith(c):
            #print('���b����n��β�ģ���ô�Ϳ��Է�Ƭ�ˡ�������Ƭ���ڻ�ȡb�����ж����ǲ�����#�ո��β��')
            if b.endswith(d):
                #print('b����n��β�ģ���ʼ��Ƭ')
                for i in b.split(d):
                    #���i���ڿգ��Ͳ����
                    if i !=g:
                        for u in needReplaceList:
                            i=i.replace(u,g)
                        i=i.replace(k,g)
                        iList=i.split(f)
                        for z19 in iList:
                            z19=z19.replace(f,g)
                            if z19!=g:
                                if z22 not in z19:
                                    #���z19�в�����##�ʹ�ӡ��һ����������������yum��װ�����������������λ�á�
                                    #���ǰ����ع��������ˡ�
                                    if z15 not in z19:
                                    #���z19�в�����Progress ���ʹ�ӡ������������������maven�������������λ�á�
                                    #�Ͱ�������ع��������ˡ�
                                        print(z19.decode())
                                        result+=z19.decode()
                        #print(i) ���z19���Ͳ������i�ˡ�
                b=a.recv(10240)
                #print('������Ƭ���ڻ�ȡb������ֵ��:')
                #print(b)
            else:
                #print('b������n��β��������')
                #print('b����ǰ��')
                #print(b)
                #print('b�Ƿ���[y/N]: ��β������ǣ��ͷ���y,Ȼ���ڻ�ȡ�����������ǣ��Ǿͼ�����ȡb')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                #print('z16��ֵ��')
                #print(z16)
                #print('��ʼ����')
                b=b+z16
                #print('���Ӻ���')
                #print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('�Ѿ����е����һ�������ٷ������ֹͣforѭ����')
        else:
            #print('�ⲻ�����һ�������Ҫ�ٴη�������')
            #print('b��ֵ������#�ո��β�ˣ�����whileѭ������������')
            #print('��Ȼb����#�ո��β�������Ҳ���֤#��ǰ��û��n�����ԣ���Ҫ��Ƭ����b')
            bList=b.split(d)
            for z21 in bList:
                z21=z21.replace(f,g)
                print(z21.decode())
                result+=z21.decode()
                #print('������whileѭ��֮�·�Ƭ�Ľ��')
            a.send(command)
            #print('��'+str(m)+'���������ɣ���ʼ�������ݣ������ϻ��������β')
            b=a.recv(10240)
        #����������һ�������ôb�Ľ�������������������еġ�
        #��������һ�������ôb�Ľ�������������������еġ�
        #Ϊʲô�أ�
        #��Ϊ����Ĺ�����
        #1.�жϽ���Ƿ���#�ո��β
        #    ���ǣ��ж��Ƿ���n��β
        #        �ǣ���Ƭ;���»�ȡ��b
        #        ���ǣ����ӻ�ȡ��b
        #    �ǣ�����ѭ��
        #2.���������ȡ�����������һ��forѭ��������һ��forѭ���д���b�Ľ��
        #�����������ж�ʱ�����������һ�����Ȼ��
        #��������һ��������ڴ�����b�Ľ�����ͽ���forѭ��
        m+=1
        
    
   #print('����for ѭ��')
    
    a.close()
    transport.close()   
    return result
   