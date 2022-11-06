const { Server } = require("socket.io");
const app = require('express')();
const server = require('http').createServer(app);
const cors =require("cors");

const {FRONTENDURL,FRONTENDPORT} = require("./config/config_variables");
const PORT = 4000;

app.use(cors());

const io = new Server(server,{
    cors:{
        origin: FRONTENDURL+":"+FRONTENDPORT,
    },
});
io.use((socket : any, next : any)=>{
    const userName = socket.handshake.auth.fromUserName;
    if(!userName){
        return next(new Error("invalid username"))
    }
    socket.id = userName
    next();
})

server.listen(PORT, () => {
    console.log(`listening on *:${PORT}`);
});

io.on('connection', (socket:any) => { /* socket object may be used to send specific messages to the new connected client */

    console.log('new client connected');
    console.log(socket.id);
    socket.on("private message",({content}:any)=>{
        console.log(content.touserid)
        socket.to(content.touserid).emit("private message",{
            content:content
        })
    })
});