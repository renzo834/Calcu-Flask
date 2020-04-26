from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
       
       ##operation = request.form['operation']

        ##if operation == 'add':
        sum =  1- ( 1- (1/(float(num1))))**(float(num2))
        return render_template('app.html', sum=round(sum,5))

    else:
            return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run(debug=True)