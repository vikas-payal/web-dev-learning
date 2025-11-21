// There are three ways to declare variable and constants in js 
//const 
//var
//let

const account_id=123;
var email_id="Vikas@gmail.com";
let password="DIS234";
// account_city="jaipur"; 
let isLoggedIn;

let test = true;
if(test){
    let name = "sahil"
    console.log(name)
}

if(!test){
    let name = "vikas"
    console.log(name)
}

//var is not used for declaration as it doesnt have scope functionalities

// console.log(account_id);
// console.log(email_id);
// console.log(password);
// console.log(account_city);

//Cannot assign to const
// account_id=325;

// isLoggedIn = true;

//log uisng console.table
console.table([
    account_id,
    email_id,
    password,
    isLoggedIn
    // account_city
])

// console.log(typeof(account_city));