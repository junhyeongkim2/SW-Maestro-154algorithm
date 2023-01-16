const path = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = require("fs").readFileSync(path).toString().trim().split("\n");

const [n, ...commands] = input;
const deck = [];
const answer = [];

for (let i = 0; i < n; i++) {
  switch (commands[i]) {
    case "pop_front":
      answer.push(deck.shift() || -1);
      break;
    case "pop_back":
      answer.push(deck.pop() || -1);
      break;
    case "size":
      answer.push(deck.length);
      break;
    case "empty":
      answer.push(deck.length === 0 ? 1 : 0);
      break;
    case "front":
      answer.push(deck[0] || -1);
      break;
    case "back":
      answer.push(deck[deck.length - 1] || -1);
      break;
    default:
      if (commands[i].includes("push_front"))
        deck.unshift(commands[i].slice(11));
      else deck.push(commands[i].slice(10));
      break;
  }
}

console.log(answer.join("\n"));
