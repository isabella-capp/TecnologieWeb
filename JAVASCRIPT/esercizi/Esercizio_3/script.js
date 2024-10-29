/* ESERCIZIO:
1.  Nel file index.html creare un campo di input e un bottone.
2.  Scrivere codice Javascript data una sequenza di voti di lunghezza
    non nota a priori, ne restituisca la media e la variabilità:
    - elenco dei voti inseriti
    - voto minimo e voto massimo
    - media aritmetica e giudizio sintetico (6 fasce tra 18 e 33)
    - variabilità come “errore medio” e giudizio sintetico (4 fasce tra 0 e 7.5)
3.  Ciascun voto deve essere un numero compreso tra 18 e 33:
4.  controllare opportunamente i dati in input
5.  Definire un oggetto Statistics per l’esecuzione di tutti i calcoli */

class Statistics {
    constructor(voti) {
        this.voti = voti;

        this.average = function () {
            var somma = 0;
            for (var i = 0; i < this.voti.length; i++) {
                somma += this.voti[i];
            }
            return (somma / this.voti.length).toFixed();
        };

        this.min = function () {
            return Math.min(...this.voti);
        };

        this.max = function () {
            return Math.max(...this.voti);
        };

        this.variabilita = function () {
            var mean = this.average();
            console.log(mean);
            var sumError = 0;
            var grade;
            for (grade of this.voti) {
                sumError = sumError + Math.abs(grade - mean);
            }

            return (sumError / this.voti.length).toFixed(2);
        };
    }
}

function computeStatistics(){
    const statisticsContainer = document.getElementById('statistics-container');
    statisticsContainer.innerHTML = '';

    var inputField = document.querySelector('.input-voti')
    var input = inputField.value.trim();

    if (!input) {
        showError("Inserisci almeno un voto!");
        return;
    }

    var grades = input.split(',').map(Number);

    if(!checkIfCorrectRange(grades))
    {
        showError("Devi inserire voti compresi tra 18 e 33!");
        return;
    }

    var voti = new Statistics(grades); 

    const votiInseriti = document.createElement('p');
    votiInseriti.textContent = "Voti inseriti: " + grades.toString();
    statisticsContainer.appendChild(votiInseriti);

    const votoMinimo = document.createElement('p');
    votoMinimo.textContent = "Voto minimo: " + voti.min();
    statisticsContainer.appendChild(votoMinimo);

    const votoMassimo = document.createElement('p');
    votoMassimo.textContent = "Voto massimo: " + voti.max();
    statisticsContainer.appendChild(votoMassimo);

    const mediaVoti = document.createElement('p');
    mediaVoti.textContent = "Media dei voti: " + voti.average();
    statisticsContainer.appendChild(mediaVoti);

    const variabilitaVoti = document.createElement('p');
    variabilitaVoti.textContent = "Variazione dei voti: " + voti.variabilita();
    statisticsContainer.appendChild(variabilitaVoti);
}

// Function to check if all values are in the correct range (18-33)  and if not, return false. Else, return true.
function checkIfCorrectRange(voti){
    for(var i = 0; i < voti.length; i++){
        if(voti[i] < 18 || voti[i] > 33){
            return false;
        }
    }
    return true;
}

// Function to show a messag error
function showError(message) {
    // insert a paragraph with the eror message
    document.getElementById('statistics-container').innerHTML = `<p class="error">${message}</p>`;
}
