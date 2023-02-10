

from starlite import Controller, get, Template


class SpaController(Controller):
    path = "/"

    @get()
    async def get(self) -> Template:
        return Template(name="app.html.jinja", context={"title": "Python socketio chat"})
