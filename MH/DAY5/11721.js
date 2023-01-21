const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
let input = fs.readFileSync(filePath).toString();

for(let i=0; i<input.length/10; i++){
  console.log(input.slice(10*i,10*i+10))
}