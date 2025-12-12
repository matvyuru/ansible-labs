#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule
import platform
import socket

def run_module():
    module = AnsibleModule(argument_spec={})
    
    facts = {
        'lab_facts': {
            'environment': 'Ansible Laboratory',
            'hostname': socket.gethostname(),
            'platform': platform.platform(),
            'python_version': platform.python_version()
        }
    }
    
    result = dict(
        changed=False,
        facts=facts
    )
    
    module.exit_json(**result, ansible_facts=facts)

if __name__ == '__main__':
    run_module()
# Улучшение обработки ошибок
# Дополнительные системные проверки
