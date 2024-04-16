# pip install rasa==2.0.2
# rasa run actions
# rasa run --cors "*" --enable-api
# pip install rasa-nlu==0.11.5
# greenlet==0.4.16
# pip install slackclient==1.3.1

# rasa train


from flask import Flask, render_template, request, session, url_for, redirect, jsonify,session, url_for, redirect, jsonify,send_from_directory,flash
import pymysql
from werkzeug.utils import secure_filename
import pathlib
import pandas as pd
import os
import random
import glob
import geocoder
import datetime
import nltk
import requests
import json
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import random
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
import threading
import numpy as np
from sklearn.decomposition import TruncatedSVD
lock = threading.Lock()

app = Flask(__name__)
output=[]#("message stark","hi")]
app.secret_key = 'any random string'
app.config['UPLOADED_PHOTOS_DEST'] = 'static/profile/'
app.config['UPLOADED_PHOTOS_DEST1'] = 'static/addlist/'
app.config['UPLOADED_PHOTOS_DEST2'] = 'static/addlistrevies/'
# app.config['UPLOADED_PHOTOS_DEST2'] = 'static/landdocumentfromseller/'

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
GOOGLE_MAPS_API_KEY = 'AIzaSyDwaXa3JZsFqv71812tm1k5FokRzLrX0RM'
##################################   Mail to mycitypedia user #########################################################################
#pass:ynlnfxmpwvtxolst
def sendemailtouser(usermail,ogpass):   
    fromaddr = "rizwan159753@gmail.com"
    toaddr = usermail
   
    #instance of MIMEMultipart 
    msg = MIMEMultipart() 
  
    # storing the senders email address   
    msg['From'] = fromaddr 
  
    # storing the receivers email address  
    msg['To'] = toaddr 
  
    # storing the subject  
    msg['Subject'] = " MYCITYPEDIA.COM"
  
    # string to store the body of the mail 
    body = ogpass
  
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
  
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
  
    # start TLS for security 
    s.starttls() 
  
    # Authentication 
    s.login(fromaddr, "prgesaomryelgyjk") 
  
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
  
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
  
    # terminating the session 
    s.quit()
    
##################################   Mail to mycitypedia #########################################################################


def dbConnection():
    connection = pymysql.connect(host="localhost", user="root", password="root", database="012-mycitypedia", autocommit=True)
    return connection


def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")
        
        
                
con = dbConnection()
cursor = con.cursor()


@app.route('/', methods=["GET","POST"])
def main():
    
    return render_template('home-v1.html')

@app.route('/index', methods=["GET","POST"])
def index():
    if 'uid' in session:
        USERID=session['uid']
        print(USERID)
        rec_lst = []
        try:
            rec_lst = recommend(int(USERID))
        except Exception as e:
            print(e)
            rec_lst = []
        print(rec_lst) 
        
        recomfinal_lst=[]
        for k in rec_lst:
            cursor.execute('SELECT * FROM addlisting WHERE Id = %s', (str(k)))
            dowdata = cursor.fetchone()
            if dowdata != None:
                recomfinal_lst.append(dowdata)
                
        # print(rec_lst)
        print(recomfinal_lst)   
        newrow=[]
        for row in recomfinal_lst:
            
            row=list(row)
            folders = row[13]  
            print(folders) 
             
            dir_list = os.listdir('static/addlist/'+folders)
            row.append('static/addlist/'+folders+'/'+dir_list[random.randint(0, len(dir_list)-1)])
            newrow.append(row)  
            
        print(newrow)   
    return render_template('index.html',newrow=newrow)


def get_current_location():
    g = geocoder.ip('me')
    if g.latlng:
        return g.latlng
    else:
        return None

@app.route('/adminlogin', methods=["GET","POST"])
def adminlogin():
    
    return render_template('adminlogin.html')

@app.route('/about',methods=["GET","POST"])
def about():
    return render_template('about.html')

@app.route('/contact',methods=["GET","POST"])
def contact():
    if request.method =='POST':
        print("in record")
        details = request.form
        Username = details['fname']
        email = details['email']
        massage = details['comment']
        con = dbConnection()
        cursor = con.cursor()
        sql = "INSERT INTO contact(name, email, massage) VALUES (%s, %s, %s)"
        val = (Username, email, massage)
        cursor.execute(sql, val)
        con.commit()
        msg = "contact-form Submited Successfully....." 
        return msg 
    return render_template('contact.html')


