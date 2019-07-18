from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter
import pprint


def train_nlu(data, configs, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    fixed_model_name = configs.split("/")[2] + "_with_duckling"
    # save model
    model_directory = trainer.persist(model_dir, fixed_model_name=fixed_model_name)


def run_nlu(model_dir):
    interpreter = Interpreter.load(model_dir)
    # pprint.pprint(interpreter.parse(u"i want ot see @trhgnhat on the next morning at 10 am"))
    result = interpreter.parse(u"i want ot see @trhgnhat on the next morning at 10 am")
    # print(result["entities"][0]["value"])  # 2019-07-15T10:00:00.000+07:00
    from dateutil.parser import parse
    from dateutil.relativedelta import relativedelta
    dt_obj = parse(result["entities"][0]["value"])
    # print(dt_obj.date().ctime())  # Mon Jul 15 00:00:00 2019
    # print(dt_obj.ctime())  # dt_obj.ctime() Mon Jul 15 10:00:00 2019
    # print(dt_obj.time())  # 10:00:00
    # print(dt_obj.timetz())  # 10:00:00+07:00
    new_dt_obj = dt_obj.date() + relativedelta(hours=dt_obj.hour, minutes=dt_obj.minute,
                                               second=dt_obj.second) + relativedelta(minutes=-5)
    dt_obj = parse(result["entities"][0]["value"])
    dt_obj = dt_obj.date() + relativedelta(hours=dt_obj.hour, minutes=dt_obj.minute, second=dt_obj.second)
    remind_dt_obj = dt_obj + relativedelta(minutes=-5)  # 5 minutes before
    # print(new_dt_obj)  # 2019-07-15 09:55:00
    print(remind_dt_obj.isoformat())  # 2019-07-15T09:55:00


if __name__ == '__main__':
    config_dir = "custom_nlu_config_1/nlu_config.md"
    # train_nlu('./data/test_data.md', 'configs/nlu_configs/' + config_dir, './models/nlu')
    run_nlu('./models/nlu/default/' + config_dir.split("/")[0] + "_with_duckling")
