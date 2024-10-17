class PromptUtils:

    @staticmethod
    def create_sd_prompt(descriptive_prompt: str, style: str) -> str:
        style = style.lower()
        if style == "cyberpunk":
            prompt = "3d render, wearing a stylish cyberpunk outfit, 4k, 8k, VR gaming booths, glowing neon pink and blue, blurry background, intricate details, (masterpiece:1.2), (best quality:1.2), (realistic:1.2), <lora:more_details:0.3>, (perfect composition:1.4), cyberpunk style, cyberpunk 2077<lora:sdxl_cyberpunk:0.65>"
        elif style == "hogwarts":
            prompt = "4k, 8k, highly detailed, black uniform, black robe, dark background, stone archway, cinematic lighting, intricate details, (masterpiece:1.2), (best quality:1.2), (realistic:1.2), <lora:harry_potter_v1:1>"
        elif style == "astronaut":
            prompt = "3d render, 4k, 8k, wearing a futuristic cyberpunk outfit, astronaut uniform, (astronaut adventure:1.5), inside a spaceship, with galaxy view, intricate details, (masterpiece:1.2), (best quality:1.2), (realistic:1.2), <lora:more_details:0.3>, (perfect composition:1.4)"
        elif style == "hawaii":
            prompt = "3d render, 4k, 8k, wearing beach shirt, (beach:1.2), lively background, with a vibrant Hawaiian luau, sunlight, day time, lush tropical greenery, hibiscus and orchid flowers, tiki torches, seashells, sand, intricate details, (masterpiece:1.2), (best quality:1.2), (realistic:1.2), <lora:more_details:0.3>, (perfect composition:1.4)"
        elif style == "secret agent":
            prompt = "3d render, 4k, 8k, a dimly lit, futuristic room crisscrossed with vibrant laser beams, hidden passageways hinted at in the shadows, cryptic codes glowing on the walls. A stylish secret agent outfit, (secret agent outfit: 1.2), reminiscent of James Bond, intricate details, (masterpiece:1.2), (best quality:1.2), (realistic:1.2), <lora:more_details:0.3>, (perfect composition:1.4)"
        elif style == "cowboy":
            prompt = "3d render, 4k, 8k, wearing a classic cowboy clothes, (cowboy: 1.5), rustic western saloon interior, wooden barrels, hay bales, burlap textures, wanted posters in the background, horseshoes, cowboy hats, bandanas, sheriff badges, dimly lit, intricate details, (masterpiece:1.2), (best quality:1.2), (perfect composition:1.4)"
        else:
            prompt = f"in the style of {style}, <lora:more_details:0.3>, (high detail:1.1), (detailed face:1.2), (perfect composition:1.4)"
        
        # new_prompt = f"((masterpiece)), (extremely intricate:1.2), (realistic:0.5), (digital painting:1), ({style.lower()}:1.3), {descriptive_prompt}, <lora:more_details:0.3>, (high detail:1.1), (detailed face:1.2), (perfect composition:1.4)"
        return f"{descriptive_prompt}, {prompt}"

    @staticmethod
    def get_sd_negative_prompt() -> str:
        return "nsfw, naked, (low quality, worst quality:1.4), cgi, text, chinese, usa, america, signature, watermark, extra limbs, bad hands, ugly fingers, bad finger, anime, deformed, BadDream, (UnrealisticDream:1.2)"
