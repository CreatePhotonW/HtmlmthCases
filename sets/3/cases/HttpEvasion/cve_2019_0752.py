from collections import deque, OrderedDict

from utils import TransformFunction
import evasions.http


def get_cases(long_descriptions=False):
    cases = []

    cases.append(TransformFunction("HttpEvasion-null-001", None, evasions.http.null))

    cases.append(TransformFunction("HttpEvasion-http-011", None, evasions.http.contentencoding_deflate, evasions.http.encode_deflate_compression_none))
    cases.append(TransformFunction("HttpEvasion-http-012", None, evasions.http.contentencoding_deflate, evasions.http.encode_deflate_compression_min))
    cases.append(TransformFunction("HttpEvasion-http-013", None, evasions.http.contentencoding_deflate, evasions.http.encode_deflate_compression_some))
    cases.append(TransformFunction("HttpEvasion-http-014", None, evasions.http.contentencoding_deflate, evasions.http.encode_deflate_compression_max))

    cases.append(TransformFunction("HttpEvasion-http-015", None, evasions.http.transferencoding_chunked, evasions.http.encode_chunked_varysize.parameterize(min_chunksize=16, max_chunksize=64)))
    cases.append(TransformFunction("HttpEvasion-http-016", None, evasions.http.transferencoding_chunked, evasions.http.encode_chunked_varysize_leadingzeros.parameterize(min_chunksize=16, max_chunksize=64, leadingzeros=15)))

    cases.append(TransformFunction("HttpEvasion-http-017", None, evasions.http.status_code_4xx.parameterize(statuscode=414)))

    cases.append(TransformFunction("HttpEvasion-http-501", None,
                                   evasions.http.status_code_4xx.parameterize(statuscode=414),
                                   evasions.http.contentencoding_deflate,
                                   evasions.http.encode_deflate_compression_max,
                                   evasions.http.transferencoding_chunked,
                                   evasions.http.encode_chunked_varysize_leadingzeros.parameterize(min_chunksize=16, max_chunksize=64, leadingzeros=15)))

    simple_index = len(cases)

    # description cleanup
    if not long_descriptions:
        TransformFunction.cleanup_descriptions(cases, simple_index)

    return OrderedDict([(c.name, c) for c in cases])
