const serverPort = 5000,
  http = require("http"),
  express = require("express"),
  app = express(),
  server = http.createServer(app),
  WebSocket = require("ws"),
  websocketServer = new WebSocket.Server({ server });

websocketServer.on("connection", (webSocketClient) => {
  webSocketClient.send('{ "connection" : "ok"}');

  //when a message is received
  webSocketClient.on("message", (message) => {
    console.log("asd", message);

    wss.broadcast(`{ "general" : ${message} }`)
    //for each websocket client
    websocketServer.clients.forEach((client) => {
      //send the client the current message
      client.send(`{ "general" : ${message} }`);
    });
  });

  webSocketClient.on("close", () => {
    webSocketClient.close();
    console.log("close");
  });
});

server.listen(serverPort, () => {
  console.log(`Websocket server started on port ` + serverPort);
});
