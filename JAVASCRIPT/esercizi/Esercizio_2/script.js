const arr = [
    {
        url: "https://www.armandoalpantheon.it/wp-content/uploads/2023/03/Primavera-a-Roma-%E2%80%93-Il-Colosseo-e-gli-scavi-di-Ostia-Antica-armando-al-pantheon-768x480.jpg",
        title: "Colosseo",
        description: "Originariamente conosciuto come Anfiteatro Flavio è il più grande anfiteatro romano del mondo.",
    },
    {
        url: "https://png.pngtree.com/background/20230525/original/pngtree-floral-wallpaper-with-brown-and-brown-paint-picture-image_2735082.jpg",
        title: "Linguaggio dei fiori",
        description: "Modo di comunicazione ottocentesco per cui i fiori e gli allestimenti floreali venivano utilizzati per esprimere sensazioni che non sempre potevano essere pronunciate.",
    },
    {
        url: "https://www.donne.it/wp-content/uploads/2023/10/intelligenza-artificiale-768x512.jpg",
        title: "Intelligenza Artificiale",
        description: "Nel suo significato più ampio, è la capacità di un sistema artificiale di simulare l'intelligenza umana attraverso l'ottimizzazione di funzioni matematiche.",
    },
];


function createCard(data) {
    
    const container = document.getElementById("container");

    const card = document.createElement('div');
    card.classList.add('card');
    
    const cardContainer = document.createElement('div');
    cardContainer.classList.add('card-container');
    
    const img = document.createElement('img');
    img.classList.add('card-image');
    img.src = data.url;
    cardContainer.appendChild(img);
    
    const text = document.createElement('div');
    text.classList.add('card-text');
    cardContainer.appendChild(text);
    
    const title = document.createElement('h3');
    title.classList.add('card-title');
    title.textContent = data.title;
    text.appendChild(title);
    
    const desc = document.createElement('p');
    desc.classList.add('card-description');
    desc.textContent = data.description;
    text.appendChild(desc);
    
    card.appendChild(cardContainer);
    container.appendChild(card);
    
}
