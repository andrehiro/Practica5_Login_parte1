# Practica5_Login_parte1
Andre Alexander Hidrogo Rocha 08/11/2023 Primera parte del login por medio de Flask

Para realizar esta practica necesitas los siguientes programas:
- Python (preferentemente 3.8.0)
- Mysql
- Microsoft developer tools

### Una vez tienes los programas necesarios deberas seguir estos pasos:

##### Crear la estructura del directorio
- database
- src
  * models  
    - entities
  * static
    - css
    - img
  * templates
    - auth
- env

#### Archivos de la aplicacion
En la carpeta source creamos los archivos app.py y config.py, en estos creamos la clase DevelpmentConfig y en app.py importamos esta clase.

Despues creamos la pagina principal de html llamada base.html, la cual podemos mostrar con render_template. Lo unico que le debemos a agregar a esta pagina que no conocemos son los siguietes bloques de codigo en donde corresponden.

{% block miCSS %}{% endblock %}
{% block titulo %}{% endblock %}
{% block cuerpo %} {% endblock %}

#### Uso de formularios
Por ulitmo agregaremos un formulario a la pagina. Puedes encontrar plantillas de formularios en esta liga:

https://mdbootstrap.com/docs/standard/extended/login/
