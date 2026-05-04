# TEST_LOG

## Task 1 Red

第一次執行測試時，Task 1 測試失敗。

錯誤原因：
目前 task1_csv_to_json.py 中的 filter_by_admission() 與 count_by_dept() 尚未實作，函式內仍為 pass，因此回傳 None。

測試結果摘要：

```text
test_count_by_dept_correct ... FAIL
test_count_by_dept_empty ... FAIL
test_count_by_dept_missing_dept_name ... FAIL
test_filter_empty_input ... FAIL
test_filter_keeps_correct_rows ... ERROR
test_filter_missing_admission_key ... ERROR
test_filter_removes_others ... ERROR

FAILED (failures=4, errors=3)
```

## Task 1 Green

請貼上 Task 1 測試通過的結果。

```text
test_count_by_dept_correct (test_task1.TestTask1CsvToJson.test_count_by_dept_correct) ... ok
test_count_by_dept_empty (test_task1.TestTask1CsvToJson.test_count_by_dept_empty) ... ok
test_count_by_dept_missing_dept_name (test_task1.TestTask1CsvToJson.test_count_by_dept_missing_dept_name) ... ok
test_filter_empty_input (test_task1.TestTask1CsvToJson.test_filter_empty_input) ... ok
test_filter_keeps_correct_rows (test_task1.TestTask1CsvToJson.test_filter_keeps_correct_rows) ... ok
test_filter_missing_admission_key (test_task1.TestTask1CsvToJson.test_filter_missing_admission_key) ... ok
test_filter_removes_others (test_task1.TestTask1CsvToJson.test_filter_removes_others) ... ok
```

## Task 2 Red

test_empty_student_list ... ERROR
test_missing_student_fields_use_empty_string ... ERROR
test_root_tag_and_attrs ... ERROR
test_student_attrs_exist ... ERROR
test_student_attrs_values_correct ... ERROR
test_student_count_matches ... ERROR
test_xml_is_valid ... ERROR

FAILED (errors=7)

## Task 2 Green

請貼上 Task 2 測試通過的結果。

```text
test_empty_student_list (test_task2.TestTask2JsonToXml.test_empty_student_list) ... ok
test_missing_student_fields_use_empty_string (test_task2.TestTask2JsonToXml.test_missing_student_fields_use_empty_string) ... ok
test_root_tag_and_attrs (test_task2.TestTask2JsonToXml.test_root_tag_and_attrs) ... ok
test_student_attrs_exist (test_task2.TestTask2JsonToXml.test_student_attrs_exist) ... ok
test_student_attrs_values_correct (test_task2.TestTask2JsonToXml.test_student_attrs_values_correct) ... ok
test_student_count_matches (test_task2.TestTask2JsonToXml.test_student_count_matches) ... ok
test_xml_is_valid (test_task2.TestTask2JsonToXml.test_xml_is_valid) ... ok
```

## Refactor 紀錄

請描述你重構了哪些部分，以及測試是否仍通過。
