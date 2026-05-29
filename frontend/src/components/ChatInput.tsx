import React from 'react';
import './ChatInput.css';

interface ChatInputProps {
  value: string;
  onChange: (value: string) => void;
  onSend: () => void;
  isLoading: boolean;
}

const ChatInput: React.FC<ChatInputProps> = ({ value, onChange, onSend, isLoading }) => {
  const handleKeyPress = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      onSend();
    }
  };

  return (
    <div className="chat-input-wrapper">
      <div className="chat-input-container">
        <textarea
          className="chat-input"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your message... (Shift+Enter for new line)"
          disabled={isLoading}
          rows={1}
        />
        <button
          className="send-button"
          onClick={onSend}
          disabled={isLoading || value.trim() === ''}
          aria-label="Send message"
        >
          📤
        </button>
      </div>
      <p className="input-hint">Press Enter to send, Shift+Enter for new line</p>
    </div>
  );
};

export default ChatInput;
