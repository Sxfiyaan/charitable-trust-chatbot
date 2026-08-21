from pathlib import Path


class PromptService:

    PROMPTS_PATH = Path("app/prompts")

    @classmethod
    def _load_prompt(cls, filename: str) -> str:
        prompt_path = cls.PROMPTS_PATH / filename

        return prompt_path.read_text(encoding="utf-8")

    @classmethod
    def get_system_prompt(cls) -> str:
        return cls._load_prompt("system_prompt.txt")

    @classmethod
    def get_faq_prompt(cls) -> str:
        return cls._load_prompt("faq_prompt.txt")

    @classmethod
    def get_donation_prompt(cls) -> str:
        return cls._load_prompt("donation_prompt.txt")

    @classmethod
    def get_volunteer_prompt(cls) -> str:
        return cls._load_prompt("volunteer_prompt.txt")