from flask import Flask  

from auth import auth_bp  

from routes import main_bp  

app = Flask(__name__)  

app.secret_key = 'neco_tajneho'  

app.register_blueprint(auth_bp)  

app.register_blueprint(main_bp)  

if __name__ == '__main__':  
    app.run(debug=True)  
