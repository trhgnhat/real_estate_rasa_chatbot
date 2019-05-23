from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
import pprint


def train_nlu(data, configs, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    fixed_model_name = configs.split("/")[2]
    # save model
    model_directory = trainer.persist(model_dir, fixed_model_name=fixed_model_name)


def run_nlu(model_dir):
    interpreter = Interpreter.load(model_dir)
    pprint.pprint(interpreter.parse(u"This large and nice double bedroom located in Hoxton is very confortable"))


if __name__ == '__main__':
    config_dir = "custom_nlu_config_1/nlu_config.md"
    # train_nlu('./data/data.json', 'configs/nlu_configs/' + config_dir, './models/nlu')
    run_nlu('./models/nlu/default/' + config_dir.split("/")[0])
