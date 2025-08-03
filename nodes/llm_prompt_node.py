class LLMPromptNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"input_prompt": ("STRING", "Text prompt")}}
    RETURN_TYPES = ("STRING",)
    FUNCTION = "refine_prompt"

    def __init__(self):
        from llama_cpp import Llama
        self.model = Llama(model_path="models/Llama-2-7b.ggmlv3.q4_0.bin")

    def refine_prompt(self, input_prompt):
        augmented = self.model(f"Improve this prompt for image generation: {input_prompt}")
        return (augmented["choices"][0]["text"], )