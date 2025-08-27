document.addEventListener("DOMContentLoaded", () => {
    const senha = document.getElementById('senha');
    const container = document.getElementById('strengthBarContainer');
    const barFill = document.getElementById('strengthBarFill');
    const text = document.getElementById('strengthText');
    const confirmacao = document.getElementById('confirmacao_senha');
    const erro = document.getElementById('erro-senha');
    const botao = document.getElementById('submit-button');

    const labels = ['Muito fraca', 'Fraca', 'Média', 'Forte', 'Muito forte'];
    const colors = ['#ff0000', '#FF8000', '#FFD700', '#4CAF50', '#2196F3'];
    const form = document.getElementById('form-cadastro') || document.querySelector('form');



    form.addEventListener('submit', function (e) {
      if (senha.value !== confirmacao.value) {
        e.preventDefault();
        if (erro) { erro.textContent = 'As senhas não conferem.'; erro.style.display = 'block'; confirmacao.focus(); disableButton(); }
      } else { if (erro) erro.style.display = 'none'; enableButton(); }
    });


    senha.addEventListener('input', () => {
        const value = senha.value.trim();

        if (value === "") {
            container.style.height = '0';
            barFill.style.width = '0%';
            text.textContent = '';
            return;
        }

        container.style.height = '15px';
        const score = zxcvbn(value).score;

        text.textContent = labels[score];
        barFill.style.width = `${((score + 1) / 5) * 100}%`;
        barFill.style.backgroundColor = colors[score];
    });

    senha.addEventListener('input', checkPasswords);

});


function checkPasswords() {

    function disableButton() { botao.classList.add('btn-disabled'); botao.disabled = true; }
    function enableButton() { botao.classList.remove('btn-disabled'); botao.disabled = false; }

    disableButton();

    if (confirmacao.value) {
        if (senha.value === confirmacao.value) {
            if (erro) erro.style.display = 'none';
            checkRequireds();
        } else {
            if (erro) {
                erro.textContent = 'As senhas não conferem.';
                erro.style.display = 'block';
                disableButton();
            }
        }
    } else {
        if (erro) erro.style.display = 'none';
    }
}