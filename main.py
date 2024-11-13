from flask import Flask, render_template, request

app = Flask(__name__)

def isPalindrome(num):
    num_str = str(num)  
    if num_str == num_str[::-1]:  
        return 'It is a Palindrome'
    else:
        return 'Not a Palindrome '+num_str[::-1] + ' and inputed number is '+str(num)

def fibonacci(num):
    if num <= 10000:
        n=num
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        
        return fib_sequence
    else:
        return f'enter value less then 10,000 as your value is {num} which is much larger'


@app.route('/')
def start():
    return render_template('index.html')

@app.route('/work', methods=['POST', 'GET'])
def playnum():
    if request.method == 'POST':
        num = request.form['number']  
        try:
            num = int(num)  
        except ValueError:
            return 'Invalid input, please enter a valid number.'

        if 'Palindrome' in request.form:  
            return isPalindrome(num)
        elif 'Square' in request.form:
            return f'The square is: {num * num}' 
        elif 'Fibonnaci' in request.form:
            return fibonacci(num)

    return 'Invalid request'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
