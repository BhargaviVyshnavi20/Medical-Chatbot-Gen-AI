// Function to add a user message bubble
function addUserMessage(text) {
    const chatArea = document.getElementById("chatArea");
    const msg = document.createElement("div");
    msg.className = "message user";
    msg.innerHTML = `<div class="bubble">${text}</div>`;
    chatArea.appendChild(msg);
    scrollBottom();
}

// Function to add a bot message bubble
function addBotMessage(text) {
    const chatArea = document.getElementById("chatArea");
    const msg = document.createElement("div");
    msg.className = "message bot";
    
    // This allows the browser to render the bullet points and bold text
    msg.innerHTML = `
        <div class="icon">🩺</div>
        <div class="bubble">${text}</div>
    `;
    
    chatArea.appendChild(msg);
    scrollBottom();
}



// Function to handle the auto-scroll
function scrollBottom() {
    const chatArea = document.getElementById("chatArea");
    chatArea.scrollTop = chatArea.scrollHeight;
}

// The main function to send data to Flask
function sendMessage() {
    const userInput = document.getElementById("userInput");
    const text = userInput.value.trim();
    
    if (!text) return;

    // 1. Show user message immediately
    addUserMessage(text);
    userInput.value = "";

    // 2. Prepare data for Flask (matching request.form["msg"])
    const formData = new FormData();
    formData.append("msg", text);

    // 3. Fetch call to the backend
    fetch("/get", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.text();
    })
    .then(data => {
        // 4. Show the AI's actual answer
        addBotMessage(data);
    })
    .catch(error => {
        console.error("Error:", error);
        addBotMessage("I am having trouble connecting to the server. Please check your connection.");
    });
}

// Function for the suggestion buttons
function sendQuick(text) {
    const userInput = document.getElementById("userInput");
    userInput.value = text;
    sendMessage();
}

// Enable the "Enter" key to send messages
document.addEventListener("DOMContentLoaded", function() {
    const userInput = document.getElementById("userInput");
    userInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});