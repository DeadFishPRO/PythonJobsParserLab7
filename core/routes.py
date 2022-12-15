from core import api
from flask import jsonify
from core.utils import get_jobs
from flask_restx import Resource, reqparse

ns = api.namespace('/', description='PythonJobs APIs')

parser = reqparse.RequestParser()
parser.add_argument('count', type=int, required=True, help="Число вакансий, которые нужно вывести:")
parser.add_argument('shuffle', type=bool, help="Перемешать вакансии:")
parser_copy = parser
@ns.route('/get-jobs/by-count')
class DailyHoroscopeAPI(Resource):
    @ns.doc(parser=parser_copy)
    def get(self):
        args = parser.parse_args()
        count = args.get('count')
        shuffle = args.get('shuffle')
        data = get_jobs(count,shuffle)
        return jsonify(Jobs=data,TotalJobs=count)
