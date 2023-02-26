import pexpect
from flask import Flask

api = Flask(__name__)
s = 0

@api.route('/start/')
def start_log():
    global s
    s = pexpect.spawn('telnet 192.168.1.66')
    s.expect('ansible-controller login:')
    s.sendline('tester')
    s.expect('Password:')
    s.sendline('tester')
    return 'start logging...\n'

@api.route('/stop/')
def stop_log():
    global s
    s.sendcontrol(']')
    s.expect('>')
    s.sendline('quit')
    s.close()
    del s
    return "stop logging...\n"

if __name__ == "__main__":
    api.run(debug=True, host="0.0.0.0")
