import { useState,useEffect } from 'react';
import socket from '../../objects/socket';
import { messageInterface } from '../../interfaces/interface';



const ChatBox = () => {

socket.on("private message",({content}:any)=>{
  messages.push(content)  
})
 
const [fromUserName,setFromUserName] = useState<string>("");
const [texts,setTexts] = useState<messageInterface>({
  userid:"",
  text:""
});
const [isAuthenticated,setIsAuthenticated] = useState<boolean>(false)
const [messages, setMessages ] = useState<messageInterface[]>([]);
const [toUserName, setToUserName] = useState<string>("")

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
      socket.auth = {fromUserName};
      try{
        socket.connect();
        setIsAuthenticated (true)
      }catch(err){
        console.log(err)
      };
};

const handleSubmitMessage= (event:any)=>{
  event.preventDefault()
  
  let messageBody : messageInterface = {
    userid:fromUserName,
    text:event.target.value
  }
  socket.emit("private message",{
    content : messageBody
  })
  setTexts(messageBody)
  messages.push(texts);
}
return (
  <div className="">
    <div style={{display:isAuthenticated?"none":""}}>
      <input id='FromUserName' onChange={handleChangeUserName}/>
      <input id='ToUserName' onChange={handleChangeUserName}/>
      <button onSubmit={handleSubmitUserName}>Enter</button>
    </div>
    <>
    {
      messages.forEach((message:messageInterface)=>{
        <>
        <b>{message.userid}</b>
        <b>{message.text}</b>
        </>
      }) 
    }
    <input id='message' onChange={handleSubmitMessage}/>
    </>
  </div>
 )
}
export default ChatBox;