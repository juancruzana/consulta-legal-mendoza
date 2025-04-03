document.getElementById('search-button').addEventListener('click', function() {
    const query = document.getElementById('search-input').value.trim();
    const searchContainer = document.getElementById('searchContainer');
    
    if (query !== '') {
        // Aplicar estilo fixed al contenedor de búsqueda
        searchContainer.classList.add('fixed');
        
        // Mostrar resultados (simulado)
        const resultsContainer = document.getElementById('searchResults');
        resultsContainer.style.display = 'block';
        resultsContainer.innerHTML = `<h2>Resultados para: "${query}"</h2>
                                   <p>Resultado 1 relacionado con ${query}</p>
                                   <p>Resultado 2 relacionado con ${query}</p>
                                   <p>Resultado 3 relacionado con ${query}</p>`;
        
        // Desplazar la página hacia arriba si es necesario
        window.scrollTo({top: 0, behavior: 'smooth'});
        
        // En una implementación real, aquí harías una petición AJAX o redirigirías
        // a una página de resultados con el parámetro de búsqueda
    }
});

document.getElementById('search-input').addEventListener('keyup', function(e) {
    if (e.key === 'Enter') {
        document.getElementById('search-button').click();
    } else {
        // Aquí podrías implementar sugerencias de búsqueda
        // mostrarSugerencias(this.value);
    }
});

// Si quieres que el search-box vuelva a su posición original al borrar la búsqueda
document.getElementById('search-input').addEventListener('input', function(e) {
    if (this.value.trim() === '') {
        document.getElementById('searchContainer').classList.remove('fixed');
        document.getElementById('searchResults').style.display = 'none';
    }
});

// Ejemplo de función para mostrar sugerencias
function mostrarSugerencias(query) {
    const container = document.getElementById('suggestions-container');
    if (query.length > 2) {
        // Simulación de sugerencias (en una implementación real, esto vendría de un servidor)
        const sugerencias = ['producto 1', 'producto 2', 'categoría especial'];
        
        container.innerHTML = '';
        sugerencias.forEach(sug => {
            const div = document.createElement('div');
            div.className = 'suggestion-item';
            div.textContent = sug;
            div.addEventListener('click', function() {
                document.getElementById('search-input').value = sug;
                container.style.display = 'none';
                document.getElementById('search-button').click();
            });
            container.appendChild(div);
        });
        
        container.style.display = 'block';
    } else {
        container.style.display = 'none';
    }
}