@app.route('/login', methods=["GET","POST"])
def login():
    
    return render_template('login.html')

@app.route('/register',methods=['POST','GET'])
def register():
    
    return render_template('register.html')

@app.route('/login1',methods=['POST'])
def login1():
    if request.method == 'POST':
        Email = request.form.get("email")
        Password = request.form.get("password")
        print(Password)
        con = dbConnection()
        cursor = con.cursor()
        result_count = cursor.execute('SELECT * FROM userregisters WHERE Email = %s AND Password = %s', (Email, Password))
        print(result_count)
        
        if result_count == 1:
            res = cursor.fetchone()
            print(res)
            session['user'] = res[1]
            session['uid'] = res[0]
            session['image'] = res[5]
            # Successful login logic
            # return jsonify({'message': 'Login successful', 'user_id': res[0]})
            return "success"
        else:
            # Failed login logic
            # return jsonify({'message': 'Login failed'})
            return "fail"

        con.close()
    

@app.route('/get_otp', methods=['POST'])
def get_otp():
    if request.method =='POST':
        print("in record")
        details = request.form
        usermail = details['email1']
        OTP = random.randint(1000, 9999)
        ogpass = "The MYCITYPEDIA verification tech successfully sent your OTP IS. "+ str(OTP)
        sendemailtouser(usermail,ogpass)
        return jsonify({'success': True, 'otp': OTP})

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    if request.method =='POST':
        print("in record")
        details = request.form
        otp_entered = details['otp']
        otp_backend = details['otp1']
        print(otp_entered)
        print(otp_backend)
        
    # otp_entered = request.form.get('otp')
    # otp_backend = request.form.get('otp_backend') 
    
    
        if otp_entered == otp_backend:
            return jsonify({'success': True})
        else:
            return jsonify({'success': False})
        


@app.route('/register1',methods=['POST'])
def register1():
    
    print("ouy")
    if request.method =='POST':
        print("in record")
        details = request.form
        Username = details['user_name']
        email = details['email1']
        Mobile = details['mobile'] 
        Password = details['user_password']
        Address = details['Address'] 
        Pancard = details['Pancard']
        uploadimg = request.files['file']
        con = dbConnection()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM userregisters WHERE Email = %s', (email))
        res = cursor.fetchone()
        # var password = "Abcdefg1";
        
        filename_secure = secure_filename(uploadimg.filename)
        uploadimg.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename_secure))
        filenamepath = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename_secure)
        
        if not res:
            # OTP = random.randint(1000, 9999)
            # usermail = email
            # ogpass = "The MYCITYPEDIA verification tech successfully sent your OTP IS. "+ OTP
            # sendemailtouser(usermail,ogpass)
            
            sql = "INSERT INTO userregisters(Username, Email, Mobile, Password, Profile_Img, Address, Pancard) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (Username, email, Mobile, Password, filenamepath,Address,Pancard)
            cursor.execute(sql, val)
            con.commit()
        
            message = "Registration USER successfully added by USER side. Username: " + Username
            # return redirect(url_for('index'))
            return jsonify({'message': message})
            message = "Already available"
            
        else:
            message = "Registration USER not  added by USER side. Username: " + Username
            dbClose()
            # return redirect(url_for('index'))
            return jsonify({'message': message})
        
              
@app.route('/SessionHandle1',methods=['POST','GET'])
def SessionHandle1():
    if request.method == "POST":
        details = request.form
        name = details['name']
        session['user1'] = name
        strofuser = name
        print (strofuser.encode('utf8', 'ignore'))
        return strofuser      


@app.route('/chatbot')
def chatbot():
    img=session['image']
    
    return render_template('chatbot.html',img=img)



@app.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')


