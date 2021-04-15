import { useState, useEffect, useRef } from "react";

/*---Material UI---*/
import { makeStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";
import Divider from "@material-ui/core/Divider";
import Typography from "@material-ui/core/Typography";

import CloseIcon from "@material-ui/icons/Close";
import IconButton from "@material-ui/core/IconButton";

import { Input } from "./Input";
import { Messages } from "./Messages";

const useStyles = makeStyles({
  root: {
    maxHeight: "100%",
  },
  header: {
    height: "5vh",
  },
  chat: {
    height: "80vh",
    overflowY: "auto",
  },
  input: {
    height: "15vh",
  },
});

let socket: any;

export const Chat = ({
  URL,
  username,
  endChat,
  room,
}: {
  URL: string;
  username: string;
  endChat: any;
  room: string;
}) => {
  const classes = useStyles();
  const [message, setMessage] = useState("");
  const init: Array<any> = [];
  const [messages, setMessages] = useState(init);
  const endRef = useRef<null | HTMLDivElement>(null);

  useEffect(() => {
    socket = new WebSocket(URL);
    socket.onopen = () => {};
    return () => {};
  }, [URL]);

  const scrollToBottom = () => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    socket.onmessage = (evt: any) => {

      setMessages([...messages, JSON.parse(evt.data)]);
      scrollToBottom();
    };
  }, [messages]);

  const sendMessage = (event: any) => {
    event.preventDefault();

    if (message) {
      socket.send(JSON.stringify({ username, message }));

      setMessage("");
    }
  };

  const close = () => {
    socket.onclose = function(event :any) {
        console.log("WebSocket is closed now.");
      };
  };

  return (
    <Grid container className={classes.root}>
      <Grid container className={classes.header}>
        <Grid item xs={11}>
          <Typography variant="h5">Chat</Typography>
        </Grid>
        <Grid item xs={1}>
          <IconButton
            aria-label="close"
            onClick={(e) => {
              endChat(e);
              close();
            }}
          >
            <CloseIcon />
          </IconButton>
        </Grid>
      </Grid>

      <Grid item xs={12}>
        <Divider />
      </Grid>

      <Grid container className={classes.chat}>
        <Grid item xs={12}>
          <Messages messages={messages} />
          <div ref={endRef} />
        </Grid>
      </Grid>

      <Grid item xs={12}>
        <Divider />
      </Grid>

      <Grid container className={classes.input}>
        <Grid item xs={12}>
          <Input
            sendMessage={sendMessage}
            setMessage={setMessage}
            message={message}
          />
        </Grid>
      </Grid>
    </Grid>
  );
};
