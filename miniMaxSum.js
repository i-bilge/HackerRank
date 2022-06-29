let arr = [1,3,5,7,9];

function miniMaxSum(array) {
    // Write your code here
    let maxVal = Math.max(...array);
    let minVal = Math.min(...array);
    let sum = 0;
    array.forEach(element => {
        sum += element;
    });
    console.log(sum-maxVal, sum-minVal);
}

miniMaxSum(arr);