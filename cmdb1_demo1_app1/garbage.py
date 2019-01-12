def RemoterControlInvoke4ok2(host,port,userName,commands,eventId,node):
    #这个方法tar 和maven，非交互式的都可以了。现在复制它，开发需要交互式的过程
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #此时会话已打开
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
        print('发送第'+str(m)+'次命令前获取b的值，同上，开始循环获取消息,直到，获得得到#空格结尾，才可以输入第'+str(m)+'条命令')
        n=1
        while not b.endswith(c):
            print('如果b是以n结尾的，那么就可以分片了。分完了片，在获取b，在判断它是不是以#空格结尾。')
            if b.endswith(d):
                print('b是以n结尾的，开始分片')
                for i in b.split(d):
                    #如果i等于空，就不输出
                    if i !=l:
                        print(i)
                b=a.recv(10240)
                print('分完了片，在获取b，它的值是:')
                print(b)
            else:
                print('b,不是以n结尾，叠加它')
                print('b,叠加前是')
                print(b)
                z16=a.recv(10240)
                print('z16的值是')
                print(z16)
                print('开始叠加')
                b=b+z16
                print('叠加后是')
                print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('已经进行到最后一条，不再发送命令，停止for循环。')
        else:
            print('b的值现在是#空格结尾了，结束while循环，输入命令')
            a.send(command)
            print('第'+str(m)+'条命令发送完成，开始接收数据，理论上会是命令结尾')
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

def RemoterControlInvoke4ok3(host,port,userName,commands2,eventId,node):
    #这个方法tar 和maven，非交互式的都可以了。现在复制它，开发需要交互式的过程
    #yum交互过程开发完了。期待，日后有其他的交互行为使用这个方法处理过程。
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #此时会话已打开
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
        print('发送第'+str(m)+'次命令前获取b的值，同上，开始循环获取消息,直到，获得得到#空格结尾，才可以输入第'+str(m)+'条命令')
        n=1
        while not b.endswith(c):
            print('如果b是以n结尾的，那么就可以分片了。分完了片，在获取b，在判断它是不是以#空格结尾。')
            if b.endswith(d):
                print('b是以n结尾的，开始分片')
                for i in b.split(d):
                    #如果i等于空，就不输出
                    if i !=g:
                        print(i)
                b=a.recv(10240)
                print('分完了片，在获取b，它的值是:')
                print(b)
            else:
                print('b不是以n结尾，叠加它')
                print('b叠加前是')
                print(b)
                print('b是否以[y/N]: 结尾，如果是，就发送y\n,然后在获取结果。如果不是，那就继续获取b')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                print('z16的值是')
                print(z16)
                print('开始叠加')
                b=b+z16
                print('叠加后是')
                print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('已经进行到最后一条，不再发送命令，停止for循环。')
        else:
            print('b的值现在是#空格结尾了，结束while循环，输入命令')
            a.send(command)
            print('第'+str(m)+'条命令发送完成，开始接收数据，理论上会是命令结尾')
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
    
def RemoterControlInvoke4ok4(host,port,userName,commands2,eventId,node):
    #这个方法tar 和maven，非交互式的都可以了。现在复制它，开发需要交互式的过程
    #yum交互过程开发完了。期待，日后有其他的交互行为使用这个方法处理过程。
    #以下过程都只对分片结果进行处理
    #1.去除颜色
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #此时会话已打开
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
        print('发送第'+str(m)+'次命令前获取b的值，同上，开始循环获取消息,直到，获得得到#空格结尾，才可以输入第'+str(m)+'条命令')
        n=1
        while not b.endswith(c):
            print('如果b是以n结尾的，那么就可以分片了。分完了片，在获取b，在判断它是不是以#空格结尾。')
            if b.endswith(d):
                print('b是以n结尾的，开始分片')
                for i in b.split(d):
                    #如果i等于空，就不输出
                    if i !=g:
                        for u in needReplaceList:
                            i=i.replace(u,g)
                        print(i)
                b=a.recv(10240)
                print('分完了片，在获取b，它的值是:')
                print(b)
            else:
                print('b不是以n结尾，叠加它')
                print('b叠加前是')
                print(b)
                print('b是否以[y/N]: 结尾，如果是，就发送y\n,然后在获取结果。如果不是，那就继续获取b')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                print('z16的值是')
                print(z16)
                print('开始叠加')
                b=b+z16
                print('叠加后是')
                print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('已经进行到最后一条，不再发送命令，停止for循环。')
        else:
            print('b的值现在是#空格结尾了，结束while循环，输入命令')
            a.send(command)
            print('第'+str(m)+'条命令发送完成，开始接收数据，理论上会是命令结尾')
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
    
