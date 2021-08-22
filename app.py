from flask import Flask, request, render_template, redirect, url_for, session
from functools import wraps
import  gc , pymysql
from datetime import timedelta, date


def database():
    db = pymysql.connect(host='vacation-planner.mysql.database.azure.com', user='sundasnoreen@vacation-planner',
                         password='Sundas1234', database='fastlink')
    return db

app = Flask(__name__)
app.secret_key = 'FastLink'

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
@login_required
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
@login_required
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
@login_required
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
@login_required
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
@login_required
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
@login_required
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
@login_required
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
@login_required
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

@app.route('/new_work', methods=['GET', 'POST'])
@login_required
def NewWork():
    rows = ''
    error=''
    d1 = date.today()
    conn = database()
    cursor = conn.cursor()
    sql = 'SELECT * FROM `client` ORDER BY `Name`'
    sql1 = 'SELECT * FROM `employee` ORDER BY `Name`'
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.execute(sql1)
    cols = cursor.fetchall()
    if request.method == 'POST':
        try:
            Client = request.form['client']
            Employee = request.form['employee']
            Date = request.form['date']
            Store = request.form['store']
            Pur = request.form['pur']
            Amount = request.form['amount']
            Bill = request.form['cli']
            sql = 'INSERT INTO `work`(`Client`, `Employee`, `Store`, `Purchased`, `Amount`, `Bill`, `Date`) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (Client,Employee,Store,Pur,Amount,Bill,Date))
            conn.commit()
            sql1='SELECT`Balance` FROM `employee` WHERE `ID`=%s'
            cursor.execute(sql1,(Employee))
            value=cursor.fetchall()
            for a in value:
                emp_am=a[0]
            emp_am=int(emp_am)+int(Amount)
            sql2 = 'UPDATE `employee` SET `Balance`=%s WHERE `ID`=%s'
            cursor.execute(sql2, (emp_am,Employee))
            conn.commit()
            sql3= 'SELECT`Balance` FROM `client` WHERE `ID`=%s'
            cursor.execute(sql3, (Client))
            values = cursor.fetchall()
            for a in values:
                cl_am = a[0]
            cl_am = int(cl_am) + int(Bill)
            sql4 = 'UPDATE `client` SET `Balance`=%s WHERE `ID`=%s'
            cursor.execute(sql4, (cl_am, Client))
            conn.commit()
            error = "Work Executed Successfully."
        except Exception as e:
            print(e)
            error = "There seems to be some Problem , Please Try Again."
        finally:
            conn.close()
    return render_template('NewWork.html',user=session['name'],rows=rows,cols=cols,d1=d1,error=error)

@app.route('/monthly_<month>_<mon>')
@login_required
def Details(month,mon):
    Store=[]
    Sum=0
    Pur=0
    Purchased=[]
    Amount = []
    Bill = []
    Date=[]
    Empl=[]
    Employee=[]
    Client=[]
    rows = ''
    conn = database()
    cursor = conn.cursor()
    sql = 'SELECT * FROM `work` ORDER BY `Date` DESC'
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for i in rows:
            a = str(i[7])
            year, mo, date1 = a.split('-')
            m=year+"-"+mo
            if m==month:
                Store.append(i[3])
                Purchased.append(i[4])
                Amount.append(i[5])
                Bill.append(i[6])
                Date.append(i[7])
                sql1 = 'SELECT `Name` FROM `employee` WHERE `ID`=%s'
                cursor.execute(sql1, (i[2]))
                val = cursor.fetchall()
                for a in val:
                    Employee.append(a[0])
                sql2 = 'SELECT `Name` FROM `client` WHERE `ID`=%s'
                cursor.execute(sql2, (i[1]))
                val2 = cursor.fetchall()
                for a in val2:
                    Client.append(a[0])
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    for i in Bill:
        Sum=Sum+i
    for i in Amount:
        Pur=Pur+i
    values=zip(Employee,Client,Store,Purchased,Amount,Bill,Date)
    return render_template('WorkHistory.html',mon=mon,Pur=Pur,user=session['name'],rows=values,Sum=Sum)

@app.route('/employee_balance')
@login_required
def Employee_Balance():
    rows = ''
    conn = database()
    cursor = conn.cursor()
    sql='SELECT * FROM `employee` ORDER BY `Name` DESC'
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    return render_template('Employee_Balance.html',user=session['name'],rows=rows)

