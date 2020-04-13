from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

@app.route("ec2-52-53-165-168.us-west-1.compute.amazonaws.com:5000/home")
def home():
    return render_template('LandingPage.html')

@app.route("ec2-52-53-165-168.us-west-1.compute.amazonaws.com:5000/", methods=['GET','POST'])
def index():
    if(request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent': some_json}), 201
    else:
        return jsonify({'about': 'Hello World'})

@app.route('ec2-52-53-165-168.us-west-1.compute.amazonaws.com:5000/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result': num * 10})


if __name__ == '__main__':
    app.run(debug=True)