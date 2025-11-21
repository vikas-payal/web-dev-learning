let name = "vikas"
let animals = ['dog', 'cat' , 'fish', 'raccoon' , 'lion']
// for(let charInName in name){
//     console.log(name[charInName])
// }

for(let animal in animals){
    // console.log(animals[animal]);
}

let salary = {
    'rahul' : 5000,
    'sumit' : 3000,
    'rohit' : 6000
}

for(let person in salary){
    console.log(`${person} : ${salary[person]}`);
    
}

// for (let i = 0; i< 10 ; i++){
//     // if (i === 5) {
//     //     break;
//     // }
//     console.log('hi');
// }

// let count = 50;

// while (count > 0) {
//     console.log('bye');
//     count = count -10;
// }