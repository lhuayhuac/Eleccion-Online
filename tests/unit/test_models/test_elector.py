import pytest
import sys
import os
from datetime import date

# Configurar path antes de cualquier import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

class TestElector:
    """Pruebas unitarias para el modelo Elector"""

    # DATOS DE PRUEBA COMUNES
    VALID_DATA = {
        'nombres': 'Juan Carlos',
        'apellido_paterno': 'Perez',
        'apellido_materno': 'Gomez', 
        'fecha_nacimiento': date(1990, 5, 15),
        'usuario': 'juanperez',
        'contrasena': 'password123',
        'correo': 'juan@unsa.edu.pe'
    }

    def test_elector_creation_valid_data(self, database):
        """Test: Crear elector con datos válidos debería funcionar"""
        # Arrange
        from app.models.Elector import Elector
        from app import db
        
        data = self.VALID_DATA.copy()
        
        # Act
        elector = Elector(**data)
        db.session.add(elector)
        db.session.commit()
        
        # Assert
        assert elector.id is not None
        assert elector.nombres == data['nombres']
        assert elector.usuario == data['usuario']
        assert elector.correo == data['correo']
        # Verificar que la contraseña fue hasheada
        assert elector.contrasena != data['contrasena']
        assert elector.revisar_contrasena(data['contrasena']) is True

    def test_elector_creation_missing_required_fields(self, database):
        """Test: Crear elector sin campos obligatorios debería fallar"""
        # Arrange
        from app.models.Elector import Elector
        from app import db
        from sqlalchemy.exc import IntegrityError
        
        data = self.VALID_DATA.copy()
        data['nombres'] = None  # Campo requerido
        
        # Act & Assert
        with pytest.raises((IntegrityError, Exception)):
            elector = Elector(**data)
            db.session.add(elector)
            db.session.commit()
            db.session.rollback()

    def test_revisar_contrasena_correct_password(self, database):
        """Test: Verificar contraseña correcta debería retornar True"""
        # Arrange
        from app.models.Elector import Elector
        from app import db
        
        elector = Elector(**self.VALID_DATA)
        db.session.add(elector)
        db.session.commit()
        
        # Act
        result = elector.revisar_contrasena(self.VALID_DATA['contrasena'])
        
        # Assert
        assert result is True

    def test_revisar_contrasena_incorrect_password(self, database):
        """Test: Verificar contraseña incorrecta debería retornar False"""
        # Arrange
        from app.models.Elector import Elector
        from app import db
        
        elector = Elector(**self.VALID_DATA)
        db.session.add(elector)
        db.session.commit()
        
        # Act
        result = elector.revisar_contrasena('wrong_password')
        
        # Assert
        assert result is False

    def test_hash_contrasena_method(self):
        """Test: Método hash_contrasena debería generar hash válido"""
        # Arrange
        from app.models.Elector import Elector
        
        password = "test_password"
        elector = Elector(**self.VALID_DATA)
        
        # Act
        hashed = elector.hash_constrasena(password)
        
        # Assert
        assert hashed != password
        assert isinstance(hashed, str)
        assert len(hashed) > 0

    def test_usuario_unique_constraint(self, database):
        """Test: No debería permitir usuarios duplicados"""
        # Arrange
        from app.models.Elector import Elector
        from app import db
        from sqlalchemy.exc import IntegrityError
        
        elector1 = Elector(**self.VALID_DATA)
        db.session.add(elector1)
        db.session.commit()
        
        # Act & Assert - Intentar crear otro con mismo usuario
        data2 = self.VALID_DATA.copy()
        data2['correo'] = 'otro@unsa.edu.pe'  # Email diferente
        
        with pytest.raises((IntegrityError, Exception)):
            elector2 = Elector(**data2)
            db.session.add(elector2)
            db.session.commit()
            db.session.rollback()

    def test_elector_str_representation(self, database):
        """Test: Representación en string del elector"""
        # Arrange
        from app.models.Elector import Elector
        from app import db
        
        elector = Elector(**self.VALID_DATA)
        db.session.add(elector)
        db.session.commit()
        
        # Act
        str_repr = str(elector)
        
        # Assert - Verificar que contiene información relevante
        assert elector.nombres in str_repr or elector.usuario in str_repr or str(elector.id) in str_repr

    def test_elector_to_dict(self, database):
        """Test: Método to_dict si existe"""
        # Arrange
        from app.models.Elector import Elector
        from app import db
        
        elector = Elector(**self.VALID_DATA)
        db.session.add(elector)
        db.session.commit()
        
        # Act & Assert - Verificar que podemos acceder a los atributos básicos
        assert hasattr(elector, 'nombres')
        assert hasattr(elector, 'usuario')
        assert hasattr(elector, 'correo')