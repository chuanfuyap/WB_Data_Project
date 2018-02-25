from bokeh.embed import components
from bokeh.io import show, output_file,push_notebook, output_notebook
from bokeh.plotting import figure, ColumnDataSource
from bokeh.palettes import Category20, Category10
from bokeh.transform import factor_cmap
from bokeh.layouts import column
from bokeh.models import FactorRange

import pandas as pd
import numpy as np

from content_management import country_region_dict

country_to_region, region_dict = country_region_dict()

def unwrap(indicator_name, compiled_df):
    df_index = compiled_df.at['Coverage_Range', indicator_name]
    df_index = string_to_list(df_index)
    df_index = [ind for ind in df_index if len(ind)==4]
    df_index = pd.to_datetime(df_index)
    countries = compiled_df.index
    countries = countries.drop('Coverage_Range')
    data = {}
    for country in countries:
        annual_data = compiled_df.at[country,indicator_name]
        
        if not pd.isnull(annual_data):
            time_series = string_to_list(annual_data)
            if len(time_series)==len(df_index):
                #print country
                data[country]=time_series
        #print len(time_series), country, len(df_index)
        else:
            data[country]=np.nan

    unwrapping = pd.DataFrame(index=df_index, data=data, dtype=np.dtype(float) )
    return unwrapping
def string_to_list(string):
    list_ = string[1:-1]
    list_ = list_.split(',')
    list_ = [t.replace("'", '').strip() for t in list_]
    return list_
def data_to_list(string):
    list_ = string[1:-1]
    list_ = list_.split(',')
    list_ = [t.replace("'", '').strip() for t in list_]
    list_ = [float(t) for t in list_ if t != 'nan']
    list_ = [np.nan for t in list_ if t == 'nan']
    
    return list_


def plot_BAR_indicator_COUNTRY(indicator, topic, country):
    df = pd.read_csv('data/{}_cleaned.csv'.format(topic), index_col=0)
    indicator_toplot = unwrap(indicator, df)
    indicator_toplot.dropna(axis=0, inplace=True, how='all')
    
    ##world average
    indicator_toplot['World Avg.'] = indicator_toplot.mean(axis=1)
    
    ##region average
    region = country_to_region[country]
    region_countries = region_dict[region]
    region_df = indicator_toplot[region_countries]
    col_name = region+' Avg.'
    indicator_toplot[col_name]=region_df.mean(axis=1)
    
    ##process data to plot
    plot_sample = [country, col_name,'World Avg.']
    country_region_world = indicator_toplot[plot_sample]
    latest_index = indicator_toplot[country].dropna().index[-1]
    barplot = country_region_world.loc[latest_index] ## picking latest
    latest_year = latest_index.year
    ##plot
    bar_x, bar_counts = process_for_country(plot_sample, barplot, country_region_world)
    bar_graph = plot_country_barGraph(bar_x, bar_counts, indicator, latest_year, country)
    return bar_graph

def process_for_country(samples, series, df):
    df = df[df > 0]
    highest = []
    current = series
    lowest = []
    for country in samples:
        series = df[country]
        series = series[series > 0]
        highest.append(series.dropna().max())
        lowest.append(series.dropna().min())
    
    labels = ['Highest', 'Current', 'Lowest']

    x = [ (country, label) for country in samples for label in labels ]
    counts = sum(zip(highest, current, lowest), ()) # like an hstack
    
    return x, counts

def plot_country_barGraph(x, counts, indicator, year, country):
    labels = ['Highest', 'Current', 'Lowest']
    data_source = ColumnDataSource(data=dict(x=x, counts=counts))
    p = figure(x_range=FactorRange(*x), plot_width=900, plot_height=350, title="{} numbers for {} compared to World and Region Avg. in {}".format(indicator, country, year),
               toolbar_location=None, tools="")
        
    p.vbar(x='x', top='counts', width=0.9, source=data_source,
                      fill_color=factor_cmap('x', palette=Category20[3], factors=labels, start=1, end=2))
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    return p


