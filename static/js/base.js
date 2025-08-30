const searchbox = document.getElementById('searchbox')
const resultsDiv = document.getElementById('results')

let timeoutId;

searchbox.addEventListener("keyup", function() {
    clearTimeout(timeoutId); // اگر تایمر قبلی وجود داشت، لغوش کن

    const query = this.value;

    timeoutId = setTimeout(() => {
        if (query.length > 1) {
            fetch(`/search/?q=${encodeURIComponent(query)}`)
                .then(res => res.json())
                .then(data => {
                    resultsDiv.innerHTML = "";
                    data.results.forEach(item => {
                        const p = document.createElement("p");
                        p.textContent = item;
                        resultsDiv.appendChild(p);
                    });
                });
        } else {
            resultsDiv.innerHTML = "";
        }
    }, 300); // صبر کن 300 میلی‌ثانیه بعد از آخرین تایپ
});
