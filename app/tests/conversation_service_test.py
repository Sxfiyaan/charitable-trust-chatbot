from app.services.conversation_service import ConversationService

session_id = "test"

ConversationService.clear_history(session_id)

ConversationService.add_user_message(
    session_id,
    "Hi"
)

ConversationService.add_assistant_message(
    session_id,
    "Hello Akif!"
)

history = ConversationService.get_history(session_id)

print(history)