def RemoterControlInvoke4ok5(host,port,userName,commands2,eventId,node):
    #这个方法tar 和maven，非交互式的都可以了。现在复制它，开发需要交互式的过程
    #yum交互过程开发完了。期待，日后有其他的交互行为使用这个方法处理过程。
    #以下过程都只对分片结果进行处理
    #1.去除颜色
    #2.去掉\r
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #此时会话已打开
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
        print('发送第'+str(m)+'次命令前获取b的值，同上，开始循环获取消息,直到，获得得到#空格结尾，才可以输入第'+str(m)+'条命令')
        n=1
        while not b.endswith(c):
            print('如果b是以n结尾的，那么就可以分片了。分完了片，在获取b，在判断它是不是以#空格结尾。')
            if b.endswith(d):
                print('b是以n结尾的，开始分片')
                for i in b.split(d):
                    #如果i等于空，就不输出
                    if i !=g:
                        for u in needReplaceList:
                            i=i.replace(u,g)
                        i=i.replace(k,g)
                        print(i)
                b=a.recv(10240)
                print('分完了片，在获取b，它的值是:')
                print(b)
            else:
                print('b不是以n结尾，叠加它')
                print('b叠加前是')
                print(b)
                print('b是否以[y/N]: 结尾，如果是，就发送y\n,然后在获取结果。如果不是，那就继续获取b')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                print('z16的值是')
                print(z16)
                print('开始叠加')
                b=b+z16
                print('叠加后是')
                print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('已经进行到最后一条，不再发送命令，停止for循环。')
        else:
            print('b的值现在是#空格结尾了，结束while循环，输入命令')
            a.send(command)
            print('第'+str(m)+'条命令发送完成，开始接收数据，理论上会是命令结尾')
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
    
def RemoterControlInvoke4ok6(host,port,userName,commands2,eventId,node):
    #这个方法tar 和maven，非交互式的都可以了。现在复制它，开发需要交互式的过程
    #yum交互过程开发完了。期待，日后有其他的交互行为使用这个方法处理过程。
    #以下过程都只对分片结果进行处理
    #1.去除颜色
    #2.去掉' \r'
    #2.5.对while外，#前面的n进行分片。while上下都处理了
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #此时会话已打开
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
        #print(b)这里必须给b分片，虽然第一条命令不会有其他片，但是，最后那一次是以#号结尾的，它进不了while里面进行处理。所以要在这里给他分片。
        #第一条命令的开头不会受到影响，只会影响到最后1条。
        bList=b.split(d)
        print('这是在while之上分片处理的过程')
        for z20 in bList:
            print(z20)
        print('发送第'+str(m)+'次命令前获取b的值，同上，开始循环获取消息,直到，获得得到#空格结尾，才可以输入第'+str(m)+'条命令')
        n=1
        while not b.endswith(c):
            print('如果b是以n结尾的，那么就可以分片了。分完了片，在获取b，在判断它是不是以#空格结尾。')
            if b.endswith(d):
                print('b是以n结尾的，开始分片')
                for i in b.split(d):
                    #如果i等于空，就不输出
                    if i !=g:
                        for u in needReplaceList:
                            i=i.replace(u,g)
                        i=i.replace(k,g)
                        iList=i.split(f)
                        for z19 in iList:
                            print(z19)
                        #print(i) 输出z19，就不用输出i了。
                b=a.recv(10240)
                print('分完了片，在获取b，它的值是:')
                print(b)
            else:
                print('b不是以n结尾，叠加它')
                print('b叠加前是')
                print(b)
                print('b是否以[y/N]: 结尾，如果是，就发送y\n,然后在获取结果。如果不是，那就继续获取b')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                print('z16的值是')
                print(z16)
                print('开始叠加')
                b=b+z16
                print('叠加后是')
                print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('已经进行到最后一条，不再发送命令，停止for循环。')
        else:
            print('这不是最后一条命令，需要再次发送命令')
            print('b的值现在是#空格结尾了，结束while循环，输入命令')
            print('虽然b是以#空格结尾，但是我不保证#号前面没有n，所以，我要分片处理b')
            bList=b.split(d)
            for z21 in bList:
                print(z21)
                print('这是在while循环之下分片的结果')
            a.send(command)
            print('第'+str(m)+'条命令发送完成，开始接收数据，理论上会是命令结尾')
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
    
