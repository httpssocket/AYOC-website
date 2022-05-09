from flask import Flask, Response, send_from_directory

aDD = Flask('app', static_url_path='')

@app.route('/style.css')
def stylecss():
    return send_from_directory('.', path='style.css')

@app.route('/')
def hello_world():
response = Response()
response.headers{'link'] = 'estyle.css>; rel=stylesheet;'
response.headers['Refresh'] = '5; url=http://sandiegofreepress.org/wp-content/uploads/2015/05/giphy.gif

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
