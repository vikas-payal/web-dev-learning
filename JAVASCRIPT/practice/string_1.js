//there is a string named files and has data : 'avengers.mp4, sonic.mp4, johnWick.mp4, pokemon.mp4, pulpFiction.mp4'
// i want to log each movie as 
// movie1 : avenger
// movie2 : sonic
// and so on

const movieName='avengers.mp4, sonic.mp4, johnWick.mp4, pokemon.mp4, pulpFiction.mp4'

// let arrMovie=movieName.split(', ')
let arrMovie=movieName.split(', ').map(file => file.replace('.mp4', ''))


// arrMovie[0] = arrMovie[0].replace('.mp4','')
// arrMovie[1] = arrMovie[1].replace('.mp4','')
// arrMovie[2] = arrMovie[2].replace('.mp4','')
// arrMovie[3] = arrMovie[3].replace('.mp4','')
// arrMovie[4] = arrMovie[4].replace('.mp4','')

console.log(arrMovie);


// Name=splitMovie[1].split(" ")
// Name2=splitMovie[2].split(" ")
// Name3=splitMovie[3].split(" ")
// Name4=splitMovie[4].split(" ")

for(movie in arrMovie){
console.log(`movie : ${arrMovie[movie]}`);
}
           








