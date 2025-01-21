console.log("Lab 1 is running!");
import _ from 'lodash';

const holidays = [
    { name: "Christmas", date: new Date("2025-12-25") },
    { name: "Canada Day", date: new Date("2025-07-01") },
    { name: "April Fools", date: new Date("2025-04-01") },
];

let today = new Date();

holidays.forEach(holiday => {
    let dateDifference = holiday.date - today;
    let numDays = Math.ceil(dateDifference / (1000 * 60 * 60 * 24)); 
    console.log(`${holiday.name} is in ${numDays} days!`);
});

console.log(_.sample(holidays));
console.log(_.findIndex(holidays, { name: "Christmas" }));
console.log(_.findIndex(holidays, { name: "April Fools" })); 
