import couchdb
import os
import pandas as pd
import json
from flask import Flask, render_template, request

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
        exp_dicts = []
        for id in id_list:
            exp = self.pull_experiment(id)
            if exp['hplc'] is not None:
                exp['hplc']['Sample'] = f'{id}: ' + exp['hplc']['Sample']

            exp_dicts.append(exp)

        try:
            combined_hplc = pd.concat([x['hplc'] for x in exp_dicts if x['hplc'] is not None])
        except ValueError:
            combined_hplc = None
        try:
            combined_fplc = pd.concat([x['fplc'] for x in exp_dicts if x['fplc'] is not None])
        except ValueError:
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
    rj = request.get_json()

    if rj['action'] == 'get_experiment_list':
        return json.dumps(db.experiment_list), 200, {'ContentType': 'application/json'}