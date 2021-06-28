fruits = new Array();
fruits = ['apple', 'banana'];

for (key in fruits) {
    console.log(key);
}

for (value of fruits) {
    console.log(value); 
}

fruits.forEach((fruit) => console.log(fruit));
fruits.push('pear');
fruits.push('strawberry');
console.log(fruits); 

console.clear();
const result = fruits.join(',');
console.log(result);
const arr = result.split(',');
console.log(arr);
const reverseArr = fruits.reverse();
console.log(reverseArr);
const partialArr = fruits.splice(0,2);
console.log(partialArr);

console.clear();

class Student {
    constructor(name, age, enrolled, score) {
        this.name = name;
        this.age = age,
        this.enrolled = enrolled,
        this.score = score
    }
}
const students = [
    new Student('A', 29, true, 45),
    new Student('B', 28, false, 80),
    new Student('C', 30, true, 90),
    new Student('D', 40, false, 66),
    new Student('E', 18, true, 88),
];
//Q1. find a student wiht the score 90
const result1 = students.find((student, index) => student.score === 90);
console.log(result1);

console.clear();
//Q2. make an array of enrolled students
const result2 = students.filter((student) => student.enrolled === true);
console.log(result2);
console.clear();
//Q3. make an array containing only the student's scores
// result should be : [45, 80, 90, 66, 88]
const result3 = students.map((student) => student.score);
console.log(result3);
console.clear();

//Q4. check if there is a student with the score lower than 50
const result4 = students.some((student) => student.score < 50);
console.log(result4)

//Q5. compute student's average score
console.clear();
/**
 * Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, 
 * and is provided as an argument in the next call to the callback function.
 * @param callbackfn A function that accepts up to four arguments. 
 * The reduce method calls the callbackfn function one time for each element in the array.
 * @param initialValue If initialValue is specified, it is used as the initial value to start the accumulation. 
 * The first call to the callbackfn function provides this value as an argument instead of an array value.
 */
// reduce(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: readonly T[]) => T): T;
// reduce(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: readonly T[]) => T, initialValue: T): T;
const result5 = students.reduce((prev, cur) => prev+cur.score, 0);
console.log(result5/students.length);

//Q6. make a strin containing all the scores
//reslt should be:'45, 80, 90, 66, 88'
console.clear();
const result6 = (students.map((student) => student.score)).sort((a,b)=> b-a).join(', ');
console.log(result6);
