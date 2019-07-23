import gpt_2_simple as gpt2
import os

base_path = os.path.dirname(os.path.realpath(__file__))

#gpt2.download_gpt2(model_name='345M')   # model is saved into current directory under /models/117M/

name = "Reid"
sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              base_path + '/data/{}.txt'.format(name),
              model_name='345M',
              steps=2000, run_name=name)   # steps is max number of training steps

gpt2.generate(sess, run_name=name)
