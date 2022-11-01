import io from 'socket.io-client';
import { BACKENDURL, BACKENDPORT} from "../config/constant";

//URL of backend server to connect socket to backend server
const SOCKETRURL:string = BACKENDURL+":"+BACKENDPORT;

const socket = io(SOCKETRURL,{
  autoConnect : false,
});

export default socket;