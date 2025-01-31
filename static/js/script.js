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
    console.log("Gönderilen slider değeri:", value);
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

function buttonClick(key) {
    console.log("Tuşa basıldı:", key);
    sendKey(key);
}
