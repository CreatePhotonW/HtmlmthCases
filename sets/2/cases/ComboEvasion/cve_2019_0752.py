from collections import deque, OrderedDict

from utils import TransformFunction
import evasions.html
import evasions.http


def get_cases(long_descriptions=False):
    cases = []

    cases.append(TransformFunction("ComboEvasion-null-001", None, evasions.http.null))
    cases.append(TransformFunction("ComboEvasion-combo-001", None,
                                   evasions.html.entity_encoding_attributes_hex,
                                   evasions.html.external_resource_internal_script,
                                   evasions.html.bom_declared_utf_7_variant_5_encoded_as_utf_7_5_i,
                                   evasions.http.status_code_3xx.parameterize(statuscode=305),
                                   evasions.http.contentencoding_gzip,
                                   evasions.http.encode_gzip_compression_max,
                                   evasions.http.transferencoding_chunked,
                                   evasions.http.encode_chunked_equisize_leadingzeros.parameterize(chunksize=32, leadingzeros=10)))

    simple_index = len(cases)

    # description cleanup
    if not long_descriptions:
        TransformFunction.cleanup_descriptions(cases, simple_index)

    return OrderedDict([(c.name, c) for c in cases])
