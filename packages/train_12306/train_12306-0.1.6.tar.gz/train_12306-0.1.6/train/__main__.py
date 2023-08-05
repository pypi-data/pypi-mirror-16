#!usr/bin/env python
import click
from datetime import date
from .data import trains


def get_today_date():
    return ''.join(str(date.today()).split('-')[1:3])


@click.command()
@click.option('--start', prompt='起始站', help='输入出发的站点')
@click.option('--end', prompt='目的地', help='输入到达的站点')
@click.option('--train-date', prompt='出发时间', help='输入想要上车的日期', default=get_today_date())
@click.option('--train-type', type=click.Choice(['g', 'd', 't', 'k', 'z', None]), default=None)
def main(start, end, train_date, train_type):
    """

    :param start: 起始站
    :param end: 目的站
    :param train_date: 出发日期
    :param train_type: 车型
    :return: None
    """
    trains.fetch_train_tickets(start, end, date=str(train_date), train_type=train_type)
    exit(0)


if __name__ == '__main__':
    main()
