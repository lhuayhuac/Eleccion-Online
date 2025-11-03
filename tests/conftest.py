import pytest
import os
import sys

# Configurar el path CORRECTAMENTE
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

# Configurar entorno de pruebas
os.environ['FLASK_ENV'] = 'testing'

@pytest.fixture(scope='session')
def app():
    """Fixture para la aplicación Flask con todos los modelos importados"""
    from flask import Flask
    from app import db, ma
    
    # Importar TODOS los modelos para que las relaciones funcionen
    from app.models.Candidato import Candidato
    from app.models.Eleccion import Eleccion
    from app.models.Elector import Elector
    from app.models.ListaCandidato import ListaCandidato
    from app.models.Propuesta import Propuesta
    from app.models.Voto import Voto
    
    # Crear aplicación para pruebas
    app = Flask(__name__)
    
    # Configuración específica para pruebas
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'WTF_CSRF_ENABLED': False,
        'SECRET_KEY': 'test-secret-key'
    })
    
    # Inicializar extensiones
    db.init_app(app)
    ma.init_app(app)
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(scope='function')
def database(app):
    """Fixture para la base de datos"""
    from app import db
    
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()