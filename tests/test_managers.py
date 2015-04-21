from spidermon.rules import CallableRule, PythonExpressionRule, TestCaseRule
from spidermon.managers import RulesManager

from fixtures.rules import *


def test_rules():
    manager = RulesManager(RULES)
    _test_definitions(
        definitions=manager.definitions,
        values=(
            # (type,                class,                  level,                  name)
            ('rule',                SimpleRule,             settings.LEVEL_NORMAL,  'rule'),
            ('python_expression',   PythonExpressionRule,   settings.LEVEL_NORMAL,  'python_expression'),
            ('callable',            CallableRule,           settings.LEVEL_NORMAL,  '<lambda>'),
            ('callable',            CallableRule,           settings.LEVEL_NORMAL,  'a_function'),
            ('test_case',           TestCaseRule,           settings.LEVEL_NORMAL,  'ATestCase.test_method_a'),
            ('test_case',           TestCaseRule,           settings.LEVEL_NORMAL,  'ATestCase.test_method_b'),
        ),
    )


def test_rules_as_tuple2():
    manager = RulesManager(RULES_AS_TUPLE2)
    _test_definitions(
        definitions=manager.definitions,
        values=(
            # (type,                class,                  level,                  name)
            ('rule',                SimpleRule,             settings.LEVEL_NORMAL,  'RULE_OBJECT'),
            ('python_expression',   PythonExpressionRule,   settings.LEVEL_NORMAL,  'RULE_EXPRESSION'),
            ('callable',            CallableRule,           settings.LEVEL_NORMAL,  'RULE_LAMBDA'),
            ('callable',            CallableRule,           settings.LEVEL_NORMAL,  'RULE_FUNCTION'),
            ('test_case',           TestCaseRule,           settings.LEVEL_NORMAL,  'RULE_TESTCASE.test_method_a'),
            ('test_case',           TestCaseRule,           settings.LEVEL_NORMAL,  'RULE_TESTCASE.test_method_b'),
        ),
    )


def test_rules_as_tuple3():
    manager = RulesManager(RULES_AS_TUPLE3)
    _test_definitions(
        definitions=manager.definitions,
        values=(
            # (type,                class,                  level,                name)
            ('rule',                SimpleRule,             settings.LEVEL_HIGH,  'RULE_OBJECT'),
            ('python_expression',   PythonExpressionRule,   settings.LEVEL_HIGH,  'RULE_EXPRESSION'),
            ('callable',            CallableRule,           settings.LEVEL_HIGH,  'RULE_LAMBDA'),
            ('callable',            CallableRule,           settings.LEVEL_HIGH,  'RULE_FUNCTION'),
            ('test_case',           TestCaseRule,           settings.LEVEL_HIGH,  'RULE_TESTCASE.test_method_a'),
            ('test_case',           TestCaseRule,           settings.LEVEL_HIGH,  'RULE_TESTCASE.test_method_b'),
        ),
    )


def _test_definitions(definitions, values):
    for definition, rule_values in zip(definitions, values):
        rule_type, rule_class, rule_level, rule_name = rule_values
        assert isinstance(definition.rule, rule_class)
        assert rule_type == definition.type
        assert rule_level == definition.level
        assert rule_name == definition.name
