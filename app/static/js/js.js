document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const searchForm = document.querySelector('form');
    const resultDiv = document.getElementById('result');
    
    // Placeholders rotativos
    const placeholders = [
        "Ej: ¿Cómo denunciar un despido injustificado?",
        "Ej: Requisitos para un contrato de alquiler",
        "Ej: Derechos del consumidor en compras online",
        "Ej: ¿Qué hacer en un accidente de tránsito?",
        "Ej: Proceso de divorcio de mutuo acuerdo"
    ];
    
    let currentPlaceholder = 0;
    
    function rotatePlaceholder() {
        searchInput.placeholder = placeholders[currentPlaceholder];
        currentPlaceholder = (currentPlaceholder + 1) % placeholders.length;
    }
    
    setInterval(rotatePlaceholder, 3000);
    
    // Manejo del formulario con AJAX
    searchForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const query = searchInput.value.trim();
        if (!query) return;
        
        try {
            // Mostrar estado de carga
            resultDiv.innerHTML = '<div class="loading">Buscando información legal...</div>';
            
            const response = await fetch('/consulta', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ consulta: query })
            });
            
            const data = await response.json();
            
            if (data.error) {
                resultDiv.innerHTML = `<div class="error">Error: ${data.error}</div>`;
            } else {
                resultDiv.innerHTML = `
                    <h2>Respuesta Legal</h2>
                    <div class="respuesta">${data.respuesta.replace(/\n/g, '<br>')}</div>
                `;
            }
            
        } catch (error) {
            resultDiv.innerHTML = `<div class="error">Error al conectar con el servidor</div>`;
        }
    });
    
    // Foco inicial
    searchInput.focus();
});