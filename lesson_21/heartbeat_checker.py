import logging
from datetime import datetime

def analyze_heartbeat_log(input_file, output_file='hb_test.log', key='Key TSTFEED0300|7E3E|0400'):
    logging.basicConfig(
        filename=output_file,
        filemode='w',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    filtered_lines = []
    with open(input_file, 'r') as file:
        for line in file:
            if key in line:
                filtered_lines.append(line.strip())

    timestamps = []
    for line in filtered_lines:
        ts_index = line.find('Timestamp ')
        if ts_index != -1:
            ts_str = line[ts_index + 10:ts_index + 18]
            try:
                timestamp = datetime.strptime(ts_str, "%H:%M:%S")
                timestamps.append((timestamp, line))
            except ValueError:
                continue

    for i in range(len(timestamps) - 1):
        current_time, current_line = timestamps[i]
        next_time, next_line = timestamps[i + 1]

        diff = (current_time - next_time).total_seconds()
        diff = abs(diff)

        if 31 < diff < 33:
            logging.warning(f"Heartbeat delay {diff} sec. Line: {next_line}")
        elif diff >= 33:
            logging.error(f"Heartbeat delay {diff} sec. Line: {next_line}")


if __name__ == "__main__":
    analyze_heartbeat_log('hblog.txt', 'hb_test.log')
    print("Аналіз завершено. Перевірте файл hb_test.log.")
