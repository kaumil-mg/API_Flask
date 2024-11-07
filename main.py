from flask import Flask, render_template, request

app = Flask(__name__)

# Function to check if the number is a palindrome
def isPalindrome(num):
    num_str = str(num)  # Convert the number to a string
    if num_str == num_str[::-1]:  # Check if the string is equal to its reverse
        return 'It is a Palindrome'
    else:
        return 'Not a Palindrome '+num_str[::-1] + ' and og num is '+str(num)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/work', methods=['POST', 'GET'])
def playnum():
    if request.method == 'POST':
        num = request.form['number']  # Get the input number as a string
        try:
            num = int(num)  # Try to convert to float for the calculation
        except ValueError:
            return 'Invalid input, please enter a valid number.'

        if 'Palindrome' in request.form:  # Check which button was pressed
            return isPalindrome(num)
        elif 'Square' in request.form:
            return f'The square is: {num * num}'  # Return the square of the number

    return 'Invalid request'

if __name__ == '__main__':
    app.run(debug=True)
