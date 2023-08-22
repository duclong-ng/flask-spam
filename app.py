from flask import Flask, render_template, redirect, url_for, request
from controllers.spam import tv360, myVT
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone = request.form.get('yourphone')
        print(f'{phone}')
        tv360(phone)
        myVT(phone)
    
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)