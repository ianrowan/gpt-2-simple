import gpt_2_simple as gpt2
import os
from gpt_2_simple import gpt_2

base_path = os.path.dirname(os.path.realpath(__file__))
existing = False
#gpt2.download_gpt2(model_name='345M')   # model is saved into current directory under /models/117M/
sess = gpt2.start_tf_sess()
name = "Ian"

if existing:
    gpt2.finetune(sess,
                  base_path + '/data/{}.txt'.format(name),
                  model_name='345M',
                  steps=2000, run_name=name)   # steps is max number of training steps
else:
    gpt_2.train(sess,
                base_path + '/data/{}.txt'.format(name),
                model_name='SMTEST',
                steps=10000, restore_from='new')

gpt2.generate(sess, run_name=name)
