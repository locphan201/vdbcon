from flask import Blueprint, request, jsonify
from database.mysql_connector import mysql_db

mysql_blueprint = Blueprint('mysql', __name__)

@mysql_blueprint.route('/check-connection', methods=['POST'])
def index():
    try:
        data = request.form
        mysql_db.configure(**data)
        err = mysql_db.check_connection()
        
        if err:
            return jsonify({'error': err}), 404
        
        return jsonify({'status': 'Connection successful!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@mysql_blueprint.route('/show', methods=['GET'])
def list_of_tables():
    try:
        tables = mysql_db.get_tables()
        if err := mysql_db.err:
            return jsonify({'error': err.msg}), 404
        
        return jsonify({'tables': tables}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500