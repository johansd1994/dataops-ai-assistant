import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

function ChatMessage({ role, content }) {

    return (

        <div className={`message ${role}`}>

            <strong>

                {role === "user"
                    ? "👤 Tú"
                    : "🤖 Assistant"}

            </strong>

            <ReactMarkdown remarkPlugins={[remarkGfm]}>{content}</ReactMarkdown>

        </div>

    );

}

export default ChatMessage;