from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None
    
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    error = "Error: Division by zero!"
                else:
                    result = num1 / num2
            else:
                error = "Error: Invalid operation!"
                
        except ValueError:
            error = "Error: Please enter valid numbers!"
    
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
