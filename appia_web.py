import couchdb
import os
import pandas as pd
import json
from flask import Flask, render_template, request

def convert_to_columns(df: pd.DataFrame):
    to_return = {}
    for col in df.columns:
        if col != 'index':
            to_return[col] = list(df[col])
    return to_return


def prepare_for_transmission(df_dict):
    return_dict = {}

    if df_dict['hplc'] is not None:
        hplc = df_dict['hplc'].pivot_table(
            index = ['mL', 'Channel', 'Time', 'Normalization'],
            columns = 'Sample',
            values = 'Value'
        ).reset_index()
        
        return_dict['hplc_raw'] = convert_to_columns(
            hplc.loc[hplc['Normalization'] == 'Signal'].drop('Normalization', axis = 1)
        )
        return_dict['hplc_norm'] = convert_to_columns(
            hplc.loc[hplc['Normalization'] == 'Normalized'].drop('Normalization', axis = 1)
        )
    else:
        return_dict['hplc_raw'] = None
        return_dict['hplc_norm'] = None

    if df_dict['fplc'] is not None:
        return_dict['fplc'] = convert_to_columns(df_dict['fplc'])
    else:
        return_dict['fplc'] = None


    return return_dict

class Database:
    def __init__(self) -> None:
        host = os.environ['COUCHDB_HOST']
        username = os.environ['COUCHDB_USERNAME']
        password = os.environ['COUCHDB_PASSWORD']
        self.server = couchdb.Server(f'http://{username}:{password}@{host}:5984')
        if 'traces' in self.server:
            self.db = self.server['traces']
        else:
            self.db = self.server.create('traces')

        self.version = '4'

    @property
    def experiment_list(self) -> list:
        return [x['id'] for x in self.db.view('_all_docs')]

    def pull_experiment(self, id):
        doc = self.db.get(id)
        

        trace_dict = {}
        try:
            trace_dict['hplc'] = pd.read_json(doc['hplc']).melt(
                id_vars = ['mL', 'Channel', 'Time', 'Normalization'],
                var_name = 'Sample',
                value_name = 'Value'
            )
        except ValueError:
            trace_dict['hplc'] = None
        
        try:
            trace_dict['fplc'] = pd.read_json(doc['fplc'])
        except ValueError:
            trace_dict['fplc'] = None

        return trace_dict

    def pull_multiple_experiments(self, id_list):
        app.logger.debug(id_list)
        exp_dicts = []
        for id in id_list:
            exp = self.pull_experiment(id)
            if exp['hplc'] is not None and len(id_list) > 1:
                exp['hplc']['Sample'] = f'{id}: ' + exp['hplc']['Sample']

            exp_dicts.append(exp)
            
        try:
            combined_hplc = pd.concat(
                [x['hplc'] for x in exp_dicts if x['hplc'] is not None]
            ).reset_index()
        except ValueError as e:
            combined_hplc = None
        try:
            combined_fplc = pd.concat(
                [x['fplc'] for x in exp_dicts if x['fplc'] is not None]
            ).reset_index()
        except ValueError as e:
            combined_fplc = None

        return {'hplc': combined_hplc, 'fplc': combined_fplc}



app = Flask(
    __name__,
    static_folder=os.path.join('dist', 'static'),
    template_folder='dist'
)

db = Database()

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/api', methods = ['POST'])
def api():
    global db
    rj = request.get_json()

    if rj['action'] == 'get_experiment_list':
        return json.dumps(db.experiment_list), 200, {'ContentType': 'application/json'}

    elif rj['action'] == 'get_experiment_json':
        combined_dict = db.pull_multiple_experiments(rj['id_list'])
        return json.dumps(prepare_for_transmission(combined_dict)), 200, {'ContentType': 'application/json'}