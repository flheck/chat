const {
    Worker,
    isMainThread,
    parentPort,
    workerData,
    setEnvironmentData,
    getEnvironmentData,
  } = require("worker_threads"),
  WebSocket = require("ws");

const wss = null;

console.log(isMainThread, wss)

// if (isMainThread && !wss) {
//   const wss = new WebSocket.Server({
//     port: 5000,
//   });
//   setEnvironmentData("wss", wss)
  
//   // wss.on("connection", (ws) => {
//   //   let thread = new Worker(__filename, { workerData: { ws: ws } });
//   //   thread.on("error", (err) => {
//   //     throw err;
//   //   });
//   //   thread.on("exit", () => {
//   //     thread = null;
//   //   });
//   //   thread.on("message", ({ ws, data }) => {
//   //     let response = handleRequest(data);
//   //     ws.send(response);
//   //   });
//   //   console.log("hello");
//   // });
// } else {
//   console.log(getEnvironmentData('wss'));
//   // let ws = workerData.ws;
//   // ws.on("message", (data) => {
//   //   parentPort.postMessage({ ws: ws, data: data });
//   // });
// }


  
// Checking if the current thread is 
// inside the main thread or not
// by using IsMainThread API
if (isMainThread) {
  
   // This re-loads the current file
   // inside a Worker instance.
   new Worker(__filename);
} else {
  console.log('Inside Worker!2');
  console.log('1');
  console.log('2');
  console.log('3');
  console.log(isMainThread); 
}