def RemoterControlInvoke4ok7(host,port,userName,commands2,eventId,node):
    #这个方法tar 和maven，非交互式的都可以了。现在复制它，开发需要交互式的过程
    #yum交互过程开发完了。期待，日后有其他的交互行为使用这个方法处理过程。
    #以下过程都只对分片结果进行处理
    #1.去除颜色
    #2.去掉' \r'
    #2.5.对while外，#前面的n进行分片。while上下都处理了
    #3.进行完2.5后，去除一次'\r'
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #此时会话已打开
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
            print('如果b是以n结尾的，那么就可以分片了。分完了片，在获取b，在判断它是不是以#空格结尾。')
            if b.endswith(d):
                print('b是以n结尾的，开始分片')
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
                                print(z19)
                        #print(i) 输出z19，就不用输出i了。
                b=a.recv(10240)
                print('分完了片，在获取b，它的值是:')
                print(b)
            else:
                print('b不是以n结尾，叠加它')
                print('b叠加前是')
                print(b)
                print('b是否以[y/N]: 结尾，如果是，就发送y\n,然后在获取结果。如果不是，那就继续获取b')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                print('z16的值是')
                print(z16)
                print('开始叠加')
                b=b+z16
                print('叠加后是')
                print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('已经进行到最后一条，不再发送命令，停止for循环。')
        else:
            print('这不是最后一条命令，需要再次发送命令')
            print('b的值现在是#空格结尾了，结束while循环，输入命令')
            print('虽然b是以#空格结尾，但是我不保证#号前面没有n，所以，我要分片处理b')
            bList=b.split(d)
            for z21 in bList:
                z21=z21.replace(f,g)
                print(z21)
                print('这是在while循环之下分片的结果')
            a.send(command)
            print('第'+str(m)+'条命令发送完成，开始接收数据，理论上会是命令结尾')
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
   
def RemoterControlInvoke4ok8(host,port,userName,commands2,eventId,node):
    #这个方法tar 和maven，非交互式的都可以了。现在复制它，开发需要交互式的过程
    #yum交互过程开发完了。期待，日后有其他的交互行为使用这个方法处理过程。
    #以下过程都只对分片结果进行处理
    #1.去除颜色
    #2.去掉' \r'
    #2.5.对while外，#前面的n进行分片。while上下都处理了
    #2.6.进行完2.5后，去除一次'\r'
    #3.去除运行半截的结果
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #此时会话已打开
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
            print('如果b是以n结尾的，那么就可以分片了。分完了片，在获取b，在判断它是不是以#空格结尾。')
            if b.endswith(d):
                print('b是以n结尾的，开始分片')
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
                                print(z19)
                        #print(i) 输出z19，就不用输出i了。
                b=a.recv(10240)
                #print('分完了片，在获取b，它的值是:')
                #print(b)
            else:
                print('b不是以n结尾，叠加它')
                #print('b叠加前是')
                #print(b)
                print('b是否以[y/N]: 结尾，如果是，就发送y\n,然后在获取结果。如果不是，那就继续获取b')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                #print('z16的值是')
                #print(z16)
                #print('开始叠加')
                b=b+z16
                #print('叠加后是')
                #print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('已经进行到最后一条，不再发送命令，停止for循环。')
        else:
            print('这不是最后一条命令，需要再次发送命令')
            print('b的值现在是#空格结尾了，结束while循环，输入命令')
            print('虽然b是以#空格结尾，但是我不保证#号前面没有n，所以，我要分片处理b')
            bList=b.split(d)
            for z21 in bList:
                z21=z21.replace(f,g)
                print(z21)
                print('这是在while循环之下分片的结果')
            a.send(command)
            print('第'+str(m)+'条命令发送完成，开始接收数据，理论上会是命令结尾')
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
    
