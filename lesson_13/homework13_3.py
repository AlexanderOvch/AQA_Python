import xml.etree.ElementTree as ET
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    )
logger = logging.getLogger('__name__')


def find_timing_exbytes_incoming(xml_file, group_number):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        group = root.find(f".//group[number='{group_number}']")

        if group is not None:
            incoming = group.find(".//timingExbytes/incoming")
            if incoming is not None:
                logger.info(f"Для групи з номером {group_number}, значення timingExbytes/incoming: {incoming.text}")
            else:
                logger.warning(f"Не знайдено елемента 'incoming' для групи з номером {group_number}.")
        else:
            logger.warning(f"Не знайдено групи з номером {group_number}.")

    except Exception as e:
        logger.error(f"Сталася помилка при обробці XML файлу: {e}")


find_timing_exbytes_incoming('work_with_xml/groups.xml', '5')
