// Ways to declare a variable
// var, let, const
// var is original declaration, not used now as it globalizes a variable and introduces issues

// Naming Conventions
// - Only letters, numbers, underscores and dollar signs
// - Can't start with a number

// Multi-Word Formatting
// firstName     camelCase
// first_name    underscore
// FirstName     PascalCase
// firstname     lowercase

let firstName = 'John';
let lastName = 'Doe';

console.log(firstName, lastName);

let age = 30;
console.log(age);

//  can reassign variable later on

age = 31;
console.log(age);

let score;

score = 1;
if (true) {
  score = score + 1;
}

console.log(score);

const x = 100;
// cannot reassign const, also cant initialize with value

//  arrays
const arr = [1, 2, 3, 4];
arr.push(5);
console.log(arr);

const person = {
  name: 'Liam',
};
console.log(person);
person.name = 'Brad';
person.email = 'Brad@gmail.com';

console.log(person);

//  declare mult vars
