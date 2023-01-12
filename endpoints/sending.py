from fastapi import APIRouter
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocket, WebSocketDisconnect

from utils.index_html import html
from utils.websocket_manager import ConnectionManager

router = APIRouter()

manager = ConnectionManager()
messages = []


@router.get("/")
async def get():
    return HTMLResponse(html)


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    if messages:
        for text in messages:
            data = {'text': text}
            await manager.send_personal_message(data, websocket)
    try:
        while True:
            text = await websocket.receive_text()
            if text and not text.isspace():
                data = {'text': text}
                messages.append(text)
                await manager.send_personal_message(data, websocket, True)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
