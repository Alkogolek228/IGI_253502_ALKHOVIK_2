// Base class
function Car(brand, number) {
    this.brand = brand;
    this.number = number;
}

Car.prototype.getBrand = function() {
    return this.brand;
};

Car.prototype.setBrand = function(brand) {
    this.brand = brand;
};

Car.prototype.getNumber = function() {
    return this.number;
};

Car.prototype.setNumber = function(number) {
    this.number = number;
};

// Derived class
function CarOwner(brand, number, owner) {
    Car.call(this, brand, number);
    this.owner = owner;
}

CarOwner.prototype = Object.create(Car.prototype);
CarOwner.prototype.constructor = CarOwner;

CarOwner.prototype.getOwner = function() {
    return this.owner;
};

CarOwner.prototype.setOwner = function(owner) {
    this.owner = owner;
};

CarOwner.prototype.addCar = function(carArray) {
    const brand = document.getElementById('brand').value;
    const number = document.getElementById('number').value;
    const owner = document.getElementById('owner').value;
    const car = new CarOwner(brand, number, owner);
    carArray.push(car);
    this.displayCars(carArray);
};

CarOwner.prototype.displayCars = function(carArray) {
    const carList = document.getElementById('car-list');
    carList.innerHTML = '';
    carArray.forEach(car => {
        const carItem = document.createElement('div');
        carItem.textContent = `Марка: ${car.getBrand()}, Номер: ${car.getNumber()}, Владелец: ${car.getOwner()}`;
        carList.appendChild(carItem);
    });
};

CarOwner.prototype.searchCars = function(carArray, brand) {
    const results = carArray.filter(car => car.getBrand().toLowerCase() === brand.toLowerCase());
    const searchResults = document.getElementById('search-results');
    searchResults.innerHTML = '';
    results.forEach(car => {
        const resultItem = document.createElement('div');
        resultItem.textContent = `Номер: ${car.getNumber()}, Владелец: ${car.getOwner()}`;
        searchResults.appendChild(resultItem);
    });
};

document.addEventListener('DOMContentLoaded', function() {
    const carArray = [];
    const carOwner = new CarOwner();

    document.getElementById('car-form').addEventListener('submit', function(event) {
        event.preventDefault();
        carOwner.addCar(carArray);
    });

    document.getElementById('search-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const brand = document.getElementById('search-brand').value;
        carOwner.searchCars(carArray, brand);
    });
});