async function sendMessage() {
    const inputField = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");
    const user_input = inputField.value.trim();

    if (!user_input) return;

    // Display user message
    const userMessage = document.createElement("div");
    userMessage.className = "chat-message user";
    userMessage.textContent = user_input;
    chatBox.appendChild(userMessage);
    inputField.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        // Send user input to the server
        const res = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message: user_input })  // Correct key
        });

        const data = await res.json();

        // Handle bot response
        const botMessage = document.createElement("div");
        botMessage.className = "chat-message bot";
        botMessage.innerHTML = data.response || "Error: No response"; // Handle error message
        chatBox.appendChild(botMessage);
        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (err) {
        console.error("Error:", err);
    }
}
