from flask import Flask,render_template,request,redirect
import json

app = Flask(__name__)

with open('data/salary.json', 'r', encoding="utf-8") as f:
    data = f.read()


salary_list = json.loads(data)

@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route('/login',methods=['GET','POST'])
def hello_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == '123456':
            return render_template('admin.html',salary_list=salary_list)

@app.route('/delete/<name>')
def hello_delete(name):
    for sal in salary_list:
        if sal['name'] == name:
            salary_list.remove(sal)
    with open('data/salary.json', 'w', encoding="utf-8") as f:
        f.write(json.dumps(salary_list))
    return render_template("admin.html",salary_list=salary_list)

@app.route('/change/<name>')
def hello_change(name):
    for sal in salary_list:
        if sal['name'] == name:
            return render_template('change.html',sal=sal)

@app.route('/changed/<name>',methods=['POST'])
def hello_changed(name):
    for sal in salary_list:
        if sal['name'] == name:
            print(name)git rm --cached -r .idea
            sal['name'] = request.form['name']
            sal['department'] = request.form['department']
            sal['salary'] = request.form['salary']
            sal['position'] = request.form['position']
    with open('data/salary.json', 'w', encoding="utf-8") as f:
        f.write(json.dumps(salary_list))
    return render_template('admin.html',salary_list=salary_list)

@app.route('/add')
def hello_add():
    return render_template('add.html')

@app.route('/add2',methods=['POST'])
def hello_add2():
    name = request.form['name']
    department = request.form['department']
    position = request.form['position']
    salary = request.form['salary']
    salary_list.append({'name':name,'department':department,'position':position,'salary':salary})
    with open('data/salary.json', 'w', encoding="utf-8") as f:
        f.write(json.dumps(salary_list))

    return render_template('admin.html',salary_list=salary_list)


if __name__ == '__main__':
    app.run()
