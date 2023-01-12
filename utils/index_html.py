html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>Sending</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Отправить</button>
        </form>
        <br>
        <div id='messages'></div>
        <script>
            let ws = new WebSocket(`ws://localhost:8000/ws`);
                ws.onopen = () => {
                console.log('Подключение установлено')
            }
            ws.onmessage = (event) => {
                let messages = document.getElementById('messages')
                let message = document.createElement('div')
                let data = JSON.parse(event.data)
                let count = document.createTextNode(`${data.count}. `)
                let content = document.createTextNode(data.text)
                if (data.count) {
                    message.appendChild(count)
                }
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                let input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""
