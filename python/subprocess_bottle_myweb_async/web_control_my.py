# -*- coding: utf-8 -*-
import subprocess
import command
import cmd_all
import sys
from bottle import Bottle, abort, route, run, request, response, static_file



app = Bottle()
@app.route("/")
def index():
    return static_file('index.html', root='./static')

@app.route('/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='./static')


'''
>>> import cmd_all
>>> dir(cmd_all)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cmd_conn_counts', 'cmd_nginx_restart', 'cmd_op
ened_port', 'cmd_server_restart', 'cmd_uptime']
>>> cmd = cmd_from_form(value="opened_port")
>>> cmd
'netstat -lnp'
'''
def cmd_from_form(value):
    cmd_function = getattr(cmd_all, "cmd_%s" % value, cmd_all.cmd_uptime)
    return cmd_function()

 

#@post('/manipulate/') # or @route('/login', method='POST')
@app.route('/manipulate', method='POST')
def manipulate():
    if request.POST.get('manipulate','').strip() and request.POST.get('ip','').strip():
        cmd = cmd_from_form(request.POST.get('manipulate',''))
        ip = request.POST.get('ip')
        out = command.remote(ip, cmd, capture = True, timeout = 10)
        ''' for testing ajax
        file_object = open('thefile.txt', 'w')
        all_the_text = [cmd, ip]
        file_object.write(str(all_the_text))
        file_object.close( )
        '''
        return '<pre>SUCCEEDED : %s</pre><pre>RETURN CODE: %s</pre><pre>COMMAND EXECUTED IS: %s</pre><pre>%s</pre>' % (out.succeeded, out.return_code, cmd, out.stdout)


@app.route('/operation')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')

    while True:
        try:
            message = wsock.receive()
            '''
            >>> message = u'bat_bt_service_proxy&192.168.1.78'
            >>> message.encode("utf-8").split('&')
            ['bat_bt_service_proxy', '192.168.1.78']
            >>> message.encode("utf-8").split('&')[0]
            'bat_bt_service_proxy'
            '''
            cmd = cmd_from_form(message.encode("utf-8").split('&')[0])
            ip = message.encode("utf-8").split('&')[1]
            wsock.send("<pre>COMMAND EXECUTED IS: %s</pre><br /><pre>SCRIPT LOCATE ON: %s</pre>" % (cmd, ip))
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE )
            while True:
                out = p.stdout.readline()
                # Popen.poll(): 检查子进程是否结束。并设置和返回.returncode属性。
                if out == '' and p.poll() != None:
                    break
                if out != '':
                    #out = outstr + out + "\n"
                    #sys.stdout.write(out)
                    # 不使用textarea接收callback
                    wsock.send("<pre>%s</pre>" % out)
                    # 使用textarea接收callback
                    #wsock.send(out)
                    sys.stdout.flush()
            wsock.send("All operations have done!")
        except WebSocketError:
            break
if __name__ == '__main__':
    #run(host='0.0.0.0', port=8080, reloader=True, debug=True)
    from gevent.pywsgi import WSGIServer
    from geventwebsocket import WebSocketHandler, WebSocketError
    server = WSGIServer(("0.0.0.0", 8080), app,handler_class=WebSocketHandler)
    server.serve_forever()
