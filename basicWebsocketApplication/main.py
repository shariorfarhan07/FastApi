from fastapi import FastAPI, WebSocket, WebSocketDisconnect,Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify a list of allowed origins (e.g., ["http://localhost:3000"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Lets Chat</title>
    </head>
    <body>
        <h1>Lets Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://127.0.0.1:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
                
                
                
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode("From Me:"+input.value)
                message.style.color = "green";
                message.appendChild(content)
                messages.appendChild(message)
                
                
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        print("connect", websocket)
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        print("disconnect", websocket)
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        print("personal message", message,WebSocket)
        await websocket.send_text(message)

    async def broadcast(self, message: str,id=None):

        for connection in self.active_connections:
            if id != connection:
                await connection.send_text(message)
                # 1,2,3,4,5

manager = ConnectionManager()

@app.get("/")
async def get():
    print("test")
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print("ws connect", websocket)
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"User: {data}",websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
