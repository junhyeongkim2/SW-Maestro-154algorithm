const path = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = require('fs').readFileSync(path).toString().trim().split('');

let stack = [];
let answer = 0;

for(var i in input){
    if(input[i] === '('){
        stack.push(input[i]);
    }else{
        if(input[i-1] === '('){
            stack.pop();
            answer += stack.length;
        }else{
            stack.pop();
            answer ++;
        }
    }
}
console.log(answer);