const notes = [73,67,38,33];

function gradingStudents(grades) {
    // Write your code here
    let newArr = [];
    grades.forEach(e => {
        if (e >= 38) {
            let dif = 5-(e%5);
            if (dif < 3) {
                e = e+dif;
                newArr.push(e);
            } else {
                newArr.push(e);
            }
        } 
        else {
            newArr.push(e);
        }
    });
    return newArr;
}

console.log(gradingStudents(notes));