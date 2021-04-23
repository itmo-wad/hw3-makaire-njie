from flask import Flask, render_template,request,send_from_directory,session,flash

app = Flask(__name__)
app.secret_key = "secret key"

#user login area
logins = {
    'admin':'pass' # username is admin and password is pass 
    }

@app.route('/', methods=['Get','POST'])

def index():
    
      if not session.get('logged_in'):
          return render_template('index.html')
      
      else:
                 
        return render_template('main.html')
        
          
@app.route('/login', methods=['GET','POST'])
def login():
    
    if request.method=='GET':
        session['logged_in'] = False
        return index() 
    
    else:
        if "email" not in request.form :
                found=0
                for k,v in logins.items():
                    if request.form['username'] == k:
                        if request.form['password'] == v:
                            session['logged_in'] = True
                            found=1
                            break
                if found ==0 :
                    flash('Wrong Username or Password!')
                return index()    
        else:
             username = request.form.get('username')
             password = request.form.get('password')
             found = 0
             for k,v in logins.items():
                 if username == k :
                     flash('Username aleady exists!')
                     session['logged_in'] = False
                     found = 1
                     return do_reg()
             if found == 0 :
                logins.update( {username : password} )
                session['logged_in'] = True
                return index()
   
@app.route('/static/<image_name>')
def index2(image_name):
       return send_from_directory('static/images',image_name)

@app.route('/static/<path:path>')
def index3(path):
     return app.send_static_file(path)
  
if __name__ == '__main__':

    app.run( port='5000',threaded=True)

