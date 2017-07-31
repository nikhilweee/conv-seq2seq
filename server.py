from flask import Flask, render_template, request
import subprocess


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        result = None
    if request.method == 'POST':
        query = request.form['query']
        cmd = 'th generate-lines.lua \
            -path experiments/fullyconv/model_best_cpu.th7 \
            -sourcedict data/raw/tokenized.sen-que/dict.sen.th7 \
            -targetdict data/raw/tokenized.sen-que/dict.que.th7 \
            -beam 5'.split()
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, input=query.encode())
        result = proc.stdout.decode().split('\t')[1]

    return render_template('index.html', result=result)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, threaded=True)
