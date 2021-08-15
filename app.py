from flask import Flask, request, render_template, redirect, url_for, session
from functools import wraps
import random , gc , math , pymysql , smtplib , ssl
from datetime import timedelta, date

def database():
    db = pymysql.connect(host='vacation-planner.mysql.database.azure.com', user='sundasnoreen@vacation-planner',
                         password='Sundas1234', database='fastlink')
    return db

app = Flask(__name__)
app.secret_key = 'sundas'

@app.before_request
def Session_Timeout():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=4)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = ''
    conn=database()
    cursor=conn.cursor()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            sql = 'SELECT * FROM `admins`'
            cursor.execute(sql)
            read = cursor.fetchall()
            for row in read:
                if username != row[2] or password != row[3]:
                    error = 'Invalid Credentials. Please Try Again.'
                else:
                    session['logged in'] = True
                    session['category'] = row[0]
                    session['name'] = row[1]
                    session['password'] = row[3]
                    session['user'] = row[2]
                    session['email'] = row[4]
                    return redirect(url_for('Home'))
        except:
            error = "Sorry, We couldn't Log you In, Please Try Again."
        finally:
            conn.close()
    return render_template('login.html', error=error)

@app.route('/home_page')
def Home():
    return render_template('index.html',user=session['name'])

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return decorated_function

@app.route('/logout')
@login_required
def logout():
    session.clear()
    gc.collect()
    return redirect(url_for('login'))

@app.route('/employees_list')
def Employee():
    rows = ''
    conn = database()
    cursor = conn.cursor()
    sql = 'SELECT * FROM `employee` ORDER BY `Name`'
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    return render_template('Employee.html',val="Employees",user=session['name'],rows=rows)

@app.route('/update_Employees')
def Up_Employee():
    rows = ''
    conn = database()
    cursor = conn.cursor()
    sql = 'SELECT * FROM `employee` ORDER BY `Name`'
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    return render_template('Update.html',user=session['name'],rows=rows)

@app.route('/add_Employees', methods=['GET', 'POST'])
def Add_Employee():
    conn = database()
    cursor = conn.cursor()
    error=''
    if request.method == 'POST':
        try:
            Name = request.form['name']
            CNIC = request.form['cnic']
            Num = request.form['no']
            Address = request.form['address']
            sql='INSERT INTO `employee`(`Name`, `CNIC`, `Phone`, `Address`) VALUES (%s,%s,%s,%s)'
            cursor.execute(sql,(Name,CNIC,Num,Address))
            conn.commit()
            error="Added Successfully."
        except:
            error = "There seems to be some Problem , Please Try Again."
        finally:
            conn.close()
    return render_template('AddEmployee.html',val="Employee",user=session['name'],error=error)

@app.route('/update_<id>_<name>_<cnic>_<num>_<ad>', methods=['GET', 'POST'])
def Update_Employee(id,name,cnic,num,ad):
    conn = database()
    cursor = conn.cursor()
    error=''
    if request.method == 'POST':
        try:
            Name = request.form['name']
            CNIC = request.form['cnic']
            Num = request.form['no']
            Address = request.form['address']
            sql='UPDATE `employee`SET `Name`=%s,`CNIC`=%s,`Phone`=%s,`Address`=%s WHERE `ID`=%s'
            cursor.execute(sql,(Name,CNIC,Num,Address,id))
            conn.commit()
            error="Data Updated."
        except:
            error = "There seems to be some Problem , Please Try Again."
        finally:
            conn.close()
    return render_template('UpdateEmployee.html',val="Employee",user=session['name'],name=name,cnic=cnic,num=num,ad=ad,error=error)

@app.route('/clients_list')
def Client():
    rows = ''
    conn = database()
    cursor = conn.cursor()
    sql = 'SELECT * FROM `client` ORDER BY `Name`'
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    return render_template('Employee.html',val="Clients",user=session['name'],rows=rows)

@app.route('/update_Clients')
def Up_Client():
    rows = ''
    conn = database()
    cursor = conn.cursor()
    sql = 'SELECT * FROM `client` ORDER BY `Name`'
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    return render_template('UpdateCl.html',user=session['name'],rows=rows)

@app.route('/add_Clients', methods=['GET', 'POST'])
def Add_Client():
    conn = database()
    cursor = conn.cursor()
    error=''
    if request.method == 'POST':
        try:
            Name = request.form['name']
            CNIC = request.form['cnic']
            Num = request.form['no']
            Address = request.form['address']
            sql='INSERT INTO `client`(`Name`, `CNIC`, `Phone`, `Address`) VALUES (%s,%s,%s,%s)'
            cursor.execute(sql,(Name,CNIC,Num,Address))
            conn.commit()
            error="Added Successfully."
        except:
            error = "There seems to be some Problem , Please Try Again."
        finally:
            conn.close()
    return render_template('AddEmployee.html',val="Client",user=session['name'],error=error)

@app.route('/update_client_<id>_<name>_<cnic>_<num>_<ad>', methods=['GET', 'POST'])
def Update_Client(id,name,cnic,num,ad):
    conn = database()
    cursor = conn.cursor()
    error=''
    if request.method == 'POST':
        try:
            Name = request.form['name']
            CNIC = request.form['cnic']
            Num = request.form['no']
            Address = request.form['address']
            sql='UPDATE `client`SET `Name`=%s,`CNIC`=%s,`Phone`=%s,`Address`=%s WHERE `ID`=%s'
            cursor.execute(sql,(Name,CNIC,Num,Address,id))
            conn.commit()
            error="Data Updated."
        except:
            error = "There seems to be some Problem , Please Try Again."
        finally:
            conn.close()
    return render_template('UpdateEmployee.html',val="Client",user=session['name'],name=name,cnic=cnic,num=num,ad=ad,error=error)

app.debug=True
app.run(host="0.0.0.0")