@app.route('/profile',methods=['POST','GET'])
def profile():
    username=session['user']
    img=session['image']
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM userregisters WHERE Username = %s and Profile_Img = %s', (username,img))
    data1 = cursor.fetchone()
    # print(data1)
    data2 = list(data1)
    # print(data2)
    
    cursor.execute('SELECT * FROM addlisting WHERE User = %s', (username))
    data = cursor.fetchall()
    print(data)
    
    newrow=[]
    for row in data:
        row=list(row)
        folders = row[13]  
        
        dir_list = os.listdir('static/addlist/'+folders)
        row.append('static/addlist/'+folders+'/'+dir_list[random.randint(0, len(dir_list)-1)])
        newrow.append(row)
    print(newrow)
  

    return render_template('profile.html',username=username,img=img,data2=data2,newrow=newrow)


@app.route('/addlisting',methods=['POST','GET'])
def addlisting():
 
    return render_template('add-listing.html')




@app.route('/addlistingdata',methods=['POST'])
def addlistingdata():
    if request.method =='POST':
        print("in record")
        username=session['user']
        details = request.form
        Title = details['Title']
        categorySelect = details['categorySelect']
        Contact = details['Contact'] 
        Email = details['Email']
        Description = details['Description']
        City = details['City']
        Current_Address = details['Current_Address']
        State = details['State']
        Zip = details['Zip']
        Facebook = details['Facebook']
        Pinterest = details['Pinterest']
        Twitter = details['Twitter']
       
        openingTimeSelect = details['openingTimeSelect']
        closing = details['closing']
        random_number = random.randint(1000, 9999)

        print(random_number)
        
      
        uploaded_files =request.files.getlist('upload_imgs[]')
        print("------------------------------")
        print(uploaded_files)        
        print("------------------------------")
        for uploaded_file in uploaded_files:
            
            filename_secure = secure_filename(uploaded_file.filename)
            print(filename_secure)
            upload_folder = os.path.join(app.config['UPLOADED_PHOTOS_DEST1'], str(random_number))
            pathlib.Path(upload_folder).mkdir(exist_ok=True)
            uploaded_file.save(os.path.join(upload_folder, filename_secure))
        
        print(Title) 
        print(categorySelect)
      
        con = dbConnection()
        cursor = con.cursor()
        sql = "INSERT INTO addlisting(Title, categorySelect, Contact, Email, Description, City, Current_Address, State, Zip, Facebook, Pinterest, Twitter, random_number, openingTimeSelect, closing, User) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (Title, categorySelect, Contact, Email, Description, City, Current_Address, State, Zip, Facebook, Pinterest, Twitter, random_number, openingTimeSelect, closing, username)
        cursor.execute(sql, val)
        con.commit()
     
        return "Success"



@app.route('/alladdlist',methods=['POST','GET'])
def alladdlist():
    if 'user1' in session:
    
        con = dbConnection()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM addlisting')
        data = cursor.fetchall()
        # print(data)
        newrow=[]
        for row in data:
            row=list(row)
            folders = row[13]  
            
            dir_list = os.listdir('static/addlist/'+folders)
            row.append('static/addlist/'+folders+'/'+dir_list[random.randint(0, len(dir_list)-1)])
            newrow.append(row)
        # print(newrow)
    
        return render_template('alladdlist.html',newrow=newrow)


@app.route('/userlistfull',methods=['POST','GET'])
def userlistfull():
    username=session['user']
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM addlisting WHERE User = %s', (username))
    data = cursor.fetchall()
    
    newrow=[]
    for row in data:
        row=list(row)
        folders = row[13]  
        
        dir_list = os.listdir('static/addlist/'+folders)
        row.append('static/addlist/'+folders+'/'+dir_list[random.randint(0, len(dir_list)-1)])
        newrow.append(row)
    print(newrow)
   
    
    return render_template('userlistfull.html',newrow=newrow)

@app.route('/logout')
def logout():
    session.pop('uid')
    return redirect(url_for('main'))

@app.route('/logout1')
def logout1():
   session.pop('user1')
   return redirect(url_for('main'))
   



@app.route('/acept/<Id>',methods=['POST','GET'])
def acept(Id):
    print(Id)
    print()
    
    # new_value = "ACCEPT"
    sql1 = "UPDATE addlisting SET status = 'ACCEPT' WHERE Id = %s"
    val1 = (Id,)  # Make sure it's a tuple
    lock.acquire()    
    cursor = con.cursor()
    try:
        cursor.execute(sql1, val1)
        con.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        lock.release()
    
    return redirect(url_for('alladdlist'))


