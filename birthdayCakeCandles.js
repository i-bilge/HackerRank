let candles = [3, 2, 1,3];

function birthdayCakeCandles(arr) {
    // Write your code here
    let maxVal = Math.max(...arr);
    let count = 0;

    arr.forEach(element => {
        if (element == maxVal) {
            count += 1;
        }
    });
    return count;
}

console.log(birthdayCakeCandles(candles));