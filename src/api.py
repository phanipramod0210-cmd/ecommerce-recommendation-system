from flask import Flask, jsonify, request
import joblib
app = Flask(__name__)
MODEL='model/als_model.joblib'
try:
    recs = joblib.load(MODEL)
except:
    recs = []

@app.route('/recommend', methods=['GET'])
def recommend():
    user = request.args.get('user', None)
    topn = int(request.args.get('n', 5))
    return jsonify({'user':user, 'recommendations': recs[:topn]})

if __name__ == '__main__':
    app.run(port=8002)
