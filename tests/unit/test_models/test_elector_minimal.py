import pytest
import sys
import os
from datetime import date

# Configurar path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

class TestElectorMinimal:
    """Pruebas mínimas para Elector sin dependencias complejas"""
    
    def test_elector_basic_creation(self):
        """Test básico de creación sin base de datos"""
        from app.models.Elector import Elector
        
        data = {
            'nombres': 'Ana Maria',
            'apellido_paterno': 'Gonzales',
            'apellido_materno': 'Perez',
            'fecha_nacimiento': date(1995, 3, 10),
            'usuario': 'anagonzales',
            'contrasena': 'testpass123',
            'correo': 'ana@unsa.edu.pe'
        }
        
        elector = Elector(**data)
        
        # Verificaciones básicas
        assert elector.nombres == 'Ana Maria'
        assert elector.usuario == 'anagonzales'
        assert elector.correo == 'ana@unsa.edu.pe'
        assert elector.contrasena != 'testpass123'  # Debe estar hasheada
    
    def test_password_hashing_works(self):
        """Test que el hashing de contraseñas funciona"""
        from app.models.Elector import Elector
        from datetime import date
        
        elector = Elector(
            nombres='Test',
            apellido_paterno='User',
            apellido_materno='Test',
            fecha_nacimiento=date(2000, 1, 1),
            usuario='testuser',
            contrasena='mysecretpassword',
            correo='test@unsa.edu.pe'
        )
        
        # La contraseña correcta debe verificar True
        assert elector.revisar_contrasena('mysecretpassword') is True
        
        # Contraseña incorrecta debe verificar False
        assert elector.revisar_contrasena('wrongpassword') is False
    
    def test_hash_method_independent(self):
        """Test del método hash_constrasena de forma aislada"""
        from app.models.Elector import Elector
        from datetime import date
        
        elector = Elector(
            nombres='Test',
            apellido_paterno='User', 
            apellido_materno='Test',
            fecha_nacimiento=date(2000, 1, 1),
            usuario='testuser2',
            contrasena='password',
            correo='test2@unsa.edu.pe'
        )
        
        new_password = "completely_different"
        hashed = elector.hash_constrasena(new_password)
        
        # Verificaciones del hash
        assert hashed != new_password
        assert isinstance(hashed, str)
        assert len(hashed) > 20  # Los hashes bcrypt son largos

    def test_elector_attributes(self):
        """Test que todos los atributos están presentes"""
        from app.models.Elector import Elector
        from datetime import date
        
        elector = Elector(
            nombres='Carlos',
            apellido_paterno='Lopez',
            apellido_materno='Martinez',
            fecha_nacimiento=date(1985, 7, 20),
            usuario='carlosl',
            contrasena='pass123',
            correo='carlos@unsa.edu.pe'
        )
        
        # Verificar que todos los atributos existen
        expected_attrs = ['nombres', 'apellido_paterno', 'apellido_materno', 
                         'fecha_nacimiento', 'usuario', 'contrasena', 'correo']
        
        for attr in expected_attrs:
            assert hasattr(elector, attr), f"Falta atributo: {attr}"