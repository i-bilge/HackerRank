const st = "11:05:45PM";

function timeConversion(s) {
    let hourTipe = s.substring(8,10);
    let hour = s.substring(0,2);
    let emptyS = s.substring(2,8);
    let newHour;

    if (hourTipe == "PM" && hour != 12) {
        newHour = Number(hour)+12;
    } 
    else if (hourTipe == "AM" && hour == 12){
        newHour = "00";
    }
    else newHour = hour;
    return newHour + emptyS;
}

console.log(timeConversion(st));