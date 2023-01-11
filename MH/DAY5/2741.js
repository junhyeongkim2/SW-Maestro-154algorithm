const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
let input = fs.readFileSync(filePath).toString();
let answer = '';

for(let i=1; i<=input; i++){
  answer += i + "\n";
}
console.log(answer)