@app.route('/reject/<int:Id>', methods=['POST', 'GET'])
def reject(Id):
    sql1 = "DELETE FROM addlisting WHERE Id = %s"
    val1 = (Id,)  # Notice the comma, this creates a tuple
    lock.acquire() 
    cursor = con.cursor()
    cursor.execute(sql1, val1)
    con.commit()
    con.close()  # Move this to a finally block to ensure it's always executed
    lock.release()
    return redirect(url_for('alladdlist'))







@app.route('/Listings/<name>',methods=['POST','GET'])
def Listings(name):
    # print(name)
    status="ACCEPT"
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM addlisting WHERE categorySelect = %s and status = %s', (name,status))
    data = cursor.fetchall()
    newrow=[]
    for row in data:
        row=list(row)
        folders =row[13] 
        
        dir_list = os.listdir('static/addlist/'+folders)
        row.append('static/addlist/'+folders+'/'+dir_list[random.randint(0, len(dir_list)-1)])
        newrow.append(row)
    # print(newrow)
  
    return render_template('Listings.html',newrow=newrow)

@app.route('/show/<listnameId>',methods=['POST','GET'])
def show(listnameId):
    print(listnameId)
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM addlisting WHERE Id = %s ', (listnameId))
    data = cursor.fetchone()
    newrow=[]
    row=list(data)
    BUSSNESS = row[1]  
    folders = row[13] 
    dir_list = os.listdir('static/addlist/'+folders)
    # print(dir_list)
    
    path = 'static/addlist/' + folders + '/'
    updated_list = [path + filename for filename in dir_list]
    print("updated_list")
    # print(updated_list)
    row.append('static/addlist/'+folders+'/'+dir_list[random.randint(0, len(dir_list)-1)])
    print("---------------------------------------------")
    newrow.append(row)
    # print(newrow)
    cursor.execute('SELECT * FROM review WHERE BUSSNESS = %s and IDBUSS = %s', (BUSSNESS,listnameId))
    data1 = cursor.fetchall()
    # print(data1)
    newrow2=[]
    for row1 in data1:
        row1=list(row1)
        folders1 = row1[4] 
        print(folders1)
        dir_list1 = os.listdir('static/addlistrevies/'+folders1)
        row1.append('static/addlistrevies/'+folders1+'/'+dir_list1[random.randint(0, len(dir_list1)-1)])
        newrow2.append(row1)
    print(newrow2)
    return render_template('show.html',newrow=newrow,updated_list=updated_list,newrow2=newrow2)
################################################################################################################################
@app.route('/Listings1/<name>',methods=['POST','GET'])
def Listings1(name):
    print(name)
    status="ACCEPT"
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM addlisting WHERE categorySelect = %s and status = %s', (name,status))
    data = cursor.fetchall()
    newrow=[]
    for row in data:
        row=list(row)
        folders =row[13]  
        
        dir_list = os.listdir('static/addlist/'+folders)
        row.append('static/addlist/'+folders+'/'+dir_list[random.randint(0, len(dir_list)-1)])
        newrow.append(row)
    print(newrow)
    
  
  
    
    return render_template('Listings1.html',newrow=newrow)

@app.route('/show1/<listnameId>',methods=['POST','GET'])
def show1(listnameId):
    print(listnameId)
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM addlisting WHERE Id = %s ', (listnameId))
    data = cursor.fetchone()
    newrow=[]
    row=list(data)
    BUSSNESS = row[1]  
    folders = row[13]   
    dir_list = os.listdir('static/addlist/'+folders)
    # print(dir_list)
    
    path = 'static/addlist/' + folders + '/'
    updated_list = [path + filename for filename in dir_list]
    # print("updated_list")
    # print(updated_list)
    
    
    
    row.append('static/addlist/'+folders+'/'+dir_list[random.randint(0, len(dir_list)-1)])
    print("---------------------------------------------")
    newrow.append(row)
    
    cursor.execute('SELECT * FROM review WHERE BUSSNESS = %s and IDBUSS = %s', (BUSSNESS,listnameId))
    data1 = cursor.fetchall()
    print(data1)
    newrow2=[]
    for row1 in data1:
        row1=list(row1)
        folders1 = row1[4]  
        dir_list1 = os.listdir('static/addlistrevies/'+folders1)
        row1.append('static/addlistrevies/'+folders1+'/'+dir_list1[random.randint(0, len(dir_list1)-1)])
        newrow2.append(row1)
    print(newrow2)
    
    return render_template('show1.html',newrow=newrow,updated_list=updated_list,newrow2=newrow2)

