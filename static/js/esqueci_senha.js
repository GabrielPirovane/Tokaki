document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('formEsqueciSenha');
  const formContent = document.getElementById('formContent');

  form.addEventListener('submit', function(e) {
    e.preventDefault(); // evita envio real

    const emailInput = document.getElementById('email');
    const email = emailInput.value.trim();
    if (!email) {
      alert('Digite um email válido!');
      return;
    }

    // Troca o conteúdo do form
    formContent.innerHTML = `
      <div class="my-5">
        <h3 class="text-center my-2">Verifique seu email!</h3>
        <h5 class="text-center subtitulo mb-2">
          Enviamos as instruções de recuperação de senha no endereço de e-mail informado!
        </h5>
      </div>
      <center>
        <button type="button" id="voltar" class="btn w-50 botao fs-3">Voltar</button>
      </center>
    `;

    document.getElementById('voltar').addEventListener('click', function() {
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
  });
});
