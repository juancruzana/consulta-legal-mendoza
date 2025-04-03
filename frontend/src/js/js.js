document.addEventListener('DOMContentLoaded', function() {
    // Elementos del DOM
    const searchInput = document.getElementById('searchInput');
    const searchButton = document.getElementById('searchButton');
    const resultsContainer = document.getElementById('results');

    // Placeholders rotativos
    const placeholders = [
        "Describe tu situación legal...",
        "Buscar leyes sobre contratos...",
        "Consultar normativas vigentes...",
        "Buscar legislación laboral...",
        "Consultar derechos del consumidor..."
    ];

    let currentPlaceholder = 0;

    // Función para rotar placeholders
    function rotatePlaceholder() {
        searchInput.setAttribute('placeholder', placeholders[currentPlaceholder]);
        currentPlaceholder = (currentPlaceholder + 1) % placeholders.length;
    }

    // Rotar placeholder cada 3 segundos
    setInterval(rotatePlaceholder, 3000);

    // Manejar la búsqueda
    function handleSearch() {
        const query = searchInput.value.trim();
        
        if (query.length > 0) {
            // Mostrar estado de carga
            searchButton.disabled = true;
            searchButton.textContent = 'Buscando...';
            
            // Simular búsqueda
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
                
                // Restaurar botón
                searchButton.disabled = false;
                searchButton.textContent = 'Buscar';
            }, 1000);
        }
    }

    // Event Listeners
    searchButton.addEventListener('click', handleSearch);
    
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            handleSearch();
        }
    });

    // Animación de entrada
    document.body.classList.add('loaded');
    
    // Focus automático en el input
    searchInput.focus();

    // Mejoras de accesibilidad
    searchInput.addEventListener('focus', function() {
        this.setAttribute('aria-expanded', 'true');
    });

    searchInput.addEventListener('blur', function() {
        this.setAttribute('aria-expanded', 'false');
    });

    // Prevenir múltiples envíos
    let busquedaEnProceso = false;
    
    function prevenirMultiplesEnvios() {
        if (busquedaEnProceso) {
            return true;
        }
        busquedaEnProceso = true;
        setTimeout(() => {
            busquedaEnProceso = false;
        }, 1000);
        return false;
    }
}); 