####################################################################CHATBOT############################################################
@app.route('/getRequest', methods=["GET","POST"])
def getRequest():
    print("GET")
    if request.method =='POST':
        print("Post")
        userText = request.form['userMessage']
        print(userText)
        data = json.dumps({"sender": "Rasa","message": userText})
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
        res = res.json()
        print()
        print("Output")
        print(res)
        print()
        val = res[0]['text']
        output.append(val)
        print()
        print("val")
        print(val)
        print()
        responses = val
        
        return responses
  



####################################################################feedback users############################################################
@app.route('/Review', methods=["POST"])
def Review():
    print("GET")
    USERID=session['uid']
    username=session['user']
    img=session['image']
    if request.method =='POST':
        print("Post")
        rating = request.form.get('rating')
        comment = request.form.get('comment')
        BUSSNESS = request.form.get('BUSSNESS')
        IDBUSS = request.form.get('IDNUSS')
        
        upload_imgs =request.files.getlist('upload_imgs[]')
        random_number = random.randint(1000, 9999)

        print(random_number)
        print(rating,comment,upload_imgs)
        
        for uploaded_file in upload_imgs:
            print(uploaded_file)
            filename_secure = secure_filename(uploaded_file.filename)
            print(filename_secure)
            upload_folder = os.path.join(app.config['UPLOADED_PHOTOS_DEST2'], str(random_number))
            pathlib.Path(upload_folder).mkdir(exist_ok=True)
            uploaded_file.save(os.path.join(upload_folder, filename_secure))
        
        con = dbConnection()
        cursor = con.cursor()
        sql = "INSERT INTO review(username, comments, rating, randomno, userimage, BUSSNESS ,IDBUSS, USERID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (username, comment, rating, random_number, img, BUSSNESS ,IDBUSS, USERID)
        cursor.execute(sql, val)
        print("Query submitted...")
        con.commit()
        
        msg = "Review Submited Successfuly....." 
        return msg
            
      
#################################################recommended business###############################################################################
def recommend(USERID):
    conn = dbConnection()
    cur = conn.cursor()
    sql="SELECT USERID,IDBUSS,rating from review"
    cur.execute(sql)
    table_rows = cur.fetchall()
    print(table_rows)
    df = pd.DataFrame(table_rows,columns=['USERID','IDBUSS','rating'])
    #df.to_csv("Reco.csv")
    print()
    print("printign np.unique(df['IDBUSS']")
    print(np.unique(df['IDBUSS']))
    a=len(np.unique(df['IDBUSS']))

    print()
    print("printing a")
    print(a)
    print()
    df = df.astype({"USERID": int,"IDBUSS": int,"rating": int })
    ratings_utility_matrix=df.pivot_table(values='rating', index='USERID', columns='IDBUSS', fill_value=0)
    X = ratings_utility_matrix.T
    print("---------------------------")
    print(X)
    print("--------------------")
    import sklearn
    from sklearn.decomposition import TruncatedSVD
    SVD = TruncatedSVD(n_components=int(2))
    decomposed_matrix = SVD.fit_transform(X)
    correlation_matrix = np.corrcoef(decomposed_matrix)
    i = USERID
    product_names = list(X.index)
    product_ID = product_names.index(i)
    correlation_product_ID = correlation_matrix[product_ID]
    Recommend = list(X.index[correlation_product_ID > 0.70])
#     Recommend.remove(i) 
    return Recommend[0:5]

################################################################################################################################
if __name__ == '__main__':
    app.run(debug=True)
    # app.run('0.0.0.0')