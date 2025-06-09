from datetime import datetime
import logging


def read_filtered_lines(input_file, key):
    filtered = []
    with open(input_file, 'r') as file:
        for line in file:
            if key in line:
                filtered.append(line.strip())
    return filtered

def extract_timestamps_from_lines(lines):
    timestamps = []
    for line in lines:
        ts_index = line.find('Timestamp ')
        if ts_index != -1:
            ts_str = line[ts_index + 10:ts_index + 18]
            try:
                timestamp = datetime.strptime(ts_str, "%H:%M:%S")
                timestamps.append((timestamp, line))
            except ValueError:
                continue
    return timestamps

def log_heartbeat_issues(timestamps, output_file):
    logging.basicConfig(
        filename=output_file,
        filemode='w',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s')

    for i in range(len(timestamps) - 1):
        current_time, _ = timestamps[i]
        next_time, next_line = timestamps[i + 1]
        diff = (current_time - next_time).total_seconds()

        if 31 < diff < 33:
            logging.warning(f"Heartbeat delay {diff} sec. Line: {next_line}")
        elif diff >= 33:
            logging.error(f"Heartbeat delay {diff} sec. Line: {next_line}")

def analyze_heartbeat_log(input_file, output_file, key='Key TSTFEED0300|7E3E|0400'):
    lines = read_filtered_lines(input_file, key)
    timestamps = extract_timestamps_from_lines(lines)
    log_heartbeat_issues(timestamps, output_file)



if __name__ == '__main__':
    analyze_heartbeat_log('hblog.txt', 'hb_test.log')
