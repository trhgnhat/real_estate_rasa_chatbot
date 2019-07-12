from rasa.nlu.training_data import load_data

# This re-uses the Rasa NLU converters code to turn a JSON Rasa NLU training
# file into MD format and save it

# Assumes you have Rasa NLU installed :-)

# If you want other options, look at the NLU code to work out how to handle them

# USE AT YOUR OWN RISK

input_md_file = ['../data/test_data.md', '../data/training_data.md']

# *******************************************************
# TAKE CARE: output_md_file is overwritten automatically
# *******************************************************


for each in input_md_file:
    with open(each.replace(".md", ".json"), 'w') as f:
        f.write(load_data(each).as_json())
    print("Done for", each, 'file')
input("Press Enter to exit")
