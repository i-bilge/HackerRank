// Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

// Lily decides to share a contiguous segment of the bar selected such that:

// The length of the segment matches Ron's birth month, and,
// The sum of the integers on the squares is equal to his birth day.
// Determine how many ways she can divide the chocolate.

// Example
// s = [2,2,1,3,2]
// d= 4
// m= 2

// Lily wants to find segments summing to Ron's birth day, d=4  with a length equalling his birth month, m=2. In this case, there are two segments meeting her criteria:  [2,2]and [1,3].

// Function Description

// Complete the birthday function in the editor below.

// birthday has the following parameter(s):

// int s[n]: the numbers on each of the squares of chocolate
// int d: Ron's birth day
// int m: Ron's birth month
// Returns

// int: the number of ways the bar can be divided

//------------SOLUTION------------------
const s = [1,2,1,3,2];
const d= 3;
const m= 2;



function birthday(s, d, m) {
    // Write your code here
    function splitArrayIntoSubs(arr, len) {
        var chunks = [], i = 0, n = arr.length;
        while (i+len < n) {
          chunks.push(arr.slice(i, i+len));
          i++
        }
        return chunks;
      }
    let subArrays=splitArrayIntoSubs(s,m);
    let counter = 0;
    subArrays.forEach(el => {
        const sum = el.reduce((partialSum, a) => partialSum + a, 0);
        if (sum == d) counter++
    });
    console.log(counter);
}



  birthday(s, d, m)