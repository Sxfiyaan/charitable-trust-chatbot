from app.services.prompt_service import PromptService


print("SYSTEM PROMPT:")
print(PromptService.get_system_prompt())

print("\nFAQ PROMPT:")
print(PromptService.get_faq_prompt())

print("\nDONATION PROMPT:")
print(PromptService.get_donation_prompt())

print("\nVOLUNTEER PROMPT:")
print(PromptService.get_volunteer_prompt())