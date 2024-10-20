document.addEventListener("DOMContentLoaded", function() {
    // Cridem a l'endpoint de l'API fent un fetch
    fetch('http://127.0.0.1:8000/alumne/list',
        {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
    })  // Aquí debes poner la URL del API_________________________________________
        .then(response => {
            if (!response.ok) {
                throw new Error("Error a la resposta del servidor");
            }
            return response.json();
        })
        .then(data => {
            const alumnesTableBody = document.querySelector("#tablaAlumne tbody");
            alumnesTableBody.innerHTML = ""; // Netejar la taula abans d'afegir res
            
            // Iterar sobre los alumnos y agregarlos al DOM
            data.forEach(alumne => {
                const row = document.createElement("tr");

                const nomAluCell = document.createElement("td");
                nomAluCell.textContent = alumne.Nombre;
                row.appendChild(nomAluCell);

                const cicAluCell = document.createElement("td");
                cicAluCell.textContent = alumne.Ciclo;
                row.appendChild(cicAluCell);

                const curAluCell = document.createElement("td");
                curAluCell.textContent = alumne.Curso;
                row.appendChild(curAluCell);

                const gruAluCell = document.createElement("td");
                gruAluCell.textContent = alumne.Grupo;
                row.appendChild(gruAluCell);

                const descAluCell = document.createElement("td");
                descAluCell.textContent = alumne.DescAula;
                row.appendChild(descAluCell);

                ____________________________________________

                alumnesTableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error("Error capturat:", error);
            alert("Error al carregar la llista d'alumnes");
        });
});