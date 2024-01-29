const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = fs.readFileSync(filePath).toString().split(" ").map(Number);
let [month, day] = input;
const week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
console.log(week[new Date(`2007-${month}-${day}`).getDay()]);
