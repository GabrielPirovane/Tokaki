document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('formEsqueciSenha');
  const formContent = document.getElementById('formContent');

  form.addEventListener('submit', async function (e) {
    e.preventDefault();

    const emailInput = document.getElementById('email');
    const submitButton = form.querySelector('button[type="submit"]');

    if (!emailInput.value.trim()) {
      alert('Digite um email válido!');
      return;
    }


    try {
      submitButton.disabled = true;
      submitButton.textContent = 'Processando...';
      const response = await fetch('/esqueci-senha', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ email: emailInput.value.trim() })
      });

      if (!response.ok) throw new Error('Erro ao enviar email');

      // troca o conteúdo do form
      formContent.innerHTML = `
        <div class="my-5">
          <h3 class="text-center my-2">Verifique seu email!</h3>
          <h5 class="text-center subtitulo mb-2">
            Enviamos as instruções de recuperação de senha no endereço de e-mail informado, caso seja válido.
          </h5>
        </div>
        <center>
          <button type="button" id="voltar" class="btn w-50 botao fs-3">Voltar</button>
        </center>
      `;

      document.getElementById('voltar').addEventListener('click', function () {
        formContent.innerHTML = `
          <div class="my-5">
            <label for="email" class="titulo-form">Insira seu endereço de email</label>
            <input type="email" class="form-control" id="email" name="email" placeholder="exemplo@email.com" required>
          </div>
          <center>
            <button type="submit" class="btn w-50 botao fs-3">Prosseguir</button>
          </center>
        `;
      });

    } catch (err) {
      alert('Ocorreu um erro ao tentar enviar o email. Tente novamente.');
      console.error(err);

      // Reabilita o botão caso dê erro
      submitButton.disabled = false;
      submitButton.textContent = 'Prosseguir';
    }
  });
});
