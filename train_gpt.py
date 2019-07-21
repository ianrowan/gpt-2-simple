import gpt_2_simple as gpt2
import os

base_path = os.path.dirname(os.path.realpath(__file__))

gpt2.download_gpt2(model_name='345M')   # model is saved into current directory under /models/117M/

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              '{base_path}/data/elon1.csv',
              model_name='345M',
              steps=10000)   # steps is max number of training steps

gpt2.generate(sess)