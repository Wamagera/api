from flask import Flask
from flask_restful import Api,Resource,reqarse
app = Flask( __name__)
api = Api(app)
@app.route('/')

questions = []
class questions (Resource):
    def post(self,title):
        parser = reqparse.Requestparser()
        parser.add_argument("title")
        parser.add_argument("question")
        args=parser.parse_args()

        for title in questions:
            if (title==questions[""]):
                return "invalid format! please enter a title"
            if (question==questions[""]):
                return"invalid format! please enter a question"

        question = {
        "title":args[]"title"],
        "question":args["question"]
        }
questions.append (question)
return question, 201
