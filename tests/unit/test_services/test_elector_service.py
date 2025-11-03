import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Configurar path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.insert(0, project_root)

class TestElectorServiceImpl:
    """Pruebas para ElectorServiceImpl con mocks"""
    
    def test_elector_service_import(self):
        """Test: Verificar que podemos importar ElectorServiceImpl"""
        try:
            from app.services.PersonaServicioImpl import ElectorServiceImpl
            assert True, "Import exitoso de ElectorServiceImpl"
        except ImportError as e:
            pytest.fail(f"No se pudo importar ElectorServiceImpl: {e}")
    
    @patch('app.services.PersonaServicioImpl.Elector')
    @patch('app.services.PersonaServicioImpl.db')
    def test_get_elector_by_id_success(self, mock_db, mock_elector):
        """Test: Obtener elector por ID exitosamente"""
        # Arrange
        from app.services.PersonaServicioImpl import ElectorServiceImpl
        
        mock_elector_instance = Mock()
        mock_elector.query.get.return_value = mock_elector_instance
        
        service = ElectorServiceImpl()
        elector_id = 1
        
        # Act
        result = service.get_elector_by_id(elector_id)
        
        # Assert
        mock_elector.query.get.assert_called_once_with(elector_id)
        assert result == mock_elector_instance
    
    @patch('app.services.PersonaServicioImpl.Elector')
    @patch('app.services.PersonaServicioImpl.db')
    def test_create_elector_success(self, mock_db, mock_elector):
        """Test: Crear elector exitosamente"""
        # Arrange
        from app.services.PersonaServicioImpl import ElectorServiceImpl
        from datetime import date
        
        service = ElectorServiceImpl()
        
        # Mock del modelo elector
        mock_elector_model = Mock()
        mock_elector_model.nombres = "Juan"
        mock_elector_model.apellido_paterno = "Perez"
        mock_elector_model.apellido_materno = "Gomez"
        mock_elector_model.fecha_nacimiento = date(1990, 1, 1)
        mock_elector_model.usuario = "juanperez"
        mock_elector_model.correo = "juan@unsa.edu.pe"
        
        contrasena = "password123"
        
        # Act
        result = service.create_elector(mock_elector_model, contrasena)
        
        # Assert
        mock_db.session.add.assert_called_once()
        mock_db.session.commit.assert_called_once()
        assert result is not None
    
    @patch('app.services.PersonaServicioImpl.Elector')
    @patch('app.services.PersonaServicioImpl.db')
    def test_get_elector_by_email_success(self, mock_db, mock_elector):
        """Test: Obtener elector por email exitosamente"""
        # Arrange
        from app.services.PersonaServicioImpl import ElectorServiceImpl
        
        mock_elector_instance = Mock()
        mock_elector.query.filter_by.return_value.first.return_value = mock_elector_instance
        
        service = ElectorServiceImpl()
        email = "test@unsa.edu.pe"
        
        # Act
        result = service.get_elector_by_email(email)
        
        # Assert
        mock_elector.query.filter_by.assert_called_once_with(correo=email)
        assert result == mock_elector_instance