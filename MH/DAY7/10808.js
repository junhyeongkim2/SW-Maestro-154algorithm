const path = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = require('fs').readFileSync(path).toString().trim();

let arr = Array.from(26);
let num = 97;

for(let i=0; i<26; i++){
  arr[i] = String.fromCharCode(num);
  num++;
}

for(let j=0; j<26; j++){
  arr[j] = input.split(arr[j]).length-1
}

console.log(arr.join(' '))