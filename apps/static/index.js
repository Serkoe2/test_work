async function getRates(url = '', data = {}){
    const response = await fetch("http://127.0.0.1:5000/api/getRates/", {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
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
    getRates('https://example.com/answer', data)
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
    display.innerHTML = '';
}

let rateInput = document.querySelector("#input-type-left");
let iconInput = document.querySelector("#input-group-left");
let display = document.querySelector(".display");

document.querySelectorAll('.rate').forEach((val) => {val.addEventListener('click', btn_click);});
document.querySelector('.clear').addEventListener('click', clear);