# python 2
from __future__ import absolute_import

# builtin
from unittest import TestCase, main

# custom
from blowdrycss.filehandler import FileFinder
from blowdrycss.classparser import ClassParser
from blowdrycss.utilities import unittest_file_path, delete_file_paths
import blowdrycss_settings as settings


class TestClassParser(TestCase):
    def test_build_file_path_list(self):
        delete_these = (
            unittest_file_path('test_examplesite', 'clashing_aliases.html'),
            unittest_file_path('test_examplesite', 'modify.html'),
            unittest_file_path('test_examplesite', 'property_aliases.html'),
        )
        delete_file_paths(file_paths=delete_these)

        expected_file_paths = {
            # unittest_file_path('test_examplesite', 'clashing_aliases.html'),
            # unittest_file_path('test_examplesite', 'modify.html'),
            # unittest_file_path('test_examplesite', 'property_aliases.html'),
            unittest_file_path('test_generic', 'blowdry.html'),
            unittest_file_path('test_html', 'index.html'),
            unittest_file_path('test_html', 'media_query.html'),
            unittest_file_path('test_html', 'test.html'),
            unittest_file_path('test_aspx', 'test.aspx'),
            unittest_file_path('test_jinja', 'test.jinja2'),
        }
        settings.file_types = ('*.html', '*.aspx', '*.jinja2')                                  # Override file_types
        project_directory = unittest_file_path()
        file_finder = FileFinder(project_directory=project_directory)
        self.assertTrue('.aspx' in list(file_finder.file_dict), msg=settings.file_types)
        class_parser = ClassParser(file_dict=file_finder.file_dict)
        self.assertEqual(
                set(class_parser.file_path_list), expected_file_paths,
                msg='\n' + str(set(class_parser.file_path_list)) + '\n' + str(expected_file_paths) + '\nsettings: ' + str(settings.html_docs)
        )
        settings.file_types = ('*.html', )                                                      # Reset file_types

    def test_build_class_set(self):
        # integration test
        expected_class_set = {
            'row', 'bgc-green', 'padding-top-30', 'padding-bottom-30', 'bgc-pink', 'color-h979591',
            'purple', 'padding-left-5', 'squirrel', 'text-align-center', 'large-up', 'border-1',
            'padding-25-820-up', 'margin-5-2-5-2-1000-up',
            # Embedded <script></script>
            'jquery1', 'jquery2', 'jquery3', 'jquery4', 'jquery5', 'jquery6', 'jquery7', 'jquery8',
            'jquery9', 'jquery10', 'jquery11', 'jquery12', 'jquery13', 'jquery14', 'jquery15', 'jquery16',
            'jquery17',
            'dojo1', 'dojo2', 'dojo3', 'dojo4', 'dojo5', 'dojo6', 'dojo7', 'dojo8', 'dojo9', 'dojo10', 'dojo11',
            'dojo12',
        }
        settings.file_types = ('*.aspx', '*.jinja2')                                            # Override file_types
        project_directory = unittest_file_path()
        file_finder = FileFinder(project_directory=project_directory)
        self.assertFalse('.html' in list(file_finder.file_dict), msg=settings.file_types)
        self.assertTrue('.aspx' in list(file_finder.file_dict), msg=settings.file_types)
        class_parser = ClassParser(file_dict=file_finder.file_dict)
        self.assertEqual(class_parser.class_set, expected_class_set, msg=class_parser.class_set)
        settings.file_types = ('*.html', )                                                      # Reset file_types

    def test_build_class_set_CSharp_cs_file(self):
        # integration test
        expected_class_set = {
            'font-size-14', 'large-up', 'padding-bottom-2', 'white-hover',
            'hide', 'small-6', 'columns', 'border-right-width-2',
            'incorrect-class-25', 'squirrel',
            'material-icons', 'large-3', 'xlarge-2', 'vertical-align-middle', 'padding-bottom-17',
            'orange', 'h000', 'margin-top-10', 'margin-bottom-72',
            # Attributes.Add("class", ...)
            'pink', 'xsmall-only', 'height-12', 'width-100p', 'inline',
        }
        settings.file_types = ('*.cs', )                                            # Override file_types
        project_directory = unittest_file_path()
        file_finder = FileFinder(project_directory=project_directory)
        self.assertFalse('.html' in list(file_finder.file_dict), msg=settings.file_types)
        self.assertTrue('.cs' in list(file_finder.file_dict), msg=settings.file_types)
        class_parser = ClassParser(file_dict=file_finder.file_dict)
        self.assertEqual(class_parser.class_set, expected_class_set, msg=class_parser.class_set)
        settings.file_types = ('*.html', )                                                      # Reset file_types


if __name__ == '__main__':
    main()


