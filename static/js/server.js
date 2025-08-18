import {
  initFormValidation,
  initCPFInput,
  initCEPInput,
  initTelefone,
  initDataNascimentoInput,
  initSenha
} from '/static/js/cadastro.js';

initFormValidation();
initCPFInput();
initCEPInput();
initTelefone();
initDataNascimentoInput();
initSenha();

document.addEventListener("DOMContentLoaded", () => {
  const senha = document.getElementById('senha');
  const container = document.getElementById('strengthBarContainer');
  const barFill = document.getElementById('strengthBarFill');
  const text = document.getElementById('strengthText');

  const labels = ['Muito fraca', 'Fraca', 'Média', 'Forte', 'Muito forte'];
  const colors = ['#ff0000', '#FF8000', '#FFD700', '#4CAF50', '#2196F3'];

  senha.addEventListener('input', () => {
    const value = senha.value.trim();

    if (value === "") {
      container.style.height = '0';   // some quando o campo está vazio
      barFill.style.width = '0%';
      text.textContent = '';
      return;
    }

    container.style.height = '15px';  // aparece quando tem texto
    const score = zxcvbn(value).score;

    text.textContent = labels[score];
    barFill.style.width = `${((score + 1) / 5) * 100}%`;
    barFill.style.backgroundColor = colors[score];
  });
});


