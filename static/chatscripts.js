document.addEventListener('DOMContentLoaded', () => {
    console.log("dom loaded")
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    
    var input = document.getElementById("msg_input");
    var user_name = input.dataset.user_name;
    console.log("got username:")
    console.log(user_name)
    var channel = input.dataset.channel_name;
    console.log("got channel:")
    console.log(channel)
    var feedback = document.getElementById("banned_words");
    
    // When connected, configure text input
    socket.on('connect', () => {
        console.log("socket connected")
        input.addEventListener("keyup", function(event) {
            if (event.key === "Enter") {
                console.log("sending message:")
                const msg_to_send = input.value;
                socket.emit('send_message', {'name': user_name, 'text': msg_to_send, 'channel': channel});
            }
        })
    });

    // result of sent message
    socket.on('message_status', data => {
        console.log("message_status returned:")
        console.log(data);
        if (data.length > 0) {
            console.log("found used words")
            feedback.innerHTML = data;
        }
        else {
            console.log("message okay")
            input.value = '';
            feedback.innerHTML = '';
        }
    });

    // When a message comes in, add it
    socket.on('distribute_message', data => {
        if (channel == data.channel) {
            const p = document.createElement('p');
            p.innerHTML = `${data.message.user_name} ${data.message.time}: <br>${data.message.text}`;
            document.querySelector('#chat').append(p);
        }
    });
});