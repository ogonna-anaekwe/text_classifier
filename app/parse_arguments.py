import argparse

def parse_arguments():
    # create argument parser to invoke script through the command line
    version_parser = argparse.ArgumentParser(description='captures user-inputed version to route the prediction service to the corresponding version.')

    # define argument key, type, and help text
    version_parser.add_argument('version', type=int, help='version of the model to serve')

    # parse arguments
    args = version_parser.parse_args()
    return args