const ufMap = {
  "AC": "Acre",
  "AL": "Alagoas",
  "AP": "Amapá",
  "AM": "Amazonas",
  "BA": "Bahia",
  "CE": "Ceará",
  "DF": "Distrito Federal",
  "ES": "Espírito Santo",
  "GO": "Goiás",
  "MA": "Maranhão",
  "MT": "Mato Grosso",
  "MS": "Mato Grosso do Sul",
  "MG": "Minas Gerais",
  "PA": "Pará",
  "PB": "Paraíba",
  "PR": "Paraná",
  "PE": "Pernambuco",
  "PI": "Piauí",
  "RJ": "Rio de Janeiro",
  "RN": "Rio Grande do Norte",
  "RS": "Rio Grande do Sul",
  "RO": "Rondônia",
  "RR": "Roraima",
  "SC": "Santa Catarina",
  "SP": "São Paulo",
  "SE": "Sergipe",
  "TO": "Tocantins"
};


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
    checkEmail();

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

    Array.from(radios).forEach(r => r.addEventListener('change', checkRequireds));
    senha.addEventListener('input', checkPasswords);
    confirmacao.addEventListener('input', checkPasswords);
    nome.addEventListener('input', checkRequireds);
    sobrenome.addEventListener('input', checkRequireds);
    nomeUsuario.addEventListener('input', checkRequireds);
    email.addEventListener('input', checkRequireds);

    clearErrorOnInput('nome', 'erro-nome');
    clearErrorOnInput('sobrenome', 'erro-sobrenome');
    clearErrorOnInput('nome_usuario', 'erro-nome-usuario');
    clearErrorOnInput('senha', 'erro-senha');
    clearErrorOnInput('confirmacao_senha', 'erro-senha');
    clearErrorOnInput('data_nascimento', 'erro-data-nascimento');
    clearErrorOnInput('email', 'erro-email-backend');
    clearErrorOnInput('cpf', 'erro-cpf');
    clearErrorOnInput('telefone', 'erro-telefone');
    clearErrorOnInput('cep', 'erro-cep');
    checkRequireds();
    checkPasswords();


  });
}

function checkEmail() {
  const emailInput = document.getElementById('email');
  const erroEmail = document.getElementById('erro-email-js');

  if (!emailInput || !erroEmail) return;

  emailInput.addEventListener('input', function () {
    const value = this.value.trim();

    // Regex simples para verificar estrutura básica do email
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

    // Opcional: atualizar botão de submit
    checkRequireds();
  });
}

export function formatCPF(digits) {
  const p1 = digits.slice(0, 3);
  const p2 = digits.slice(3, 6);
  const p3 = digits.slice(6, 9);
  const p4 = digits.slice(9, 11);
  let formatted = '';
  if (p1) formatted += p1;
  if (p2) formatted += '.' + p2;
  if (p3) formatted += '.' + p3;
  if (p4) formatted += '-' + p4;
  return formatted;
}

export function initCPFInput() {
  const cpfInput = document.getElementById('cpf');
  if (!cpfInput) return;

  cpfInput.addEventListener('input', function () {
    let digits = this.value.replace(/\D/g, '').slice(0, 11);
    this.value = formatCPF(digits);
  });

  cpfInput.addEventListener('paste', function (e) {
    const pasted = (e.clipboardData || window.clipboardData).getData('text');
    const digits = pasted.replace(/\D/g, '').slice(0, 11);
    this.value = formatCPF(digits);
    e.preventDefault();
  });
}

export function formatCEP(digits) {
  // garante só números (quem chama pode já ter limpo, mas fica seguro)
  digits = String(digits).replace(/\D/g, '').slice(0, 8);
  const p1 = digits.slice(0, 5);
  const p2 = digits.slice(5, 8);
  let formatted = '';
  if (p1) formatted += p1;
  if (p2) formatted += '-' + p2;
  return formatted;
}

export function initCEPInput() {
  const cepInput = document.getElementById('cep');
  if (!cepInput) return;

  const logradouroInput = document.getElementById('logradouro');
  const bairroInput = document.getElementById('bairro');
  const cidadeInput = document.getElementById('cidade');
  const ufInput = document.getElementById('estado');

  async function buscarCEP(cep) {
    try {
      const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
      const data = await response.json();
      if (data.erro) throw new Error("CEP não encontrado");

      if (logradouroInput) logradouroInput.value = data.logradouro || '';
      if (bairroInput) bairroInput.value = data.bairro || '';
      if (cidadeInput) cidadeInput.value = data.localidade || '';
      if (ufInput) {
        const nomeUF = ufMap[data.uf];
        const option = Array.from(ufInput.options).find(opt => opt.text.trim() === nomeUF);
        if (option) {
          option.selected = true;
        } else {
          ufInput.selectedIndex = 0;
        }
      }
    } catch (err) {
      console.error(err);
      if (logradouroInput) logradouroInput.value = '';
      if (bairroInput) bairroInput.value = '';
      if (cidadeInput) cidadeInput.value = '';
      if (ufInput) ufInput.selectedIndex = 0;
    }
  }

  cepInput.addEventListener('input', function () {
    let digits = this.value.replace(/\D/g, '').slice(0, 8);
    this.value = formatCEP(digits);

    if (digits.length === 8) {
      buscarCEP(digits);
    } else {
      if (logradouroInput) logradouroInput.value = '';
      if (bairroInput) bairroInput.value = '';
      if (cidadeInput) cidadeInput.value = '';
      if (ufInput) ufInput.selectedIndex = 0;
    }
  });

  // Listener de paste
  cepInput.addEventListener('paste', function (e) {
    const pasted = (e.clipboardData || window.clipboardData).getData('text');
    const digits = pasted.replace(/\D/g, '').slice(0, 8);
    this.value = formatCEP(digits);
    e.preventDefault();

    if (digits.length === 8) {
      buscarCEP(digits);
    } else {
      if (logradouroInput) logradouroInput.value = '';
      if (bairroInput) bairroInput.value = '';
      if (cidadeInput) cidadeInput.value = '';
      if (ufInput) ufInput.selectedIndex = 0;
    }
  });
}

