from flask import flask
from flask_restful import Api, Resource, reqarse
app = Flak(__name__)
api = Api(app)
@app.route('/')

questions= [
        {"title":"can tomorrow be today?",
        "question":"if china is 8 hrs of the usa does that mean china's tomorrow is usa's today?"
        },
        {"title":"TDD and OOP",
        "question":"can someone usse TDD and OPP cocurrently or is it either or the other
        }
]

class questions (Resource):
    def get(self,title):
        for title in questions:
            if(title==questions["title"]):
                return question, 200
        return "question you are looking for maybe deleted or is under moderation",404

if __name__ == '__main__':
    app.run(debug = True)
