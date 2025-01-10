document.getElementById("prediction-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const formData = new FormData(this);

    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.result) {
            document.getElementById("result").innerText = "Prediction: Stock price will go " + data.result;
        } else {
            document.getElementById("result").innerText = "Error: " + data.error;
        }
    });
});
