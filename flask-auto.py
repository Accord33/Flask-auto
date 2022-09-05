import sys
import os
import shutil
import json

def create():
    os.mkdir(f"{dir}/{sys.argv[2]}")
    with open(f"{dir}/{sys.argv[2]}/app.py", "w") as f:
        f.write("""

from flask import Flask, render_template, request
from config import config
from config import route
import json

app = Flask(__name__)

@app.route('/')
def main():
    html, args = route.getter('')
    return render_template(html, args=args)

@app.route('/<path:path>', methods=['POST','GET']) 
def free_path(path) :
    html, args = route.getter(path)
    return render_template(html, args=args)
    

if __name__ == '__main__':
    print('Python Flask Server')
    
    app.run(port=config.port, host=config.host, debug=config.debug)


""")

    os.mkdir(f"{dir}/{sys.argv[2]}/templates")
    with open(f"{dir}/{sys.argv[2]}/templates/main.html","w") as f:
        f.write("<h1>Hello Flask Auto Framework</h1>")
    os.mkdir(f"{dir}/{sys.argv[2]}/static")
    os.mkdir(f"{dir}/{sys.argv[2]}/static/css")
    os.mkdir(f"{dir}/{sys.argv[2]}/static/js")
    os.mkdir(f"{dir}/{sys.argv[2]}/static/img")
    os.mkdir(f"{dir}/{sys.argv[2]}/config")
    with open(f"{dir}/{sys.argv[2]}/config/config.py", "w") as f:
        f.write("""
#Server access port
port = 8000
#host name
host = 'localhost'
#debug mode default True
debug = True
""")
    with open(f"{dir}/{sys.argv[2]}/config/route.py","w") as f:
        f.write("""
from flask import render_template
import json

with open('config/ways.json', 'r') as f:
        routes = json.loads(f.read())

def getter(path):
    if path == '':
        html = f'{routes[path]}.html'
        args = None
        return html, args        
    elif path == 'home':
        html = f'{routes[path]}.html'
        args = None
        return html, args
        """)
    with open(f"{dir}/{sys.argv[2]}/config/ways.json","w") as f:
        f.write('''
{
    "":"main"
}''')
    print("Complate All")


def build():
    sys.path.append(dir)
    import FlaskFile as ff
    os.mkdir(f"{dir}/{ff.servername}")
    os.mkdir(f"{dir}/{ff.servername}/templates")
    os.mkdir(f"{dir}/{ff.servername}/static")
    os.mkdir(f"{dir}/{ff.servername}/static/css")
    os.mkdir(f"{dir}/{ff.servername}/static/js")
    os.mkdir(f"{dir}/{ff.servername}/static/img")
    os.mkdir(f"{dir}/{ff.servername}/config")

    for i in ff.html:
        shutil.copy(f"./{i}",f"{dir}/{ff.servername}/templates/")

    with open(f"{dir}/{ff.servername}/config/config.py", "w") as f:
        f.write(f"""
#Server access port
port = {ff.port}
#host name
host = '{ff.host}'
#debug mode default True
debug = {ff.debug}
""")

    with open(f"{dir}/{ff.servername}/app.py", "w") as f:
        f.write("""
from flask import Flask, render_template, request
from config import config as config


app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello Flask'

@app.route('/<path:path>') 
def free_path( path ) :
    return render_template(f'{path}.html')

if __name__ == '__main__':
    print('Python Flask Server')
    app.run(port=config.port, host=config.host, debug=config.debug)

""")
    print("Complate All")


def generate():
    path = list()
    path2 = ["templates"]
    for i in range(2,1000):
        try:
            path.append(sys.argv[i])
        except IndexError:
            break
    for j in path:
        if j != path[-1]:
            path2.append(j)
            try:
                os.mkdir("/".join(path2))
            except FileExistsError:
                continue
        else:
            path2.append(j)
            file = "/".join(path2)
            with open(f"{file}.html", "w") as f:
                f.write(f'THIS IS #{j} HTML FILE')
    path2.pop(0)
    print(path2)
    path2 = "/".join(path2)

    with open("config/ways.json", "r") as f:
        data = json.loads(f.read())
    with open("config/ways.json", "w") as f:
        data[path2] = path2
        jdumps = json.dumps(data)
        f.write(f"{jdumps}")
    with open("config/route.py","a") as f:
        f.write(f"\n    elif path == '{path2}':")
        f.write("""
        html = f'{routes[path]}.html'
        args = None
        return html, args""")


def delete():
    if input("Do you really want to delete the app?(Y/n) > ") == "Y":
        shutil.rmtree(f"{dir}/{sys.argv[2]}")
        print("Complate All")
    else:
        print("Nothing to do")


command = sys.argv[1]
dir = os.getcwd()

eval(f"{command}()")