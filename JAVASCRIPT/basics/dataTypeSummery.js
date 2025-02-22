// primitive data type

// Number
// Boolean
// String
// null
// undefined
// BigInt
// symbol

//dynamically Typed : JS

const PI = 3.14;

let userEmail; //let userEmail = undefined; //same

const Id = Symbol('314');
const anotherId = Symbol('314');

// console.log(Id == anotherId);

const bigNumber = 5327344326257257615326015713n

// console.log(typeof bigNumber);
// console.log(bigNumber);

let oneNumber = 5;
let anotherNumber = '5'

// console.log(oneNumber === anotherNumber);

//== : value
// === : value and data type

//NOT-PROMITIVE DATA TYPES
//RFERENCE

const bestAnimes = ['naruto', 'blue-lock' , 'demon-slayer', ['zero','one' , 'two', 'three']]
// console.log(bestAnimes[3][2]);

const myObj = {
    name : 'Satyanshu',
    age : 34,
    email : 'Satyanshu.bhardwaj123@gmail.com',
    favHeroes : [3435, 'iron-man', 'black-panther']
}

// console.log(myObj.email);
// console.log(myObj.favHeroes[0]);
// myObj.email = 'BharwdajSatyanshu@gmail.com'
// console.log(myObj.email);


// console.log(myObj); //

let name = 'Satyanshu';
let newName = name;
newName = 'Vikas'

console.log(name);
console.log(newName);



let marvelHeroes = ['cpatian-america', 'rocket', 'groot' , 'iron-man']

let newMarvelHeroes = marvelHeroes;
newMarvelHeroes[0] = 'sam';

console.log(marvelHeroes);
console.log(newMarvelHeroes);



