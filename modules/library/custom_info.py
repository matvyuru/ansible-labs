#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule
import datetime

def run_module():
    module_args = dict(
        student_name=dict(type='str', required=True),
        lab_number=dict(type='int', default=1)
    )
    
    result = dict(
        changed=False,
        message='',
        timestamp=''
    )
    
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    
    student_name = module.params['student_name']
    lab_number = module.params['lab_number']
    
    result['message'] = f"Лабораторная работа {lab_number} выполнена студентом {student_name}"
    result['timestamp'] = datetime.datetime.now().isoformat()
    result['student'] = student_name
    result['lab'] = lab_number
    
    module.exit_json(**result)

if __name__ == '__main__':
    run_module()
# Финальные улучшения
