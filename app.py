from flask import Flask, render_template, redirect, url_for, request
from controllers.spam import tv360, myVT
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone = request.form.get('phone')
        runSpam(phone)
 
    return render_template('index.html')

@app.route('/rest', methods=['GET'])
def restSend():
    phone = ""
    if request.args.get("phone"):
        phone = request.args["phone"]
        runSpam(phone)
    return f'Spam phone: {phone}'

def runSpam(phone):
    print(f'{phone}')
    tv360(phone)
    myVT(phone)

if __name__ == '__main__':
  app.run(host='0.0.0.0')