document.addEventListener("DOMContentLoaded", loadContacts);

let contacts = [];
let currentPage = 1;
const itemsPerPage = 3;

async function loadContacts() {
    toggleLoader(true);
    try {
        const response = await fetch('/contact/', {
            headers: {
                'x-requested-with': 'XMLHttpRequest'
            }
        });
        const text = await response.text();
        try {
            contacts = JSON.parse(text);
            console.log('Contacts loaded:', contacts);
            displayTable();
        } catch (e) {
            console.error('Failed to parse JSON:', e);
            console.error('Response text:', text);
        }
    } finally {
        toggleLoader(false);
    }
}

function toggleLoader(show) {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        preloader.style.display = show ? 'flex' : 'none';
    }
}

function displayTable() {
    toggleLoader(true);
    const tbody = document.querySelector("#contactsTable tbody");
    tbody.innerHTML = '';
    let pageData = contacts.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);
    pageData.forEach(contact => {
        let row = tbody.insertRow();
        row.innerHTML = `
            <td>${contact.name}</td>
            <td>${contact.description}</td>
            <td>${contact.phonenumber}</td>
            <td>${contact.email}</td>
            <td><img src="/partners/${contact.img}" width="100"/></td>
            <td><input type="checkbox" class="contactCheckbox" data-id="${contact.id}"></td>
        `;
        row.onclick = () => showContactDetails(contact);
    });
    displayPagination();
    toggleLoader(false);
}

function displayPagination() {
    const paginationDiv = document.getElementById("pagination");
    paginationDiv.innerHTML = '';
    const totalPages = Math.ceil(contacts.length / itemsPerPage);

    for (let i = 1; i <= totalPages; i++) {
        let pageLink = document.createElement('button');
        pageLink.textContent = i;
        pageLink.onclick = () => {
            currentPage = i;
            displayTable();
        };
        paginationDiv.appendChild(pageLink);
    }
}

function sortTable(column) {
    contacts.sort((a, b) => {
        if (a[column] < b[column]) return -1;
        if (a[column] > b[column]) return 1;
        return 0;
    });
    displayTable();
}

function filterTable() {
    const filterText = document.getElementById("filter").value.toLowerCase();
    contacts = contacts.filter(contact => 
        contact.name.toLowerCase().includes(filterText) ||
        contact.description.toLowerCase().includes(filterText) ||
        contact.phonenumber.includes(filterText) ||
        contact.email.toLowerCase().includes(filterText)
    );
    displayTable();
}

function showContactDetails(contact) {
    document.getElementById("selectedContact").innerHTML = `
        <p>ФИО: ${contact.name}</p>
        <p>Описание: ${contact.description}</p>
        <p>Телефон: ${contact.phonenumber}</p>
        <p>Email: ${contact.email}</p>
        <img src="/partners/${contact.img}" width="100" />
    `;
}
function showAddForm() {
    document.getElementById("addForm").style.display = "block";
}

function validatePhone() {
    const phone = document.getElementById("phonenumber").value;
    const isValid = /^(\+375|8)[ ]?(\(\d{2}\))[ ]?\d{3}[ -]?\d{2}[ -]?\d{2}$/.test(phone);
    document.getElementById("phoneValidation").textContent = isValid ? '' : 'Неверный формат телефона';
    toggleValidation("phonenumber", isValid);
}

function validateUrl() {
    const url = document.getElementById("imgUrl").value;
    const isValid = /^(https?:\/\/).+\.(php|html)$/.test(url);
    document.getElementById("urlValidation").textContent = isValid ? '' : 'Неверный формат URL';
    toggleValidation("imgUrl", isValid);
}

function toggleValidation(id, isValid) {
    const element = document.getElementById(id);
    element.classList.toggle("invalid", !isValid);
}

async function addContact(event) {
    event.preventDefault(); // Предотвратить отправку формы по умолчанию

    const form = document.getElementById('contactForm');
    const formData = new FormData(form);

    try {
        const response = await fetch('/add_contact/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: new URLSearchParams(formData)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        if (result.status === 'success') {
            contacts.push(result.contact);
            displayTable();
            form.reset();
            alert('Сотрудник успешно добавлен');
        } else {
            alert('Ошибка при добавлении сотрудника');
        }
    } catch (error) {
        console.error('Error adding contact:', error);
        alert('Ошибка при добавлении сотрудника');
    }
}

async function updateContactDescription(contactId, newDescription) {
    const response = await fetch('/update_contact_description/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken') // Получите CSRF токен
        },
        body: new URLSearchParams({
            'id': contactId,
            'description': newDescription
        })
    });

    const result = await response.json();
    if (result.status === 'success') {
        console.log(`Description for contact ID ${contactId} updated successfully`);
    } else {
        console.error(`Failed to update description for contact ID ${contactId}:`, result.message);
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function generateBonus() {
    const checkboxes = document.querySelectorAll('.contactCheckbox');
    const selectedContacts = [];

    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            const contactId = checkbox.getAttribute('data-id');
            const selectedContact = contacts.find(contact => contact.id == contactId);
            if (selectedContact) {
                selectedContacts.push(selectedContact);
            }
        }
    });

    if (selectedContacts.length > 0) {
        const rewardedContacts = [];
        selectedContacts.forEach(contact => {
            const newDescription = prompt(`Введите новое описание для сотрудника ${contact.name}:`, contact.description);
            if (newDescription !== null) {
                updateContactDescription(contact.id, newDescription);
                contact.description = newDescription;
                rewardedContacts.push(contact.name);
            }
        });
        displayTable();
        displayRewardedContacts(rewardedContacts);
    } else {
        alert('Пожалуйста, выберите сотрудников для премирования.');
    }
}

function displayRewardedContacts(rewardedContacts) {
    const rewardedContactsDiv = document.getElementById('rewardedContacts');
    rewardedContactsDiv.innerHTML = '<h3>Премированные сотрудники:</h3>';
    rewardedContacts.forEach(name => {
        const p = document.createElement('p');
        p.textContent = name;
        rewardedContactsDiv.appendChild(p);
    });
}

let sortDirection = {}; // Объект для хранения направления сортировки для каждого столбца

function sortTable(columnIndex) {
    const table = document.getElementById("contactsTable");
    const tbody = table.querySelector("tbody");
    const rows = Array.from(tbody.rows);

    // Определите направление сортировки
    if (!sortDirection[columnIndex]) {
        sortDirection[columnIndex] = 'asc';
    } else {
        sortDirection[columnIndex] = sortDirection[columnIndex] === 'asc' ? 'desc' : 'asc';
    }

    // Сортировка строк
    rows.sort((a, b) => {
        const cellA = a.cells[columnIndex].innerText.toLowerCase();
        const cellB = b.cells[columnIndex].innerText.toLowerCase();

        if (cellA < cellB) {
            return sortDirection[columnIndex] === 'asc' ? -1 : 1;
        }
        if (cellA > cellB) {
            return sortDirection[columnIndex] === 'asc' ? 1 : -1;
        }
        return 0;
    });

    // Обновите таблицу
    tbody.innerHTML = '';
    rows.forEach(row => tbody.appendChild(row));

    // Обновите иконку направления сортировки
    updateSortIcons(columnIndex);
}

function updateSortIcons(columnIndex) {
    const icons = document.querySelectorAll('th span[id^="sortIcon"]');
    icons.forEach(icon => icon.innerText = ''); // Очистите все иконки

    const sortIcon = document.getElementById(`sortIcon${columnIndex}`);
    sortIcon.innerText = sortDirection[columnIndex] === 'asc' ? '▲' : '▼';
}
