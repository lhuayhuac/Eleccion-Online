import pytest
import sys
import os

# Configurar path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.insert(0, project_root)

class TestCandidatoSimple:
    """Pruebas SIMPLES para Candidato"""
    
    def test_candidato_import(self):
        """Test: Verificar que podemos importar Candidato"""
        try:
            from app.models.Candidato import Candidato
            assert True, "Import exitoso de Candidato"
        except ImportError as e:
            pytest.fail(f"No se pudo importar Candidato: {e}")
    
    def test_candidato_schema_import(self):
        """Test: Verificar que podemos importar CandidatoSchema"""
        try:
            from app.models.Candidato import CandidatoSchema
            assert True, "Import exitoso de CandidatoSchema"
        except ImportError as e:
            pytest.fail(f"No se pudo importar CandidatoSchema: {e}")
    
    def test_candidato_fields_exist(self):
        """Test: Campos esperados en Candidato"""
        from app.models.Candidato import Candidato
        
        expected_fields = ['id_candidato', 'nombres', 'apellido_paterno', 
                          'apellido_materno', 'rol', 'id_lista']
        
        # Verificar que los campos existen en la tabla
        for field in expected_fields:
            assert field in Candidato.__table__.columns, f"Falta campo: {field}"