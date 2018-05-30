                function timeNow(){
                    var now=new Date();
                    var d=now.getDate();
                    if (d<10){
                        d='0'+d;
                    }
                    var M=now.getMonth()+1;
                    if (M<10){
                        M='0'+M;
                    }
                    var y=now.getFullYear();
                    var m=now.getMinutes();
                    if (m<10){
                        m='0'+m;
                    }
                    var h=now.getHours();
                    if (h<10){
                        h='0'+h;
                    }
                    var s=now.getSeconds();
                    if (s<10){
                        s='0'+s;
                    }
                    var ms=(now.getMilliseconds()).toString();
                    if (ms<10){
                        ms='0'+ms;
                    }
                    var result=y+M+d+h+m+s+ms;
                    return result;
                };
                function range(begin,end){
                    var Array=[];
                    
                    for (var i=begin ; i<=end ; i++ ) {
                        Array.push(i);
                    }
                    return Array;
                };

