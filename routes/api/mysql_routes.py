from flask import Blueprint, request, jsonify
from database.mysql_connector2 import mysql_db

mysql_blueprint = Blueprint('mysql', __name__)

@mysql_blueprint.route('/check-connection', methods=['POST'])
def check_connection():
    try:
        data = request.form
        mysql_db.configure(**data)
        err = mysql_db.check_connection()
        
        if err:
            return jsonify({'error': err}), 404
        
        return jsonify({'status': 'Connection successful!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@mysql_blueprint.route('/', methods=['GET'])
def index():
    try:
        db_cfg = {
            'host': mysql_db.hostname,
            'user': mysql_db.username,
            'pass': mysql_db.password,
            'data': mysql_db.database
        }
        
        return jsonify({'config': db_cfg}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@mysql_blueprint.route('/show/', methods=['GET'])
def show_tables():
    try:
        tables = mysql_db.get_tables()
        return jsonify({'tables': tables}), 200 
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@mysql_blueprint.route('/<table>/', methods=['GET', 'POST', 'DELETE'])
def database_query(table):
    try:
        if request.method == 'GET':
            rows = mysql_db.select_query(table)
            return jsonify({'rows': rows}), 400
        elif request.method == 'POST':
            rows = mysql_db.select_query(table)
            return jsonify({'rows': rows}), 400
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@mysql_blueprint.route('/<table>/<act_or_id>/', methods=['GET', 'PUT', 'DELETE'])
def table_query(table, act_or_id):
    try:
        query = ''
        if request.method == 'GET':
            if act_or_id == 'describe':
                columns = mysql_db.describe_table(table)
                return jsonify({'columns': columns}), 200
            
            query = f'select * from {table} where id = {act_or_id}'
            return jsonify({'tables': query}), 200
        
        elif request.method == 'PUT':
            query = f'update {table} set something where id = {act_or_id}'
            return jsonify({'tables': query}), 200
        
        elif request.method == 'DELETE':
            query = f'delete from {table} where id = {act_or_id}'
            return jsonify({'tables': query}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500