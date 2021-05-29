from flask import Flask,render_template,request,redirect,url_for
import pymysql
 

app = Flask(__name__)
conn = pymysql.connect(host="localhost",user="root",password="",database="rocktypedb")


@app.route("/")
def ShowData():
    with conn:
        cur=conn.cursor()
        cur.execute('SELECT * FROM rocktypedb')
        rows=cur.fetchall()
    return render_template('rocks.html', datas = rows)



@app.route("/rock")
def ShowForm():
    return render_template('addrocks.html')



@app.route("/delete/<string:id_data>",methods=['GET'])
def delete(id_data):
    with conn:
        cur=conn.cursor()
        cur.execute('DELETE from rocktypedb where id=%s', (id_data))
        conn.commit()
    return redirect(url_for('ShowData'))



@app.route("/insert",methods=['POST'])
def insert():
    if request.method=='POST':
        Type=request.form['Type']
        Classify=request.form['Classify']
        Name=request.form['Name'] 
        with conn.cursor() as cursor:
            sql="Insert into 'rocktypedb' ('Type','Classify','Name') values(%s,%s,%s)"
            cursor.execute(sql,('Type','Classify','Name'))
            conn.commit()
        return redirect(url_for('ShowData')) 



@app.route("/Update",methods=['POST'])
def update():
    if request.method=='POST':
        ID_update=request.form['ID']
        Type=request.form['Type']
        Classify=request.form['Classify']
        Name=request.form['Name'] 
        with conn.cursor() as cursor:
            sql="update rocktypedb set Type=%s, Classify=%s, Name=%s where ID=%s"
            cursor.execute(sql,('Type','Classify','Name','ID_update'))
            conn.commit() 
        return redirect(url_for('ShowData'))   


if __name__ == "__main__":
    app.run(debug=True)        



