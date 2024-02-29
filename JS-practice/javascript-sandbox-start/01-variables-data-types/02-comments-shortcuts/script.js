// single line of code comment
//  cntrl / auto comments, can also use on already written line of code

/*
comments for 
for mutiple 
lines of code
*/

console.log(100);
console.log('Hello World');
console.log(20, 'hello', true);

const x = 100;
console.log(x);

console.error('Alert');

console.warn('warning');

console.table({ name: 'brad', email: 'brad@gmail.com' });

console.group('simple');
console.log(x);
console.error('Alert');
console.warn('Warning');
console.groupEnd();

const styles = 'padding: 10px; background-color: white; color: green;';

console.log('%c Hello World', styles);
