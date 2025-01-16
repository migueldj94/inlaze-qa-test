

# Prueba Técnica QA - Inlaze

Este repositorio contiene los scripts de automatización desarrollados para la prueba técnica de QA de Inlaze. Los scripts están escritos en Python utilizando Selenium.

## Requisitos
- Python 3.8 o superior.
- Navegador Chrome instalado.
- ChromeDriver compatible con la versión del navegador.

## Instalación
1. Clona este repositorio:
   ```bash
   git@github.com:migueldj94/inlaze-qa-test.git
   cd inlaze-qa-test

## Ejecución
Asegúrate de que ChromeDriver está en el PATH.
Ejecuta las pruebas con:  pytest tests/

## Detalles de los Scripts
Este script automatiza las pruebas del registro de usuario, validando:

Registro exitoso con datos válidos.
Restricciones en el campo nombre (mínimo dos palabras).
Validación del formato del email y que sea único.
Reglas de seguridad de la contraseña.
Verificación de coincidencia entre las dos contraseñas ingresadas.
Restricción de envío del formulario si hay campos vacíos.

test_login_valido.py
Este script automatiza las pruebas del login, validando:

Inicio de sesión exitoso con credenciales correctas.
Restricción de envío del formulario si hay campos vacíos.
Visualización del nombre del usuario después de iniciar sesión.
Cierre de sesión exitoso.



