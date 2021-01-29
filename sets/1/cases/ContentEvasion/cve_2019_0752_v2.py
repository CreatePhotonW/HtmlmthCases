from collections import deque, OrderedDict

from utils import TransformFunction
import evasions.cve_2019_0752
import evasions.html


def get_cases(long_descriptions=False):
    case_basename = "ContentEvasion-content-"

    diverage_stack = deque()
    diverage_count_stack = deque()
    cases = []

    # singles/minimums
    cases.append(TransformFunction("ContentEvasion-null-001", None, evasions.cve_2019_0752.null))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_html_comments))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_vbscript_comments))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_html_tag))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_xuacompatible_value))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_Expires))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_div_container_id))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_div_content_id))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_div_content_string))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_container_width))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_content_width))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.change_trigger_to_scrollTop))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_div_html_with_javascript_createelement))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.set_vbscript_tag_language))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_xuacompatible))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_vbscript_open_tag_andreplace_with_document_write_js))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_ar1_size))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_ar2))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_addressOfGremlin))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_gremlin_existence_check))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.change_dictionary_entry))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.change_exists_string))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_on_error))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_cleanup))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_vtable_address))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_pld_address))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_pld_address, evasions.cve_2019_0752.winexecToSystem, evasions.cve_2019_0752.remove_powershell_comment))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_pld_address, evasions.cve_2019_0752.winexecToSystem, evasions.cve_2019_0752.remove_powershell_comment, evasions.cve_2019_0752.obfuscate_cmd_commandline))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_pld_address, evasions.cve_2019_0752.change_path_traversal))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.change_powershell_comment_Bs))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.replace_pld_address, evasions.cve_2019_0752.change_path_traversal, evasions.cve_2019_0752.remove_powershell_comment))

    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_vbscript_comments, evasions.cve_2019_0752.rename_variables))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_vbscript_comments, evasions.cve_2019_0752.reorder_functions))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_vbscript_comments, evasions.cve_2019_0752.vbscript_whitespace))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_vbscript_comments, evasions.cve_2019_0752.linesplit))
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_vbscript_comments, evasions.cve_2019_0752.stringsplit))
    # test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, remove_vbscript_comments, maths))

    simple_index = len(cases)

    # helper for later
    def CodeTransformCases(test_cases, diverage_stack, diverage_count_stack, test_case_basename=case_basename):
        # assumes that remove_vbscript_comments has already been applied
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.rename_variables))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.reorder_functions))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.vbscript_whitespace))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.linesplit))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.stringsplit))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        # test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], maths))
        # diverage_stack.append(test_cases[-1])
        # diverage_count_stack[-1] += 1

    def vbscriptCases(test_cases, diverage_stack, diverage_count_stack, test_case_basename=case_basename):
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.replace_ar1_size))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.remove_ar2))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.replace_addressOfGremlin))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.remove_gremlin_existence_check))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.change_dictionary_entry))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.change_exists_string))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.remove_on_error))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.remove_cleanup))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.replace_pld_address))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1

        diverage_count_stack.append(0)
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.change_powershell_comment_Bs))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        CodeTransformCases(test_cases, diverage_stack, diverage_count_stack, test_case_basename)

        for i in range(diverage_count_stack.pop()):
            diverage_stack.pop()
        diverage_count_stack.append(0)
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.winexecToSystem, evasions.cve_2019_0752.remove_powershell_comment))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.winexecToSystem, evasions.cve_2019_0752.remove_powershell_comment, evasions.cve_2019_0752.obfuscate_cmd_commandline))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        CodeTransformCases(test_cases, diverage_stack, diverage_count_stack, test_case_basename)

        for i in range(diverage_count_stack.pop()):
            diverage_stack.pop()
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.replace_vtable_address))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.change_path_traversal))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1
        test_cases.append(TransformFunction(test_case_basename + "{:03d}".format(len(test_cases)), None, diverage_stack[-1], evasions.cve_2019_0752.remove_powershell_comment))
        diverage_stack.append(test_cases[-1])
        diverage_count_stack[-1] += 1

        diverage_count_stack.append(0)
        CodeTransformCases(test_cases, diverage_stack, diverage_count_stack, test_case_basename)
        for i in range(diverage_count_stack.pop()):
            diverage_stack.pop()

    # frankensteins
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, evasions.cve_2019_0752.remove_html_comments, evasions.cve_2019_0752.remove_vbscript_comments))
    diverage_stack.append(cases[-1])

    diverage_count_stack.append(0)
    CodeTransformCases(cases, diverage_stack, diverage_count_stack)

    for i in range(diverage_count_stack.pop()):
        diverage_stack.pop()
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, diverage_stack[-1], evasions.cve_2019_0752.remove_html_tag)) # incompatibale with vbscript_whitespace in some cases?
    diverage_stack.append(cases[-1])
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, diverage_stack[-1], evasions.cve_2019_0752.replace_xuacompatible_value))
    diverage_stack.append(cases[-1])
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, diverage_stack[-1], evasions.cve_2019_0752.remove_Expires))
    diverage_stack.append(cases[-1])
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, diverage_stack[-1], evasions.cve_2019_0752.replace_div_container_id))
    diverage_stack.append(cases[-1])
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, diverage_stack[-1], evasions.cve_2019_0752.replace_div_content_id))
    diverage_stack.append(cases[-1])
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, diverage_stack[-1], evasions.cve_2019_0752.replace_div_content_string))
    diverage_stack.append(cases[-1])
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, diverage_stack[-1], evasions.cve_2019_0752.replace_container_width))
    diverage_stack.append(cases[-1])
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, diverage_stack[-1], evasions.cve_2019_0752.replace_content_width))
    diverage_stack.append(cases[-1])
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, diverage_stack[-1], evasions.cve_2019_0752.change_trigger_to_scrollTop))
    diverage_stack.append(cases[-1])
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, diverage_stack[-1], evasions.cve_2019_0752.replace_div_html_with_javascript_createelement))
    diverage_stack.append(cases[-1])
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, diverage_stack[-1], evasions.cve_2019_0752.set_vbscript_tag_language))
    diverage_stack.append(cases[-1])

    diverage_count_stack.append(0)
    CodeTransformCases(cases, diverage_stack, diverage_count_stack)

    for i in range(diverage_count_stack.pop()):
        diverage_stack.pop()
    diverage_count_stack.append(0)
    vbscriptCases(cases, diverage_stack, diverage_count_stack)

    for i in range(diverage_count_stack.pop()):
        diverage_stack.pop()
    diverage_count_stack.append(0)
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, diverage_stack[-1], evasions.cve_2019_0752.remove_vbscript_open_tag_andreplace_with_document_write_js))
    diverage_stack.append(cases[-1])
    diverage_count_stack[-1] += 1
    cases.append(TransformFunction(case_basename + "{:03d}".format(len(cases)), None, diverage_stack[-1], evasions.cve_2019_0752.remove_xuacompatible))
    diverage_stack.append(cases[-1])
    diverage_count_stack[-1] += 1
    vbscriptCases(cases, diverage_stack, diverage_count_stack, case_basename)

    # description cleanup
    if not long_descriptions:
        TransformFunction.cleanup_descriptions(cases, simple_index)

    return OrderedDict([(c.name, c) for c in cases])