@app.route('/pay_emp_<id>_<bal>_<name>', methods=['GET', 'POST'])
@login_required
def Pay_Employee(id,bal,name):
    conn = database()
    cursor = conn.cursor()
    error=''
    left=0
    if request.method == 'POST':
        try:
            Pending=bal
            Paying = request.form['paying']
            if int(Paying)>int(Pending):
                error = "You are paying more than the Pending Amount."
            else:
                left = int(Pending)-int(Paying)
                sql2 = 'UPDATE `employee` SET `Balance`=%s WHERE `ID`=%s'
                cursor.execute(sql2, (left, id))
                conn.commit()
                error = "Balance Updated. Pending Amount Now is " + str(left) + " PKR."

        except:
            error = "There seems to be some Problem , Please Try Again."
        finally:
            conn.close()
    return render_template('Pay_Emp.html',val="Employee's",user=session['name'],bal=bal,name=name,error=error)

@app.route('/client_balance')
@login_required
def Client_Balance():
    rows = ''
    conn = database()
    cursor = conn.cursor()
    sql='SELECT * FROM `client` ORDER BY `Name` DESC'
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    return render_template('Client_Balance.html',user=session['name'],rows=rows)

@app.route('/pay_cli_<id>_<bal>_<name>', methods=['GET', 'POST'])
@login_required
def Pay_Client(id,bal,name):
    conn = database()
    cursor = conn.cursor()
    error=''
    left=0
    if request.method == 'POST':
        try:
            Pending=bal
            Paying = request.form['paying']
            if int(Paying)>int(Pending):
                error = "Client is paying more than the Pending Amount."
            else:
                left = int(Pending)-int(Paying)
                sql2 = 'UPDATE `client` SET `Balance`=%s WHERE `ID`=%s'
                cursor.execute(sql2, (left, id))
                conn.commit()
                error = "Balance Updated. Pending Amount Now is " + str(left) + " PKR."

        except:
            error = "There seems to be some Problem , Please Try Again."
        finally:
            conn.close()
    return render_template('Pay_Emp.html',val="Client's",user=session['name'],bal=bal,name=name,error=error)

@app.route('/Employees_<id>_<name>')
@login_required
def ID_Em(id,name):
    Store = []
    Purchased = []
    Amount = []
    Bill = []
    Date = []
    Empl = []
    Client = []
    rows=''
    error=''
    conn = database()
    cursor = conn.cursor()
    try:
        sql = 'SELECT * FROM `work` WHERE `Employee`=%s ORDER BY `Date` DESC'
        cursor.execute(sql,(id))
        rows = cursor.fetchall()
        for i in rows:
            Store.append(i[3])
            Purchased.append(i[4])
            Amount.append(i[5])
            Bill.append(i[6])
            Date.append(i[7])
            sql1 = 'SELECT `Name` FROM `client` WHERE `ID`=%s'
            cursor.execute(sql1, (i[1]))
            val = cursor.fetchall()
            for a in val:
                Client.append(a[0])
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    info = zip(Client, Store, Purchased, Amount, Bill, Date)
    return render_template('Single.html',Name=name,val="Client",user=session['name'],rows=info,name=name,error=error)

@app.route('/Clients_<id>_<name>')
@login_required
def ID_Cl(id,name):
    Store = []
    Purchased = []
    Amount = []
    Bill = []
    Date = []
    Client = []
    rows=''
    error=''
    conn = database()
    cursor = conn.cursor()
    try:
        sql = 'SELECT * FROM `work` WHERE `Client`=%s ORDER BY `Date` DESC'
        cursor.execute(sql,(id))
        rows = cursor.fetchall()
        for i in rows:
            Store.append(i[3])
            Purchased.append(i[4])
            Amount.append(i[5])
            Bill.append(i[6])
            Date.append(i[7])
            sql1 = 'SELECT `Name` FROM `employee` WHERE `ID`=%s'
            cursor.execute(sql1, (i[2]))
            val = cursor.fetchall()
            for a in val:
                Client.append(a[0])
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    info = zip(Client, Store, Purchased, Amount, Bill, Date)
    return render_template('Single.html',Name=name,val="Employee",user=session['name'],rows=info,name=name,error=error)

