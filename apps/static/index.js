async function getRates(data = {}){
    const response = await fetch("http://127.0.0.1:5000/api/getRates/", {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    return await response.json();
}

async function clearStory(){
    const response = await fetch("http://127.0.0.1:5000/api/clearStory/", {
        method: 'POST',
    });

    return await response.json();
}


function btn_click(e){
    elem = e.target
    iconInput.textContent = elem.dataset.icon;
    value = rateInput.value;
    data = {
        'rate': elem.dataset.rate,
        'value': value ? parseInt(value) : 1,
    };
    getRates(data)
    .then((data) => {
        if (data["status"])
        display.innerHTML += `${data["result"]}<br\>`;
        else
            alert(data["result"]);
    });

}

function clear(e){
    elem = e.target
    iconInput.textContent = elem.dataset.icon;
    rateInput.value = '';
    

    clearStory().then((data) => {
        if (data["status"])
            display.innerHTML = '';
        else
            alert(data["result"]);
    });
}

let rateInput = document.querySelector("#input-type-left");
let iconInput = document.querySelector("#input-group-left");
let display = document.querySelector(".display");

document.querySelectorAll('.rate').forEach((val) => {val.addEventListener('click', btn_click);});
document.querySelector('.clear').addEventListener('click', clear);