def plot_LINE_indicator_COUNTRY(indicator, topic, country):
    df = pd.read_csv('data/{}_cleaned.csv'.format(topic), index_col=0)
    indicator_toplot = unwrap(indicator, df)
    indicator_toplot.dropna(axis=0, inplace=True, how='all')
    
    ##world average
    indicator_toplot['World Avg.'] = indicator_toplot.mean(axis=1)
    
    ##region average
    region = country_to_region[country]
    region_countries = region_dict[region]
    region_df = indicator_toplot[region_countries]
    col_name = region+' Avg.'
    indicator_toplot[col_name]=region_df.mean(axis=1)
    
    ##process data to plot
    plot_sample = [country, col_name,'World Avg.']
    country_region_world = indicator_toplot[plot_sample]
    
    line_graph = plot_lineGraph_country(country_region_world, indicator, country)
    return line_graph

def plot_lineGraph_country(dataframe, indicator, country):
    dataframe = dataframe[dataframe > 0]
    dataframe = dataframe.interpolate(method='time')
    p = figure(x_axis_type="datetime", plot_width=900, plot_height=350,
               toolbar_location=None, tools="", title='{} change over time for {} compared to World and Region Avg.'.format(indicator, country))
    dataframe.index.name = 'Date'
    colors = Category10[3]
    names = list(dataframe.columns)
    for col, name, color in zip(dataframe.columns, names,colors):
        p.line(dataframe.index, dataframe[col], line_width=5, legend=col,color=color,alpha=0.8
                          ,muted_color=color, muted_alpha=0.1,)

    p.legend.location = "top_left"
    p.legend.click_policy="hide"
    
    return p

def plot_BAR_indicator_top5(indicator, topic):
    df = pd.read_csv('data/{}_cleaned.csv'.format(topic), index_col=0)
    indicator_toplot = unwrap(indicator, df)
    indicator_toplot.dropna(axis=0, inplace=True, how='all')
    ##locating top5
    barplot = indicator_toplot.iloc[-1].dropna()
    barplot.sort_values(inplace=True, ascending=False)
    ##plot
    countries = list(barplot[:5].index)
    latest_year = indicator_toplot.index[-1].year
    bar_x, bar_counts = process_top5(countries, barplot, indicator_toplot)
    bar_graph = plot_barGraph(bar_x, bar_counts, indicator, latest_year)
    
    return bar_graph

def plot_barGraph(x, counts, indicator, year):
    labels = ['Highest', 'Current', 'Lowest']
    data_source = ColumnDataSource(data=dict(x=x, counts=counts))
    p = figure(x_range=FactorRange(*x), plot_width=900, plot_height=350, title="Top 5 Countries for {} in {}".format(indicator, year),
               toolbar_location=None, tools="")
        
    p.vbar(x='x', top='counts', width=0.9, source=data_source,
                      fill_color=factor_cmap('x', palette=Category20[3], factors=labels, start=1, end=2))
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    return p

def process_top5(countries, series, df):
    df = df[df > 0]
    highest = []
    current = list(series[:5])
    lowest = []
    for country in countries:
        series = df[country]
        series = series[series > 0]
        highest.append(series.dropna().max())
        lowest.append(series.dropna().min())
    
    labels = ['Highest', 'Current', 'Lowest']

    x = [ (country, label) for country in countries for label in labels ]
    counts = sum(zip(highest, current, lowest), ()) # like an hstack
    
    return x, counts


def plot_LINE_indicator_top5(indicator, topic):
    df = pd.read_csv('data/{}_cleaned.csv'.format(topic), index_col=0)
    indicator_toplot = unwrap(indicator, df)
    indicator_toplot.dropna(axis=0, inplace=True, how='all')
    ##locating top5
    top5 = indicator_toplot.iloc[-1].dropna()
    top5.sort_values(inplace=True, ascending=False)
    top5 = list(top5[:5].index)
    ##plot
    line_plot = indicator_toplot[top5]
    line_graph = plot_lineGraph(line_plot, indicator)
    return line_graph

def plot_lineGraph(dataframe, indicator):
    dataframe = dataframe[dataframe > 0]
    dataframe = dataframe.interpolate(method='time')
    p = figure(x_axis_type="datetime", plot_width=900, plot_height=350,
               toolbar_location=None, tools="", title='{} change over time for Top 5 Countries'.format(indicator))
    dataframe.index.name = 'Date'
    colors = Category10[5]
    names = list(dataframe.columns)
    for col, name, color in zip(dataframe.columns, names,colors):
        p.line(dataframe.index, dataframe[col], line_width=5, legend=col,color=color,alpha=0.8
                          ,muted_color=color, muted_alpha=0.1,)

    p.legend.location = "top_left"
    p.legend.click_policy="hide"
    
    return p

