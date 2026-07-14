import { useState } from "react";

import api from "../services/api";

import ChatInput from "../components/ChatInput";
import ChatMessage from "../components/ChatMessage";
import Loading from "../components/Loading";

function Home() {

    const [messages, setMessages] = useState([]);

    const [loading, setLoading] = useState(false);

    const sendMessage = async (message) => {

        setMessages((old) => [
            ...old,
            {
                role: "user",
                content: message,
            },
        ]);

        setLoading(true);

        try {

            const response = await api.post(
                "/chat",
                {
                    message,
                }
            );

            setMessages((old) => [

                ...old,

                {
                    role: "assistant",
                    content: response.data.response,
                },

            ]);

        } catch {

            setMessages((old) => [

                ...old,

                {

                    role: "assistant",

                    content: "Error consultando el backend.",

                },

            ]);

        }

        setLoading(false);

    };

    return (

        <div className="container">

            <h1>🤖 DataOps AI Assistant</h1>

            <p>
                AWS Bedrock • Claude • Athena • S3
            </p>

            <div className="chat-box">

                {

                    messages.map((message, index) => (

                        <ChatMessage

                            key={index}

                            role={message.role}

                            content={message.content}

                        />

                    ))

                }

                {loading && <Loading />}

            </div>

            <ChatInput

                onSend={sendMessage}

            />

        </div>

    );

}

export default Home;