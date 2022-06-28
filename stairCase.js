n = 8;

function staircase(num) {
    // Write your code here
    for (let i = 1; i <= num; i++) {
        console.log(" ".repeat(num-i) + "#".repeat(i));
    }
}
staircase(n);

//With arrow Function
let stairCase = num => {
    for (let i = 1; i <= num; i++) {
        console.log(" ".repeat(num-i) + "#".repeat(i));
    }
}
stairCase(n)