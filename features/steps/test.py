from behave import given, when, then
from utils.capitalize import up,down,cap


@given(u'The string gets uppercased')
def step_impl(context):
    pass


@when(u'I input "{inp_u}"')
def step_impl(context, inp_u):
    context.uppered = up(inp_u)


@then(u'I get "{out_u}"')
def step_impl(context, out_u):
    assert(context.uppered == out_u)


@given(u'The string gets lowercased')
def step_impl(context):
    pass


@when(u'I input "{inp_l}"')
def step_impl(context, inp_l):
    context.lowered = down(inp_l)


@then(u'I get "{out_l}"')
def step_impl(context, out_l):
    assert(context.lowered == out_l)


@given(u'The string gets capitalized')
def step_impl(context):
    pass


@when(u'I input "{inp_c}"')
def step_impl(context, inp_c):
    context.capitalized = down(inp_c)


@then(u'I get "{out_c}"')
def step_impl(context, out_c):
    assert(context.capitalized == out_c)
