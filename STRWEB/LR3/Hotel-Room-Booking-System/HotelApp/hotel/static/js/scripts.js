document.addEventListener("DOMContentLoaded", function() {
    const countdownElement = document.getElementById('countdown');
    const countdownDuration = 60 * 60 * 1000; // 1 hour in milliseconds

    // Get the end time from localStorage or set it to 1 hour from now
    let endTime = localStorage.getItem('countdownEndTime');
    if (!endTime) {
        endTime = Date.now() + countdownDuration;
        localStorage.setItem('countdownEndTime', endTime);
    }

    function updateCountdown() {
        const now = Date.now();
        const timeLeft = endTime - now;

        if (timeLeft <= 0) {
            countdownElement.textContent = "Time's up!";
            localStorage.removeItem('countdownEndTime');
        } else {
            const hours = Math.floor((timeLeft / (1000 * 60 * 60)) % 24);
            const minutes = Math.floor((timeLeft / (1000 * 60)) % 60);
            const seconds = Math.floor((timeLeft / 1000) % 60);

            countdownElement.textContent = `${hours}h ${minutes}m ${seconds}s`;
        }
    }

    // Update the countdown every second
    setInterval(updateCountdown, 1000);
    updateCountdown();
});

document.addEventListener("DOMContentLoaded", function() {
    const birthdateForm = document.getElementById('birthdate-form');
    const birthdateInput = document.getElementById('birthdate');
    const messageElement = document.getElementById('message');
    const parentalConsentGroup = document.getElementById('parental-consent-group');
    const parentalConsentCheckbox = document.getElementById('parental-consent');
    const dayOfWeekMessage = document.getElementById('day-of-week-message');

    // Проверка, если возраст уже сохранен в сессии
    if (!sessionStorage.getItem('ageVerified')) {
        $('#birthdateModal').modal('show');
    }

    birthdateInput.addEventListener('change', function() {
        const birthdate = new Date(birthdateInput.value);
        const today = new Date();
        let age = today.getFullYear() - birthdate.getFullYear();
        const monthDifference = today.getMonth() - birthdate.getMonth();
        const dayDifference = today.getDate() - birthdate.getDate();

        if (monthDifference < 0 || (monthDifference === 0 && dayDifference < 0)) {
            age--;
        }

        const daysOfWeek = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"];
        const dayOfWeek = daysOfWeek[birthdate.getDay()];

        dayOfWeekMessage.textContent = `День недели вашего рождения: ${dayOfWeek}.`;

        if (age >= 18) {
            messageElement.textContent = `Вы совершеннолетний.`;
            parentalConsentGroup.style.display = 'none';
        } else {
            parentalConsentGroup.style.display = 'block';
        }
    });

    birthdateForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const birthdate = new Date(birthdateInput.value);
        const today = new Date();
        let age = today.getFullYear() - birthdate.getFullYear();
        const monthDifference = today.getMonth() - birthdate.getMonth();
        const dayDifference = today.getDate() - birthdate.getDate();

        if (monthDifference < 0 || (monthDifference === 0 && dayDifference < 0)) {
            age--;
        }

        const daysOfWeek = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"];
        const dayOfWeek = daysOfWeek[birthdate.getDay()];

        if (age >= 18) {
            messageElement.textContent = `Вы совершеннолетний. День недели вашего рождения: ${dayOfWeek}.`;
            $('#birthdateModal').modal('hide');
            sessionStorage.setItem('ageVerified', 'true');
        } else {
            if (parentalConsentCheckbox.checked) {
                messageElement.textContent = `Вы несовершеннолетний. День недели вашего рождения: ${dayOfWeek}. Разрешение родителей получено.`;
                $('#birthdateModal').modal('hide');
                sessionStorage.setItem('ageVerified', 'true');
            } else {
                alert("Вы несовершеннолетний. Вам необходимо разрешение родителей на использование сайта.");
            }
        }
    });

    // Пагинация
    const roomCards = document.querySelectorAll('.room-card');
    const paginationLinks = document.querySelectorAll('.page-link');

    function showPage(page) {
        roomCards.forEach((card, index) => {
            card.style.display = (index === page - 1) ? 'block' : 'none';
        });
    }

    paginationLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const page = parseInt(this.getAttribute('data-page'));
            showPage(page);
        });
    });

    // Показать первую страницу по умолчанию
    showPage(1);

    // Эффект параллакса
    const body = document.querySelector('body');
    const cards = document.querySelectorAll('.parallax-card .card-body');
    const walk = { x: 20, y: 15 };

    function parallax(e) {
        cards.forEach(card => {
            const width = card.offsetWidth;
            const height = card.offsetHeight;
            let { offsetX: x, offsetY: y } = e;

            const xWalk = Math.round((e.x / width / 2 * walk.x) - (walk.x / 2));
            const yWalk = Math.round((e.y / height / 2 * walk.y) - (walk.y / 2));

            card.style.transform = `rotateY(${-xWalk}deg) rotateX(${yWalk}deg)`;
        });
    }

    body.addEventListener('mousemove', parallax);
});

document.addEventListener('DOMContentLoaded', function () {
    const sliderContainer = document.querySelector('.slider-container');
    const slider = document.querySelector('.slider');
    const slides = document.querySelectorAll('.slide');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    const pagination = document.querySelector('.pagination');
    let currentIndex = 0;
    let autoSlideInterval;
    const settings = {
        loop: true,
        navs: true,
        pags: true,
        auto: true,
        stopMouseHover: true,
        delay: 5 // seconds
    };

    function updateSlider() {
        slider.style.transform = `translateX(-${currentIndex * 100}%)`;
        updatePagination();
    }

    function nextSlide() {
        if (currentIndex < slides.length - 1) {
            currentIndex++;
        } else if (settings.loop) {
            currentIndex = 0;
        }
        updateSlider();
    }

    function prevSlide() {
        if (currentIndex > 0) {
            currentIndex--;
        } else if (settings.loop) {
            currentIndex = slides.length - 1;
        }
        updateSlider();
    }

    function updatePagination() {
        if (settings.pags) {
            pagination.querySelectorAll('div').forEach((dot, index) => {
                dot.classList.toggle('active', index === currentIndex);
            });
        }
    }

    function startAutoSlide() {
        if (settings.auto) {
            autoSlideInterval = setInterval(nextSlide, (settings.delay || 5) * 1000);
        }
    }

    function stopAutoSlide() {
        clearInterval(autoSlideInterval);
    }

    if (settings.navs) {
        prevButton.addEventListener('click', prevSlide);
        nextButton.addEventListener('click', nextSlide);
    } else {
        prevButton.style.display = 'none';
        nextButton.style.display = 'none';
    }

    if (settings.pags) {
        pagination.innerHTML = '';
        slides.forEach((_, index) => {
            const dot = document.createElement('div');
            dot.addEventListener('click', () => {
                currentIndex = index;
                updateSlider();
            });
            pagination.appendChild(dot);
        });
        updatePagination();
    } else {
        pagination.style.display = 'none';
    }

    if (settings.auto) {
        startAutoSlide();
        if (settings.stopMouseHover) {
            sliderContainer.addEventListener('mouseenter', stopAutoSlide);
            sliderContainer.addEventListener('mouseleave', startAutoSlide);
        }
    }
});