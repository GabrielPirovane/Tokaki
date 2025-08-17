document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('form-cadastro') || document.querySelector('form');
  if (!form) return;

  const senha = document.getElementById('senha');
  const confirmacao = document.getElementById('confirmacao_senha');
  const erro = document.getElementById('erro-senha');
  const botao = document.getElementById('submit-button') || document.querySelector('button[type="submit"]');

  if (!senha || !confirmacao || !botao) return;


  function disableButton() {
    botao.classList.add('btn-disabled');
    botao.disabled = true; 
  }

  function enableButton() {
    botao.classList.remove('btn-disabled');
    botao.disabled = false;
  }

  form.addEventListener('submit', function (e) {
    if (senha.value !== confirmacao.value) {
      e.preventDefault();
      if (erro) {
        erro.textContent = 'As senhas não conferem.';
        erro.style.display = 'block';
        disableButton();
        confirmacao.focus();
      }

    } else {
      if (erro) erro.style.display = 'none';
      enableButton();
    }
  });

  function checkPasswords() {
    if (senha.value === '' && confirmacao.value === '') {
      enableButton();
      if (erro) erro.style.display = 'none';
      return;
    }

    if (senha.value === confirmacao.value) {
      if (erro) erro.style.display = 'none';
      enableButton();
    } else {

      if (erro && confirmacao.value.length > 0) {
        erro.textContent = 'As senhas não conferem.';
        erro.style.display = 'block';
      }
    disableButton();
    }

  }

  senha.addEventListener('input', checkPasswords);
  confirmacao.addEventListener('input', checkPasswords);


  checkPasswords();
});
