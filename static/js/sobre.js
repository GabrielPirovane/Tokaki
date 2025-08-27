const elementos = document.querySelectorAll('.animar-scroll');

function animarAoScroll() {
  const alturaTela = window.innerHeight;

  elementos.forEach(el => {
    const posicaoElemento = el.getBoundingClientRect().top;

    if (posicaoElemento < alturaTela - 50) { 
      el.classList.add('ativo');
    }
  });
}

window.addEventListener('scroll', animarAoScroll);
window.addEventListener('load', animarAoScroll);