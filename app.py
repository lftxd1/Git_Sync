from flask import Flask
import os
app = Flask(__name__)

import subprocess

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/PaperSystem',methods=['POST'])
def paperSystem():
    os.system('cd C:\serve\PaperSystem && git reset --hard FETCH_HEAD && git pull https://gitee.com/m_lftxd1/PaperSystem.git')
    return '更新成功'

@app.route('/CsnSystem',methods=['POST'])
def csnSysyem():
    os.system('cd /d D:\serve\csn-lab-manage-system && git reset && git pull')
    return '更新成功'

if __name__ == '__main__':
    app.run("127.0.0.1",port=3000)
