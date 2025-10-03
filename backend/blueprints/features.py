from flask import Blueprint, render_template

features_bp = Blueprint('features', __name__)

@features_bp.route('/features')
def features():
    return render_template('features.html')
