import gpt_2_simple as gpt2
import os

base_path = os.path.dirname(os.path.realpath(__file__))

prompt = input("Write a few words or click enter for random: ")

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='Ian')
gpt2.generate(sess, run_name='Ian', prefix=prompt if prompt is not ""else None)
'''
output = gpt2.generate(sess, run_name='andrewyang', prefix=prompt if prompt is not ""else None, return_as_list=True, nsamples=5)

for i in range(len(output)):
    print(output[i].split("\n")[0])
'''