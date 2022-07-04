//How many apples and oranges are falled to house?

let s = 7;      //start point of house
let t = 11;     //end point of house
let a = 5;      //apple tree
let b = 15;     //orange tree
let apples = [-2, 2, 1];//falled apples
let oranges = [5, -6];  //falled oranges

function countApplesAndOranges(s, t, a, b, apples, oranges) {
    // Write your code here
    let countA = 0;
    let countB = 0;
    apples.forEach(e => {
        let x = e+a;
        if (x >= s && x <= t) {
            countA += 1;
        }
    });
    oranges.forEach(e => {
        let x = e+b;
        if (x >= s && x <= t) {
            countB += 1;
        }
    });
    console.log(countA);
    console.log(countB);
}
countApplesAndOranges(s, t, a, b, apples, oranges);