import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";

const useStyles = makeStyles({
  messageAdmin: {
    backgroundColor: "#ee00ff",
  },
  messageUser: {
    backgroundColor: "#555dff",
  },
});

export const Messages = ({ messages }: { messages: any }) => {
  const classes = useStyles();
  console.log(messages);
  return (
    <List>
      {messages.map((data: any, index: number) => {
     console.log(data.general);
        return (
          <React.Fragment key={"messages-" + index}>
            <ListItem key={"msg-user-" + index}>
              <Grid
                container
                direction="row"
                justify="flex-start"
                alignItems="center"
              >
                <Grid item xs={4}>

                  {!!data?.general?.username ? (
                    <Card className={classes.messageUser}>
                      <CardContent>
                        <ListItemText
                          primary={data.general.message}
                          secondary={data.general.username}
                        ></ListItemText>
                      </CardContent>
                    </Card>
                  ) : null}
                </Grid>
              </Grid>
            </ListItem>
          </React.Fragment>
        );
      })}
    </List>
  );
};
