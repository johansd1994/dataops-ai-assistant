import { useState } from "react";

function ChatInput({ onSend }) {

    const [message, setMessage] = useState("");

    const handleSend = () => {

        if (!message.trim()) return;

        onSend(message);

        setMessage("");
    };

    return (

        <div className="chat-input">

            <input
                type="text"
                placeholder="Escribe una pregunta..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                onKeyDown={(e) => {
                    if (e.key === "Enter") {
                        handleSend();
                    }
                }}
            />

            <button onClick={handleSend}>
                Enviar
            </button>

        </div>

    );

}

export default ChatInput;