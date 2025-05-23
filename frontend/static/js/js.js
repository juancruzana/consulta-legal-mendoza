document.addEventListener('DOMContentLoaded', function() {
    // 🧠 Elementos del DOM
    const searchInput = document.getElementById('searchInput');

    // 🌀 Lista de placeholders rotativos para el input
    const placeholders = [
        "Describe tu situación legal...",
        "Buscar leyes sobre contratos...",
        "Consultar normativas vigentes...",
        "Buscar legislación laboral...",
        "Consultar derechos del consumidor..."
    ];

    let currentPlaceholder = 0;

    // 🔁 Cambia el placeholder cada 3 segundos
    function rotatePlaceholder() {
        searchInput.setAttribute('placeholder', placeholders[currentPlaceholder]);
        currentPlaceholder = (currentPlaceholder + 1) % placeholders.length;
    }

    setInterval(rotatePlaceholder, 3000); // ⏱️ Intervalo para rotar

    // ✅ Agrega clase para animación de entrada si usás CSS
    document.body.classList.add('loaded');

    // 🎯 Pone el foco automáticamente en el campo al cargar la página
    searchInput.focus();

    // 🦾 Accesibilidad: indicar que el campo está expandido cuando tiene foco
    searchInput.addEventListener('focus', function() {
        this.setAttribute('aria-expanded', 'true');
    });

    searchInput.addEventListener('blur', function() {
        this.setAttribute('aria-expanded', 'false');
    });

    // 🚫 Comentado: esta función era para búsqueda falsa en el frontend,
    // pero ahora Flask se encarga de manejar la lógica real con OpenAI.

    /*
    function handleSearch() {
        const query = searchInput.value.trim();

        if (query.length > 0) {
            searchButton.disabled = true;
            searchButton.textContent = 'Buscando...';

            setTimeout(() => {
                resultsContainer.style.display = 'block';
                resultsContainer.innerHTML = `
                    <h3>Resultados relacionados:</h3>
                    <ul>
                        <li>Artículo relacionado con: "${query}"</li>
                        <li>Normativa vigente sobre el tema</li>
                        <li>Jurisprudencia relacionada</li>
                    </ul>
                `;

                searchButton.disabled = false;
                searchButton.textContent = 'Buscar';
            }, 1000);
        }
    }

    // ⛔ Esto estaba atado al click y enter, pero ya no lo necesitamos
    searchButton.addEventListener('click', handleSearch);

    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            handleSearch();
        }
    });
    */

    // ⚠️ Si algún día querés hacer todo vía AJAX, podés volver a usar handleSearch()
});
