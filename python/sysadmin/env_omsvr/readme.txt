virtual env 的目录结构
(env_omsvr)[root@www env_omsvr]# pwd
/devops/env_omsvr
(env_omsvr)[root@www env_omsvr]# ll
total 28
drwxr-xr-x  2 root root 4096 Apr 14 15:05 bin
drwxr-xr-x  2 root root 4096 Apr 13 20:42 include
drwxr-xr-x  3 root root 4096 Apr 13 20:42 lib
drwxr-xr-x  2 root root 4096 Apr 14 21:26 OMAudit
drwxr-xr-x  4 root root 4096 Apr 14 16:20 OMServer
drwxr-xr-x 10 root root 4096 Apr 14 15:07 OMserverweb
-rw-r--r--  1 root root  121 Apr 14 22:20 requirements.txt


主要的交互区域
页面占位符  -->
        <font class="ajaxmodulerunresult">[user@omserver]# <img src='/static/images/cursor_f01.gif' align='absmiddle'></fo
nt><br>
        <div class="ajaxmodulerunresult" id="placeholder" style="height:430px;OVERFLOW-y:auto;font-family: Verdana, Arial,
Vrinda,Tahoma;"></div>

AJAX交互 -->
        var url = '/autoadmin/module_run/?ModuleID='+$F("ModuleID")+'&hosts='+serverappvalue+urlpar;
        var myAjax = new Ajax.Request(
        url,
        {
                method: 'get',
                onComplete: showResponse
        });
        function showResponse(originalRequest)
        {
                $('placeholder').innerHTML = originalRequest.responseText+'<br>'+$('placeholder').innerHTML;
        }

