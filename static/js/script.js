'use strict';
window.addEventListener('load', () => {
    handleOperationChange();
    setupFormSubmit();
});

window.addEventListener('hashchange', () => {
    handleOperationChange();
});

function handleOperationChange() {
    let url = new URL(location.href);
    let operation = 'encrypt';

    if (url.hash == '#decrypt') {
        operation = 'decrypt';
    }

    let actions = document.querySelectorAll('a[class*="operation-action"]');
    actions.forEach(action => {
        if (action.getAttribute('data-id') === operation) {
            action.classList.add('selected');
        } else {
            action.classList.remove('selected');
        }
    })
    let sections = document.querySelectorAll('div[class*="operation-section"]');
    sections.forEach(section => {
        if (section.getAttribute('data-id') === operation) {
            section.classList.add('selected');
        } else {
            section.classList.remove('selected');
        }
    })
}

function setupFormSubmit() {
    let encrypt_form = document.querySelector('form[name="encrypt"]');
    if (encrypt_form) {
        encrypt_form.addEventListener('submit', (event) => {
            handleEncryptFormSubmit(event);
        })
    }

    let decrypt_form = document.querySelector('form[name="decrypt"]');
    if (decrypt_form) {
        decrypt_form.addEventListener('submit', (event) => {
            handleDecryptFormSubmit(event);
        })
    }
}

function handleEncryptFormSubmit(event) {
    let formData = new FormData(event.target);
    let submitButton = document.querySelector('input[type="submit"][data-button="encrypt"]');
    if (submitButton) {
        submitButton.value = 'Encrypting...';
    }

    if (formData && formData.get('message') != "") {
        let messageTextarea = document.getElementById('message');
        messageTextarea.classList.remove('error');

        let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                let response = JSON.parse(this.responseText);

                if (response.status === 'success') {
                    let cipherOutput = document.querySelector('div[id="cipher-output"]');
                    if (cipherOutput) {
                        cipherOutput.innerText = response.cipher;
                    }
                }

                let submitButton = document.querySelector('input[type="submit"][data-button="encrypt"]');
                if (submitButton) {
                    submitButton.value = 'Encrypt';
                }
            }
        };
        xhttp.open("POST", "/encrypt/", true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send(`message=${formData.get('message')}`);
    } else {
        let messageTextarea = document.getElementById('message');
        messageTextarea.classList.add('error');

        submitButton.value = 'Encrypt';
    }

    event.preventDefault();
}

function handleDecryptFormSubmit(event) {
    let formData = new FormData(event.target);
    let submitButton = document.querySelector('input[type="submit"][data-button="decrypt"]');
    if (submitButton) {
        submitButton.value = 'Decrypting...';
    }

    if (formData && formData.get('cipher') != "") {
        let cipherTextarea = document.getElementById('cipher');
        cipherTextarea.classList.remove('error');

        let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                let response = JSON.parse(this.responseText);

                if (response.status === 'success') {
                    let messageOutput = document.querySelector('div[id="message-output"]');
                    if (messageOutput) {
                        messageOutput.innerText = response.message;
                    }
                }

                let submitButton = document.querySelector('input[type="submit"][data-button="decrypt"]');
                if (submitButton) {
                    submitButton.value = 'Decrypt';
                }
            }
        };
        xhttp.open("POST", "/decrypt/", true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send(`cipher=${formData.get('cipher')}`);
    } else {
        let cipherTextarea = document.getElementById('cipher');
        cipherTextarea.classList.add('error');

        submitButton.value = 'Decrypt';
    }

    event.preventDefault();
}