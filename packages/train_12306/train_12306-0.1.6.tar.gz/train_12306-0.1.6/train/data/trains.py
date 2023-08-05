"""
fetch train tickets and print them
"""
import json
import webbrowser
from colorama import Fore
from ..spider import fetch_trains
from prettytable import PrettyTable
from ..utils import tickets_util, common_util

URL = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.' \
      'train_date={date}&leftTicketDTO.' \
      'from_station={from_station_key}&leftTicketDTO.to_station={to_station_key}&purpose_codes=ADULT'

TICKETS_TABLE_HEADER = ["车次", "站点", "起止时间", "历时", "商务座", "特等座",
                        "一等座", "二等座", "软卧", "硬卧", "软座", "硬座", "无座"]

OFFICIAL_WEB = 'https://kyfw.12306.cn/otn/leftTicket/init'


def fetch_train_tickets(from_station, to_station, date=None, train_type=None):
    """get input data and print final result

    :param train_type
    :param from_station
    :param to_station
    :param date
    :return: if data is invalidate then return False
    """
    date = tickets_util.validate_raw_date(date)

    if not isinstance(date, str):
        print(common_util.make_colorful_font(date['message'], Fore.RED))
        return date['result']

    from_station_key = tickets_util.get_station_key(from_station)
    to_station_key = tickets_util.get_station_key(to_station)

    fetch_url = URL.format(date=date, from_station_key=from_station_key, to_station_key=to_station_key)
    train_tickets = fetch_trains.TrainTickets(fetch_url)
    tickets_result = train_tickets.fetch_tickets()

    # with open('./data/tickets_data.json', encoding="utf-8") as f:
    #     tickets_result = json.loads(f.read())

    if tickets_result['result']:
        print_train_tickets(tickets_result['data'], train_type)
    else:
        print(common_util.make_colorful_font(tickets_result['message'], Fore.RED))
        return False
    determine_input = input('到官网购票? y/n ')
    if determine_input == 'y':
        webbrowser.open_new(OFFICIAL_WEB)


def print_train_tickets(tickets_result_data, train_type):
    """make and print a table

    :param train_type
    :param tickets_result_data: fetched result
    :return: None
    """

    if train_type is not None:
        target_train = tickets_util.filter_target_train(train_type.upper())
        tickets_result_data = filter(target_train, tickets_result_data)

    tickets_table = PrettyTable(TICKETS_TABLE_HEADER)
    for ticket_dict in tickets_result_data:
        ticket_data = ticket_dict["queryLeftNewDTO"]
        tickets_table_row = [
            ticket_data["station_train_code"],
            '{}\n{}'.format(common_util.make_colorful_font(ticket_data["from_station_name"]),
                            common_util.make_colorful_font(ticket_data["end_station_name"])),
            '{}\n{}'.format(ticket_data["start_time"], ticket_data["arrive_time"]),
            ticket_data["lishi"],
            tickets_util.handle_font_color(ticket_data["swz_num"]),
            tickets_util.handle_font_color(ticket_data["tz_num"]),
            tickets_util.handle_font_color(ticket_data["zy_num"]),
            tickets_util.handle_font_color(ticket_data["ze_num"]),
            tickets_util.handle_font_color(ticket_data["rw_num"]),
            tickets_util.handle_font_color(ticket_data["yw_num"]),
            tickets_util.handle_font_color(ticket_data["rz_num"]),
            tickets_util.handle_font_color(ticket_data["yz_num"]),
            tickets_util.handle_font_color(ticket_data["wz_num"])
        ]
        tickets_table.add_row(tickets_table_row)
        del tickets_table_row
    print(tickets_table)
