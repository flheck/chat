import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";

import Fab from "@material-ui/core/Fab";
import SendIcon from "@material-ui/icons/Send";

export const Input = ({
  setMessage,
  sendMessage,
  message,
}: {
  setMessage: any;
  sendMessage: any;
  message: any;
}) => {
  return (
    <Grid container style={{ padding: "20px" }}>
      <Grid item xs={11}>
        <TextField
          id="message-input"
          label={"Message"}
          name="message"
          value={message}
          onChange={({ target: { value } }) => setMessage(value)}
          onKeyPress={(event) =>
            event.key === "Enter" ? sendMessage(event) : null
          }
          style={{ width: "100%" }}
        />
      </Grid>
      <Grid item xs={1}>
        <Fab
          color="primary"
          aria-label="send"
          className="sendButton"
          onClick={(e) => sendMessage(e)}
        >
          <SendIcon />
        </Fab>
      </Grid>
    </Grid>
  );
};
