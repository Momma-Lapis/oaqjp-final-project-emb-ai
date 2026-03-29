function RunEmotionDetector() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            } else {
                document.getElementById("system_response").innerHTML = "Error: " + xhttp.status;
            }
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}

// Backward-compatible alias in case older HTML still references this name.
function RunSentimentAnalysis() {
    RunEmotionDetector();
}
