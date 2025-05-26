document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById("consultaForm");
    const input = document.getElementById("searchInput");
    const result = document.getElementById("result");
    const button = document.getElementById("searchButton");
    const searchContainer = document.querySelector('.search-container');


    const placeholders = [
        "Describe tu situación legal...",
        "Buscar leyes sobre contratos...",
        "Consultar normativas vigentes...",
        "Buscar legislación laboral...",
        "Consultar derechos del consumidor..."
    ];

    let currentPlaceholder = 0;
    setInterval(() => {
        input.setAttribute('placeholder', placeholders[currentPlaceholder]);
        currentPlaceholder = (currentPlaceholder + 1) % placeholders.length;
    }, 3000);

    form.addEventListener("submit", function(e) {
        e.preventDefault();

        const consulta = input.value.trim();
        if (!consulta) return;

        // Desactiva el botón y muestra cargando
        button.disabled = true;
        button.textContent = "Consultando...";
        result.innerHTML = ""; // Limpia resultado anterior

        fetch("/api/consulta", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ consulta: consulta })
        })
        .then(res => res.json())
        .then(data => {
            if (data.respuesta) {
                result.style.display = "block";
                result.innerHTML = `
                    <p>${data.respuesta}</p>
                `;
            } else {
                result.innerHTML = "<p>Ocurrió un error.</p>";
            }
        })
        
        .catch(err => {
            result.innerHTML = "<p>Error en la consulta.</p>";
        })
        .finally(() => {
            button.disabled = false;
            button.textContent = "Hacer otra consulta";
        });

        searchInput.addEventListener('input', () => {
            if (searchInput.value.trim() === "") {
                result.style.display = "none";
            }
        });        
    });
});

