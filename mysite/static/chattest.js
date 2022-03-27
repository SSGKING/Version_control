"use strict";

let ws = undefined;
function log(msg){
    let ta = document.getElementById("messages");
    ta.value = ta.value +msg + "\n";
    ta.scrollTop = ta.scrollHeight;

}
function maybesend(ev){
    if(ev.keycode == 13)
        send();
}
function send(){
    let el = document.getElementById("tosend");
    let txt = el.value;
    
    if(ws == undefined){
        log("not connected");
    }else{
        log("Send: "+txt);
        ws.send(txt);
    }
    el.value = "";
}


function message(ev){
    let data = ev.data;
    log("Recv "+data);

}

function join(){

    let url = "ws://"+document.location.hostname+":2000";
    log("connecting to: "+url);
    let sock = new WebSocket(url);
    sock.onopen = () => {
        log("Connected");
        ws = sock;
        sock.onmessage = message;
    }
    sock.onerror = ev => {
        log("error:"+ev);
    }
    sock.onclose = () =>{
        log("CLOSED");
        ws = undefined;
    }

}
function hide() {
    var x = document.getElementById("chatDiv");
    if (x.style.display === "none")
    {
        x.style.display = "block";
    }else{
        x.style.display = "none";
    }

}
join();