@app.route('/work_details_monthly',methods=['GET', 'POST'])
@login_required
def History():
    Store=[]
    Values=[]
    mon=''
    rows = ''
    conn = database()
    cursor = conn.cursor()
    sql='SELECT * FROM `work` ORDER BY `Date` DESC'
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for i in rows:
            a=str(i[7])
            year,mo,date1=a.split('-')
            if mo=='01':
                month="January"
            elif mo=='02':
                month="February"
            elif mo=='03':
                month="March"
            elif mo=='04':
                month="April"
            elif mo=='05':
                month="May"
            elif mo == '06':
                month = "June"
            elif mo == '07':
                month = "July"
            elif mo == '08':
                month = "August"
            elif mo == '09':
                month = "September"
            elif mo == '10':
                month = "October"
            elif mo == '11':
                month = "November"
            else:
                month="December"
            vals=month+" "+year
            if vals in Store:
                pass
            else:
                Store.append(vals)
                Values.append(year+"-"+mo)
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    info=zip(Store,Values)
    if request.method=='POST':
        months=request.form['month']
        for Values,Store in info:
            print(Values,Store)
            if Store==months:
                print(Values+Store)
                mon=Values
            print("He"+mon)
        return redirect(url_for('Details',month=months,mon=mon))
    return render_template('Select_Month.html',user=session['name'],rows=info)

@app.route('/work_details_daily',methods=['GET', 'POST'])
@login_required
def Daily():
    Store=[]
    Values=[]
    mon=''
    rows = ''
    conn = database()
    cursor = conn.cursor()
    sql='SELECT * FROM `work` ORDER BY `Date` DESC'
    sql1 = 'SELECT * FROM `work` ORDER BY `Date` ASC'
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            d1=row[7]
            break
        cursor.execute(sql1)
        cols = cursor.fetchall()
        for col in cols:
            d2 = col[7]
            break
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    if request.method=='POST':
        da=request.form['date']
        return redirect(url_for('Date_Wise',da=da))
    return render_template('Daily.html',user=session['name'],d1=d1,d2=d2)

@app.route('/monthly_<da>')
@login_required
def Date_Wise(da):
    Store=[]
    Sum=0
    Pur=0
    Purchased=[]
    Amount = []
    Bill = []
    Date=[]
    Empl=[]
    Employee=[]
    Client=[]
    rows = ''
    conn = database()
    cursor = conn.cursor()
    sql = 'SELECT * FROM `work` WHERE `Date`=%s'
    try:
        cursor.execute(sql,(da))
        rows = cursor.fetchall()
        for i in rows:
            Store.append(i[3])
            Purchased.append(i[4])
            Amount.append(i[5])
            Bill.append(i[6])
            Date.append(i[7])
            sql1 = 'SELECT `Name` FROM `employee` WHERE `ID`=%s'
            cursor.execute(sql1, (i[2]))
            val = cursor.fetchall()
            for a in val:
                Employee.append(a[0])
            sql2 = 'SELECT `Name` FROM `client` WHERE `ID`=%s'
            cursor.execute(sql2, (i[1]))
            val2 = cursor.fetchall()
            for a in val2:
                Client.append(a[0])
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    for i in Bill:
        Sum=Sum+i
    for i in Amount:
        Pur=Pur+i
    values=zip(Employee,Client,Store,Purchased,Amount,Bill,Date)
    return render_template('WorkHistory.html',mon=da,Pur=Pur,user=session['name'],rows=values,Sum=Sum)

@app.route('/password', methods=['GET', 'POST'])
@login_required
def Password():
    error = ''
    username = session['user']
    Password = session['password']
    conn = database()
    cursor = conn.cursor()
    try:
        if request.method == 'POST':
            Pre = request.form['pre']
            New = request.form['new']
            repeat = request.form['repeat']
            if repeat != New:
                error = "Passwords doesn't match."
            elif Pre != Password:
                error = 'Please Enter Your Correct Current Password.'
            elif Pre == New:
                error = 'You are using your Current Password.'
            elif repeat == New and Pre == Password:
                sql = 'UPDATE `admins` SET `Password`=%s WHERE `Login`=%s'
                cursor.execute(sql, (New, username))
                conn.commit()
                return redirect(url_for('logout'))
            else:
                error = "Password couldn't be changed.Please Try Again Later."
    except:
        error = "There Seems to be some Problem, Please Try Again."
    finally:
        conn.close()
    return render_template('password.html', error=error, user=session['name'])

@app.route('/generate_monthly_bill')
@login_required
def Options_Bill():
    return render_template('Options.html')

@app.route('/update_balance')
@login_required
def Options_Balance():
    return render_template('Balance Options.html')

