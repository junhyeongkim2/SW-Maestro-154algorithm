const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
// let input = fs.readFileSync(filePath).toString().trim();
// console.log([...input].sort().join(""));
let input = fs.readFileSync(filePath).toString().trim(); // trim 없으면 '출력 형식이 잘못되었습니다.' 뜸.
let temp = input[0];
for (let i = 1; i < input.length; i++) {
    if (temp[i - 1] < input[i]) temp = input[i] + temp;
    else temp = temp + input[i];
}
temp = temp.split("").reverse().join("");
console.log(temp);

//결국은 정렬 문제 아닌가? 왜 sort함수 써서 정렬하면 틀렸다고 나오지?
