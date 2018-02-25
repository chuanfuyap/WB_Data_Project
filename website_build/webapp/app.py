from flask import Flask, render_template, request, url_for, redirect, jsonify
from content_management import Indicator, country_and_region, model_features
from graph_content import plot_BAR_indicator_top5, plot_LINE_indicator_top5, plot_BAR_indicator_COUNTRY,plot_LINE_indicator_COUNTRY,plot_BAR_indicator_REGION,plot_LINE_indicator_REGION
from bokeh.layouts import column
from bokeh.embed import components
import dill
import pickle

economy_model = dill.load(open('data/econ2.dill', 'r'))
poverty_model = dill.load(open('data/pov2.dill', 'r'))
dev_model = dill.load(open('data/dev2.dill', 'r'))
finance_model = dill.load(open('data/fin2.dill', 'r'))
                          
indicator_dict = Indicator()
country_names, region_names = country_and_region()
model_feat =model_features()

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/about/')
def about_page():
    return render_template("about.html")

@app.route('/map/')
def map_page():
    try:
        return render_template("map.html")
    except Exception as e:
        return render_template("500.html", error=e)
@app.route('/model/')
def model_page():
    try:
        return render_template("model.html",
                               econ_feat = model_feat['Economy'],
                               dev_feat = model_feat['Development'],
                               fin_feat = model_feat['Finance'],
                               pov_feat = model_feat['Poverty'])
    except Exception as e:
        return render_template("500.html", error=e)

@app.route('/graph/')
def dashboard():
    try:
        
        graph_data = []
        for key in indicator_dict.keys():
            barplot = plot_BAR_indicator_top5(indicator_dict[key][0], key)
            lineplot = plot_LINE_indicator_top5(indicator_dict[key][0],key)
            graphs = column(barplot, lineplot)
            script, div =components(graphs)
            graph_data.append((script, div))
        
        
        return render_template("graph.html", indicator_dict = indicator_dict,
                               country_list = country_names,
                               region_list = region_names,
                               econ_script=graph_data[1][0], econ_graph=graph_data[1][1],
                               health_script=graph_data[5][0], health_graph=graph_data[5][1],
                               edu_script=graph_data[2][0], edu_graph=graph_data[2][1],
                               fin_script=graph_data[4][0], fin_graph=graph_data[4][1],
                               dev_script=graph_data[0][0], dev_graph=graph_data[0][1],
                               pov_script=graph_data[6][0], pov_graph=graph_data[6][1],
                               env_script=graph_data[3][0], env_graph=graph_data[3][1])
    except Exception as e:
        return render_template("500.html", error=e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/_plot_economy')
def econ_data():
    indicator = request.args.get('econ_indicator', 'potato', type=str)
    print (indicator)
    
    barplot = plot_BAR_indicator_top5(indicator, 'Economy')
    lineplot = plot_LINE_indicator_top5(indicator, 'Economy')
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)
@app.route('/_plot_economyregion')
def econ_region():
    indicator = request.args.get('econ_indicator', 'potato', type=str)
    region = request.args.get('region', 'potato', type=str)
    print (indicator)
    print (region)
    
    barplot = plot_BAR_indicator_REGION(indicator, 'Economy', region)
    lineplot = plot_LINE_indicator_REGION(indicator, 'Economy', region)
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)
@app.route('/_plot_economycountry')
def econ_country():
    indicator = request.args.get('econ_indicator', 'potato', type=str)
    country = request.args.get('country', 'potato', type=str)
    print (indicator)
    print(country)
    
    barplot = plot_BAR_indicator_COUNTRY(indicator, 'Economy', country)
    lineplot = plot_LINE_indicator_COUNTRY(indicator, 'Economy', country)
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)




@app.route('/_plot_health')
def health_data():
    indicator = request.args.get('health_indicator', 'potato', type=str)
    print (indicator)
    
    barplot = plot_BAR_indicator_top5(indicator, 'Health')
    lineplot = plot_LINE_indicator_top5(indicator, 'Health')
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    
    return jsonify(script = script, graph= div)
@app.route('/_plot_healthregion')
def health_region():
    indicator = request.args.get('indicator', 'potato', type=str)
    region = request.args.get('region', 'potato', type=str)
    print (indicator)
    print (region)
    
    barplot = plot_BAR_indicator_REGION(indicator, 'Health', region)
    lineplot = plot_LINE_indicator_REGION(indicator, 'Health', region)
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)
@app.route('/_plot_healthcountry')
def health_country():
    indicator = request.args.get('indicator', 'potato', type=str)
    country = request.args.get('country', 'potato', type=str)
    print (indicator)
    print(country)
    
    barplot = plot_BAR_indicator_COUNTRY(indicator, 'Health', country)
    lineplot = plot_LINE_indicator_COUNTRY(indicator, 'Health', country)
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)




