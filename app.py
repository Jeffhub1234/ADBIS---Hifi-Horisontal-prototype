from flask import Flask, render_template

app = Flask(__name__)

# Test route
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/kalender')
def kalender():
    return render_template('kalender copy.html')

@app.route('/kurser')
def kurser():
    return render_template('kurser.html')

@app.route('/bookinger')
def bookinger():
    return render_template('bookinger.html')

@app.route('/kursusdetaljer')
def kursusdetaljer():
    return render_template('kursusdetaljer.html')

@app.route('/medarbejdere')
def medarbejdere():
    return render_template('medarbejdere.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')




if __name__ == '__main__':
    app.run(debug=True, port=5000)