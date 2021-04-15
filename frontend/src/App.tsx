import { useState } from "react";


import { Chat } from "./components/Chat";
import { Preface } from "./components/Preface";

export const App = ({ URL }: { URL: string }) => {
  const [username, setUsername] = useState("");
  const [roomId, setRoomId] = useState("sameroom");
  const [toggleChat, setToggleChat] = useState(false);

  const startChat = (event: any) => {
    event.preventDefault();

    if (username !== "") {
      setToggleChat(!toggleChat);
    }
  };

  const endChat = (event: any) => {
    event.preventDefault();
    setToggleChat(!toggleChat);
    setUsername("");
  };

  return (
    <>
      {toggleChat ? (
        <Chat username={username} room={roomId} endChat={endChat} URL={URL} />
      ) : (
        <Preface
          setUsername={setUsername}
          username={username}
          startChat={startChat}
        />
      )}
    </>
  );
};
