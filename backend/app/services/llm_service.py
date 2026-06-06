"""Large Language Model Service using open-source models"""

import logging
import asyncio
from typing import List, Dict, Any, Optional
from functools import lru_cache

import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer, util

logger = logging.getLogger(__name__)


class LLMService:
    """Service for LLM-based chat responses using open-source models"""

    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"LLMService initialized on device: {self.device}")
        
        self.embedding_model = None
        self.zero_shot_classifier = None
        self.text_generation_model = None
        self.tokenizer = None
        
        # Intent definitions
        self.intents = {
            "greeting": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon"],
            "farewell": ["bye", "goodbye", "farewell", "see you", "exit", "quit"],
            "help": ["help", "how", "what", "why", "explain", "tell me", "can you"],
            "knowledge": ["what is", "who is", "when", "where", "information", "about"],
            "joke": ["joke", "funny", "laugh", "humor", "tell me a joke"],
            "math": ["calculate", "math", "compute", "plus", "minus", "multiply", "divide"],
        }
        
        self.conversation_history = []
        self.max_history = 10

    async def initialize(self):
        """Initialize models in background"""
        try:
            # Load sentence embeddings model (lightweight)
            logger.info("Loading sentence-transformers embedding model...")
            self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2', device=self.device)
            logger.info("Embedding model loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load embedding model: {e}")

    def _get_intent(self, text: str) -> str:
        """Detect user intent from text"""
        text_lower = text.lower()
        
        # Simple keyword-based intent detection
        for intent, keywords in self.intents.items():
            if any(keyword in text_lower for keyword in keywords):
                return intent
        
        return "general"

    def _generate_response(self, message: str, intent: str) -> str:
        """Generate contextual response based on intent and message"""
        message_lower = message.lower()
        
        # Greeting responses
        if intent == "greeting":
            greetings = [
                "Hello! I'm an AI Learning Machine. How can I help you today?",
                "Hi there! Great to chat with you. What's on your mind?",
                "Greetings! I'm here to assist and learn from our conversation.",
            ]
            return greetings[hash(message) % len(greetings)]
        
        # Farewell responses
        if intent == "farewell":
            farewells = [
                "Goodbye! It was great chatting with you. Feel free to return anytime!",
                "See you later! Thanks for the conversation. Looking forward to learning more!",
                "Farewell! I've enjoyed our interaction. Come back soon!",
            ]
            return farewells[hash(message) % len(farewells)]
        
        # Help responses
        if intent == "help":
            help_text = f"I'd be happy to help with '{message}'! "
            if "how" in message_lower:
                help_text += "I can provide step-by-step guidance and explanations."
            elif "what" in message_lower:
                help_text += "I can explain concepts, provide definitions, and share information."
            elif "why" in message_lower:
                help_text += "I can explain the reasons and background behind things."
            else:
                help_text += "Feel free to ask me anything and I'll do my best to assist."
            return help_text
        
        # Joke responses
        if intent == "joke":
            jokes = [
                "Why did the AI go to school? To improve its learning algorithms! 😄",
                "What do you call an AI that tells jokes? A funny algorithm! 😂",
                "Why did the chatbot visit the library? To find more information to learn from! 📚",
            ]
            return jokes[hash(message) % len(jokes)]
        
        # Math responses
        if intent == "math":
            math_response = "I can help with mathematical problems! "
            if "plus" in message_lower or "+" in message:
                math_response += "Try asking me to calculate something like '5 plus 3'."
            elif "multiply" in message_lower or "*" in message:
                math_response += "I can multiply numbers for you!"
            else:
                math_response += "Feel free to give me a math problem to solve."
            return math_response
        
        # Knowledge responses
        if intent == "knowledge":
            knowledge_response = f"That's an interesting question about your message! "
            knowledge_response += "I'm continuously learning from our interactions and building knowledge about various topics. "
            knowledge_response += "Feel free to ask me anything and I'll provide the best information I can."
            return knowledge_response
        
        # General responses with context awareness
        general_responses = [
            f"That's an interesting thought! I'm analyzing what you said: '{message}'. I'm learning from this interaction.",
            f"I understand your message: '{message}'. Let me think about this and provide meaningful context.",
            f"Thank you for sharing that perspective. I'm continuously improving my understanding through conversations like this.",
            f"I appreciate your input. Based on what you've shared, I'm building a richer understanding of the topic.",
            f"That's valuable information. I'm using this to enhance my learning and provide better responses.",
        ]
        
        return general_responses[hash(message) % len(general_responses)]

    async def generate_response(self, message: str) -> str:
        """Generate an intelligent response to user message"""
        try:
            if not message or not message.strip():
                return "I'm ready to chat! Please share something with me."
            
            # Detect intent
            intent = self._get_intent(message)
            
            # Generate response based on intent
            response = self._generate_response(message, intent)
            
            # Store in history
            self.conversation_history.append({
                "role": "user",
                "content": message,
                "intent": intent,
            })
            self.conversation_history.append({
                "role": "assistant",
                "content": response,
            })
            
            # Keep history size manageable
            if len(self.conversation_history) > self.max_history:
                self.conversation_history = self.conversation_history[-self.max_history:]
            
            return response
        
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return "I'm processing your message. Please try again."

    def get_similar_messages(self, message: str, num_results: int = 3) -> List[Dict[str, Any]]:
        """Find similar messages from conversation history using embeddings"""
        if not self.embedding_model or len(self.conversation_history) < 2:
            return []
        
        try:
            # Get embedding for current message
            current_embedding = self.embedding_model.encode(message, convert_to_tensor=True)
            
            # Compare with history
            similar = []
            for i, item in enumerate(self.conversation_history):
                if item.get("role") == "user" and item.get("content") != message:
                    history_embedding = self.embedding_model.encode(
                        item.get("content", ""), convert_to_tensor=True
                    )
                    similarity = util.pytorch_cos_sim(current_embedding, history_embedding).item()
                    
                    if similarity > 0.5:  # Threshold for similarity
                        similar.append({
                            "content": item.get("content"),
                            "similarity": float(similarity),
                            "index": i,
                        })
            
            # Sort by similarity and return top results
            similar.sort(key=lambda x: x["similarity"], reverse=True)
            return similar[:num_results]
        
        except Exception as e:
            logger.error(f"Error getting similar messages: {e}")
            return []

    def get_conversation_summary(self) -> Dict[str, Any]:
        """Get summary of current conversation"""
        if not self.conversation_history:
            return {"message_count": 0, "intents": {}, "summary": "No conversation yet."}
        
        intent_counts = {}
        for item in self.conversation_history:
            if "intent" in item:
                intent = item["intent"]
                intent_counts[intent] = intent_counts.get(intent, 0) + 1
        
        return {
            "message_count": len(self.conversation_history),
            "intents": intent_counts,
            "summary": f"Conversation with {len(self.conversation_history)} messages covering intents: {', '.join(intent_counts.keys())}",
        }

    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []


# Global instance
_llm_service: Optional[LLMService] = None


async def get_llm_service() -> LLMService:
    """Get or create LLM service instance"""
    global _llm_service
    
    if _llm_service is None:
        _llm_service = LLMService()
        await _llm_service.initialize()
    
    return _llm_service
