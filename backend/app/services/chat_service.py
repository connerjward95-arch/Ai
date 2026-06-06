"""Chat service for managing conversations"""

import logging
from typing import Any, Dict, List, Optional
import asyncio

from app.services.llm_service import get_llm_service

logger = logging.getLogger(__name__)


class ChatService:
    """Service for handling chat operations using intelligent LLM"""

    def __init__(self):
        self.conversations: Dict[str, List[Dict]] = {}
        self.llm_service = None

    async def _ensure_llm_initialized(self):
        """Ensure LLM service is initialized"""
        if self.llm_service is None:
            self.llm_service = await get_llm_service()

    async def process_message(self, message: str, session_id: Optional[str] = None) -> str:
        """
        Process user message and generate intelligent response using LLM
        """
        try:
            await self._ensure_llm_initialized()
            
            # Generate intelligent response from LLM service
            response = await self.llm_service.generate_response(message)
            
            # Store in conversation history
            if session_id:
                if session_id not in self.conversations:
                    self.conversations[session_id] = []
                
                self.conversations[session_id].append({
                    "role": "user",
                    "content": message,
                })
                self.conversations[session_id].append({
                    "role": "assistant",
                    "content": response,
                })
            
            return response
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            raise

    async def get_history(
        self,
        session_id: Optional[str],
        limit: int = 50,
    ) -> List[Dict[str, Any]]:
        """
        Retrieve conversation history for a session
        """
        try:
            if not session_id or session_id not in self.conversations:
                return []
            
            history = self.conversations[session_id][-limit:]
            return [
                {
                    "message": item.get("content", ""),
                    "sender": "user" if item.get("role") == "user" else "ai",
                    "timestamp": "",
                }
                for item in history
            ]
        except Exception as e:
            logger.error(f"Error retrieving history: {e}")
            raise

    async def get_similar_messages(
        self,
        message: str,
        session_id: Optional[str] = None,
        limit: int = 3,
    ) -> List[Dict[str, Any]]:
        """
        Get semantically similar messages from conversation history
        """
        try:
            await self._ensure_llm_initialized()
            similar = self.llm_service.get_similar_messages(message, limit)
            return similar
        except Exception as e:
            logger.error(f"Error getting similar messages: {e}")
            return []

    async def get_conversation_summary(self, session_id: Optional[str]) -> Dict[str, Any]:
        """
        Get summary of conversation
        """
        try:
            await self._ensure_llm_initialized()
            return self.llm_service.get_conversation_summary()
        except Exception as e:
            logger.error(f"Error getting conversation summary: {e}")
            return {"summary": "Unable to generate summary"}

    def clear_history(self, session_id: Optional[str] = None):
        """
        Clear conversation history
        """
        if session_id and session_id in self.conversations:
            del self.conversations[session_id]
        elif not session_id:
            self.conversations.clear()
            if self.llm_service:
                self.llm_service.clear_history()
