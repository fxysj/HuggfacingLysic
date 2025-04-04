from flask import Blueprint, request, jsonify
from transformers import BertTokenizer, GPT2LMHeadModel, TextGenerationPipeline

api = Blueprint('api', __name__)

model_id = "uer/gpt2-chinese-lyric"
tokenizer = BertTokenizer.from_pretrained(model_id)
model = GPT2LMHeadModel.from_pretrained(model_id)
generator = TextGenerationPipeline(model=model, tokenizer=tokenizer)

@api.route("/generate", methods=["POST"])
def generate_text():
    data = request.get_json()
    text = data.get("text", "")
    result = generator(text_inputs=text, max_length=100, do_sample=True)
    return jsonify(result)
