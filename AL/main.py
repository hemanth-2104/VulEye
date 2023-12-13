import os
import argparse
import json
import subprocess
import threading
from time import sleep

def multiple():
    for i in range(5):
        command = f'python run.py --output_dir="./Models/model{i}" --train_data_file="./Files/train.jsonl" --model_type=roberta --tokenizer_name=microsoft/codebert-base --model_name_or_path=microsoft/codebert-base --do_eval --do_test --eval_data_file="./Files/valid.jsonl" --test_data_file="./Files/test.jsonl" --epoch 1 --block_size 400 --train_batch_size 16 --eval_batch_size 16 --learning_rate 2e-5 --max_grad_norm 1.0 --evaluate_during_training --seed 123456 > train.log 2>&1'
        subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Command '{i}' has completed.")

    actual = []
    length = 0
    with open("./Files/test.jsonl", 'r') as json_file:
        for line in json_file:
            try:
                data = json.loads(line)
                actual.append(data['target'])
                # Process the 'data' dictionary here
                print(data)
                length += 1
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
    matrix = [[-1 for i in range(5)] for hjk in range(length)]
    for i in range(5):
        with open(f".Models/model{i}/predictions.txt", 'r') as p:
            for j in range(length):
                a = p.readline()
                matrix[j][i] = int(a[-2])

    tp, tn, fp, fn = 0, 0, 0, 0
    for k in range(length):
        if matrix[k].count(0) >= 3:
            if actual[k] == 0:
                tn += 1
            else:
                fp += 1
        else:
            if actual[k] == 1:
                tp += 1
            else:
                fn += 1
    print("True Positive : ", tp)
    print("True Negative : ", tn)
    print("False Positive : ", fp)
    print("False Negative : ", fn)


    


def execute(path):
    # Read the content of the input file
    with open(path, 'r') as file:
        file_content = file.read()

    # Create a JSON content with the code
    json_content = {
        "project": "",
        "commit_id": "",
        "target": -1,
        "func": file_content,
        "idx": "-1"
    }
    
    # Write JSON content to a test file
    with open("./Files/test.jsonl", 'w') as json_file:
        json.dump(json_content, json_file)

    # commands = []
    
    # Generate commands for running models
    for i in range(5):
        command = f'python run.py --output_dir="./Models/model{i}" --train_data_file="./Models/train.jsonl" --model_type=roberta --tokenizer_name=microsoft/codebert-base --model_name_or_path=microsoft/codebert-base --do_eval --do_test --eval_data_file="./Files/valid.jsonl" --test_data_file="./Files/test.jsonl" --epoch 1 --block_size 400 --train_batch_size 1 --eval_batch_size 1 --learning_rate 2e-5 --max_grad_norm 1.0 --evaluate_during_training --seed 123456 > train.log 2>&1'
        subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Command '{i}' has completed.")

    # Collect predictions
    predict = [-1] * 5
    for i in range(5):
        with open(f"./Models/model{i}/predictions.txt", 'r') as p:
            a = p.readline()
            predict[i] = int(a[-2])

    # Print predictions
    for k in range(5):
        print(f"Model {k} Output : {predict[k]} - {'Not Vulnerable' if predict[k] == 0 else 'Vulnerable'}")

    # Calculate the final decision based on voting
    final_decision = 0 if predict.count(0) >= 3 else 1
    with open('./output.txt', 'w') as file:
        file.write(f'{final_decision}\n')
    print(f"Based on Ensemble learning: '{final_decision}' wins")
    print(f"Code is {'Vulnerable' if final_decision == 1 else 'Not Vulnerable'}")

if __name__ == "__main__":
    key = 2
    if key == 1:
        multiple()
    else:
        # 

        # Parsing command-line arguments
        parser = argparse.ArgumentParser(description='Compile a C++ code file')
        parser.add_argument('-code', dest='cpp_file', help='Specify the C++ code file to compile')
        args = parser.parse_args()

        programfile = args.cpp_file

        if programfile and (programfile.endswith('.c') or programfile.endswith('.cpp')):
            if os.path.exists(programfile):
                execute(programfile)
            else:
                print("File doesn't exist at the location")
        else:
            print("Input C/C++ file for code vulnerability")
