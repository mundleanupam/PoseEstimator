import csv

option = None


def pytest_addoption(parser):
    parser.addoption(
        "--dataset", action="store", default="dataset0",
        help="""my options: 
        dataset0 
        or dataset1 
        or dataset2 
        or dataset3 
        or dataset4 
        or dataset5"""
    )


def data_provider():
    dataset = option
    if dataset is None:
        return """Please specify a filename from options" \
               dataset1 or dataset2 or dataset3 or dataset4
               or dataset5 or dataset6. By default it sets to
               dataset0
               """
    if dataset in ["dataset0", "dataset1", "dataset2", "dataset3", "dataset4", "dataset5"]:
        last_time = 0.0
        row_dict = []
        output_dataset_file = dataset + '_output.csv'
        try:
            with open('datasets/' + output_dataset_file) as infile:
                readoutput = csv.DictReader(infile, delimiter=',')
                for row in readoutput:
                    row_dict.append([row.get('time'), row.get(' steering_angle'),
                                     row.get(' encoder'), row.get(' angular_velocity'),
                                     row.get(' X'),
                                     row.get(' Y'), row.get(' Th'), last_time])
                    last_time = float(row.get('time'))
        except Exception as e:
            print(e+"Error: cannot open file")
        return row_dict
    else:
        return """Wrong Input File -
        Please specify a filename from options" \
        dataset0 or dataset1 or dataset2 or dataset3
        or dataset4 or dataset5"""


def pytest_configure(config):
    global option
    option = config.option.dataset
    print("Running the dataset: "+option)







