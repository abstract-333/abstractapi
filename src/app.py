from webob import Request, Response

from api import API

app = API()


@app.route(path="/home")
def home(
    request: Request,
    response: Response,
):
    response.text = "HIIIII"


@app.route(path="/home/{name}")
def home(
    request: Request,
    response: Response,
    name: str,
):
    response.text = f"Hello, {name}"
