document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('formEjercicio1');
    const msgError = document.getElementById('msgError');

    if (form) {
        form.addEventListener('submit', event => {
            event.preventDefault();

            const inputs = form.querySelectorAll('.inputCampo');
            let errores = [];
            let esValido = true;

            inputs.forEach(input => input.classList.remove('input-error'));
            msgError.textContent = '';

            inputs.forEach(input => {
                const valor = input.value.trim();

                if (valor === '') {
                    errores.push(`El campo ${input.name} no puede estar vacío.`);
                    input.classList.add('input-error');
                    esValido = false;
                } else if (input.type === 'number' && +valor <= 0) {
                    errores.push(`El campo ${input.name} debe ser mayor a 0.`);
                    input.classList.add('input-error');
                    esValido = false;
                }
            });

            if (!esValido) {
                msgError.textContent = errores.join(' ');
            } else {
                form.submit();
            }
        });
    }
});