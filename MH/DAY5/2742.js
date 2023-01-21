const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
let input = Number(fs.readFileSync(filePath).toString());
let answer = '';

for(let i=input; i>0; i--){
  answer += i + '\n'
}

console.log(answer)