@app.route('/monthly_bill_client', methods=['GET', 'POST'])
@login_required
def cl_mo_bill():
    Store=[]
    Values=[]
    mon=''
    rows = ''
    conn = database()
    cursor = conn.cursor()
    sql='SELECT * FROM `work` ORDER BY `Date` DESC'
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for i in rows:
            a=str(i[7])
            year,mo,date1=a.split('-')
            if mo=='01':
                month="January"
            elif mo=='02':
                month="February"
            elif mo=='03':
                month="March"
            elif mo=='04':
                month="April"
            elif mo=='05':
                month="May"
            elif mo == '06':
                month = "June"
            elif mo == '07':
                month = "July"
            elif mo == '08':
                month = "August"
            elif mo == '09':
                month = "September"
            elif mo == '10':
                month = "October"
            elif mo == '11':
                month = "November"
            else:
                month="December"
            vals=month+" "+year
            if vals in Store:
                pass
            else:
                Store.append(vals)
                Values.append(year+"-"+mo)
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    info=zip(Store,Values)
    if request.method=='POST':
        months=request.form['month']
        return redirect(url_for('Bill_Client',month=months,mon=vals))
    return render_template('Select_Month.html',user=session['name'],rows=info)

@app.route('/client_bill_<month>_<mon>')
@login_required
def Bill_Client(month,mon):
    Amount = []
    Client=[]
    conn = database()
    cursor = conn.cursor()
    sql1 = 'SELECT * FROM `client`'
    cursor.execute(sql1)
    val = cursor.fetchall()
    try:
        for k in val:
            amount=0
            Client.append(k[1])
            sql = 'SELECT * FROM `work` WHERE `Client`=%s ORDER BY `Date` DESC'
            cursor.execute(sql,k[0])
            names = cursor.fetchall()
            for i in names:
                a = str(i[7])
                year, mo, date1 = a.split('-')
                m = year + "-" + mo
                if m == month:
                    for j in names:
                        amount=amount+j[6]
                    Amount.append(amount)
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    values=zip(Client,Amount)
    return render_template('CLient_Bill.html',na="Client",month=mon,user=session['name'],rows=values)

@app.route('/monthly_bill_employee', methods=['GET', 'POST'])
@login_required
def emp_mo_bill():
    Store=[]
    Values=[]
    mon=''
    rows = ''
    conn = database()
    cursor = conn.cursor()
    sql='SELECT * FROM `work` ORDER BY `Date` DESC'
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for i in rows:
            a=str(i[7])
            year,mo,date1=a.split('-')
            if mo=='01':
                month="January"
            elif mo=='02':
                month="February"
            elif mo=='03':
                month="March"
            elif mo=='04':
                month="April"
            elif mo=='05':
                month="May"
            elif mo == '06':
                month = "June"
            elif mo == '07':
                month = "July"
            elif mo == '08':
                month = "August"
            elif mo == '09':
                month = "September"
            elif mo == '10':
                month = "October"
            elif mo == '11':
                month = "November"
            else:
                month="December"
            vals=month+" "+year
            if vals in Store:
                pass
            else:
                Store.append(vals)
                Values.append(year+"-"+mo)
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    info=zip(Store,Values)
    if request.method=='POST':
        months=request.form['month']
        return redirect(url_for('Bill_Employee',month=months,mon=vals))
    return render_template('Select_Month.html',user=session['name'],rows=info)

@app.route('/employee_bill_<month>_<mon>')
@login_required
def Bill_Employee(month,mon):
    Amount = []
    Client=[]
    conn = database()
    cursor = conn.cursor()
    sql1 = 'SELECT * FROM `employee`'
    cursor.execute(sql1)
    val = cursor.fetchall()
    try:
        for k in val:
            amount=0
            Client.append(k[1])
            sql = 'SELECT * FROM `work` WHERE `Employee`=%s ORDER BY `Date` DESC'
            cursor.execute(sql,k[0])
            names = cursor.fetchall()
            for i in names:
                a = str(i[7])
                year, mo, date1 = a.split('-')
                m = year + "-" + mo
                if m == month:
                    for j in names:
                        amount=amount+j[6]
                    Amount.append(amount)
    except:
        error = " Unable to fetch data."
    finally:
        conn.close()
    values=zip(Client,Amount)
    return render_template('CLient_Bill.html',na="Employee",month=mon,user=session['name'],rows=values)

if __name__ == "__main__":
    app.run(debug=True)
