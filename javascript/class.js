class User {
    constructor(firstName, lastName, age){
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }

    get age(){
        return this._age;
    }

    set age(value){
        this._age = value > 0 ? value : 0;
    }
}

const user = new User('Steve', 'Jobs', -1);
console.log(user.age);

const user1 = new User('Steve', 'Jobs', 30);
console.log(user1.age);