const selectElement = document.querySelector('#id_products');

    selectElement.addEventListener('change', (event) => {

        const resultado = document.querySelector('#total');

        cantidad = selectElement.length;

        var total=0;

        for (var i=0;i<cantidad;i++) {

            if (selectElement.selectedOptions[i]) {
                contenido= selectElement.selectedOptions[i].textContent;

                parcial = contenido.substr(contenido.indexOf('$')+2)

                parcial2= parseFloat(parcial);

                total = total+parcial2;
            }
        }
            resultado.textContent = `$${total}`;

        });