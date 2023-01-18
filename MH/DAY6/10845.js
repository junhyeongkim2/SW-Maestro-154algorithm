const path = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = require("fs").readFileSync(path).toString().trim().split("\n");
const [n, ...commands] = input;

let queue = [];
let answer = [];

for (let i = 0; i < n; i++) {
  switch (commands[i]) {
    case "pop":
      answer.push(queue.shift() || -1);
      // if(queue.length === 0) answer.push(-1);
      // else answer.push(queue.shift());
      break;
    case "size":
      answer.push(queue.length);
      break;
    case "empty":
      answer.push(queue.length ? 0 : 1);
      // if(queue.length === 0) answer.push(1);
      // else answer.push(0);
      break;
    case "front":
      answer.push(queue[0] || -1);
      // if(queue.length === 0) answer.push(-1);
      // else answer.push(queue[0]);
      break;
    case "back":
      answer.push(queue[queue.length - 1] || -1);
      // if(queue.length === 0) answer.push(-1);
      // else answer.push(queue[queue.length-1]);
      break;
    default:
      queue.push(commands[i].split(" ")[1]);
      break;
  }
}

console.log(answer.join("\n"));
