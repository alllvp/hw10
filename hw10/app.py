from flask import Flask
import utils

candidates = utils.load_data("data", "candidates.json")  # словарь - кандидаты
app = Flask(__name__)


def handle_bad_request(e):
    return 'такой страницы не существует', 400

app.register_error_handler(404, handle_bad_request)


@app.route("/")
def page_index():

    output = "<pre>"
    for eachcandidate in candidates:
       output += f"{eachcandidate['name']} -\n"
       output += f"{eachcandidate['position']}\n"
       output += f"{eachcandidate['skills']}\n\n"
    output += "<pre>"
    return output


@app.route("/candidates/<int:id>/")
def page_candidate(id):
    output = 'такой страницы не существует'
    for eachcandidate in candidates:
        if eachcandidate['id'] == id:
            output = f"<img src='{eachcandidate['picture']}'>\n<pre>\n"
            output += f"{eachcandidate['name']} -\n"
            output += f"{eachcandidate['position']}\n"
            output += f"{eachcandidate['skills']}\n<pre>"
    return output


@app.route("/skills/<skill>/")
def page_skills(skill):
    output = '<pre>'
    marker = False
    for eachcandidate in candidates:
        if skill.lower() in eachcandidate['skills'].lower():
            marker = True
            output += f"{eachcandidate['name']} -\n"
            output += f"{eachcandidate['position']}\n"
            output += f"{eachcandidate['skills']}\n<pre>"
    if marker == False:
        output = 'не найдено<pre>'
    return output

app.run()