from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random string

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('signin'))
    answer_already_submitted = session.pop('answer_already_submitted', False)  # Remove flag from session
    return render_template('index.html', answer_already_submitted=answer_already_submitted)

@app.route('/clear')
def clear_session():
    session.clear()
    return 'Session data cleared'


CHALLS = [
    "chall1_freebie",
    "chall1_jackiesw10",
    "chall1_mst",
    "chall1_j_williamson_administrators",
    "chall1_0.5.1_y",
    "chall1_2024-03-02"
    "chall1_10.0.2.15",
    "chall2_Canyon_View_Apartments",
    "chall2_blow_up_provo_temple",
    "chall2_fertilizer_bomb",
    "chall2_Jimmer_Fredette",
    "chall2_f3rt@l1z3r_b0mb"
]

@app.route('/submit', methods=['POST'])
def submit():
    if 'data' not in session:
        session['data'] = []

    data = request.form['data']

    if 'chall1_answers' not in session:
        session['chall1_answers'] = 0
    if 'chall2_answers' not in session:
        session['chall2_answers'] = 0
    if 'chall3_answers' not in session:
        session['chall3_answers'] = 0

    if 'submitted_answers' not in session:
        session['submitted_answers'] = []

    # Check if the data is correct
    if data.lower() in CHALLS and data.lower() not in session['submitted_answers']:
        chall = data.split("_")[0]
        if chall == "chall1":
            session['chall1_answers'] += 1
        if chall == "chall2":
            session['chall2_answers'] += 1
        if chall == "chall3":
            session['chall3_answers'] += 1
        session['submitted_answers'].append(data.lower())
    else:
        session['answer_already_submitted'] = True
    session['data'].append(data)
    return redirect(url_for('index'))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
