from http import client
import subprocess
import sys
import asyncio
import tornado
import tornado.ioloop
import tornado.websocket
PORT = 2000
class User(tornado.websocket.WebSocketHandler):
    allUsers = {}
    ids = 0
    def __init__(self,*args,**kw):

        super().__init__(*args,**kw)
    def open(self):
        self.myid = User.ids
        User.ids += 1
        User.allUsers[self.myid] = self
        print(f"open: {self.myid}")
        self.broadcast(f"User Joined: {self.myid}")
    def on_message(self,msg):
        print("MESSAGE",msg)
        self.broadcast(msg)
    def on_close(self):
        print("Close")
        self.broadcast(f"User left {self.myid}")
        del User.allUsers[self.myid]
        
    def check_origin(self,o):
        return True
    def broadcast(self,msg):
        for clientid in User.allUsers:
            if self.myid != clientid:
                User.allUsers[clientid].write_message(msg)

    

if __name__ != "__main__":
    print("spawning tornado")
    P = subprocess.Popen(
        [sys.executable,
        __file__
        ]
    )
else:
    print("starting tornado")
    eventloop = asyncio.new_event_loop()
    asyncio.set_event_loop(eventloop)
    app = tornado.web.Application(
        [
            ("/",User)

        ]
    )
    app.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()