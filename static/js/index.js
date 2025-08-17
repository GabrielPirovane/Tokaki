export function initFormValidation() {
  document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('form-cadastro') || document.querySelector('form');
    if (!form) return;

    const senha = document.getElementById('senha');
    const nome = document.getElementById('nome');
    const sobrenome = document.getElementById('sobrenome');
    const nomeUsuario = document.getElementById('nome_usuario');
    const email = document.getElementById('email');
    const confirmacao = document.getElementById('confirmacao_senha');
    const erro = document.getElementById('erro-senha');
    const botao = document.getElementById('submit-button');
    const radios = document.getElementsByName('tipo_usuario');

    if (!senha || !confirmacao || !botao) return;

    function disableButton() { botao.classList.add('btn-disabled'); botao.disabled = true; }
    function enableButton() { botao.classList.remove('btn-disabled'); botao.disabled = false; }

    disableButton();

    form.addEventListener('submit', function (e) {
      if (senha.value !== confirmacao.value) {
        e.preventDefault();
        if (erro) { erro.textContent = 'As senhas não conferem.'; erro.style.display = 'block'; confirmacao.focus(); disableButton(); }
      } else { if (erro) erro.style.display = 'none'; enableButton(); }
    });

    function checkRequireds() {
      const tipoUsuario = document.querySelector('input[name="tipo_usuario"]:checked')?.value;
      if (!nome.value || !sobrenome.value || !nomeUsuario.value || !email.value || !senha.value || !tipoUsuario) disableButton();
      else enableButton();
    }

    function checkPasswords() {
      if (senha.value !== '' && senha.value === confirmacao.value) checkRequireds();
      else disableButton();
    }

    Array.from(radios).forEach(r => r.addEventListener('change', checkRequireds));
    senha.addEventListener('input', checkPasswords);
    confirmacao.addEventListener('input', checkPasswords);
    nome.addEventListener('input', checkRequireds);
    sobrenome.addEventListener('input', checkRequireds);
    nomeUsuario.addEventListener('input', checkRequireds);
    email.addEventListener('input', checkRequireds);

    checkRequireds();
    checkPasswords();
  });
}
