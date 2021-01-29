from collections import deque, OrderedDict

from utils import TransformFunction
import evasions.html


def get_cases(long_descriptions=False):
    cases = []

    # singles/minimums
    # html based evasions
    cases.append(TransformFunction("HtmlEvasion-null-001", None, evasions.html.null))
    cases.append(TransformFunction("HtmlEvasion-html-001", None, evasions.html.remove_html_comments))
    cases.append(TransformFunction("HtmlEvasion-html-002", None, evasions.html.pad_body_with_div)) # horizontal
    cases.append(TransformFunction("HtmlEvasion-html-003", None, evasions.html.move_body_to_nested_div)) # vertical
    cases.append(TransformFunction("HtmlEvasion-html-004", None, evasions.html.move_body_to_nested_div_pad_children_in_last_one.parameterize(N=950))) # vertical then horizontal
    cases.append(TransformFunction("HtmlEvasion-html-005", None, evasions.html.move_body_to_nested_div_with_children.parameterize(N=1041, M=1000000))) # vertical then tree
    cases.append(TransformFunction("HtmlEvasion-html-006", None, evasions.html.xua_meta_change_value_8))
    cases.append(TransformFunction("HtmlEvasion-html-007", None, evasions.html.xua_meta_change_value_8, evasions.html.script_language_add_encode))
    cases.append(TransformFunction("HtmlEvasion-html-008", None, evasions.html.xua_meta_change_value_8, evasions.html.script_language_add_encode, evasions.html.encoded_script))

    cases.append(TransformFunction("HtmlEvasion-html-009", None, evasions.html.insert_slash_after_opening_tag_names))
    cases.append(TransformFunction("HtmlEvasion-html-010", None, evasions.html.insert_many_slash_after_html_opening_tag_name))
    cases.append(TransformFunction("HtmlEvasion-html-011", None, evasions.html.insert_many_slash_after_opening_tag_names.parameterize(N=783)))

    cases.append(TransformFunction("HtmlEvasion-html-012", None, evasions.html.attributes_reverse))
    cases.append(TransformFunction("HtmlEvasion-html-013", None, evasions.html.attributes_insert_newlines))
    cases.append(TransformFunction("HtmlEvasion-html-014", None, evasions.html.attributes_insert_many_newlines.parameterize(multiplier=30)))

    cases.append(TransformFunction("HtmlEvasion-html-015", None, evasions.html.entity_encoding_attributes_hex))
    cases.append(TransformFunction("HtmlEvasion-html-016", None, evasions.html.entity_encoding_attributes_dec))
    cases.append(TransformFunction("HtmlEvasion-html-017", None, evasions.html.entity_encoding_attributes_mix))

    cases.append(TransformFunction("HtmlEvasion-html-018", None, evasions.html.remove_content_type_http_equiv_meta))
    cases.append(TransformFunction("HtmlEvasion-html-019", None, evasions.html.xua_move_meta_to_headers))

    cases.append(TransformFunction("HtmlEvasion-html-020", None, evasions.html.external_resource_internal_script))

    # cases.append(TransformFunction("HtmlEvasion-html-021", None, evasions.html.data_url_internal_script_url_gen_no_b64_declare_b64_encode_data_percent_encode_data))
    # cases.append(TransformFunction("HtmlEvasion-html-022", None, evasions.html.data_url_internal_script_url_gen_no_b64_declare_b64_encode_data_percent_encode_data_min))
    # cases.append(TransformFunction("HtmlEvasion-html-023", None, evasions.html.data_url_internal_script_url_gen_nonstd_b64_declare_b64_encode_data_percent_encode_data))
    # cases.append(TransformFunction("HtmlEvasion-html-024", None, evasions.html.data_url_internal_script_url_gen_nonstd_b64_declare_b64_encode_data_percent_encode_data_no))
    # cases.append(TransformFunction("HtmlEvasion-html-025", None, evasions.html.data_url_internal_script_url_gen_nonstd_b64_declare_b64_encode_data_percent_encode_url))
    # cases.append(TransformFunction("HtmlEvasion-html-026", None, evasions.html.data_url_internal_script_url_gen_std_b64_declare_b64_encode_data_percent_encode_data))
    # cases.append(TransformFunction("HtmlEvasion-html-027", None, evasions.html.data_url_internal_script_url_gen_std_b64_declare_b64_encode_data_percent_encode_data_no))
    # cases.append(TransformFunction("HtmlEvasion-html-028", None, evasions.html.data_url_internal_script_url_gen_std_b64_declare_b64_encode_data_percent_encode_url))

    # Content-Type based evasions
    cases.append(TransformFunction("HtmlEvasion-html-100", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_no_type))
    cases.append(TransformFunction("HtmlEvasion-html-101", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_text_html))
    # cases.append(TransformFunction("HtmlEvasion-html-102", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_text_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-103", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_application_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-104", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_application_xhtml_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-105", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_image_svg_xml))

    # cases.append(TransformFunction("HtmlEvasion-html-106", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.convert_to_xhtml_http_declared_no_type_inferred_html))
    # cases.append(TransformFunction("HtmlEvasion-html-107", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.convert_to_xhtml_http_declared_text_html_inferred_html))
    # cases.append(TransformFunction("HtmlEvasion-html-108", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.convert_to_xhtml_http_declared_text_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-109", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.convert_to_xhtml_http_declared_application_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-110", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.convert_to_xhtml_http_declared_application_xhtml_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-111", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.convert_to_xhtml_http_declared_image_svg_xml))

    cases.append(TransformFunction("HtmlEvasion-html-112", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_html, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_no_type))
    cases.append(TransformFunction("HtmlEvasion-html-113", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_html, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_text_html))
    # cases.append(TransformFunction("HtmlEvasion-html-114", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_html, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_text_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-115", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_html, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_application_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-116", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_html, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_application_xhtml_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-117", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_html, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_image_svg_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-118", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_html, evasions.html.convert_to_xhtml_http_declared_no_type_inferred_html))
    # cases.append(TransformFunction("HtmlEvasion-html-119", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_html, evasions.html.convert_to_xhtml_http_declared_text_html_inferred_html))
    # cases.append(TransformFunction("HtmlEvasion-html-120", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_html, evasions.html.convert_to_xhtml_http_declared_text_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-121", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_html, evasions.html.convert_to_xhtml_http_declared_application_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-122", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_html, evasions.html.convert_to_xhtml_http_declared_application_xhtml_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-123", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_html, evasions.html.convert_to_xhtml_http_declared_image_svg_xml))

    cases.append(TransformFunction("HtmlEvasion-html-124", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_xml, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_no_type))
    cases.append(TransformFunction("HtmlEvasion-html-125", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_xml, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_text_html))
    # cases.append(TransformFunction("HtmlEvasion-html-126", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_xml, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_text_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-127", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_xml, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_application_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-128", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_xml, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_application_xhtml_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-129", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_xml, evasions.html.convert_to_xhtml_no_xml_tag_http_declared_image_svg_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-130", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_xml, evasions.html.convert_to_xhtml_http_declared_no_type_inferred_html))
    # cases.append(TransformFunction("HtmlEvasion-html-131", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_xml, evasions.html.convert_to_xhtml_http_declared_text_html_inferred_html))
    # cases.append(TransformFunction("HtmlEvasion-html-132", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_xml, evasions.html.convert_to_xhtml_http_declared_text_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-133", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_xml, evasions.html.convert_to_xhtml_http_declared_application_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-134", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_xml, evasions.html.convert_to_xhtml_http_declared_application_xhtml_xml))
    # cases.append(TransformFunction("HtmlEvasion-html-135", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.meta_declared_text_xml, evasions.html.convert_to_xhtml_http_declared_image_svg_xml))

    # End Content-Type based evasions

    ##### xml based evasions
    # mix of singles and combos
    # parsed_as_xml_case = TransformFunction("", None, evasions.html.remove_content_type_http_equiv_meta, evasions.html.convert_to_xhtml_http_declared_text_xml)
    # cases.append(TransformFunction("HtmlEvasion-html-200", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_dec))
    # cases.append(TransformFunction("HtmlEvasion-html-201", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_hex))
    # cases.append(TransformFunction("HtmlEvasion-html-202", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_mix))
    # cases.append(TransformFunction("HtmlEvasion-html-203", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-204", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities))
    # cases.append(TransformFunction("HtmlEvasion-html-205", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_cdata_dec))
    # cases.append(TransformFunction("HtmlEvasion-html-206", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_cdata_hex))
    # cases.append(TransformFunction("HtmlEvasion-html-207", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_cdata_mix))
    # cases.append(TransformFunction("HtmlEvasion-html-208", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_cdata_cdata))
    # cases.append(TransformFunction("HtmlEvasion-html-209", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_cdata_internal_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-210", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_cdata_internal_entities))
    # cases.append(TransformFunction("HtmlEvasion-html-211", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_mix,
    #                                evasions.html.entity_encoding_cdata_mix))
    # cases.append(TransformFunction("HtmlEvasion-html-212", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_cdata_internal_entities))
    # cases.append(TransformFunction("HtmlEvasion-html-213", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_root_internal_entity))
    #
    # cases.append(TransformFunction("HtmlEvasion-html-214", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-215", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-216", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_cdata_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-217", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_cdata_internal_entities,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    # # cases.append(TransformFunction("HtmlEvasion-html-200", None, parsed_as_xml_case, evasions.html.entity_encoding_attributes_internal_entities, evasions.html.entity_encoding_cdata_internal_entities, evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity)) # crashes IE
    # cases.append(TransformFunction("HtmlEvasion-html-218", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    #
    # cases.append(TransformFunction("HtmlEvasion-html-219", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity,
    #                                evasions.html.entity_encoding_internal_parameter_entity_declaration_nested_internal_parameter_entities))
    #
    # cases.append(TransformFunction("HtmlEvasion-html-220", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-221", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_cdata_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-222", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_cdata_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity))
    #
    # cases.append(TransformFunction("HtmlEvasion-html-223", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_cdata_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_mix))
    #
    # cases.append(TransformFunction("HtmlEvasion-html-224", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_cdata_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_mix,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity.parameterize(
    #                                    min_value_length=2)
    #                                ))
    #
    # cases.append(TransformFunction("HtmlEvasion-html-225", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_cdata_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_mix,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity.parameterize(
    #                                    min_value_length=2),
    #                                evasions.html.entity_encoding_internal_parameter_entity_declaration_nested_internal_parameter_entities.parameterize(
    #                                    number_of_nested=99730)
    #                                ))
    #
    # cases.append(TransformFunction("HtmlEvasion-html-226", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_cdata_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_mix,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity.parameterize(
    #                                    min_value_length=2),
    #                                evasions.html.entity_encoding_internal_parameter_entity_declaration_nested_internal_parameter_entities.parameterize(
    #                                    number_of_nested=99730),
    #                                evasions.html.entity_encoding_internal_parameter_entity_declaration_mix
    #                                ))
    ##### End xml based evasions

    ##### Encoding based minimal cases

    # declaring (header or BOM) as utf8/utf7 and sending as utf16le/utf16be -> infinite loop? (except when utf8 BOM + utf16le encoding)
    cases.append(TransformFunction("HtmlEvasion-html-300", None, evasions.html.no_declared_encoding_encoded_as_utf_8))
    cases.append(TransformFunction("HtmlEvasion-html-301", None, evasions.html.no_declared_encoding_encoded_as_utf_16_le))
    cases.append(TransformFunction("HtmlEvasion-html-302", None, evasions.html.http_declared_utf_8_encoded_as_utf_8))
    cases.append(TransformFunction("HtmlEvasion-html-303", None, evasions.html.http_declared_utf_16be_encoded_as_utf_16_be))
    cases.append(TransformFunction("HtmlEvasion-html-304", None, evasions.html.http_declared_utf_16_encoded_as_utf_16_le))
    cases.append(TransformFunction("HtmlEvasion-html-305", None, evasions.html.http_declared_utf_16le_encoded_as_utf_16_le))
    cases.append(TransformFunction("HtmlEvasion-html-306", None, evasions.html.http_declared_utf_7_encoded_as_utf_7_0))
    cases.append(TransformFunction("HtmlEvasion-html-307", None, evasions.html.http_declared_utf_7_encoded_as_utf_7_1))
    cases.append(TransformFunction("HtmlEvasion-html-308", None, evasions.html.http_declared_utf_7_encoded_as_utf_7_2))
    cases.append(TransformFunction("HtmlEvasion-html-309", None, evasions.html.http_declared_utf_7_encoded_as_utf_7_3))
    cases.append(TransformFunction("HtmlEvasion-html-310", None, evasions.html.http_declared_utf_7_encoded_as_utf_7_4))
    cases.append(TransformFunction("HtmlEvasion-html-311", None, evasions.html.http_declared_utf_7_encoded_as_utf_7_5))
    cases.append(TransformFunction("HtmlEvasion-html-312", None, evasions.html.http_declared_utf_7_encoded_as_utf_7_5_i))
    cases.append(TransformFunction("HtmlEvasion-html-313", None, evasions.html.bom_declared_utf_8_encoded_as_utf_8))
    # cases.append(TransformFunction("HtmlEvasion-html-314", None, evasions.html.bom_declared_utf_8_encoded_as_utf_16_le))
    cases.append(TransformFunction("HtmlEvasion-html-315", None, evasions.html.bom_declared_utf_16be_encoded_as_utf_16_be))
    cases.append(TransformFunction("HtmlEvasion-html-316", None, evasions.html.bom_declared_utf_16le_encoded_as_utf_16_le))
    # all BOM utf7 [1,5] + encode utf_7 [0, 5i] all work, but only doing a subset so reduce number of cases
    cases.append(TransformFunction("HtmlEvasion-html-317", None, evasions.html.bom_declared_utf_7_variant_1_encoded_as_utf_7_3))
    cases.append(TransformFunction("HtmlEvasion-html-318", None, evasions.html.bom_declared_utf_7_variant_2_encoded_as_utf_7_3))
    cases.append(TransformFunction("HtmlEvasion-html-319", None, evasions.html.bom_declared_utf_7_variant_3_encoded_as_utf_7_3))
    cases.append(TransformFunction("HtmlEvasion-html-320", None, evasions.html.bom_declared_utf_7_variant_4_encoded_as_utf_7_3))
    cases.append(TransformFunction("HtmlEvasion-html-321", None, evasions.html.bom_declared_utf_7_variant_5_encoded_as_utf_7_3))
    cases.append(TransformFunction("HtmlEvasion-html-322", None, evasions.html.bom_declared_utf_7_variant_1_encoded_as_utf_7_5_i))
    cases.append(TransformFunction("HtmlEvasion-html-323", None, evasions.html.bom_declared_utf_7_variant_2_encoded_as_utf_7_5_i))
    cases.append(TransformFunction("HtmlEvasion-html-324", None, evasions.html.bom_declared_utf_7_variant_3_encoded_as_utf_7_5_i))
    cases.append(TransformFunction("HtmlEvasion-html-325", None, evasions.html.bom_declared_utf_7_variant_4_encoded_as_utf_7_5_i))
    cases.append(TransformFunction("HtmlEvasion-html-326", None, evasions.html.bom_declared_utf_7_variant_5_encoded_as_utf_7_5_i))

    # # IE mode <= 9: BOM has precedence over HTTP declaration (except when BOM = UTF-7 apparently, weird stuff happens)
    base = TransformFunction("", None, evasions.html.xua_meta_change_value_8, evasions.html.xua_move_meta_to_headers)
    cases.append(TransformFunction("HtmlEvasion-html-327", None, base, evasions.html.http_declared_utf_16_bom_declared_utf_8_encoded_as_utf_8))
    cases.append(TransformFunction("HtmlEvasion-html-328", None, base, evasions.html.http_declared_utf_16be_bom_declared_utf_8_encoded_as_utf_8))
    cases.append(TransformFunction("HtmlEvasion-html-329", None, base, evasions.html.http_declared_utf_16le_bom_declared_utf_8_encoded_as_utf_8))
    cases.append(TransformFunction("HtmlEvasion-html-330", None, base, evasions.html.http_declared_utf_7_bom_declared_utf_8_encoded_as_utf_8))
    cases.append(TransformFunction("HtmlEvasion-html-331", None, base, evasions.html.http_declared_utf_16be_bom_declared_utf_8_encoded_as_utf_16_le))
    cases.append(TransformFunction("HtmlEvasion-html-332", None, base, evasions.html.http_declared_utf_7_bom_declared_utf_8_encoded_as_utf_16_le))
    cases.append(TransformFunction("HtmlEvasion-html-333", None, base, evasions.html.http_declared_utf_8_bom_declared_utf_16be_encoded_as_utf_16_be))
    cases.append(TransformFunction("HtmlEvasion-html-334", None, base, evasions.html.http_declared_utf_16_bom_declared_utf_16be_encoded_as_utf_16_be))
    cases.append(TransformFunction("HtmlEvasion-html-335", None, base, evasions.html.http_declared_utf_16le_bom_declared_utf_16be_encoded_as_utf_16_be))
    cases.append(TransformFunction("HtmlEvasion-html-336", None, base, evasions.html.http_declared_utf_7_bom_declared_utf_16be_encoded_as_utf_16_be))
    cases.append(TransformFunction("HtmlEvasion-html-337", None, base, evasions.html.http_declared_utf_8_bom_declared_utf_16le_encoded_as_utf_16_le))
    cases.append(TransformFunction("HtmlEvasion-html-338", None, base, evasions.html.http_declared_utf_16be_bom_declared_utf_16le_encoded_as_utf_16_le))
    cases.append(TransformFunction("HtmlEvasion-html-339", None, base, evasions.html.http_declared_utf_7_bom_declared_utf_16le_encoded_as_utf_16_le))

    cases.append(TransformFunction("HtmlEvasion-html-340", None, base, evasions.html.http_declared_utf_8_bom_declared_utf_7_variant_1_encoded_as_utf_8))
    cases.append(TransformFunction("HtmlEvasion-html-341", None, base, evasions.html.http_declared_utf_8_bom_declared_utf_7_variant_1_encoded_as_utf_16_le))
    cases.append(TransformFunction("HtmlEvasion-html-342", None, base, evasions.html.http_declared_utf_8_bom_declared_utf_7_variant_1_encoded_as_utf_16_be))
    cases.append(TransformFunction("HtmlEvasion-html-343", None, base, evasions.html.http_declared_utf_16_bom_declared_utf_7_variant_1_encoded_as_utf_16_le))
    cases.append(TransformFunction("HtmlEvasion-html-344", None, base, evasions.html.http_declared_utf_16be_bom_declared_utf_7_variant_1_encoded_as_utf_16_be))
    cases.append(TransformFunction("HtmlEvasion-html-345", None, base, evasions.html.http_declared_utf_16le_bom_declared_utf_7_variant_1_encoded_as_utf_16_le))
    cases.append(TransformFunction("HtmlEvasion-html-346", None, base, evasions.html.http_declared_utf_8_bom_declared_utf_7_variant_5_encoded_as_utf_8))
    cases.append(TransformFunction("HtmlEvasion-html-347", None, base, evasions.html.http_declared_utf_8_bom_declared_utf_7_variant_5_encoded_as_utf_16_le))
    cases.append(TransformFunction("HtmlEvasion-html-348", None, base, evasions.html.http_declared_utf_8_bom_declared_utf_7_variant_5_encoded_as_utf_16_be))
    cases.append(TransformFunction("HtmlEvasion-html-349", None, base, evasions.html.http_declared_utf_16_bom_declared_utf_7_variant_5_encoded_as_utf_16_be))
    cases.append(TransformFunction("HtmlEvasion-html-350", None, base, evasions.html.http_declared_utf_16be_bom_declared_utf_7_variant_5_encoded_as_utf_16_le))
    cases.append(TransformFunction("HtmlEvasion-html-351", None, base, evasions.html.http_declared_utf_16le_bom_declared_utf_7_variant_5_encoded_as_utf_16_be))

    # IE mode > 9: HTTP declaration has precedence over BOM
    # base = TransformFunction("", None, evasions.html.xua_meta_change_value_10, evasions.html.xua_move_meta_to_headers)
    # cases.append(TransformFunction("HtmlEvasion-html-360", None, base, evasions.html.http_declared_utf_8_bom_declared_utf_16le_encoded_as_utf_8))
    # cases.append(TransformFunction("HtmlEvasion-html-361", None, base, evasions.html.http_declared_utf_8_bom_declared_utf_16be_encoded_as_utf_8))
    # cases.append(TransformFunction("HtmlEvasion-html-362", None, base, evasions.html.http_declared_utf_8_bom_declared_utf_7_variant_1_encoded_as_utf_8))
    # cases.append(TransformFunction("HtmlEvasion-html-363", None, base, evasions.html.http_declared_utf_8_bom_declared_utf_7_variant_5_encoded_as_utf_8))
    # cases.append(TransformFunction("HtmlEvasion-html-364", None, base, evasions.html.http_declared_utf_16_bom_declared_utf_16be_encoded_as_utf_16_le))
    # cases.append(TransformFunction("HtmlEvasion-html-365", None, base, evasions.html.http_declared_utf_16_bom_declared_utf_8_encoded_as_utf_16_le))
    # cases.append(TransformFunction("HtmlEvasion-html-366", None, base, evasions.html.http_declared_utf_16_bom_declared_utf_7_variant_1_encoded_as_utf_16_le))
    # cases.append(TransformFunction("HtmlEvasion-html-367", None, base, evasions.html.http_declared_utf_16_bom_declared_utf_7_variant_5_encoded_as_utf_16_be))
    # cases.append(TransformFunction("HtmlEvasion-html-368", None, base, evasions.html.http_declared_utf_16le_bom_declared_utf_16be_encoded_as_utf_16_le))
    # cases.append(TransformFunction("HtmlEvasion-html-369", None, base, evasions.html.http_declared_utf_16le_bom_declared_utf_8_encoded_as_utf_16_le))
    # cases.append(TransformFunction("HtmlEvasion-html-370", None, base, evasions.html.http_declared_utf_16le_bom_declared_utf_7_variant_1_encoded_as_utf_16_le))
    # cases.append(TransformFunction("HtmlEvasion-html-371", None, base, evasions.html.http_declared_utf_16le_bom_declared_utf_7_variant_5_encoded_as_utf_16_be))
    # cases.append(TransformFunction("HtmlEvasion-html-372", None, base, evasions.html.http_declared_utf_16be_bom_declared_utf_16le_encoded_as_utf_16_be))
    # cases.append(TransformFunction("HtmlEvasion-html-373", None, base, evasions.html.http_declared_utf_16be_bom_declared_utf_8_encoded_as_utf_16_be))
    # cases.append(TransformFunction("HtmlEvasion-html-374", None, base, evasions.html.http_declared_utf_16be_bom_declared_utf_7_variant_1_encoded_as_utf_16_be))
    # cases.append(TransformFunction("HtmlEvasion-html-375", None, base, evasions.html.http_declared_utf_16be_bom_declared_utf_7_variant_5_encoded_as_utf_16_le))
    # cases.append(TransformFunction("HtmlEvasion-html-376", None, base, evasions.html.http_declared_utf_7_bom_declared_utf_16le_encoded_as_utf_7_5_i))
    # cases.append(TransformFunction("HtmlEvasion-html-377", None, base, evasions.html.http_declared_utf_7_bom_declared_utf_16be_encoded_as_utf_7_5_i))
    # cases.append(TransformFunction("HtmlEvasion-html-378", None, base, evasions.html.http_declared_utf_7_bom_declared_utf_8_encoded_as_utf_7_5_i))
    #
    ##### End Encoding based minimal cases

    simple_index = len(cases)


    ################### All combos

    ################## IE = 8 combo path
    base = evasions.html.remove_html_comments
    cases.append(TransformFunction("HtmlEvasion-html-500", None, base, evasions.html.remove_content_type_http_equiv_meta))
    cases.append(TransformFunction("HtmlEvasion-html-501", None, cases[-1], evasions.html.xua_meta_change_value_8))
    cases.append(TransformFunction("HtmlEvasion-html-502", None, cases[-1], evasions.html.xua_move_meta_to_headers))
    cases.append(TransformFunction("HtmlEvasion-html-503", None, cases[-1], evasions.html.script_language_add_encode))
    cases.append(TransformFunction("HtmlEvasion-html-504", None, cases[-1], evasions.html.encoded_script))
    base = cases[-1]
    # path1
    cases.append(TransformFunction("HtmlEvasion-html-505", None, cases[-1], evasions.html.external_resource_internal_script))
    cases.append(TransformFunction("HtmlEvasion-html-506", None, cases[-1], evasions.html.attributes_reverse))
    cases.append(TransformFunction("HtmlEvasion-html-507", None, cases[-1], evasions.html.meta_declared_text_xml))
    cases.append(TransformFunction("HtmlEvasion-html-508", None, cases[-1], evasions.html.convert_to_xhtml_http_declared_no_type_inferred_html))
    cases.append(TransformFunction("HtmlEvasion-html-509", None, cases[-1], evasions.html.attributes_insert_many_newlines.parameterize(multiplier=30)))
    cases.append(TransformFunction("HtmlEvasion-html-510", None, cases[-1], evasions.html.entity_encoding_attributes_mix))
    cases.append(TransformFunction("HtmlEvasion-html-511", None, cases[-1], evasions.html.insert_many_slash_after_opening_tag_names.parameterize(N=783)))
    cases.append(TransformFunction("HtmlEvasion-html-512", None, cases[-1], evasions.html.http_declared_utf_7_bom_declared_utf_16be_encoded_as_utf_16_be))
    # path2
    cases.append(TransformFunction("HtmlEvasion-html-513", None, base, evasions.html.attributes_reverse))
    cases.append(TransformFunction("HtmlEvasion-html-514", None, cases[-1], evasions.html.meta_declared_text_xml))
    cases.append(TransformFunction("HtmlEvasion-html-515", None, cases[-1], evasions.html.attributes_insert_many_newlines.parameterize(multiplier=30)))
    cases.append(TransformFunction("HtmlEvasion-html-516", None, cases[-1], evasions.html.entity_encoding_attributes_mix))
    cases.append(TransformFunction("HtmlEvasion-html-517", None, cases[-1], evasions.html.move_body_to_nested_div))
    cases.append(TransformFunction("HtmlEvasion-html-518", None, cases[-1], evasions.html.http_declared_utf_8_bom_declared_utf_7_variant_5_encoded_as_utf_16_le))

    ##################


    ###################  IE = 9 combo path
    # data url path
    # base = TransformFunction("", None, evasions.html.remove_html_comments, evasions.html.remove_content_type_http_equiv_meta)
    # cases.append(TransformFunction("HtmlEvasion-html-600", None, base, evasions.html.xua_meta_change_value_9))
    # cases.append(TransformFunction("HtmlEvasion-html-601", None, base, evasions.html.xua_move_meta_to_headers))
    # cases.append(TransformFunction("HtmlEvasion-html-602", None, cases[-1], evasions.html.data_url_internal_script_url_gen_nonstd_b64_declare_b64_encode_data_percent_encode_url))
    # cases.append(TransformFunction("HtmlEvasion-html-603", None, cases[-1], evasions.html.attributes_reverse))
    # cases.append(TransformFunction("HtmlEvasion-html-604", None, cases[-1], evasions.html.meta_declared_text_html))
    # cases.append(TransformFunction("HtmlEvasion-html-605", None, cases[-1], evasions.html.convert_to_xhtml_http_declared_image_svg_xml))
    # parsed_as_xml_case = cases[-1]
    # # XML case path
    # cases.append(TransformFunction("HtmlEvasion-html-606", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_dec))
    # cases.append(TransformFunction("HtmlEvasion-html-607", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_hex))
    # cases.append(TransformFunction("HtmlEvasion-html-608", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_mix))
    # cases.append(TransformFunction("HtmlEvasion-html-609", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-610", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities))
    # # cases.append(TransformFunction("HtmlEvasion-html-611", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_dec))
    # # cases.append(TransformFunction("HtmlEvasion-html-612", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_hex))
    # # cases.append(TransformFunction("HtmlEvasion-html-613", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_mix))
    # # cases.append(TransformFunction("HtmlEvasion-html-614", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_cdata))
    # # cases.append(TransformFunction("HtmlEvasion-html-615", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_internal_entity))
    # # cases.append(TransformFunction("HtmlEvasion-html-616", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_internal_entities))
    # # cases.append(TransformFunction("HtmlEvasion-html-617", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_attributes_mix,
    # #                                evasions.html.entity_encoding_cdata_mix))
    # # cases.append(TransformFunction("HtmlEvasion-html-618", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_attributes_internal_entities,
    # #                                evasions.html.entity_encoding_cdata_internal_entities))
    # cases.append(TransformFunction("HtmlEvasion-html-619", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_root_internal_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-620", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-621", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    # # cases.append(TransformFunction("HtmlEvasion-html-622", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_internal_entity,
    # #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    # # cases.append(TransformFunction("HtmlEvasion-html-623", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_internal_entities,
    # #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    # # cases.append(TransformFunction("HtmlEvasion-html-624", None, parsed_as_xml_case, evasions.html.entity_encoding_attributes_internal_entities, evasions.html.entity_encoding_cdata_internal_entities, evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity)) # crashes IE
    # cases.append(TransformFunction("HtmlEvasion-html-625", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-626", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity,
    #                                evasions.html.entity_encoding_internal_parameter_entity_declaration_nested_internal_parameter_entities))
    # cases.append(TransformFunction("HtmlEvasion-html-627", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity))
    # # cases.append(TransformFunction("HtmlEvasion-html-628", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_internal_entities,
    # #                                evasions.html.entity_encoding_root_internal_entity))
    # # cases.append(TransformFunction("HtmlEvasion-html-629", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_attributes_internal_entities,
    # #                                evasions.html.entity_encoding_cdata_internal_entities,
    # #                                evasions.html.entity_encoding_root_internal_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-630", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_cdata_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_mix))
    # cases.append(TransformFunction("HtmlEvasion-html-631", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_cdata_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_mix,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity.parameterize(
    #                                    min_value_length=2)
    #                                ))
    # cases.append(TransformFunction("HtmlEvasion-html-632", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_cdata_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_mix,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity.parameterize(
    #                                    min_value_length=2),
    #                                evasions.html.entity_encoding_internal_parameter_entity_declaration_nested_internal_parameter_entities.parameterize(
    #                                    number_of_nested=99730)
    #                                ))
    # # data url + ... + entity_encoding_internal_parameter_entity_declaration_mix -> too large value ?
    # # cases.append(TransformFunction("HtmlEvasion-html-633", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_attributes_internal_entities,
    # #                                evasions.html.entity_encoding_cdata_internal_entities,
    # #                                evasions.html.entity_encoding_root_internal_entity,
    # #                                evasions.html.entity_encoding_internal_entity_declaration_mix,
    # #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity.parameterize(
    # #                                    min_value_length=2),
    # #                                evasions.html.entity_encoding_internal_parameter_entity_declaration_nested_internal_parameter_entities.parameterize(
    # #                                    number_of_nested=99730),
    # #                                evasions.html.entity_encoding_internal_parameter_entity_declaration_mix
    # #                                ))
    # cases.append(TransformFunction("HtmlEvasion-html-634", None, cases[-1], evasions.html.http_declared_utf_16be_bom_declared_utf_8_encoded_as_utf_8))
    #

    ###################




    ################## IE = 10 combo path
    # base = TransformFunction("", None, evasions.html.remove_html_comments, evasions.html.remove_content_type_http_equiv_meta)
    # cases.append(TransformFunction("HtmlEvasion-html-700", None, base, evasions.html.xua_meta_change_value_10))
    # cases.append(TransformFunction("HtmlEvasion-html-701", None, base, evasions.html.xua_move_meta_to_headers))
    # cases.append(TransformFunction("HtmlEvasion-html-702", None, cases[-1], evasions.html.external_resource_internal_script))
    # cases.append(TransformFunction("HtmlEvasion-html-703", None, cases[-1], evasions.html.meta_declared_text_html))
    # cases.append(TransformFunction("HtmlEvasion-html-704", None, cases[-1], evasions.html.attributes_reverse))
    # base = cases[-1]
    # # path 1 (html)
    # cases.append(TransformFunction("HtmlEvasion-html-705", None, cases[-1], evasions.html.attributes_insert_many_newlines.parameterize(multiplier=30)))
    # cases.append(TransformFunction("HtmlEvasion-html-706", None, cases[-1], evasions.html.entity_encoding_attributes_mix))
    # cases.append(TransformFunction("HtmlEvasion-html-707", None, cases[-1], evasions.html.move_body_to_nested_div_with_children.parameterize(N=1041, M=1000000)))
    # cases.append(TransformFunction("HtmlEvasion-html-708", None, cases[-1], evasions.html.http_declared_utf_7_bom_declared_utf_16be_encoded_as_utf_7_5_i))
    #
    # # path 2 (xml)
    # cases.append(TransformFunction("HtmlEvasion-html-709", None, base, evasions.html.convert_to_xhtml_http_declared_application_xhtml_xml))
    # parsed_as_xml_case = cases[-1]
    # cases.append(TransformFunction("HtmlEvasion-html-710", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_dec))
    # cases.append(TransformFunction("HtmlEvasion-html-711", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_hex))
    # cases.append(TransformFunction("HtmlEvasion-html-712", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_mix))
    # cases.append(TransformFunction("HtmlEvasion-html-713", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-714", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities))
    # # cases.append(TransformFunction("HtmlEvasion-html-715", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_dec))
    # # cases.append(TransformFunction("HtmlEvasion-html-716", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_hex))
    # # cases.append(TransformFunction("HtmlEvasion-html-717", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_mix))
    # # cases.append(TransformFunction("HtmlEvasion-html-718", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_cdata))
    # # cases.append(TransformFunction("HtmlEvasion-html-719", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_internal_entity))
    # # cases.append(TransformFunction("HtmlEvasion-html-720", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_internal_entities))
    # # cases.append(TransformFunction("HtmlEvasion-html-721", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_attributes_mix,
    # #                                evasions.html.entity_encoding_cdata_mix))
    # # cases.append(TransformFunction("HtmlEvasion-html-722", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_attributes_internal_entities,
    # #                                evasions.html.entity_encoding_cdata_internal_entities))
    # cases.append(TransformFunction("HtmlEvasion-html-723", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_root_internal_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-724", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-725", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    # # cases.append(TransformFunction("HtmlEvasion-html-726", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_internal_entity,
    # #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    # # cases.append(TransformFunction("HtmlEvasion-html-727", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_internal_entities,
    # #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    # # cases.append(TransformFunction("HtmlEvasion-html-728", None, parsed_as_xml_case, evasions.html.entity_encoding_attributes_internal_entities, evasions.html.entity_encoding_cdata_internal_entities, evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity)) # crashes IE
    # cases.append(TransformFunction("HtmlEvasion-html-729", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-730", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity,
    #                                evasions.html.entity_encoding_internal_parameter_entity_declaration_nested_internal_parameter_entities))
    # cases.append(TransformFunction("HtmlEvasion-html-731", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity))
    # # cases.append(TransformFunction("HtmlEvasion-html-732", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_cdata_internal_entities,
    # #                                evasions.html.entity_encoding_root_internal_entity))
    # # cases.append(TransformFunction("HtmlEvasion-html-733", None, parsed_as_xml_case,
    # #                                evasions.html.entity_encoding_attributes_internal_entities,
    # #                                evasions.html.entity_encoding_cdata_internal_entities,
    # #                                evasions.html.entity_encoding_root_internal_entity))
    # cases.append(TransformFunction("HtmlEvasion-html-734", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_cdata_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_mix))
    # cases.append(TransformFunction("HtmlEvasion-html-735", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_cdata_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_mix,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity.parameterize(
    #                                    min_value_length=2)
    #                                ))
    # cases.append(TransformFunction("HtmlEvasion-html-736", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_cdata_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_mix,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity.parameterize(
    #                                    min_value_length=2),
    #                                evasions.html.entity_encoding_internal_parameter_entity_declaration_nested_internal_parameter_entities.parameterize(
    #                                    number_of_nested=51730)
    #                                ))
    # # data url + ... + entity_encoding_internal_parameter_entity_declaration_mix -> too large value ?
    # cases.append(TransformFunction("HtmlEvasion-html-737", None, parsed_as_xml_case,
    #                                evasions.html.entity_encoding_attributes_internal_entities,
    #                                evasions.html.entity_encoding_cdata_internal_entities,
    #                                evasions.html.entity_encoding_root_internal_entity,
    #                                evasions.html.entity_encoding_internal_entity_declaration_mix,
    #                                evasions.html.entity_encoding_internal_entity_declaration_internal_parameter_entity.parameterize(
    #                                    min_value_length=2),
    #                                evasions.html.entity_encoding_internal_parameter_entity_declaration_nested_internal_parameter_entities.parameterize(
    #                                    number_of_nested=32730),
    #                                evasions.html.entity_encoding_internal_parameter_entity_declaration_mix
    #                                ))
    # cases.append(TransformFunction("HtmlEvasion-html-738", None, cases[-1], evasions.html.http_declared_utf_7_encoded_as_utf_7_5_i))


    # description cleanup
    if not long_descriptions:
        TransformFunction.cleanup_descriptions(cases, simple_index)

    return OrderedDict([(c.name, c) for c in cases])
