from flask import Flask,jsonify,request
import ipl

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello WOrld'

@app.route('/api/teams')
def teams():
    team =ipl.teamAPI()
    return jsonify(team)

@app.route('/api/teamvteam')
def teamvteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = ipl.teamVteamAPI(team1,team2)
    print(response)
    return jsonify(response)

app.run(debug=True)