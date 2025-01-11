// Toggle chatbot visibility
function openChatbot() {
    const chatbotWindow = document.getElementById("chatbot-window");
    chatbotWindow.classList.toggle("hidden");
}

// Simulated AI response function
async function getAIResponse() {
    const chatInput = document.getElementById("chat-input");
    const chatOutput = document.getElementById("chat-output");

    if (!chatInput.value.trim()) {
        alert("Please type a question!");
        return;
    }

    const userMessage = chatInput.value.trim();
    chatInput.value = ""; // Clear input

    // Display user message
    const userMessageElement = document.createElement("div");
    userMessageElement.textContent = `You: ${userMessage}`;
    chatOutput.appendChild(userMessageElement);

    // Simulate AI response
    const response = await fetchAIResponse(userMessage);

    // Display AI response
    const aiMessageElement = document.createElement("div");
    aiMessageElement.textContent = `AI: ${response}`;
    chatOutput.appendChild(aiMessageElement);
}

// Simulate AI API call
async function fetchAIResponse(prompt) {
    const apiKey = "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"; // Replace with your actual API key
    const endpoint = "https://api.openai.com/v1/completions"; // OpenAI API endpoint

    const requestData = {
        model: "text-davinci-003", // Choose your desired model
        prompt: prompt,
        max_tokens: 100, // Adjust token limit based on your requirements
        temperature: 0.7 // Adjust creativity level
    };

    try {
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`
            },
            body: JSON.stringify(requestData)
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        return data.choices[0].text.trim(); // Extract AI's response
    } 
    catch (error) {
        console.error("Error fetching AI response:", error);
        return "Sorry, I couldn't process your request. Please try again later.";
    }

}
