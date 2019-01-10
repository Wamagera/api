from flask import Flask
from flask_restful import Api,Resource,reqarse
app = Flask( __name__)
api = Api(app)
@app.route('/')
meetups = [{
        "title":"vision 2030",
        "description":"discussion on the attainability of vision 2030.",
        "venue":"kicc grounds",
        "date":"4th June,2019",
        "time":"2100hrs"}
        {"title":"TDD",
        "description":"lecture on the benefits of TDD and how to "
        "venue":"PAC",
        "date":"3rd Feb, 2018",
        "time":"1400hrs"}]

class meetups (Resource):
    def get(self,meetup):
        for meetup in meetups:
            if(meetup==meetups["True"]):
                return meeetups, 200
            return "meetup you are looking for has been deleted or is under moderation",404

if __name__ == '__main__':
    app.run(debug = True)
