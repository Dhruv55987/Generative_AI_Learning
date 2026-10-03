let selectedMode = null;

function selectMode(mode) {

```
selectedMode = mode;

const currentMode = document.getElementById("currentMode");

if (mode === 1) {
    currentMode.innerText = "Angry 😡";
}

if (mode === 2) {
    currentMode.innerText = "Sad 😢";
}

if (mode === 3) {
    currentMode.innerText = "Funny 😂";
}
```

}

function sendMessage() {

```
const input = document.getElementById("userInput");
const chatBox = document.getElementById("chatBox");

const message = input.value.trim();

if (message === "") {
    return;
}

if (selectedMode === null) {
    alert("Please select an AI mode first.");
    return;
}

// User message
const userMessage = document.createElement("div");

userMessage.className = "user-message";
userMessage.innerText = message;

chatBox.appendChild(userMessage);

input.value = "";

// Placeholder for AI response
// Your Python/LangChain backend will provide the actual response.

const botMessage = document.createElement("div");

botMessage.className = "bot-message";
botMessage.innerText = "AI response will appear here.";

chatBox.appendChild(botMessage);

chatBox.scrollTop = chatBox.scrollHeight;
```

}

function exitChat() {

```
const chatBox = document.getElementById("chatBox");

chatBox.innerHTML = "";

const message = document.createElement("div");

message.className = "bot-message";
message.innerText = "Goodbye!";

chatBox.appendChild(message);
```

}

// Press Enter to send
document.getElementById("userInput").addEventListener("keypress", function(event) {

```
if (event.key === "Enter") {
    sendMessage();
}
```

});
