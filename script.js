document.getElementById("predictBtn").addEventListener("click", async () => {
    const studentData = {
        name: document.getElementById("name").value,
        skills: document.getElementById("skills").value.split(",").map(s => s.trim()),
        interests: [document.getElementById("interest").value],
        cgpa: parseFloat(document.getElementById("cgpa").value),
        courses: document.getElementById("courses").value.split(",").map(c => c.trim())
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(studentData)
        });

        const result = await response.json();

        document.getElementById("result").innerText = "Best Internship Match: " + result.best_fit;
        document.getElementById("place").innerText = "Place/Company: " + result.place;

        // Clean list function
        const displayList = (id, items) => {
            const box = document.getElementById(id);
            box.innerHTML = ""; // Clear previous results

            items.forEach(item => {
                const div = document.createElement("div");
                div.className = "result-item";
                div.innerText = "• " + item;  // You can remove • if you want no markers
                box.appendChild(div);
            });
        };

        displayList("strengths", result.strengths);
        displayList("weaknesses", result.weaknesses);
        displayList("areas", result.areas);

    } catch (error) {
        console.error(error);
        alert("Backend not running!");
    }
});