const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = fs.readFileSync(filePath).toString().trim();
input = BigInt(input);
const dp = [];
dp[1] = BigInt(1);
dp[2] = BigInt(1);
 
for(let i=3; i<=input; i++){
  dp[i] = dp[i-1] + dp[i-2];
}

console.log(dp[input].toString())