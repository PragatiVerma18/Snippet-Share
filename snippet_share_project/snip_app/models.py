from django.db import models
from django.core.validators import RegexValidator
from django import forms


class Snip(models.Model):
    alphanumeric = RegexValidator(
        r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    title = models.CharField(max_length=40, default="Untitled")
    text = models.TextField()
    link_code = models.CharField(
        max_length=8, unique=True, validators=[alphanumeric])
    langs = [('text', 'None'),
            ('Markup', 'markup'),
            ('html', 'html'),
             ('CSS', 'css'),
             ('C-like', 'clike'),
             ('JavaScript', 'javascript, js'),
             ('Arduino', 'arduino'),
             ('Bash', 'bash, shell'),
             ('BASIC', 'basic'),
             ('C', 'c'),
             ('C#', 'csharp, cs, dotnet'),
             ('Cpp', 'cpp'),
             ('CoffeeScript', 'coffeescript, coffee'),
             ('CMake', 'cmake'),
             ('Clojure', 'clojure'),
             ('Django/Jinja2', 'django, jinja2'),
             ('Docker', 'docker, dockerfile'),
             ('Git', 'git'),
             ('GameMaker Language', 'gml, gamemakerlanguage'),
             ('Go', 'go'),
             ('GraphQL', 'graphql'),
             ('Groovy', 'groovy'),
             ('Haml', 'haml'),
             ('HTTP', 'http'),
             ('Icon', 'icon'),
             ('Java', 'java'),
             ('JavaDoc', 'javadoc'),
             ('JSDoc', 'jsdoc'),
             ('JSON', 'json'),
             ('JSONP', 'jsonp'),
             ('JSON5', 'json5'),
             ('Kotlin', 'kotlin'),
             ('LaTeX', 'latex, tex, context'),
             ('Latte', 'latte'),
             ('Less', 'less'),
             ('LiveScript', 'livescript'),
             ('Lua', 'lua'),
             ('Makefile', 'makefile'),
             ('Markdown', 'markdown, md'),
             ('MATLAB', 'matlab'),
             ('nginx', 'nginx'),
             ('Objective-C', 'objectivec'),
             ('OpenCL', 'opencl'),
             ('Parser', 'parser'),
             ('Pascal', 'pascal, objectpascal'),
             ('Perl', 'perl'),
             ('PHP', 'php'),
             ('PL/SQL', 'plsql'),
             ('PowerShell', 'powershell'),
             ('Pug', 'pug'),
             ('Python', 'python, py'),
             ('R', 'r'),
             ('React JSX', 'jsx'),
             ('React TSX', 'tsx'),
             ('Regex', 'regex'),
             ('Ruby', 'ruby, rb'),
             ('Rust', 'rust'),
             ('SAS', 'sas'),
             ('Sass (Sass)', 'sass'),
             ('Sass (Scss)', 'scss'),
             ('Scala', 'scala'),
             ('SQL', 'sql'),
             ('Stylus', 'stylus'),
             ('Swift', 'swift'),
             ('Twig', 'twig'),
             ('TypeScript', 'typescript, ts'),
             ('Velocity', 'velocity'),
             ('vim', 'vim'),
             ('Visual Basic', 'visual-basic, vb'),
             ('Wiki markup', 'wiki'),
             ('YAML', 'yaml, yml'),
             ('Zig', 'zig'),

             ]
    lang = models.CharField(max_length=18, choices=langs, default='text')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link_code+" : "+self.text[:20]
