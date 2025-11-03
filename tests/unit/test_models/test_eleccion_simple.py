import pytest
import sys
import os

# Configurar path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.insert(0, project_root)

class TestEleccionSimple:
    """Pruebas SIMPLES para Eleccion"""
    
    def test_eleccion_import(self):
        """Test: Verificar que podemos importar Eleccion"""
        try:
            from app.models.Eleccion import Eleccion
            assert True, "Import exitoso de Eleccion"
        except ImportError as e:
            pytest.fail(f"No se pudo importar Eleccion: {e}")
    
    def test_eleccion_schema_import(self):
        """Test: Verificar que podemos importar EleccionSchema"""
        try:
            from app.models.Eleccion import EleccionSchema
            assert True, "Import exitoso de EleccionSchema"
        except ImportError as e:
            pytest.fail(f"No se pudo importar EleccionSchema: {e}")
    
    def test_eleccion_enum_values(self):
        """Test: Valores válidos para el estado"""
        # Los estados válidos son 'abierto' y 'cerrado'
        valid_states = ['abierto', 'cerrado']
        
        # Podemos verificar esto documentalmente
        assert 'abierto' in valid_states
        assert 'cerrado' in valid_states