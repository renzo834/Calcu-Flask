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
        num3 = request.form['num3']

        operation = request.form['operation']

        if operation == 'add':
            sum = float(num1) + float(num2) + float(num3)
            return render_template('app.html', sum=sum)

        elif operation == 'subtract':
            sum = float(num1) - float(num2) - float(num3)
            return render_template('app.html', sum=sum)

        elif operation == 'multiply':
            sum = float(num1) * float(num2) * float(num3)
            return render_template('app.html', sum=sum)

        elif operation == 'divide':
            sum = (float(num1) / float(num2)) / float(num3)
            return render_template('app.html', sum=sum)

        elif operation == 'raiz':
            sum = (float(num1) * float(num2) * float(num3)) ** float(1/2)
            return render_template('app.html', sum=sum)

        else:
            return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()