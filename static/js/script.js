let isButtonPressed = false;

function sendKey(key) {
    fetch("/keypress", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ key: key })
    })
    .then(response => response.json())
    .then(data => console.log("Server Output:", data));
}

function sendSliderValue(value) {
    console.log("Slider Value:", value);
    fetch("/slider", {  
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value: value })
    })
    .then(response => response.json())
}

function sliderChange(event) {
    sendSliderValue(event.target.value);
}

function buttonDown(key) {
    if (!isButtonPressed) {
        console.log("Tuşa basıldı:", key);
        isButtonPressed = true;
        fetch("/button_down", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ key: key, status: "Button Clicked" })
        })
        .then(response => response.json())
        .then(data => console.log(data));
    }
}

function buttonUp(key) {
    if (isButtonPressed) {
        console.log("Tuş bırakıldı:", key);
        isButtonPressed = false;
        fetch("/button_up", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ key: key, status: "Button Released" })
        })
        .then(response => response.json())
        .then(data => console.log(data));
    }
}