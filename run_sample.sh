
# train
python srl_main.py --do_train --fp16 --train_data_path=./data/test.stanford_new.json  --dev_data_path=./data/test.stanford_new.json --test_data_path=./data/test.stanford_new.json  --use_bert --bert_model bert-large-uncased  --use_crf --n_mlp=200 --max_seq_length=256 --train_batch_size=4 --direct --eval_batch_size=4 --num_train_epochs=100 --warmup_proportion=0.06 --learning_rate=1e-5 --patient=10 --model_name=model2 --knowledge=dep


# test
#python srl_main.py --do_test --eval_model=./models/test_model/model --test_data_path=./data/demo/train.stanford.json --eval_batch_size=2

