import React from 'react';
import './ChatMessage.css';

interface Message {
  id: string;
  content: string;
  sender: 'user' | 'ai';
  timestamp: Date;
}

interface ChatMessageProps {
  message: Message;
}

const formatTime = (date: Date) => {
  return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
};

const ChatMessage: React.FC<ChatMessageProps> = ({ message }) => {
  const { content, sender, timestamp } = message;
  const isUser = sender === 'user';

  return (
    <div className={`message ${isUser ? 'user-message' : 'ai-message'}`}>
      <div className="message-avatar">
        {isUser ? '👤' : '🤖'}
      </div>
      <div>
        <div className="message-content">
          {content}
        </div>
        <div className="message-timestamp">
          {formatTime(timestamp)}
        </div>
      </div>
    </div>
  );
};

export default ChatMessage;
