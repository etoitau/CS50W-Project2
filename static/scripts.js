document.addEventListener('DOMContentLoaded', () => {
    console.log("dom loaded")
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When connected, configure text input
    socket.on('connect', () => {
        console.log("socket connected")
        var input = document.getElementById("msg_input");
        input.addEventListener("keyup", function(event) {

            if (event.key === "Enter") {
                const msg_to_send = input.value;
                socket.emit('send_message', {'text': msg_to_send});
                input.value = '';
            }
        })
        document.querySelector('#msg_input').onsubmit = function() {
            const msg_to_send = this.value;
            socket.emit('send_message', {'text': msg_to_send});
        };
    });

    // When a message comes in, add it
    socket.on('distribute_message', data => {
        const p = document.createElement('p');
        p.innerHTML = `from someone: ${data.text_blast}`;
        document.querySelector('#chat').append(p);
    });
});