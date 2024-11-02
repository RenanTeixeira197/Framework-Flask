from flask import Flask, render_template, request  # type: ignore
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        user_data = request.form.get('username')
        pass_data = request.form.get('password')
        
        if not user_data:
            msg = "Usuário Inválido!"
            return render_template('login.html', msg=msg)
        
        if not pass_data:
            msg = "Senha Inválida!"
            return render_template('login.html', msg=msg)
        
        if user_data == 'admin' and pass_data == 'admin':
            return render_template('success.html')
        else:
            msg = "Usuário ou senha incorretos!"
            return render_template('login.html', msg=msg)
    
    return render_template('login.html')
