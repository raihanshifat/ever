import { useState,useEffect } from 'react';
import socket from '../../objects/socket';
import { messageInterface } from '../../interfaces/interface';

const ChatBox = () => {
 
const [fromUserName,setFromUserName] = useState<string>("");
const [toUserName, setToUserName] = useState<string>("");
const [messageBody,setMessageBody] = useState<string>("");
const [isAuthenticated,setIsAuthenticated] = useState<boolean>(false);
const [messages, setMessages ] = useState<messageInterface[]>([]);

socket.off("private message").on("private message",({content}:any)=>{
  setMessages((prev)=>[...prev,content])
})

const handleChangeUserName = (event : any)=>{
  if(event.target.id === "FromUserName"){
    setFromUserName(event.target.value.trim())
  }
  else{
    setToUserName(event.target.value.trim())
  }
};

const handleSubmitUserName = (event : any) =>{
   event.preventDefault()
   console.log(fromUserName)
      socket.auth = {fromUserName};
      try{
        socket.connect();
        setIsAuthenticated (true)
      }catch(err){
        console.log(err)
      };
};

const handleMessage = (event:any) =>{
  setMessageBody(event.target.value)
}

const handleSubmitMessage= (event:any)=>{
  event.preventDefault()
  
  let message : messageInterface = {
    fromuserid:fromUserName,
    text:messageBody,
    touserid:toUserName
  }
  socket.emit("private message",{
    content : message
  })
  setMessages((prev)=>[...prev,message]);
}

return (
  <div className="">
    <div style={{display:isAuthenticated?"none":""}}>
      <input id='FromUserName' onChange={handleChangeUserName}/>
      <input id='ToUserName' onChange={handleChangeUserName}/>
      <button onClick={handleSubmitUserName}>Enter</button>
    </div>
    {messages.map((message, index) => {
        return (
          <div key={index}>
            <p>{message.fromuserid}</p>
            <p>{message.text}</p>
          </div>
        )
      })}
    <input id='message' onChange={handleMessage}/>
    <button onClick={handleSubmitMessage}>Enter</button>
  </div>
 )
};

export default ChatBox;