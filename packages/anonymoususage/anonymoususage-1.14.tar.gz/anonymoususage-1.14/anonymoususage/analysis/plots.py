__author__ = 'calvin'

import logging
import itertools
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import DateFormatter
from collections import Iterable, Counter
from anonymoususage.tools import *


__all__ = ['plot_total_statistics', 'plot_state', 'plot_timer', 'plot_statistic']


def _get_figure(n_items, **subplot_kwargs):
    figure, plots = plt.subplots(nrows=n_items, ncols=1, **subplot_kwargs)
    if n_items == 1:
        return figure, plots
    else:
        plots = plots.flatten()
        return figure, plots[:n_items]


def plot_total_statistics(dbconn, table_names):
    """
    Plot the cumulative statistics for table names in a bar plot.
    :param dbconn: database connection
    :param table_names: list of table names to plot
    """
    fig, plot = _get_figure(1)
    stat_count = {t: 0 for t in table_names}
    uuids = get_uuid_list(dbconn)
    for table in stat_count.iterkeys():
        for uuid in uuids:
            last_row = get_last_row(dbconn, table, uuid=uuid)
            if last_row:
                count = last_row[0]['Count']
                stat_count[table] += count

    table_names, table_values = zip(*stat_count.items())
    ind = np.arange(len(table_names))
    colors = [c for c in itertools.islice(plot._get_lines.color_cycle, 0, len(table_names))]
    plot.bar(ind, table_values, color=colors)
    # add some text for labels, title and axes ticks
    plot.set_ylabel('Count')
    plot.set_title('Statistic Totals')
    plot.set_xticks(ind+0.35)
    plot.set_xticklabels(table_names)
    plt.show()


def plot_state(dbconn, table_names):
    """
    Plot the distribution of users for a State.
    :param dbconn: database connection
    :param table_names: list of State table names to plot
    """
    fig, plots = _get_figure(len(table_names), sharey=True)
    if isinstance(plots, Iterable):
        plots = plots.flatten()
    else:
        plots = [plots]
    uuids = get_uuid_list(dbconn)
    for ii, table in enumerate(table_names):
        counter = Counter()
        options = set()
        for uuid in uuids:
            last_row = get_last_row(dbconn, table, uuid=uuid)
            if last_row:
                state = last_row[0]['State']
                options.add(state)
                counter[state] += 1
        plot = plots[ii]
        ind = np.arange(len(options))
        values = [counter[k] for k in options]
        colors = [c for c in itertools.islice(plot._get_lines.color_cycle, 0, len(options))]
        plot.bar(ind, values, color=colors)
        plot.set_ylabel('Count')
        plot.set_title('%s' % table)
        plot.set_xticks(ind+0.35)
        plot.set_xticklabels(list(options))
    plt.show()


def plot_timer(dbconn, table_names, show_average=True, time_units='minutes'):
    """
    Plot the total and average times of Timers.
    :param dbconn: database connection
    :param show_average: Show the average times on a secondary y-axis (boolean).
    :param table_names: list of Timer table names to plot
    """
    fig, plot = _get_figure(1, sharey=True)
    uuids = get_uuid_list(dbconn)

    average_time_s = Counter()
    total_time_s = Counter()
    if time_units == 'minutes':
        c = 60.
    elif time_units == 'hours':
        c = 3600.
    elif time_units == 'days':
        c = 86400.
    elif time_units == 'months':
        c = 2.62974e6
    for ii, table in enumerate(table_names):
        for uuid in uuids:
            last_row = get_last_row(dbconn, table, uuid=uuid)
            n_rows = get_number_of_rows(dbconn, table, uuid=uuid)
            if last_row:
                count = last_row[0]['Count']
                total_time_s[table] += count / c
                average_time_s[table] += count / n_rows / c

    average_times = [average_time_s[k] for k in table_names]
    total_times = [total_time_s[k] for k in table_names]
    ind = np.arange(len(table_names))
    w = 0.2
    plot.bar(ind, total_times, color='b', width=w, align='center', label='Total Time')
    plot.set_ylabel('Total Time (%s)' % time_units)
    plot.set_xticks(ind+w if show_average else ind)
    plot.set_xticklabels(table_names)
    if show_average:
        # Secondary axis
        ax2 = plot.twinx()
        ax2.bar(ind+w, average_times, color='r', width=w, align='center', label='Average Time')
        ax2.set_ylabel('Average Time (%s)' % time_units)

        handles, labels = plot.get_legend_handles_labels()
        handles2, labels2 = ax2.get_legend_handles_labels()

        plt.legend(handles + handles2, labels + labels2,  loc='upper center', labelspacing=1., ncol=2)

    plt.show()


def plot_statistic(dbconn, table_names, uuid=None, date_limits=(None, None), datefmt=None):
    """
    Plot statistics as a function of time for table names in a line plot.
    :param dbconn: database connection
    :param table_names: list of table names to plot
    :param uuid: UUID to plot, if None all UUIDs will be plotted
    :param data_limits: tuple of (min_datetime, max_datetime) to be used for x axis range
    :param datefmt: string formatter for the date axis

    """
    fig, plots = _get_figure(len(table_names), sharex=True)
    if isinstance(plots, Iterable):
        plots = plots.flatten()
    else:
        plots = [plots]
    plots = list(plots)
    plotted_tables = set()
    handles = []
    uuids = get_uuid_list(dbconn) if uuid is None else [uuid]
    colors = [c for c in itertools.islice(plots[0]._get_lines.color_cycle, 0, len(uuids))]

    for ii, table_name in enumerate(table_names):
        for jj, uuid in enumerate(uuids):
            data = get_datetime_sorted_rows(dbconn, table_name, uuid=uuid, column='Count')
            if len(data) > 1:
                plot = plots[ii]
                plot.set_title(table_name)
                times, counts = zip(*data)
                plot.plot_date(times, counts, '-o%s'% colors[jj], label=table_name)
                plotted_tables.add(table_name)
                if datefmt:
                    plot.xaxis.set_major_formatter(DateFormatter(datefmt))
                plot.set_xlabel('Date')
                plot.set_ylabel('Count')
                _handles = plot.get_legend_handles_labels()[0]
                if len(_handles) > len(handles):
                    handles = _handles
            else:
                logging.warning('No data for %s. Omitting from plot.' % table_name)

        if len(plotted_tables) == 0:
            logging.warning('No data for found. Failed to create plot.')
            return

    # plt.figlegend(handles, plotted_tables, loc='upper left', ncol=max(1, 3 * (len(plotted_tables) / 3)), labelspacing=0.)
    plt.figlegend(handles, uuids, loc='lower left', labelspacing=0.)

    if date_limits[0] and date_limits[1]:
        plots.set_xlim(*date_limits)
    else:
        fig.autofmt_xdate()
    fig.set_size_inches(12, 8, forward=True)
    plt.show()

