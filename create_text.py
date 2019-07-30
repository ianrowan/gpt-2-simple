import gpt_2_simple as gpt2
import os

base_path = os.path.dirname(os.path.realpath(__file__))
name = 'SatoshiSm'

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name=name)
while(True):
    print("\n\n\n")
    prompt = input("Write a few words or press enter for random: ")
    print("Thinking.....")
    gpt2.generate(sess, run_name=name, prefix=prompt if prompt is not ""else None, length=64)
'''
output = gpt2.generate(sess, run_name='andrewyang', prefix=prompt if prompt is not ""else None, return_as_list=True, nsamples=5)

for i in range(len(output)):
    print(output[i].split("\n")[0])
'''
