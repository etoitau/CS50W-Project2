document.addEventListener('DOMContentLoaded', () => {
    console.log("dom loaded");
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    // track text field
    var input = document.getElementById("msg_input");
    // pick up info planted by server
    var user_name = input.dataset.user_name;
    console.log("got username:");
    console.log(user_name);
    var channel = input.dataset.channel_name;
    console.log("got channel:");
    console.log(channel);
    // track field where report errors
    var feedback = document.getElementById("banned_words");
    
    // When connected, configure text input and when to send
    socket.on('connect', () => {
        console.log("socket connected");
        input.addEventListener("keyup", function(event) {
            if (event.key === "Enter") {
                console.log("Enter pressed");
                const msg_to_send = input.value;
                if (msg_to_send) {
                    console.log("sending message:");
                    console.log(msg_to_send);
                    socket.emit('send_message', {'name': user_name, 'text': msg_to_send, 'channel': channel});
                }  
            }
        })
    });

    // see if server noted any words not allowed. if so, report to user, else proceed
    socket.on('message_status', data => {
        console.log("message_status returned:");
        console.log(data);
        if (data.length > 0) {
            console.log("found used words");
            feedback.innerHTML = "Can't use: ".concat(data);
        }
        else {
            console.log("message okay");
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
            updateScroll();
        }
    });

    // keep chat window at most recent message unless user deliberately scrolls elsewhere
    // based on https://stackoverflow.com/a/18614561
    var scrolled = false;
    function updateScroll(){
        console.log("update scroll called");
        //console.log("scrolled bool is:");
        //console.log(scrolled);
        if(!scrolled){
            console.log("should have just scrolled");
            $('.scroll_box').scrollTop($('.scroll_box')[0].scrollHeight);
        }
    }

    $(".scroll_box").on('scroll', function(){
        console.log("scroll detected");
        scrolled=true;
        //console.log($('.scroll_box').scrollTop());
        //console.log($('.scroll_box')[0].scrollHeight - $('.scroll_box').height());
        if ($('.scroll_box')[0].scrollHeight - $('.scroll_box').height() <= $('.scroll_box').scrollTop() + 1) {
            scrolled=false;
        }
        //console.log("scrolled:");
        //console.log(scrolled);
    });
});