@app.route('/_plot_edu')
def education_data():
    indicator = request.args.get('edu_indicator', 'potato', type=str)
    print (indicator)
    
    barplot = plot_BAR_indicator_top5(indicator, 'Education')
    lineplot = plot_LINE_indicator_top5(indicator, 'Education')
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)
@app.route('/_plot_eduregion')
def edu_region():
    indicator = request.args.get('indicator', 'potato', type=str)
    region = request.args.get('region', 'potato', type=str)
    print (indicator)
    print (region)
    
    barplot = plot_BAR_indicator_REGION(indicator, 'Education', region)
    lineplot = plot_LINE_indicator_REGION(indicator, 'Education', region)
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)
@app.route('/_plot_educountry')
def edu_country():
    indicator = request.args.get('indicator', 'potato', type=str)
    country = request.args.get('country', 'potato', type=str)
    print (indicator)
    print(country)
    
    barplot = plot_BAR_indicator_COUNTRY(indicator, 'Education', country)
    lineplot = plot_LINE_indicator_COUNTRY(indicator, 'Education', country)
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)




@app.route('/_plot_env')
def env_data():
    indicator = request.args.get('indicator', 'potato', type=str)
    print (indicator)
    
    barplot = plot_BAR_indicator_top5(indicator, 'Environment')
    lineplot = plot_LINE_indicator_top5(indicator, 'Environment')
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)
@app.route('/_plot_envregion')
def env_region():
    indicator = request.args.get('indicator', 'potato', type=str)
    region = request.args.get('region', 'potato', type=str)
    print (indicator)
    print (region)
    
    barplot = plot_BAR_indicator_REGION(indicator, 'Environment', region)
    lineplot = plot_LINE_indicator_REGION(indicator, 'Environment', region)
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)
@app.route('/_plot_envcountry')
def env_country():
    indicator = request.args.get('indicator', 'potato', type=str)
    country = request.args.get('country', 'potato', type=str)
    print (indicator)
    print(country)
    
    barplot = plot_BAR_indicator_COUNTRY(indicator, 'Environment', country)
    lineplot = plot_LINE_indicator_COUNTRY(indicator, 'Environment', country)
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)



@app.route('/_plot_fin')
def fin_data():
    indicator = request.args.get('indicator', 'potato', type=str)
    print (indicator)
    
    barplot = plot_BAR_indicator_top5(indicator, 'Finance')
    lineplot = plot_LINE_indicator_top5(indicator, 'Finance')
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)
@app.route('/_plot_finregion')
def fin_region():
    indicator = request.args.get('indicator', 'potato', type=str)
    region = request.args.get('region', 'potato', type=str)
    print (indicator)
    print (region)
    
    barplot = plot_BAR_indicator_REGION(indicator, 'Finance', region)
    lineplot = plot_LINE_indicator_REGION(indicator, 'Finance', region)
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)
@app.route('/_plot_fincountry')
def fin_country():
    indicator = request.args.get('indicator', 'potato', type=str)
    country = request.args.get('country', 'potato', type=str)
    print (indicator)
    print(country)
    
    barplot = plot_BAR_indicator_COUNTRY(indicator, 'Finance', country)
    lineplot = plot_LINE_indicator_COUNTRY(indicator, 'Finance', country)
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)



@app.route('/_plot_dev')
def dev_data():
    indicator = request.args.get('indicator', 'potato', type=str)
    print (indicator)
    
    barplot = plot_BAR_indicator_top5(indicator, 'Development')
    lineplot = plot_LINE_indicator_top5(indicator, 'Development')
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)
@app.route('/_plot_devregion')
def dev_region():
    indicator = request.args.get('indicator', 'potato', type=str)
    region = request.args.get('region', 'potato', type=str)
    print (indicator)
    print (region)
    
    barplot = plot_BAR_indicator_REGION(indicator, 'Development', region)
    lineplot = plot_LINE_indicator_REGION(indicator, 'Development', region)
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)
@app.route('/_plot_devcountry')
def dev_country():
    indicator = request.args.get('indicator', 'potato', type=str)
    country = request.args.get('country', 'potato', type=str)
    print (indicator)
    print(country)
    
    barplot = plot_BAR_indicator_COUNTRY(indicator, 'Development', country)
    lineplot = plot_LINE_indicator_COUNTRY(indicator, 'Development', country)
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)



