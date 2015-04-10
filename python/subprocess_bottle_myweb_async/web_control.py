# -*- coding: utf-8 -*-
# import subprocess
import command
from bottle import route, run, request, response, static_file

@route("/")
def index():
    return static_file('index.html',root='./static')

@route('/<filepath:path>')
def static(filepath):
    return static_file(filepath,root='./static')

@route('/cgi-bin/EricLogin.cgi')
def eric_login():
    device = request.query.device
    print '\tlogin > ' + device
    with open(device, 'w') as f:
        f.write('Eric\rHo\r')
    with open('./static/index.html', 'r') as f:
        response.content_type = 'text/html'
        return f.read() + '\nlogged in to ' + device

@route('/cgi-bin/cmd.sh')
def eric_command():
    device = request.query.device
    command = request.query.command
    print '\t' + command + ' > ' + device
    with open(device, 'w') as f:
        f.write(command + '\r')
    with open('./static/index.html', 'r') as f:
        response.content_type = 'text/html'
        return f.read() + '\n' + command + 'ing command sent to ' + device

@route('/uptime')
def run_uptime():
    return '<pre>%s</pre>' % subprocess.Popen(["busybox", "uptime"], stdout=subprocess.PIPE).communicate()[0]
    
@route('/ps')
def run_ps():
    return '<pre>%s</pre>'%subprocess.Popen(["ps"],stdout=subprocess.PIPE).communicate()[0]


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, reloader=True, debug=True)
