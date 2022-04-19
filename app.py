from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = 'Buddy'
    letters = list(name)
    person = {'name':'andy'}
    return render_template('index.html', name=name, letters=letters, person=person)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/information')
def info():
    return '<h1>Party is tonight</h1>'

#dynamic route
@app.route('/party/<name>')
def party(name):
    return 'This is a page for {}'.format(name.upper())

@app.route('/debug/<thing>')
def debug_test(thing):
    return "100th letter: {}".format(thing[100])

if __name__ == '__main__':
    app.run()
