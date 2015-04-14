# omsvr batch cmd && ajax cmd audit

## 技术栈
+ pip 1.1
+ python 2.7.3
+ django 1.4.9
+ prototype 1.6.0
+ ymPrompt.js      ymPrompt消息提示组件
+ My97DatePicker   js日期控件(not used)
+ softkeyboard.js  js软键盘(not used)
+ bash.js          页面主要的AJAX交互

## 主要交互区域
+ 页面占位符  -->
        <font class="ajaxmodulerunresult">[user@omserver]# <img src='/static/images/cursor_f01.gif' align='absmiddle'></fo
nt><br>
        <div class="ajaxmodulerunresult" id="placeholder" style="height:430px;OVERFLOW-y:auto;font-family: Verdana, Arial,
Vrinda,Tahoma;"></div>

+ AJAX交互 -->
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

## 注意
+ omserver.py 不要跑在virtual_env 下 ，会出现找不到路径的情况

+ virtual env 目录结构
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
## GUI screenshots
#### cmd on GUI
![image](https://github.com/cyril7/mygit/raw/master/python/sysadmin/env_omsvr/screenshots_git/omsvr_1.jpg)

#### cmd history audit
![image](https://github.com/cyril7/mygit/raw/master/python/sysadmin/env_omsvr/screenshots_git/omsvr_audit.jpg)


## 问题反馈

  在使用中有任何问题，欢迎反馈给我，可以用以下联系方式跟我交流

* Email
