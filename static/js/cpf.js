// apenas funções exportadas
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
