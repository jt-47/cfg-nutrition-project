from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def home():
  if 'usersfood' and 'userdietary' and 'userhealth' and 'userexclusion' not in request.form:
    raise Exception('Missing inputs')


if __name__ == '__main__':
    app.run(debug=True)