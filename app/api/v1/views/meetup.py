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
        "time":"1400hrs"}
class meetups (Resource):
    def post(self,title):
        parser = reqparse.Requestparser()
        parser.add_argument("title")
        parser.add_argument("description")
        parser.add_argument("venue")
        parser.add_argument("date")
        parser.add_argument("time")
        args=parser.parse_args()

        for title in meetups:
            if(title==meetups["title"]):
                return "a meetup with the same title exists, please view it to avoid duplication",400
        meetup ={
        "title":title,
        "description":args["description"],
        "venue":args["venue"],
        "date":args["date"],
        "time":args["time"]
        }
meetups.append (meetup)
return meetup,201

if __name__ == '__main__':
    app.run(debug = True)
