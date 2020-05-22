import tensorflow as tf


from app.core.config import TOKENIZER, MODEL

def predict(model=MODEL, tokenizer=TOKENIZER, *,  sentence:str="Hello"):
    # encode context the generation is conditioned on
    input_ids = tokenizer.encode(sentence, return_tensors='tf')


    # set seed to reproduce results. Feel free to change the seed though to get different results
    tf.random.set_seed(0)

    # set top_k = 50 and set top_p = 0.95 and num_return_sequences = 1
    sample_outputs = model.generate(
        input_ids,
        do_sample=True, 
        max_length=50, 
        top_k=50, 
        top_p=0.95, 
        num_return_sequences=3
    )
    sample_output = sample_outputs[0]
    sample_output= tokenizer.decode(sample_output, skip_special_tokens=True)
    return sample_output




