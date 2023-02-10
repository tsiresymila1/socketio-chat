import os
from pathlib import Path
from typing import Any
from starlite import Starlite, StaticFilesConfig, TemplateConfig
from starlite.contrib.jinja import JinjaTemplateEngine
from app.spa.spa_controller import SpaController
import json
from modules.socketio import SocketManager

template_config = TemplateConfig(
    directory=Path(os.getcwd(), "ressources", "views"),
    engine=JinjaTemplateEngine,
)

starlite_app = Starlite(
    allowed_hosts=['*'],
    debug=False,
    template_config=template_config,
    route_handlers=[SpaController],
    middleware=[],
    static_files_config=[
        StaticFilesConfig(
            path="/static",
            directories=[Path(os.getcwd(), "public", "static")]
        ),
    ],
)

io = SocketManager(app=starlite_app)


@io.on("connect")
async def connect(sid: Any, environ: Any):
    print("Client connected : ,", sid, environ)
    # await io.emit('message', json.dumps({"sid": sid}))


@io.on('message')
async def message(sid: Any, data: Any):
    print("message : ", sid, data)
    await io.emit('message', json.dumps({"sid": sid, "data": data}))


@io.on("disconnect")
def disconnect(sid: Any):
    print("Client disconnect : ", sid)


app = io.get_asgi_app()
