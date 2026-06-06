import React from 'react';
import './ChatInput.css';

interface ChatInputProps {
  value: string;
  onChange: (value: string) => void;
  onSend: () => void;
  onMicClick: () => void;
  isLoading: boolean;
  isListening: boolean;
  micSupported: boolean;
}

const ChatInput: React.FC<ChatInputProps> = ({ value, onChange, onSend, onMicClick, isLoading, isListening, micSupported }) => {
  const handleKeyPress = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      onSend();
    }
  };

  return (
    <div className="chat-input-wrapper">
      <div className="chat-input-container">
        <button
          className={`mic-button ${isListening ? 'listening' : ''}`}
          onClick={onMicClick}
          disabled={isLoading || !micSupported}
          aria-label={isListening ? 'Stop voice input' : 'Start voice input'}
        >
          {isListening ? '🎙️' : '🎤'}
        </button>
        <textarea
          className="chat-input"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Message AI... (Shift+Enter for new line)"
          disabled={isLoading}
          rows={1}
          aria-label="Message AI input"
        />
        <button
          className="send-button"
          onClick={onSend}
          disabled={isLoading || value.trim() === ''}
          aria-label="Send message to AI"
        >
          📤
        </button>
      </div>
      <div className="input-hint-row">
        <p className="input-hint">Press Enter to send, Shift+Enter for new line</p>
        <p className="mic-hint">
          {micSupported
            ? isListening
              ? 'Listening... speak now.'
              : 'Tap the microphone button to talk to AI.'
            : 'Microphone not available in this browser.'}
        </p>
      </div>
    </div>
  );
};

export default ChatInput;
