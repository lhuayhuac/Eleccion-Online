import pytest
import sys
import os

# Configurar path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.insert(0, project_root)

class TestListaCandidatoSimple:
    """Pruebas SIMPLES para ListaCandidato sin relaciones complejas"""
    
    def test_lista_candidato_import(self):
        """Test: Verificar que podemos importar ListaCandidato"""
        try:
            from app.models.ListaCandidato import ListaCandidato, EstadoListaEnum
            assert True, "Import exitoso de ListaCandidato"
        except ImportError as e:
            pytest.fail(f"No se pudo importar ListaCandidato: {e}")
    
    def test_estado_lista_enum_values(self):
        """Test: Valores del enum EstadoListaEnum"""
        from app.models.ListaCandidato import EstadoListaEnum
        
        assert EstadoListaEnum.aprobado.value == "aprobado"
        assert EstadoListaEnum.desaprobado.value == "desaprobado" 
        assert EstadoListaEnum.pendiente.value == "pendiente"
    
    def test_lista_candidato_attributes(self):
        """Test: Atributos básicos de ListaCandidato"""
        from app.models.ListaCandidato import ListaCandidato
        
        # Solo verificar que la clase tiene los atributos esperados
        expected_attrs = ['id_lista', 'nombre', 'estado', 'id_eleccion']
        
        for attr in expected_attrs:
            assert hasattr(ListaCandidato, attr) or attr in ListaCandidato.__table__.columns, f"Falta atributo: {attr}"