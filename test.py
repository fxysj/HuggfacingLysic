from transformers import GPT2LMHeadModel,BertTokenizer,TextGenerationPipeline
if __name__ == '__main__':
    modle_id = "uer/gpt2-chinese-lyric"
    tokenizer = BertTokenizer.from_pretrained(modle_id)
    model = GPT2LMHeadModel.from_pretrained(modle_id)
    # 创建推理模型
    text_generator = TextGenerationPipeline(model=model, tokenizer=tokenizer)
    out = text_generator(text_inputs="雨滴敲打玻璃窗", max_length=100, do_sample=True)
    print(out)
#大模型是Huggfacing 模型和数据集和模型 推理模型 分词器
