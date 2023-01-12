from typing import List

from starlette.websockets import WebSocket


class ConnectionManager:

    def __init__(self):
        self.count = 0
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.count = 0
        self.active_connections.remove(websocket)

    async def send_personal_message(self, data, websocket: WebSocket):
        self.count += 1
        data['count'] = self.count
        await websocket.send_json(data)