@app.route('/_plot_pov')
def pov_data():
    indicator = request.args.get('indicator', 'potato', type=str)
    print (indicator)
    
    barplot = plot_BAR_indicator_top5(indicator, 'Poverty')
    lineplot = plot_LINE_indicator_top5(indicator, 'Poverty')
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)
@app.route('/_plot_povregion')
def pov_region():
    indicator = request.args.get('indicator', 'potato', type=str)
    region = request.args.get('region', 'potato', type=str)
    print (indicator)
    print (region)
    
    barplot = plot_BAR_indicator_REGION(indicator, 'Poverty', region)
    lineplot = plot_LINE_indicator_REGION(indicator, 'Poverty', region)
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)
@app.route('/_plot_povcountry')
def pov_country():
    indicator = request.args.get('indicator', 'potato', type=str)
    country = request.args.get('country', 'potato', type=str)
    print (indicator)
    print(country)
    
    barplot = plot_BAR_indicator_COUNTRY(indicator, 'Poverty', country)
    lineplot = plot_LINE_indicator_COUNTRY(indicator, 'Poverty', country)
    graphs = column(barplot, lineplot)
    script, div =components(graphs)
    
    return jsonify(script = script, graph= div)


@app.route('/_model_econ')
def model_econ():
    print ('hello')
    a1 = request.args.get('a1', '1', type=float)
    a2 = request.args.get('a2', '1', type=float)
    a3 = request.args.get('a3', '1', type=float)
    a4 = request.args.get('a4', '1', type=float)
    a5 = request.args.get('a5', '1', type=float)
    a6 = request.args.get('a6', '1', type=float)
    a7 = request.args.get('a7', '1', type=float)
    a8 = request.args.get('a8', '1', type=float)
    a9 = request.args.get('a9', '1', type=float)
    a10 = request.args.get('a10', '1', type=float)
    values = [[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]]
    print (values)
    output = economy_model.predict(values)[0]
    print (output)
    return jsonify(output = output)

@app.route('/_model_fin')
def model_fin():
    print ('hello')
    a1 = request.args.get('a1', '1', type=float)
    a2 = request.args.get('a2', '1', type=float)
    a3 = request.args.get('a3', '1', type=float)
    a4 = request.args.get('a4', '1', type=float)
    a5 = request.args.get('a5', '1', type=float)
    a6 = request.args.get('a6', '1', type=float)
    a7 = request.args.get('a7', '1', type=float)
    a8 = request.args.get('a8', '1', type=float)
    a9 = request.args.get('a9', '1', type=float)
    a10 = request.args.get('a10', '1', type=float)
    values = [[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]]
    print (values)
    output = finance_model.predict(values)[0]
    print (output)
    return jsonify(output = output)

@app.route('/_model_dev')
def model_dev():
    print ('hello')
    a1 = request.args.get('a1', '1', type=float)
    a2 = request.args.get('a2', '1', type=float)
    a3 = request.args.get('a3', '1', type=float)
    a4 = request.args.get('a4', '1', type=float)
    a5 = request.args.get('a5', '1', type=float)
    a6 = request.args.get('a6', '1', type=float)
    a7 = request.args.get('a7', '1', type=float)
    a8 = request.args.get('a8', '1', type=float)
    a9 = request.args.get('a9', '1', type=float)
    a10 = request.args.get('a10', '1', type=float)
    values = [[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]]
    print (values)
    output = dev_model.predict(values)[0]
    print (output)
    return jsonify(output = output)

@app.route('/_model_pov')
def model_pov():
    print ('hello')
    a1 = request.args.get('a1', '1', type=float)
    a2 = request.args.get('a2', '1', type=float)
    a3 = request.args.get('a3', '1', type=float)
    a4 = request.args.get('a4', '1', type=float)
    a5 = request.args.get('a5', '1', type=float)
    a6 = request.args.get('a6', '1', type=float)
    a7 = request.args.get('a7', '1', type=float)
    a8 = request.args.get('a8', '1', type=float)
    a9 = request.args.get('a9', '1', type=float)
    a10 = request.args.get('a10', '1', type=float)
    values = [[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]]
    print (values)
    output = poverty_model.predict(values)[0]
    print (output)
    return jsonify(output = output)

if __name__ == "__main__":
    app.run()
