import getopt
import sys
import time
from utils.split_dataset import SplitDataset
from CaseRecommender.utils.cross_fold_validation import CrossFoldValidation

__author__ = 'Arthur Fortes'

text = '__________________________________________________________________\n' \
       '\n  [Case Recommender Instructions] Split Dataset  \n' \
       '__________________________________________________________________\n\n'\
       '\nCommand: \n' \
       '  >> python split_dataset.py \n' \
       '\nArguments:\n' \
       '-h -> HELP\n' \
       '-t or --split_type=  -> Values: CrossFoldValidation | SimpleSplit \n' \
       '-f or --dataset=     -> Directory where will be writing the folds \n' \
       '-n or --num_fold=    -> Number of folds \n' \
       '-s or --space_type=  -> Values: tabulation | comma | dot - Default Value: tabulation \n' \
       '\nIF -t CrossFoldValidation :\n' \
       '-d or --dataset=     -> Dataset with directory [Accepts one file only] \n' \
       '\n IF -t SimpleSplit :\n' \
       '-d or --dataset=     -> List of feedback types [Accepts one or more files in a list] \n' \
       '-r or --test_ratio=  -> Percentage of interactions dedicated to test set [Default = 0.1 = 10%] \n' \
       '\nExamples: \n' \
       '  >> python split_dataset.py -t CrossFoldValidation -d home\\documents\\file.dat -f home\\documents\\ -n 5' \
       ' -s comma\n' \
       '  >> python split_dataset.py -t SimpleSplit -d "[home\\documents\\rate.dat, home\\documents\\rate.dat]" ' \
       '-f home\\documents\\ -n 5 -s comma -r 0.1\n'


def main(argv):
    dataset = ''
    dir_fold = ''
    num_fold = 10
    space_type = '\t'
    split_type = ''
    test_ratio = 0.1

    try:
        opts, args = getopt.getopt(argv, "h:t:d:f:n:s:r:",
                                   ["dataset=", "split_type", "dir_fold=", "num_fold=", "space_type=", "test_ratio="])
    except getopt.GetoptError:
        print(text)
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print(text)
            sys.exit()
        elif opt in ("-s", "--space_type"):
            space_type = arg
            if space_type == 'tabulation':
                space_type = '\t'
            elif space_type == 'comma':
                space_type = ','
            elif space_type == 'dot':
                space_type = '.'
            else:
                print(text)
                sys.exit()
        elif opt in ("-d", "--dataset"):
            dataset = arg
        elif opt in ("-f", "--dir_fold"):
            dir_fold = arg
        elif opt in ("-n", "--num_fold"):
            num_fold = arg
        elif opt in ("-t", "--split_type"):
            split_type = arg
        elif opt in ("-r", "--test_ratio"):
            test_ratio = arg

    if dataset == '':
        print(text)
        sys.exit()

    if split_type == '':
        print(text)
        sys.exit()

    if dir_fold == '':
        print(dir_fold)
        print("\nError: Please enter a directory to write folds!\n")
        print(text)
        sys.exit()

    print("\n[Case Recommender - Cross Fold Validation]")
    print "Dataset File(s): ", dataset
    print "Dir Folds: ", dir_fold
    print "Number of Folds: ", num_fold
    print("\nPlease wait few seconds...")
    starting_point = time.time()

    if split_type == 'CrossFoldValidation':
        CrossFoldValidation(dataset, space_type=space_type, dir_folds=dir_fold, n_folds=int(num_fold))
    elif split_type == 'SimpleSplit':
        dataset = dataset.replace('[', '').replace(']', '').replace(' ', '').split(',')
        print "Split dataset in train: ", (1-float(test_ratio)) * 100, "% and test: ", float(test_ratio)*100, "%"
        SplitDataset(dataset, space_type=space_type, dir_folds=dir_fold, n_folds=int(num_fold),
                     test_ratio=float(test_ratio))
    else:
        print(text)
        sys.exit()
    elapsed_time = time.time() - starting_point
    print("Runtime: " + str(elapsed_time / 60) + " second(s)")
    print("SplitDataset Finished!\n")


if __name__ == "__main__":
    main(sys.argv[1:])
