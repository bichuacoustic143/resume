from flask import Flask, render_template, send_file, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'HEAD'])
def home():
    if request.method == 'HEAD':
        return '', 200  # Respond to HEAD requests with an empty response
    return render_template('index.html')

@app.route('/download')
def download_resume():
    return send_file('resume_sadananda.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
