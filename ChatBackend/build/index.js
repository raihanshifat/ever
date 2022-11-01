"use strict";
const { Server } = require("socket.io");
const app = require('express')();
const server = require('http').createServer(app);
const cors = require("cors");
const { FRONTENDURL, FRONTENDPORT } = require("./config/config_variables");
const PORT = 4000;
app.use(cors());
const io = new Server(server, {
    cors: {
        origin: FRONTENDURL + ":" + FRONTENDPORT,
    },
});
// io.use((socket : Socket, next : any)=>{
//     const username = socket.handshake.auth.username;
//     if(!username){
//         return next(new Error("invalid username"))
//     }
//     socket.username = username
//     next();
// })
server.listen(PORT, () => {
    console.log(`listening on *:${PORT}`);
});
io.on('connection', (socket) => {
    console.log('new client connected');
});
