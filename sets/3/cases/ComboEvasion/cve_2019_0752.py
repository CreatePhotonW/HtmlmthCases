from collections import deque, OrderedDict

from utils import TransformFunction
import evasions.html
import evasions.http


def get_cases(long_descriptions=False):
    cases = []

    cases.append(TransformFunction("ComboEvasion-null-001", None, evasions.http.null))
    cases.append(TransformFunction("ComboEvasion-combo-011", None,
                                   evasions.html.entity_encoding_attributes_dec,
                                   evasions.html.insert_slash_after_opening_tag_names,
                                   evasions.html.bom_declared_utf_16be_encoded_as_utf_16_be,
                                   evasions.http.status_code_4xx.parameterize(statuscode=414),
                                   evasions.http.contentencoding_deflate,
                                   evasions.http.encode_deflate_compression_max,
                                   evasions.http.transferencoding_chunked,
                                   evasions.http.encode_chunked_varysize_leadingzeros.parameterize(min_chunksize=16,
                                                                                                   max_chunksize=64,
                                                                                                   leadingzeros=15)))

    simple_index = len(cases)

    # description cleanup
    if not long_descriptions:
        TransformFunction.cleanup_descriptions(cases, simple_index)

    return OrderedDict([(c.name, c) for c in cases])
