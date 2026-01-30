import ast
import sys
import subprocess

def process_case_batch(case_pair, input_list):
    if len(case_pair) != len(input_list):
        raise ValueError("inconsistent case_pair and batch_size input, length should be the same")
    sorted_batch = [sorted(bs, reverse=True) for bs in input_list]
    combined = list(zip(case_pair, sorted_batch))
    combined.sort(key=lambda x: sum(x[0]), reverse=True)
    sorted_case_pair = [pair for pair, _ in combined]
    sorted_input_list = [bs for _, bs in combined]
    return sorted_case_pair, sorted_input_list


def parse_lst_args(input_lst):

    try:
        input_lst = int(input_lst)
        return [input_lst]
    except ValueError:
        pass
    try:
        input_list = [int(bs) for bs in input_lst.split(',')]
        input_lst = input_list
        return input_lst
    except ValueError:
        pass

    try:
        input_lst = ast.literal_eval(input_lst)
        if isinstance(input_lst, list):
            if not input_lst:
                raise ValueError("Input is empty")
            else:
                return input_lst
        raise ValueError("Wrong input_lst format")
    except (ValueError, SyntaxError) as e:
        raise ValueError("Wrong input_lst format") from e


def exec_command(modified_config):
    command = ["ais_bench", modified_config, "--mode", "perf", "--debug"]

    try:
        print(f"Running command: {' '.join(command)}")
        
        # 将 stdout 和 stderr 直接指向当前的 sys.stdout/stderr
        # 这样子进程会直接打印到终端，完全保留原始格式、颜色和顺序
        subprocess.run(
            command,
            check=True,  # 替代手动检查 returncode 并抛出异常
            text=True
        )
        
    except subprocess.CalledProcessError as e:
        print(f"\nCommand failed with code {e.returncode}", file=sys.stderr)
    except Exception as e:
        print(f"\nUnexpected error: {e}", file=sys.stderr)


