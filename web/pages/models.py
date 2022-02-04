import torch
from transformers import BertTokenizer
from ratsnlp.nlpbook.classification import ClassificationDeployArguments


"""
def run_sum(model, tokenizer, context):
    inputs = tokenizer([context], max_length=1024, return_tensors='tf')
    summary_ids = model.generate(inputs['input_ids'],
                                 num_beams=20, max_length=30, early_stopping=True)
    outputs = [tokenizer.decode(g, skip_special_tokens=True, 
                            clean_up_tokenization_spaces=False) for g in summary_ids]
    
    return outputs
"""

# 유용성 점수
def kcelectra(sentence):
    args = ClassificationDeployArguments(
        pretrained_model_name= 'beomi/KcELECTRA-base',
        downstream_model_checkpoint_fpath= './'
    )

    model = torch.load('/Users/yejin/Desktop/Career/Projects/Review_Helpfulness/web/pages/kcelectra_5(맞춤법_최종0.948).pt')
    # model.load_state_dict({k.replace("model.", ""): v for k, v in fine_tuned_model_ckpt['state_dict'].items()})
    # model.eval()

    tokenizer = BertTokenizer.from_pretrained(
    args.pretrained_model_name,
    do_lower_case=False,
    )

    inputs = tokenizer(
        [sentence],
        max_length=args.max_seq_length,
        padding="max_length",
        truncation=True,
    )
    with torch.no_grad():
        outputs = model(**{k: torch.tensor(v) for k, v in inputs.items()})
        prob = outputs.logits.softmax(dim=1)
        positive_prob = round(prob[0][1].item(), 4)
        negative_prob = round(prob[0][0].item(), 4)
        pred = "유용 (useful)" if torch.argmax(prob) == 1 else "비유용 (useless)"
        result = {
        # 'sentence': sentence,
        'prediction': pred,
        'useful_percent': positive_prob,
        'useless_percent': negative_prob
    }
    return result