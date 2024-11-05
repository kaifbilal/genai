from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Lab 1 Routes
@app.route('/lab1.1')
def lab1_1():
    return render_template('lab1/1.html')

@app.route('/lab1.2')
def lab1_2():
    return render_template('lab1/2.html')

@app.route('/lab1.3')
def lab1_3():
    return render_template('lab1/3.html')

@app.route('/lab1.4')
def lab1_4():
    return render_template('lab1/4.html')

# Lab 2 Routes
@app.route('/lab2.1')
def lab2_1():
    return render_template('lab2/1.html')

@app.route('/lab2.2')
def lab2_2():
    return render_template('lab2/2.html')

@app.route('/lab2.3')
def lab2_3():
    return render_template('lab2/3.html')

@app.route('/lab2.4')
def lab2_4():
    return render_template('lab2/4.html')

# Lab 3 Routes
@app.route('/lab3.1')
def lab3_1():
    return render_template('lab3/1.html')

@app.route('/lab3.2')
def lab3_2():
    return render_template('lab3/2.html')

@app.route('/lab3.3')
def lab3_3():
    return render_template('lab3/3.html')

@app.route('/lab3.4')
def lab3_4():
    return render_template('lab3/4.html')

# Lab 4 Routes
@app.route('/lab4.1')
def lab4_1():
    return render_template('lab4/1.html')

@app.route('/lab4.2')
def lab4_2():
    return render_template('lab4/2.html')

@app.route('/lab4.3')
def lab4_3():
    return render_template('lab4/3.html')

@app.route('/lab4.4')
def lab4_4():
    return render_template('lab4/4.html')

# Lab 5 Routes
@app.route('/lab5.1')
def lab5_1():
    return render_template('lab5/1.html')

@app.route('/lab5.2')
def lab5_2():
    return render_template('lab5/2.html')

@app.route('/lab5.3')
def lab5_3():
    return render_template('lab5/3.html')

@app.route('/lab5.4')
def lab5_4():
    return render_template('lab5/4.html')

# Lab 6 Routes
@app.route('/lab6.1')
def lab6_1():
    return render_template('lab6/1.html')

@app.route('/lab6.2')
def lab6_2():
    return render_template('lab6/2.html')

@app.route('/lab6.3')
def lab6_3():
    return render_template('lab6/3.html')

@app.route('/lab6.4')
def lab6_4():
    return render_template('lab6/4.html')

# Lab 7 Routes
@app.route('/lab7.1')
def lab7_1():
    return render_template('lab7/1.html')

@app.route('/lab7.2')
def lab7_2():
    return render_template('lab7/2.html')

@app.route('/lab7.3')
def lab7_3():
    return render_template('lab7/3.html')

@app.route('/lab7.4')
def lab7_4():
    return render_template('lab7/4.html')

# Lab 8 Routes
@app.route('/lab8.1')
def lab8_1():
    return render_template('lab8/1.html')

@app.route('/lab8.2')
def lab8_2():
    return render_template('lab8/2.html')

@app.route('/lab8.3')
def lab8_3():
    return render_template('lab8/3.html')

@app.route('/lab8.4')
def lab8_4():
    return render_template('lab8/4.html')

# Lab 9 Routes
@app.route('/lab9.1')
def lab9_1():
    return render_template('lab9/1.html')

@app.route('/lab9.2')
def lab9_2():
    return render_template('lab9/2.html')

@app.route('/lab9.3')
def lab9_3():
    return render_template('lab9/3.html')

@app.route('/lab9.4')
def lab9_4():
    return render_template('lab9/4.html')

# Lab 10 Routes
@app.route('/lab10.1')
def lab10_1():
    return render_template('lab10/1.html')

@app.route('/lab10.2')
def lab10_2():
    return render_template('lab10/2.html')

@app.route('/lab10.3')
def lab10_3():
    return render_template('lab10/3.html')

@app.route('/lab10.4')
def lab10_4():
    return render_template('lab10/4.html')

# Lab 11 Routes
@app.route('/lab11.1')
def lab11_1():
    return render_template('lab11/1.html')

@app.route('/lab11.2')
def lab11_2():
    return render_template('lab11/2.html')

@app.route('/lab11.3')
def lab11_3():
    return render_template('lab11/3.html')

@app.route('/lab11.4')
def lab11_4():
    return render_template('lab11/4.html')

# Lab 12 Routes
@app.route('/lab12.1')
def lab12_1():
    return render_template('lab12/1.html')

@app.route('/lab12.2')
def lab12_2():
    return render_template('lab12/2.html')

@app.route('/lab12.3')
def lab12_3():
    return render_template('lab12/3.html')

@app.route('/lab12.4')
def lab12_4():
    return render_template('lab12/4.html')

# Lab 13 Routes
@app.route('/lab13.1')
def lab13_1():
    return render_template('lab13/1.html')

@app.route('/lab13.2')
def lab13_2():
    return render_template('lab13/2.html')

@app.route('/lab13.3')
def lab13_3():
    return render_template('lab13/3.html')

@app.route('/lab13.4')
def lab13_4():
    return render_template('lab13/4.html')

# Lab 14 Routes
@app.route('/lab14.1')
def lab14_1():
    return render_template('lab14/1.html')

@app.route('/lab14.2')
def lab14_2():
    return render_template('lab14/2.html')

@app.route('/lab14.3')
def lab14_3():
    return render_template('lab14/3.html')

@app.route('/lab14.4')
def lab14_4():
    return render_template('lab14/4.html')

# Lab 15 Routes
@app.route('/lab15.1')
def lab15_1():
    return render_template('lab15/1.html')

@app.route('/lab15.2')
def lab15_2():
    return render_template('lab15/2.html')

@app.route('/lab15.3')
def lab15_3():
    return render_template('lab15/3.html')

@app.route('/lab15.4')
def lab15_4():
    return render_template('lab15/4.html')

if __name__ == "__main__":
    app.run(debug=True)