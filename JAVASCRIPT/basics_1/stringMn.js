const name = 'Vikas Payal'
const age = 17

// console.log("name : " + name + "\nage : "  + age); // bad way

// console.log(`my name is ${name} and my age is ${age}`); // good way

//proper way of initialization of string

const newName = new String('Vikas Payal')

// console.log(newName[2]); // k
// console.log(newName.__proto__);

// console.log(newName.length);
// console.log(newName.toLocaleLowerCase());
// console.log(newName.toLocaleUpperCase());
// console.log(newName.charAt(2));

// console.log(newName.indexOf('z'));
// console.log(newName);
const firstName = newName.slice(6,2);
// console.log(firstName);

const subString = newName.substring(5,2);
// console.log(subString);

const anotherName = "     Satyanshu          "
// console.log(anotherName);

// console.log(anotherName.trim());

const ytUrl = 'https://www.youtube.com/results?search_query=hello'
const correctedYtUrl = ytUrl.replace('?','-');
// console.log(ytUrl);
// console.log(correctedYtUrl);

const paragraph = 'hello this is satyanshu bhardwaj'
const splittedPara = paragraph.split(' ')
console.log(paragraph);
console.log(splittedPara);

console.log(`the name in the above para is ${splittedPara[3]} ${splittedPara[4]}`);







// console.log(newName);

// console.log(newName);
// console.log(newName);



