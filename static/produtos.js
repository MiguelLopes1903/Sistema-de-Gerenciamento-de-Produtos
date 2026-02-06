document.addEventListener('DOMContentLoaded', () => {
    const inputArquivo = document.getElementById('inputArquivo');
    const frameImagem = document.getElementById('frameImagem');
    const botaoUpload = frameImagem.querySelector('.botao-upload');

    let imgPreview = document.createElement('img');
    imgPreview.setAttribute('id', 'previewImagem');
    imgPreview.style.display = 'none';
    frameImagem.appendChild(imgPreview);

    inputArquivo.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file && file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = function(e) {
                imgPreview.src = e.target.result;
                imgPreview.style.display = 'block';
                botaoUpload.style.opacity = 0;
                botaoUpload.style.pointerEvents = 'none';
            };
            reader.readAsDataURL(file);
        } else {
            alert("Arquivo inválido. Escolha uma imagem.");
        }
    });

    frameImagem.addEventListener('click', function(event) {
        if (imgPreview.style.display === 'block' && event.target !== inputArquivo) {
            inputArquivo.click();
        }
    });
});
