//number -> 2 to the power 52
//bigInt //rarely use
//string 
//boolean

//null
//undefined

//symbol

let name  = "vikas payal";
let age = 17;
let isLoggedIn = 1;

const score = 33;

let scoreInNumber = Number(score);

let newScore = score;
newScore = newScore + 1;

console.log(newScore);

console.log (typeof score);
console.log (typeof(scoreInNumber));
console.log(scoreInNumber);

if(isLoggedIn) console.log("user Logged In");
else console.log("user logged out");



// if (!isNaN(score)) {
//     let scoreInNumber = Number(score);
//     console.log(typeof scoreInNumber + ':' + scoreInNumber);
// }
// else{
//     let scoreInString = String(score);
//     console.log(typeof scoreInString + ':' + scoreInString);
// }


// console.table(
//     [
//         typeof(name),
//         typeof(age),
//         typeof(isLoggedIn),
//     ]
// );
    
