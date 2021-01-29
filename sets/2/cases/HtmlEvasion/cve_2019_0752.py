from collections import deque, OrderedDict

from utils import TransformFunction
import evasions.html


def get_cases(long_descriptions=False):
    cases = []

    cases.append(TransformFunction("HtmlEvasion-null-001", None, evasions.html.null))
    cases.append(TransformFunction("HtmlEvasion-html-002", None, evasions.html.pad_body_with_div.parameterize(N=500000)))
    cases.append(TransformFunction("HtmlEvasion-html-010", None, evasions.html.insert_many_slash_after_html_opening_tag_name))
    cases.append(TransformFunction("HtmlEvasion-html-015", None, evasions.html.entity_encoding_attributes_hex))
    cases.append(TransformFunction("HtmlEvasion-html-020", None, evasions.html.external_resource_internal_script))
    cases.append(TransformFunction("HtmlEvasion-html-326", None, evasions.html.bom_declared_utf_7_variant_5_encoded_as_utf_7_5_i))

    cases.append(TransformFunction("HtmlEvasion-html-550", None, evasions.html.entity_encoding_attributes_hex, evasions.html.external_resource_internal_script, evasions.html.bom_declared_utf_7_variant_5_encoded_as_utf_7_5_i))

    simple_index = len(cases)

    # description cleanup
    if not long_descriptions:
        TransformFunction.cleanup_descriptions(cases, simple_index)

    return OrderedDict([(c.name, c) for c in cases])
