import flask, random, logging, sys
import cipher
import generate_coin_codes

app = flask.Flask(__name__)

STRENGTH = 3

@app.route("/data")
def data():
	code = random.choice(generate_coin_codes.get_codes2())
	encr = cipher.encrypt(code, STRENGTH)
	print(f"\nGiving encrypted code: {encr}, original: {code}\n", file = sys.stderr)
	return encr

@app.route("/validate/<user>/<code>")
def val(user, code):
	return str(generate_coin_codes.validate_code_and_activate(code, user))

app.run("0.0.0.0", 80, debug=True)