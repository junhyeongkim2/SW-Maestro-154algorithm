const path = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
const input = require("fs").readFileSync(path).toString().split("\n");
const T = input.shift();
const st = [];

function stack(input) {
  if (input.includes("push")) {
    st.push(+input.slice(5));
  }
  if (input.includes("pop")) {
    if (st.length === 0) return -1;
    return st.pop();
  }
  if (input.includes("size")) {
    return st.length;
  }
  if (input.includes("empty")) {
    return st.length === 0 ? 1 : 0;
  }
  if (input.includes("top")) {
    if (st.length === 0) return -1;
    return st[st.length - 1];
  }
}

let answer = [];
for (let i = 0; i < T; i++) {
  const result = stack(input[i]);
  if (result !== undefined) {
    answer.push(result);
  }
}

console.log(answer.join('\n'));