const input = document.getElementById('input');
const clickbutton = document.getElementById('button');
const list = document.getElementById('list');
const button = document.getElementById('btn');

clickbutton.addEventListener('click', () => {
    addTask();
});

const state = {
    notes: [
        {text: '', status: true},
    ],
    filters: 'all'
};

input.addEventListener('keydown', (ev) => {
    if (ev.key === 'Enter') {
        ev.preventDefault();
        addTask();
    }
});

function addTask() {
    if (input.value !== '') {
        const li = document.createElement('li');
        li.textContent = input.value;

        const deleteOneButton = document.createElement('button');
        li.appendChild(deleteOneButton);
        deleteOneButton.textContent = "Delete";

        const doneButton = document.createElement('button');
        doneButton.textContent = 'Done';
        li.appendChild(doneButton);

        list.appendChild(li);
        input.value = '';

        updateDeleteAllButton();

        deleteOneButton.addEventListener('click', () => {
            li.remove();
            updateDeleteAllButton();
        });

        doneButton.addEventListener('click', () => {
            li.style.textDecoration = 'line-through';
        });
    }
}

function updateDeleteAllButton() {
    const deleteAllButton = document.getElementById('delete-all-button');

    if (list.childNodes.length > 0 && !deleteAllButton) {
        const newDeleteAllButton = document.createElement('button');
        newDeleteAllButton.id = 'delete-all-button';
        newDeleteAllButton.textContent = 'Delete all';
        button.appendChild(newDeleteAllButton);

        newDeleteAllButton.addEventListener('click', () => {
            list.innerHTML = '';
            newDeleteAllButton.remove();
        });
    } else if (list.childNodes.length === 0 && deleteAllButton ) {
        deleteAllButton.remove();
    }
}
