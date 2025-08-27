document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('form-login');
    const email = document.getElementById('email');
    const senha = document.getElementById('senha');
    const botao = document.getElementById('submit-button');
    const erroEmail = document.getElementById('erro-email-js');
    const erroSenha = document.getElementById('erro-senha-js');
    
    if (!form || !email || !senha || !botao || !erroEmail || !erroSenha) return;
    function disableButton() {
        botao.classList.add('btn-disabled');
        botao.disabled = true;
    }
    function enableButton() {
        botao.classList.remove('btn-disabled');
        botao.disabled = false;
    }
    disableButton();
    function checkRequireds() {
        const emailValido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim());
        const senhaValida = senha.value.length >= 8;

        if (email.value && senha.value && emailValido && senhaValida) enableButton();
        else disableButton();
    }
    email.addEventListener('input', function () {
        const value = this.value.trim();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (value === '') {
            erroEmail.textContent = '';
            erroEmail.style.display = 'none';
        } else if (!emailRegex.test(value)) {
            erroEmail.textContent = 'Email inválido. Insira algo como exemplo@dominio.com';
            erroEmail.style.display = 'block';
        } else {
            erroEmail.textContent = '';
            erroEmail.style.display = 'none';
        }
        checkRequireds();
    });
    senha.addEventListener('input', function () {
        if (senha.value && senha.value.length < 8) {
            erroSenha.textContent = 'A senha deve ter no mínimo 8 caracteres.';
            erroSenha.style.display = 'block';
        } else {
            erroSenha.textContent = '';
            erroSenha.style.display = 'none';
        }
        checkRequireds();
    });
    checkRequireds();
});
