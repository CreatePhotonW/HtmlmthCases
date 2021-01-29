from collections import deque, OrderedDict

from utils import TransformFunction
import evasions.http


def get_cases(long_descriptions=False):
    cases = []

    cases.append(TransformFunction("HttpEvasion-null-001", None, evasions.http.null))

    cases.append(TransformFunction("HttpEvasion-http-001", None, evasions.http.contentencoding_gzip, evasions.http.encode_gzip_compression_none))
    cases.append(TransformFunction("HttpEvasion-http-002", None, evasions.http.contentencoding_gzip, evasions.http.encode_gzip_compression_min))
    cases.append(TransformFunction("HttpEvasion-http-003", None, evasions.http.contentencoding_gzip, evasions.http.encode_gzip_compression_some))
    cases.append(TransformFunction("HttpEvasion-http-004", None, evasions.http.contentencoding_gzip, evasions.http.encode_gzip_compression_max))

    cases.append(TransformFunction("HttpEvasion-http-005", None, evasions.http.transferencoding_chunked, evasions.http.encode_chunked_equisize.parameterize(chunksize=32)))
    cases.append(TransformFunction("HttpEvasion-http-006", None, evasions.http.transferencoding_chunked, evasions.http.encode_chunked_equisize_leadingzeros.parameterize(chunksize=32, leadingzeros=10)))

    cases.append(TransformFunction("HttpEvasion-http-007", None, evasions.http.status_code_3xx.parameterize(statuscode=305)))

    cases.append(TransformFunction("HttpEvasion-http-500", None,
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
