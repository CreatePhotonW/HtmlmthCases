from collections import deque, OrderedDict

from utils import TransformFunction
import evasions.html


def get_cases(long_descriptions=False):
    cases = []

    cases.append(TransformFunction("HtmlEvasion-null-001", None, evasions.html.null))
    cases.append(TransformFunction("HtmlEvasion-html-005", None, evasions.html.move_body_to_nested_div_with_children.parameterize(N=500, M=500000)))
    cases.append(TransformFunction("HtmlEvasion-html-009", None, evasions.html.insert_slash_after_opening_tag_names))
    cases.append(TransformFunction("HtmlEvasion-html-016", None, evasions.html.entity_encoding_attributes_dec))
    cases.append(TransformFunction("HtmlEvasion-html-315", None, evasions.html.bom_declared_utf_16be_encoded_as_utf_16_be))
    cases.append(TransformFunction("HtmlEvasion-html-551", None, evasions.html.entity_encoding_attributes_dec, evasions.html.external_resource_internal_script, evasions.html.insert_slash_after_opening_tag_names, evasions.html.bom_declared_utf_16be_encoded_as_utf_16_be))

    simple_index = len(cases)

    # description cleanup
    if not long_descriptions:
        TransformFunction.cleanup_descriptions(cases, simple_index)

    return OrderedDict([(c.name, c) for c in cases])
