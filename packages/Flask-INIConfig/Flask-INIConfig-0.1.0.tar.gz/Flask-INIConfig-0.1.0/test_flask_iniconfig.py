#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nose.tools as nt
import sys

from flask import Flask
# implicit test ??
from flask.ext.iniconfig import INIConfig

if sys.version_info < (3,):
    from ConfigParser import InterpolationMissingOptionError
else:
    # pylint: disable=F0401
    from configparser import InterpolationMissingOptionError


class TestINIConfigFileOpen(object):

    @classmethod
    def setupClass(cls):
        cls.app = Flask('foo')
        INIConfig(cls.app)

    def test_file_open_fail(self):
        for type_, filepath in {
                    'list': ['test.ini'],
                    'dict': {'a': 'test.ini'},
                    'obj': object()
                }.items():
            callable = lambda fp: self.app.config.from_inifile(fp)
            callable.description = '%s_%s' % (
                    self.test_file_open_fail.__name__, type_)
            # decorators with args
            callable = nt.raises(AssertionError)(callable)
            yield callable, filepath

    def test_file_open_ok(self):
        for type_, filepath in {
                    'str': 'test.ini',
                    'unicode': u'test.ini',
                    'raw': r'test.ini',
                    'bytes': b'test.ini'
                }.items():
            callable = lambda fp: self.app.config.from_inifile(fp)
            callable.description = '%s_%s_%s' % (
                    self.test_file_open_ok.__name__, type_, filepath)
            yield callable, filepath

class TestINIConfigObjectify(object):

    def test_section_objectfication(self):
        for objectify in True, False:
            self.app = Flask('bar')
            INIConfig(self.app)
            self.app.config.from_inifile('test.ini', objectify=objectify)
            for attr in ['bools', 'ints', 'floats', 'literals', 'strs']:
                str_objectify = str(objectify).lower()
                callable = lambda name: \
                        getattr(nt, 'assert_%s' % str_objectify)(
                                hasattr(self.app.config, name))
                callable.description = '%s_%s_%s' % (
                        self.test_section_objectfication.__name__,
                        str(objectify).lower(), attr)
                # decorators with args
                yield callable, attr


class TestINIConfig(object):

    @classmethod
    def setupClass(cls):
        cls.app = Flask('bar')
        INIConfig(cls.app)

    def setup(self):
        self.app.config.from_inifile('test.ini')

    @staticmethod
    def check_type(value, type_):
        nt.assert_is_instance(value, type_)

    @staticmethod
    def check_membership(config, name):
        nt.assert_in(name, config)

    @staticmethod
    def check_no_membership(config, name):
        nt.assert_not_in(name, config)

    def test_init_app(self):
        app = Flask('bar')
        INIConfig().init_app(app)

    def test_configparser_options(self):
        app = Flask('bar')
        INIConfig(defaults={'a': 1}, dict_type=dict,
                allow_no_value=True).init_app(app)

    def test_config_method(self):
        nt.ok_(hasattr(self.app.config, 'from_inifile'))

    def test_load_nofile_noerror(self):
        self.app.config.from_inifile('nonexistant.ini')

    def test_load_flask_default(self):
        nt.ok_('DEBUG' in self.app.config)
        nt.ok_(self.app.config['DEBUG'])

    def test_load_section_case_sensitivity(self):
        settings = self.app.config.get('INTS')
        nt.assert_is_none(settings)

    def test_load_property_case_sensitivity(self):
        settings = self.app.config.get('ints')
        property = settings.get('G')
        nt.assert_is_none(property)

    def test_load_basic_types(self):
        for type_ in [int, float, bool, str]:
            settings = self.app.config['%ss' % type_.__name__]
            for key, value in settings.items():
                callable = self.check_type
                callable.description = '%s_%s_%s' % (
                        self.test_load_basic_types.__name__, type_.__name__, key)
                yield callable, value, type_

    def test_load_json_list(self):
        settings = self.app.config['literals']
        nt.assert_is_instance(settings['o'], list)

    def test_load_json_dict(self):
        settings = self.app.config['literals']
        for name in ['p', 'q']:
            callable = self.check_type
            callable.description = '%s_%s' % (
                    self.test_load_json_dict.__name__, name)
            yield callable, settings[name], dict

    def test_load_json_embedded_list(self):
        settings = self.app.config['literals']
        nt.assert_is_instance(settings['q']['b'], list)

    def test_load_json_embedded_dict(self):
        settings = self.app.config['literals']
        nt.assert_is_instance(settings['q']['c'], dict)

    def test_load_json_tuple(self):
        settings = self.app.config['literals']
        nt.assert_is_instance(settings['r'], tuple)

    def test_load_colon_separated(self):
        settings = self.app.config['colonsep']
        for name in ['v', 'w']:
            callable = self.check_membership
            callable.description = '%s_%s' % (
                    self.test_load_colon_separated.__name__, name)
            yield callable, settings, name

    def test_load_empty(self):
        settings = self.app.config['empty']
        nt.eq_(settings['x'], '')

    def test_load_settings_only(self):
        app = Flask('bar')
        INIConfig().init_app(app)
        app.config.from_inifile_sections('test.ini', ['strs'])

        for name in ['DEBUG', 'S', 'T', 'U']:
            callable = self.check_membership
            callable.description = '%s_%s' % (
                    self.test_load_settings_only.__name__, name)
            yield callable, app.config, name

        for name in ['debug', 's', 't', 'u']:
            callable = self.check_no_membership
            callable.description = '%s_%s' % (
                    self.test_load_settings_only.__name__, name)
            yield callable, app.config, name

    def test_load_settings_only_with_preserve_case(self):
        app = Flask('bar')
        INIConfig().init_app(app)
        app.config.from_inifile_sections('test.ini', ['strs'],
                preserve_case=True)

        for name in ['DEBUG', 's', 't', 'u']:
            callable = self.check_membership
            callable.description = '%s_%s' % (
                    self.test_load_settings_only_with_preserve_case.__name__, name)
            yield callable, app.config, name

        for name in ['debug', 'S', 'T', 'U']:
            callable = self.check_no_membership
            callable.description = '%s_%s' % (
                    self.test_load_settings_only_with_preserve_case.__name__, name)
            yield callable, app.config, name


class TestINIConfigInterpolation(object):

    @nt.raises(InterpolationMissingOptionError)
    def test_interpolation_error(self):
        app = Flask('baz')
        INIConfig(app)
        app.config.from_inifile('test_interpolation.ini')

    @nt.raises(InterpolationMissingOptionError)
    def test_interpolation_error_section(self):
        app = Flask('baz')
        INIConfig(app)
        app.config.from_inifile_sections(
                'test_interpolation.ini', ['interpolation_error'])

    def test_ignore_irrelevant_sections(self):
        app = Flask('baz')
        INIConfig(app)
        app.config.from_inifile_sections(
                'test_interpolation.ini', ['interpolation'])
        assert app.config.get('B') == 'a'
        assert app.config.get('C') is None
