const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./LJH/input.txt";
let input = fs.readFileSync(filePath).toString().split(" ").map(Number);
let [month, day] = input;
for (let i = month - 1; i >= 1; i--) {
    switch (i) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            day += 31;
            break;
        case 4:
        case 6:
        case 9:
        case 11:
            day += 30;
            break;
        case 2:
            day += 28;
            break;
    }
}

switch (day % 7) {
    case 0:
        console.log("SUN");
        break;
    case 1:
        console.log("MON");
        break;
    case 2:
        console.log("TUE");
        break;
    case 3:
        console.log("WED");
        break;
    case 4:
        console.log("THU");
        break;
    case 5:
        console.log("FRI");
        break;
    case 6:
        console.log("SAT");
        break;
}
