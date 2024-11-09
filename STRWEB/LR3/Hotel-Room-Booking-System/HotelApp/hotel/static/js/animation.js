const palmLeft = document.querySelector('#palm_left');
const palmRight = document.querySelector('#palm_right');
const text = document.querySelector('#text');
const chair = document.querySelector('#chair');

window.addEventListener('scroll', () => {
    let value = window.scrollY;
    palmLeft.style.left = `-${value / 0.5}px`;
    palmRight.style.left = `${value / 0.5}px`;
    text.style.bottom = `-${value}px`;
    chair.style.height = `${window.innerHeight + value}px`
});