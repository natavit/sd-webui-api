class PromptUtils:

    @staticmethod
    def refine_prompt_for_dreamshaper(prompt: str, style: str) -> str:
        new_prompt = f"((masterpiece)), (extremely intricate:1.2), (realistic:0.5), (digital painting:1), ({style.lower()}:1.3), {
            prompt}, <lora:more_details:0.3>, (high detail:1.1), (detailed face:1.2), (perfect composition:1.4)"
        return new_prompt

    @staticmethod
    def get_negative_prompt_for_dreamshaper() -> str:
        return "BadDream, (UnrealisticDream:1.2), blurry, text, watermark, lowres"