export function formatTelefone(digits) {
  // Remove qualquer caractere que não seja número
  digits = digits.replace(/\D/g, '');

  const ddd = digits.slice(0, 2);
  const parte1 = digits.slice(2, 7); // primeiros 5 dígitos do número
  const parte2 = digits.slice(7, 11); // últimos 4 dígitos

  let formatted = '';
  if (ddd) formatted += `(${ddd}) `;
  if (parte1) formatted += parte1;
  if (parte2) formatted += `-${parte2}`;

  return formatted;
}

export function initTelefone() {
  const telefoneInput = document.getElementById('telefone');
  if (!telefoneInput) return;

  telefoneInput.addEventListener('input', function () {
    let digits = this.value.replace(/\D/g, ''); // só números
    let cursorPosition = this.selectionStart;

    // conta quantos dígitos havia antes do cursor
    let digitsBeforeCursor = this.value.slice(0, cursorPosition).replace(/\D/g, '').length;

    this.value = formatTelefone(digits);

    // posiciona o cursor depois do mesmo número de dígitos
    let pos = 0;
    let countedDigits = 0;
    for (let i = 0; i < this.value.length; i++) {
      if (/\d/.test(this.value[i])) countedDigits++;
      if (countedDigits >= digitsBeforeCursor) {
        pos = i + 1;
        break;
      }
    }

    this.setSelectionRange(pos, pos);
  });
}

export function initDataNascimentoInput() {
  const dataInput = document.getElementById('data_nascimento');
  if (!dataInput) return;

  dataInput.addEventListener('input', function () {
    let v = this.value.replace(/\D/g, ''); // remove tudo que não for número

    if (v.length > 2) v = v.slice(0, 2) + '/' + v.slice(2);
    if (v.length > 5) v = v.slice(0, 5) + '/' + v.slice(5, 9); // permite até 4 dígitos do ano

    this.value = v;
  });

  dataInput.addEventListener('paste', function (e) {
    const pasted = (e.clipboardData || window.clipboardData).getData('text');
    let digits = pasted.replace(/\D/g, '').slice(0, 8); // ddmmaaaa
    let formatted = digits;
    if (digits.length > 2) formatted = digits.slice(0, 2) + '/' + digits.slice(2);
    if (digits.length > 4) formatted = formatted.slice(0, 5) + '/' + digits.slice(4, 8);
    this.value = formatted;
    e.preventDefault();
  });
}


export function initSenha() {
  document.addEventListener('DOMContentLoaded', function () {
    const senhaInput = document.getElementById('senha');
    const toggleSenhaBtn = document.getElementById('toggleSenha');

    const confirmInput = document.getElementById('confirmacao_senha');
    const toggleConfirmBtn = document.getElementById('toggleConfirmacao');


    function toggleVisibility(input, button) {
      const icon = button.querySelector("i");
      if (input.type === "password") {
        input.type = "text";
        if (icon) {
          icon.classList.remove("bi-eye");
          icon.classList.add("bi-eye-slash");
        }
      } else {
        input.type = "password";
        if (icon) {
          icon.classList.remove("bi-eye-slash");
          icon.classList.add("bi-eye");
        }
      }
    }

    function allowOnlyLettersAndNumbers(input) {
      input.addEventListener('input', function () {
        this.value = this.value.replace(/[^a-zA-Z0-9!@#$%¨&*]/g, '');
      });
    }

    if (senhaInput && toggleSenhaBtn) {
      toggleSenhaBtn.addEventListener('click', function () {
        toggleVisibility(senhaInput, toggleSenhaBtn);
      });
      allowOnlyLettersAndNumbers(senhaInput);
    }

    if (confirmInput && toggleConfirmBtn) {
      toggleConfirmBtn.addEventListener('click', function () {
        toggleVisibility(confirmInput, toggleConfirmBtn);
      });
      allowOnlyLettersAndNumbers(confirmInput);
    }
  });
}

function clearErrorOnInput(inputId, errorId) {
  const input = document.getElementById(inputId);
  const error = document.getElementById(errorId);

  if (!input || !error) return;

  input.addEventListener('input', () => {
    error.textContent = '';
    error.style.display = 'none';
    input.classList.remove('is-invalid'); 
  });
}

