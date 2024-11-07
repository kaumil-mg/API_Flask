from flask import Flask, render_template, request

app = Flask(__name__)

def isPalindrome(num):
    num_str = str(num)  
    if num_str == num_str[::-1]:  
        return 'It is a Palindrome'
    else:
        return 'Not a Palindrome '+num_str[::-1] + ' and og num is '+str(num)

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

    return 'Invalid request'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