def plot_BAR_indicator_REGION(indicator, topic, region):
    df = pd.read_csv('data/{}_cleaned.csv'.format(topic), index_col=0)
    indicator_toplot = unwrap(indicator, df)
    indicator_toplot.dropna(axis=0, inplace=True, how='all')
    
    ##region average
    region_countries = region_dict[region]
    region_df = indicator_toplot[region_countries]
    if len(region_df.columns)>10:
        find_top10 = region_df.iloc[-1].dropna()
        find_top10.sort_values(inplace=True, ascending=False)
        region_df = region_df[find_top10.index[:10]]
        region_countries=find_top10.index[:10]
    
    ##process data to plot
    latest_index = region_df.index[-1]
    barplot = region_df.loc[latest_index] ## picking latest
    latest_year = latest_index.year
    ##plot
    bar_x, bar_counts = process_for_region(region_countries, barplot, region_df)
    bar_graph = plot_barGraph_region(bar_x, bar_counts, indicator, latest_year, region)
    return bar_graph

def process_for_region(samples, series, df):
    df = df[df > 0]
    highest = []
    current = series
    lowest = []
    for country in samples:
        series = df[country]
        series = series[series > 0]
        highest.append(series.dropna().max())
        lowest.append(series.dropna().min())
    
    labels = ['Highest', 'Current', 'Lowest']

    x = [ (country, label) for country in samples for label in labels ]
    counts = sum(zip(highest, current, lowest), ()) # like an hstack
    
    return x, counts

def plot_barGraph_region(x, counts, indicator, year, region):
    labels = ['Highest', 'Current', 'Lowest']
    data_source = ColumnDataSource(data=dict(x=x, counts=counts))
    p = figure(x_range=FactorRange(*x), plot_width=1000, plot_height=350, title="{} numbers for {} in {}".format(indicator, region, year),
               toolbar_location=None, tools="")
        
    p.vbar(x='x', top='counts', width=0.9, source=data_source,
                      fill_color=factor_cmap('x', palette=Category20[3], factors=labels, start=1, end=2))
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    return p

def plot_LINE_indicator_REGION(indicator, topic, region):
    df = pd.read_csv('data/{}_cleaned.csv'.format(topic), index_col=0)
    indicator_toplot = unwrap(indicator, df)
    indicator_toplot.dropna(axis=0, inplace=True, how='all')
    
    ##region
    region_countries = region_dict[region]
    region_df = indicator_toplot[region_countries]
    if len(region_df.columns)>10:
        find_top10 = region_df.iloc[-1].dropna()
        find_top10.sort_values(inplace=True, ascending=False)
        region_df = region_df[find_top10.index[:10]]
        region_countries=find_top10.index[:10]
    
    ##process data to plot
    
    line_graph = plot_lineGraph_region(region_df, indicator, region)
    return line_graph

def plot_lineGraph_region(dataframe, indicator, region):
    dataframe = dataframe[dataframe > 0]
    dataframe = dataframe.interpolate(method='time')
    p = figure(x_axis_type="datetime", plot_width=1000, plot_height=350,
               toolbar_location=None, tools="", title='{} change over time for {}'.format(indicator, region))
    dataframe.index.name = 'Date'
    colors = Category10[10]
    names = list(dataframe.columns)
    for col, name, color in zip(dataframe.columns, names,colors):
        p.line(dataframe.index, dataframe[col], line_width=5, legend=col,color=color,alpha=0.8
                          ,muted_color=color, muted_alpha=0.1,)

    p.legend.location = "top_left"
    p.legend.click_policy="hide"
    
    return p

def plot_line():
    p = figure(plot_width=200, plot_height=200,toolbar_location=None, tools="")
    
    # add a line renderer
    p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)
    script, div = components(p)
    return script, div

def plot_bar():
    fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
    
    p = figure(x_range=fruits, plot_height=250, title="Fruit Counts",
               toolbar_location=None, tools="")
        
    p.vbar(x=fruits, top=[5, 3, 4, 2, 4, 6], width=0.9)
               
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
               
    script, div = components(p)
    return script, div
