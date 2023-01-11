const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');
const T = input.shift();

for (let i=0; i<T; i++){
  const arr = input[i].split(' ').map((item)=> +item);
  console.log(`Case #${i+1}: ${arr[0]} + ${arr[1]} = ${arr[0]+arr[1]}`)
}