def RemoterControlInvoke4ok9(host,port,userName,commands2,eventId,node):
    #这个方法tar 和maven，非交互式的都可以了。现在复制它，开发需要交互式的过程
    #yum交互过程开发完了。期待，日后有其他的交互行为使用这个方法处理过程。
    #以下过程都只对分片结果进行处理
    #1.去除颜色
    #2.去掉' \r'
    #2.5.对while外，#前面的n进行分片。while上下都处理了
    #2.6.进行完2.5后，去除一次'\r'
    #3.去除运行半截的结果
    #3.5去除打包过程中下载的半截提示。
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #此时会话已打开
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
            print('如果b是以n结尾的，那么就可以分片了。分完了片，在获取b，在判断它是不是以#空格结尾。')
            if b.endswith(d):
                print('b是以n结尾的，开始分片')
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
                                    print(z19)
                        #print(i) 输出z19，就不用输出i了。
                b=a.recv(10240)
                #print('分完了片，在获取b，它的值是:')
                #print(b)
            else:
                print('b不是以n结尾，叠加它')
                #print('b叠加前是')
                #print(b)
                print('b是否以[y/N]: 结尾，如果是，就发送y\n,然后在获取结果。如果不是，那就继续获取b')
                if b.endswith(z17):
                    a.send('y\n')
                z16=a.recv(10240)
                #print('z16的值是')
                #print(z16)
                #print('开始叠加')
                b=b+z16
                #print('叠加后是')
                #print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('已经进行到最后一条，不再发送命令，停止for循环。')
        else:
            print('这不是最后一条命令，需要再次发送命令')
            print('b的值现在是#空格结尾了，结束while循环，输入命令')
            print('虽然b是以#空格结尾，但是我不保证#号前面没有n，所以，我要分片处理b')
            bList=b.split(d)
            for z21 in bList:
                z21=z21.replace(f,g)
                print(z21)
                print('这是在while循环之下分片的结果')
            a.send(command)
            print('第'+str(m)+'条命令发送完成，开始接收数据，理论上会是命令结尾')
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
    
def RemoterControlInvoke4ok10(host,port,userName,commands2,eventId,node):
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
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #此时会话已打开
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
                                    print(z19)
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
                z16=a.recv(10240)
                #print('z16的值是')
                #print(z16)
                #print('开始叠加')
                b=b+z16
                #print('叠加后是')
                #print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('已经进行到最后一条，不再发送命令，停止for循环。')
        else:
            #print('这不是最后一条命令，需要再次发送命令')
            #print('b的值现在是#空格结尾了，结束while循环，输入命令')
            #print('虽然b是以#空格结尾，但是我不保证#号前面没有n，所以，我要分片处理b')
            bList=b.split(d)
            for z21 in bList:
                z21=z21.replace(f,g)
                print(z21)
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
    
def RemoterControlInvoke4ok11(host,port,userName,commands2,eventId,node):
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
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #此时会话已打开
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
                                    print(z19.decode())
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
                z16=a.recv(10240)
                #print('z16的值是')
                #print(z16)
                #print('开始叠加')
                b=b+z16
                #print('叠加后是')
                #print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('已经进行到最后一条，不再发送命令，停止for循环。')
        else:
            #print('这不是最后一条命令，需要再次发送命令')
            #print('b的值现在是#空格结尾了，结束while循环，输入命令')
            #print('虽然b是以#空格结尾，但是我不保证#号前面没有n，所以，我要分片处理b')
            bList=b.split(d)
            for z21 in bList:
                z21=z21.replace(f,g)
                print(z21.decode())
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
    
def RemoterControlInvoke4ok12(host,port,userName,commands,eventId,node):
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
    result=''
    private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    transport = paramiko.Transport(('192.168.20.98',22))
    transport.connect(username='root', pkey=private_key)
    a=transport.open_session()
    #此时会话已打开
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
                                        print(z19.decode())
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
                z16=a.recv(10240)
                #print('z16的值是')
                #print(z16)
                #print('开始叠加')
                b=b+z16
                #print('叠加后是')
                #print(b)
            n+=1
            #time.sleep(1)
        if m == len(commandList):
            print('已经进行到最后一条，不再发送命令，停止for循环。')
        else:
            #print('这不是最后一条命令，需要再次发送命令')
            #print('b的值现在是#空格结尾了，结束while循环，输入命令')
            #print('虽然b是以#空格结尾，但是我不保证#号前面没有n，所以，我要分片处理b')
            bList=b.split(d)
            for z21 in bList:
                z21=z21.replace(f,g)
                print(z21.decode())
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
   