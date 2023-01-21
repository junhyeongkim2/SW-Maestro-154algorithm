const path = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = Number(require("fs").readFileSync(path).toString());

for (let i = 0; i < 9; i++) {
  console.log(`${input} * ${i + 1} = ${input * (i + 1)}`);
}
