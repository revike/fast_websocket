from fastapi import APIRouter
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocket, WebSocketDisconnect

from utils.index_html import html
from utils.websocket_manager import ConnectionManager

router = APIRouter()

manager = ConnectionManager()


@router.get("/")
async def get():
    return HTMLResponse(html)


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    count = 0
    try:
        while True:
            count += 1
            text = await websocket.receive_text()
            if text and not text.isspace():
                data = {'text': text, 'count': count}
                await manager.send_personal_message(data, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
