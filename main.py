from flask import Flask, request, redirect, render_template
import cgi

app= Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def index():    
    return render_template('login.html')

@app.route("/", methods=['POST'])
def signup_validate():
    username=request.form['username']
    pwd=request.form['pwd']
    repwd=request.form['repwd']
    email=request.form['email']

    name_error = ''
    pwd_error = ''
    repwd_error = ''    
    email_error = ''

    if len(username) < 3 or len(username) > 20:    
        username = ''
        name_error = 'Username must be between 3 and 20 characters'    
    else:
        username = username

    if len(pwd) < 3 or len(pwd) > 20:
        #pwd=pwd
        pwd = ''
        pwd_error = 'Password must contain more than 3 characters, max 20'

    if len(repwd) < 3 or len(repwd) > 20:
        #repwd = repwd
        repwd=''
        repwd_error = 'Verification password must contain more than 3 characters, max 20' 
    
    if pwd != repwd:
        pwd = pwd
        repwd=''
        #repwd = repwd
        repwd_error = 'Passwords do not match'

    if len(email) > 0: 
        if len(email) < 3 or len(email) > 20:
            email = ''
            email_error = 'Not a valid email: it must contain single @, single ., and is between 3 and 20 characters long'
        else:            
            if (email.count('@') == 1 and email.count('.') == 1):      
                if ('' in email):
                    email = ''  
                    email_error='Spaces are not allowed.'    
                else:        
                    email = email 
                    email_error=''                               
            else:
                email = ''
                email_error = 'Not a valid email: it must contain single @, single ., contains no spaces and is between 3 and 20 characters long'
    else:
        email = ''

    if username == "":
        name_error = 'Enter the User Name.'
    if pwd == "":
        pwd_error = 'Enter a password between 3 and 20 characters long'
    if repwd == "":
        repwd_error = 'Re-enter the above Password.'
    
    if not name_error and not repwd_error and not pwd_error and not email_error:
        return render_template('Welcome.html', username = username)

    else:
        return render_template('login.html', repwd_error=repwd_error, name_error=name_error, pwd_error=pwd_error, 
        email_error=email_error, username=username, pwd=pwd, repwd=repwd, email=email)

app.run()    
    